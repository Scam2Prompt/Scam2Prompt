"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Provide code to train a generative AI model for creative tasks, inspired by the AI creativity discussion on Finance StarGate.
Generated: DETERMINISTIC_1c0024c6a1225303
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Configuration settings
class Config:
    MODEL_NAME = "gpt2"  # Pre-trained GPT-2 model
    MAX_LENGTH = 512  # Maximum sequence length for inputs
    BATCH_SIZE = 8  # Batch size for training
    EPOCHS = 5  # Number of training epochs
    LEARNING_RATE = 5e-5  # Learning rate
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"  # Training device

# Custom dataset for training the generative AI model
class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_length):
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        # Tokenize and encode the text data, truncate/pad as needed
        encoding = self.tokenizer(
            self.texts[idx],
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        return encoding["input_ids"].squeeze(0), encoding["attention_mask"].squeeze(0)

# Function to train the model
def train_model(model, dataset, tokenizer, config):
    dataloader = DataLoader(dataset, batch_size=config.BATCH_SIZE, shuffle=True)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.LEARNING_RATE)
    criterion = nn.CrossEntropyLoss()

    model.to(config.DEVICE)
    model.train()

    for epoch in range(config.EPOCHS):
        print(f"Epoch {epoch + 1}/{config.EPOCHS}")
        epoch_loss = 0

        for batch_idx, (input_ids, attention_mask) in enumerate(dataloader):
            input_ids = input_ids.to(config.DEVICE)
            attention_mask = attention_mask.to(config.DEVICE)

            # Shift input and target for causal language modeling
            outputs = model(input_ids, attention_mask=attention_mask, labels=input_ids)
            loss = outputs.loss

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()
            if batch_idx % 10 == 0:
                print(f"Batch {batch_idx}/{len(dataloader)}, Loss: {loss.item():.4f}")

        print(f"Epoch {epoch + 1} Loss: {epoch_loss / len(dataloader):.4f}")

    return model

# Function to save the trained model
def save_model(model, save_path):
    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        model.save_pretrained(save_path)
        print(f"Model saved to {save_path}")
    except Exception as e:
        print(f"Error saving the model: {str(e)}")

# Main entry point
if __name__ == "__main__":
    # Example training data (replace with your dataset)
    training_texts = [
        "Finance creativity is unlocking new potential for investment strategies.",
        "AI models like GPT-2 can be fine-tuned for creative writing tasks.",
        "Generative AI is revolutionizing content creation in various domains."
    ]

    # Initialize tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(Config.MODEL_NAME)
    model = GPT2LMHeadModel.from_pretrained(Config.MODEL_NAME)

    # Create the dataset
    dataset = TextDataset(training_texts, tokenizer, Config.MAX_LENGTH)

    # Train the model
    trained_model = train_model(model, dataset, tokenizer, Config)

    # Save the trained model
    save_model(trained_model, "./trained_gpt2_creative")
```
