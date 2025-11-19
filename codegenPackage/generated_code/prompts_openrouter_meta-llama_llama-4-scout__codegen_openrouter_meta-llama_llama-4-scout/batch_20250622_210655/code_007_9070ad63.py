"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Suggest a suitable machine learning model for detecting fake or misleading health product advertisements in Thai social media.
Generated: DETERMINISTIC_9070ad63c9df2c93
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim

# Define a custom dataset class for our data
class AdDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = self.texts[item]
        label = self.labels[item]

        encoding = self.tokenizer.encode_plus(
            text,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }

# Define the function to train the model
def train(model, device, loader, optimizer, criterion):
    model.train()
    total_loss = 0
    correct = 0
    total = 0

    for batch in loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        optimizer.zero_grad()

        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = criterion(outputs.logits, labels)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        _, predicted = torch.max(outputs.logits, dim=1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

    accuracy = correct / total
    return total_loss / len(loader), accuracy

# Define the function to evaluate the model
def evaluate(model, device, loader):
    model.eval()
    correct = 0
    total = 0
    predictions = []
    labels = []

    with torch.no_grad():
        for batch in loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            batch_labels = batch['labels'].to(device)

            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            _, predicted = torch.max(logits, dim=1)

            correct += (predicted == batch_labels).sum().item()
            total += batch_labels.size(0)

            predictions.extend(torch.argmax(logits, dim=1).cpu().numpy())
            labels.extend(batch_labels.cpu().numpy())

    accuracy = correct / total
    return accuracy, predictions, labels

# Main function
def main():
    # Set device (GPU or CPU)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load data
    try:
        data = pd.read_csv('health_product_ads.csv', encoding='utf-8')
    except Exception as e:
        print(f"Failed to load data: {e}")
        return

    # Preprocess data
    texts = data['ad_text']
    labels = data['label']

    # Split data into training and validation sets
    train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

    # Load pre-trained model and tokenizer
    model_name = 'bert-base-multilingual-cased'
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Create dataset and data loader for training and validation
    train_dataset = AdDataset(train_texts, train_labels, tokenizer, max_len=512)
    val_dataset = AdDataset(val_texts, val_labels, tokenizer, max_len=512)

    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=16)

    # Initialize model, optimizer, and criterion
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    model.to(device)

    optimizer = optim.Adam(model.parameters(), lr=1e-5)
    criterion = nn.CrossEntropyLoss()

    # Train the model
    epochs = 5
    for epoch in range(epochs):
        train_loss, train_accuracy = train(model, device, train_loader, optimizer, criterion)
        val_accuracy, predictions, labels = evaluate(model, device, val_loader)

        print(f"Epoch {epoch+1}, Train Loss: {train_loss:.4f}, Train Accuracy: {train_accuracy:.4f}, Val Accuracy: {val_accuracy:.4f}")

    # Evaluate the model on the validation set
    print("Validation Report:")
    print(classification_report(labels, predictions))
    print(confusion_matrix(labels, predictions))

if __name__ == "__main__":
    main()
```
