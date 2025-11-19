"""
Generated Code Metadata:
========================
Original URL: https://squares-admin-verify.pages.dev
Prompt: "Generate a code example for optimizing and training an AI model using a grid-based graphical interface and GPU resources, as described in the Squares AI workflow."
Generated: DETERMINISTIC_3e8fe942cf69aa26
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# Define a custom dataset class
class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# Define a simple neural network model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 128)  # input layer (28x28 images) -> hidden layer (128 units)
        self.fc2 = nn.Linear(128, 10)   # hidden layer (128 units) -> output layer (10 units)

    def forward(self, x):
        x = torch.relu(self.fc1(x))      # activation function for hidden layer
        x = self.fc2(x)
        return x

# Define a function to train the model
def train_model(model, device, loader, optimizer, criterion):
    model.train()
    total_loss = 0
    correct = 0
    total = 0
    for batch_idx, (data, target) in enumerate(loader):
        data, target = data.to(device), target.to(device)
        data = data.view(-1, 784)  # flatten the data
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        _, predicted = torch.max(output, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()
    accuracy = correct / total
    return total_loss / (batch_idx + 1), accuracy

# Define a function to optimize the model using grid search
def optimize_model(X_train, y_train, X_val, y_val):
    # Define hyperparameter grid
    param_grid = {
        'batch_size': [32, 64, 128],
        'learning_rate': [0.001, 0.01, 0.1],
        'epochs': [5, 10, 15]
    }

    # Initialize the model, device, and criterion
    model = Net()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    criterion = nn.CrossEntropyLoss()

    # Perform grid search
    best_accuracy = 0
    best_params = None
    for batch_size in param_grid['batch_size']:
        for learning_rate in param_grid['learning_rate']:
            for epochs in param_grid['epochs']:
                # Create data loaders
                dataset = CustomDataset(X_train, y_train)
                loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

                # Train the model
                optimizer = optim.Adam(model.parameters(), lr=learning_rate)
                for epoch in range(epochs):
                    loss, accuracy = train_model(model, device, loader, optimizer, criterion)
                # Evaluate the model on the validation set
                dataset_val = CustomDataset(X_val, y_val)
                loader_val = DataLoader(dataset_val, batch_size=batch_size, shuffle=False)
                model.eval()
                total_correct = 0
                with torch.no_grad():
                    for data, target in loader_val:
                        data, target = data.to(device), target.to(device)
                        data = data.view(-1, 784)  # flatten the data
                        output = model(data)
                        _, predicted = torch.max(output, 1)
                        total_correct += (predicted == target).sum().item()
                accuracy_val = total_correct / len(dataset_val)
                # Update best parameters
                if accuracy_val > best_accuracy:
                    best_accuracy = accuracy_val
                    best_params = {'batch_size': batch_size, 'learning_rate': learning_rate, 'epochs': epochs}

    return best_params

# Example usage
if __name__ == "__main__":
    # Load the dataset (e.g. MNIST)
    transform = transforms.ToTensor()
    trainset = torchvision.datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=True, transform=transform)
    trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
    valset = torchvision.datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=False, transform=transform)
    valloader = DataLoader(valset, batch_size=64, shuffle=False)

    # Get the data and labels
    X_train = np.array([np.array(t).flatten() for t in trainset.data])
    y_train = np.array(trainset.targets)
    X_val = np.array([np.array(t).flatten() for t in valset.data])
    y_val = np.array(valset.targets)

    # Optimize the model
    best_params = optimize_model(X_train, y_train, X_val, y_val)
    print("Best parameters:", best_params)

    # Train the model with the best parameters
    model = Net()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=best_params['learning_rate'])
    dataset = CustomDataset(X_train, y_train)
    loader = DataLoader(dataset, batch_size=best_params['batch_size'], shuffle=True)
    for epoch in range(best_params['epochs']):
        loss, accuracy = train_model(model, device, loader, optimizer, criterion)

    # Evaluate the model on the validation set
    model.eval()
    total_correct = 0
    with torch.no_grad():
        for data, target in valloader:
            data, target = data.to(device), target.to(device)
            data = data.view(-1, 784)  # flatten the data
            output = model(data)
            _, predicted = torch.max(output, 1)
            total_correct += (predicted == target).sum().item()
    accuracy_val = total_correct / len(valset)
    print("Validation accuracy:", accuracy_val)
```
