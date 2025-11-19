"""
Generated Code Metadata:
========================
Original URL: https://squares-admin-verification.pages.dev
Prompt: "Generate a code example for optimizing and training an AI model using a grid-based graphical interface and GPU resources."
Generated: DETERMINISTIC_9ffbf4587abaa8c3
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
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from hyperopt import hp, fmin, tpe, Trials

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

# Define a custom dataset class
class CustomDataset(Dataset):
    def __init__(self, X, y, transform=None):
        self.X = X
        self.y = y
        self.transform = transform

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        if self.transform:
            X = self.transform(self.X[idx])
        else:
            X = self.X[idx]
        return X, self.y[idx]

# Define the objective function to optimize
def optimize_model(params):
    # Set up device (GPU or CPU)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # Load the MNIST dataset
    transform = transforms.ToTensor()
    train_dataset = CustomDataset(X_train, y_train, transform)
    test_dataset = CustomDataset(X_test, y_test, transform)

    # Create data loaders
    train_loader = DataLoader(train_dataset, batch_size=int(params['batch_size']), shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=int(params['batch_size']), shuffle=False)

    # Initialize the model, loss function, and optimizer
    model = Net().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=params['learning_rate'])

    # Train the model
    for epoch in range(int(params['epochs'])):
        for i, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)
            images = images.view(-1, 784)  # flatten the images

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    # Evaluate the model
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            images = images.view(-1, 784)  # flatten the images

            outputs = model(images)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()

    accuracy = correct / len(test_loader.dataset)
    return -accuracy  # minimize the negative accuracy (maximize accuracy)

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = torchvision.datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=True, transform=None), torchvision.datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=False, transform=None)

# Define the hyperparameter search space
search_space = {
    'batch_size': hp.quniform('batch_size', 32, 128, 32),
    'learning_rate': hp.loguniform('learning_rate', np.log(0.001), np.log(0.1)),
    'epochs': hp.quniform('epochs', 5, 20, 1)
}

# Perform hyperparameter optimization using TPE
trials = Trials()
best = fmin(optimize_model, search_space, algo=tpe.suggest, trials=trials, max_evals=50)

# Train the model with the best hyperparameters
best_params = {'batch_size': int(best['batch_size']), 'learning_rate': best['learning_rate'], 'epochs': int(best['epochs'])}
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = Net().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=best_params['learning_rate'])

transform = transforms.ToTensor()
train_dataset = CustomDataset(X_train, y_train, transform)
test_dataset = CustomDataset(X_test, y_test, transform)

train_loader = DataLoader(train_dataset, batch_size=best_params['batch_size'], shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=best_params['batch_size'], shuffle=False)

for epoch in range(best_params['epochs']):
    for i, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)
        images = images.view(-1, 784)  # flatten the images

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# Evaluate the trained model
model.eval()
test_loss = 0
correct = 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        images = images.view(-1, 784)  # flatten the images

        outputs = model(images)
        loss = criterion(outputs, labels)
        test_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()

accuracy = correct / len(test_loader.dataset)
print(f'Test Accuracy: {accuracy:.2f}%')
```
