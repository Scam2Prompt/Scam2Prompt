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
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW
import numpy as np
import os

# Define a custom dataset class for loading training data
class CreativeDataset(Dataset):
    def __init__(self, texts, tokenizer, max_length=512):
        """
        Initializes the dataset with texts and tokenizer.

        Args:
            texts (list): List of strings to be used for training.
            tokenizer (Tokenizer): Tokenizer for encoding the texts.
            max_length (int): Maximum length of the tokenized input.
        """
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        # Tokenize the input text
        encoding = self.tokenizer.encode_plus(
            self.texts[idx],
            add_special_tokens=True,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten()
        }

# Function to load data from a text file
def load_data(file_path):
    """
    Loads the training data from a text file.

    Args:
        file_path (str): Path to the text file containing training data.

    Returns:
        list: List of strings read from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# Function to train the generative model
def train_model(model, dataloader, optimizer, num_epochs=3):
    """
    Trains the generative model.

    Args:
        model (nn.Module): The model to be trained.
        dataloader (DataLoader): DataLoader for training data.
        optimizer (Optimizer): Optimizer for model training.
        num_epochs (int): Number of epochs for training.
    """
    model.train()
    for epoch in range(num_epochs):
        for batch in dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)

            # Forward pass
            outputs = model(input_ids, attention_mask=attention_mask, labels=input_ids)
            loss = outputs.loss

            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# Main execution
if __name__ == "__main__":
    # Check if GPU is available and set device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load the pre-trained GPT-2 tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2').to(device)

    # Load data
    data_file_path = 'creative_writing_data.txt'  # Path to your data file
    texts = load_data(data_file_path)

    # Create dataset and dataloader
    dataset = CreativeDataset(texts, tokenizer)
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

    # Set up the optimizer
    optimizer = AdamW(model.parameters(), lr=5e-5)

    # Train the model
    train_model(model, dataloader, optimizer, num_epochs=3)

    # Save the model
    model_save_path = 'creative_gpt2_model'
    model.save_pretrained(model_save_path)
    tokenizer.save_pretrained(model_save_path)
    print("Model saved to", model_save_path)
```
