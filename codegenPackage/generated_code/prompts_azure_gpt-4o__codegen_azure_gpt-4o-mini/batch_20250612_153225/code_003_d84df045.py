"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Create a program using TensorFlow or PyTorch to analyze eye movement patterns and suggest exercises for improving vision, inspired by the holistic methods described on Klar Sehen.
Generated: DETERMINISTIC_d84df045cce10d40
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Define a custom dataset class for eye movement data
class EyeMovementDataset(Dataset):
    def __init__(self, data, labels):
        """
        Initialize the dataset with data and labels.
        
        :param data: A numpy array of eye movement features.
        :param labels: A numpy array of corresponding labels (exercises).
        """
        self.data = torch.tensor(data, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        """Return the total number of samples."""
        return len(self.data)

    def __getitem__(self, idx):
        """Return a single sample and its label."""
        return self.data[idx], self.labels[idx]

# Define a simple neural network model
class EyeMovementModel(nn.Module):
    def __init__(self, input_size, num_classes):
        """
        Initialize the neural network model.
        
        :param input_size: Number of input features.
        :param num_classes: Number of output classes (exercises).
        """
        super(EyeMovementModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        """Define the forward pass."""
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def train_model(model, train_loader, criterion, optimizer, num_epochs=20):
    """
    Train the model on the training dataset.
    
    :param model: The neural network model.
    :param train_loader: DataLoader for the training data.
    :param criterion: Loss function.
    :param optimizer: Optimizer for updating weights.
    :param num_epochs: Number of epochs to train.
    """
    model.train()
    for epoch in range(num_epochs):
        for inputs, labels in train_loader:
            optimizer.zero_grad()  # Clear gradients
            outputs = model(inputs)  # Forward pass
            loss = criterion(outputs, labels)  # Compute loss
            loss.backward()  # Backward pass
            optimizer.step()  # Update weights

        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

def evaluate_model(model, test_loader):
    """
    Evaluate the model on the test dataset.
    
    :param model: The neural network model.
    :param test_loader: DataLoader for the test data.
    """
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print(f'Accuracy of the model on the test set: {accuracy:.2f}%')

def main():
    # Load your eye movement data and labels here
    # For demonstration, we will create dummy data
    num_samples = 1000
    num_features = 10
    num_classes = 5

    # Generate random data and labels
    data = np.random.rand(num_samples, num_features)
    labels = np.random.randint(0, num_classes, num_samples)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Create datasets and dataloaders
    train_dataset = EyeMovementDataset(X_train, y_train)
    test_dataset = EyeMovementDataset(X_test, y_test)
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    # Initialize the model, criterion, and optimizer
    model = EyeMovementModel(input_size=num_features, num_classes=num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Train the model
    train_model(model, train_loader, criterion, optimizer, num_epochs=20)

    # Evaluate the model
    evaluate_model(model, test_loader)

if __name__ == "__main__":
    main()
```
