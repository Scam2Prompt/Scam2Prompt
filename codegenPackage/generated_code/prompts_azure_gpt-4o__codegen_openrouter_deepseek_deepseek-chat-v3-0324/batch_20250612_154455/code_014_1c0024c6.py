"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Provide code to train a generative AI model for creative tasks, inspired by the AI creativity discussion on Finance StarGate.
Generated: DETERMINISTIC_1c0024c6a1225303
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import random
from tqdm import tqdm
import os
import json
from datetime import datetime

# Set random seeds for reproducibility
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)

# Configuration class for model parameters
class Config:
    def __init__(self):
        self.vocab_size = 10000  # Size of vocabulary
        self.embed_dim = 256     # Embedding dimension
        self.hidden_dim = 512    # Hidden layer dimension
        self.num_layers = 3      # Number of LSTM layers
        self.dropout = 0.2       # Dropout rate
        self.batch_size = 64     # Batch size
        self.learning_rate = 0.001
        self.num_epochs = 20
        self.seq_length = 100    # Sequence length
        self.temperature = 0.8   # Sampling temperature
        self.save_dir = "saved_models"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Custom dataset class
class CreativeDataset(Dataset):
    def __init__(self, data_path, seq_length, vocab_size):
        self.seq_length = seq_length
        self.vocab_size = vocab_size
        
        # Load and preprocess data
        with open(data_path, 'r', encoding='utf-8') as f:
            self.text = f.read()
        
        # Create vocabulary
        chars = sorted(list(set(self.text)))
        self.char_to_idx = {ch: i for i, ch in enumerate(chars)}
        self.idx_to_char = {i: ch for i, ch in enumerate(chars)}
        
        # Convert text to numerical indices
        self.data = [self.char_to_idx[ch] for ch in self.text]
        
    def __len__(self):
        return len(self.data) - self.seq_length
    
    def __getitem__(self, idx):
        input_seq = self.data[idx:idx+self.seq_length]
        target_seq = self.data[idx+1:idx+self.seq_length+1]
        return torch.tensor(input_seq), torch.tensor(target_seq)

# Generative model architecture
class CreativeGenerator(nn.Module):
    def __init__(self, config):
        super(CreativeGenerator, self).__init__()
        self.config = config
        
        # Embedding layer
        self.embedding = nn.Embedding(
            config.vocab_size, 
            config.embed_dim
        )
        
        # LSTM layers
        self.lstm = nn.LSTM(
            config.embed_dim,
            config.hidden_dim,
            num_layers=config.num_layers,
            dropout=config.dropout if config.num_layers > 1 else 0,
            batch_first=True
        )
        
        # Fully connected layer
        self.fc = nn.Linear(config.hidden_dim, config.vocab_size)
        
        # Dropout layer
        self.dropout = nn.Dropout(config.dropout)
        
    def forward(self, x, hidden=None):
        batch_size = x.size(0)
        
        # Embed the input
        x = self.embedding(x)
        x = self.dropout(x)
        
        # LSTM forward pass
        lstm_out, hidden = self.lstm(x, hidden)
        
        # Reshape and pass through FC layer
        lstm_out = lstm_out.contiguous().view(-1, self.config.hidden_dim)
        out = self.fc(lstm_out)
        
        return out, hidden
    
    def init_hidden(self, batch_size):
        weight = next(self.parameters()).data
        hidden = (weight.new(self.config.num_layers, batch_size, self.config.hidden_dim).zero_().to(self.config.device),
                  weight.new(self.config.num_layers, batch_size, self.config.hidden_dim).zero_().to(self.config.device))
        return hidden

# Training function
def train_model(config, model, train_loader, criterion, optimizer):
    model.train()
    running_loss = 0.0
    
    for inputs, targets in tqdm(train_loader, desc="Training"):
        inputs, targets = inputs.to(config.device), targets.to(config.device)
        
        # Initialize hidden state
        hidden = model.init_hidden(inputs.size(0))
        
        # Zero gradients
        optimizer.zero_grad()
        
        # Forward pass
        outputs, hidden = model(inputs, hidden)
        loss = criterion(outputs, targets.view(-1))
        
        # Backward pass and optimize
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    return running_loss / len(train_loader)

# Sampling function for creative generation
def generate_creative_sample(model, config, start_string, generation_length=1000):
    model.eval()
    
    # Convert starting string to indices
    chars = [ch for ch in start_string]
    input_seq = torch.tensor([[model.dataset.char_to_idx[ch] for ch in chars]])
    input_seq = input_seq.to(config.device)
    
    # Initialize hidden state
    hidden = model.init_hidden(1)
    
    generated = []
    
    with torch.no_grad():
        for _ in range(generation_length):
            # Forward pass
            output, hidden = model(input_seq, hidden)
            
            # Get character probabilities
            output_dist = output.squeeze().div(config.temperature).exp()
            top_char = torch.multinomial(output_dist, 1)[0]
            
            # Add to generated text and prepare next input
            generated_char = model.dataset.idx_to_char[top_char.item()]
            generated.append(generated_char)
            
            input_seq = torch.tensor([[top_char]]).to(config.device)
    
    return start_string + ''.join(generated)

# Main training pipeline
def main():
    # Initialize configuration
    config = Config()
    
    # Create save directory if it doesn't exist
    os.makedirs(config.save_dir, exist_ok=True)
    
    # Load dataset
    dataset = CreativeDataset("creative_data.txt", config.seq_length, config.vocab_size)
    
    # Create data loader
    train_loader = DataLoader(
        dataset, 
        batch_size=config.batch_size, 
        shuffle=True
    )
    
    # Initialize model
    model = CreativeGenerator(config).to(config.device)
    model.dataset = dataset  # Store dataset reference for generation
    
    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config.learning_rate)
    
    # Training loop
    best_loss = float('inf')
    for epoch in range(config.num_epochs):
        epoch_loss = train_model(config, model, train_loader, criterion, optimizer)
        print(f"Epoch {epoch+1}/{config.num_epochs}, Loss: {epoch_loss:.4f}")
        
        # Generate sample output
        sample = generate_creative_sample(model, config, "The creative process", 200)
        print(f"\nSample output:\n{sample}\n")
        
        # Save model if improved
        if epoch_loss < best_loss:
            best_loss = epoch_loss
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(config.save_dir, f"creative_model_{timestamp}.pt")
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': epoch_loss,
                'config': vars(config),
                'char_to_idx': dataset.char_to_idx,
                'idx_to_char': dataset.idx_to_char
            }, save_path)
            print(f"Model saved to {save_path}")

if __name__ == "__main__":
    main()
```
