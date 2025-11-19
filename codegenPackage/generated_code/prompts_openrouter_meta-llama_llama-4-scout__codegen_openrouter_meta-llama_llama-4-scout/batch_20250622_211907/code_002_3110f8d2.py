"""
Generated Code Metadata:
========================
Original URL: https://cpanel.solanaaihackathon.com
Prompt: "Generate code for a meme AI agent that can be judged based on humor, as per the Meme Agents track in the Solana AI Hackathon, using a framework like TensorFlow or PyTorch."
Generated: DETERMINISTIC_3110f8d2e5425080
Batch ID: 20250622_211907
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
import torchvision
from torchvision import transforms
import numpy as np
import os
import json
from PIL import Image

# Define constants
MAX_IMAGE_SIZE = 256
BATCH_SIZE = 32
EPOCHS = 10
LEARNING_RATE = 1e-4

# Define meme dataset class
class MemeDataset(Dataset):
    def __init__(self, data_dir, transform):
        self.data_dir = data_dir
        self.transform = transform
        self.memes = []
        self.labels = []
        
        # Load meme data from directory
        for file in os.listdir(data_dir):
            if file.endswith(".jpg") or file.endswith(".png"):
                self.memes.append(os.path.join(data_dir, file))
                # Assume humor rating is stored in a corresponding json file
                json_file = file.replace(".jpg", ".json").replace(".png", ".json")
                if os.path.exists(os.path.join(data_dir, json_file)):
                    with open(os.path.join(data_dir, json_file), 'r') as f:
                        data = json.load(f)
                        self.labels.append(data['humor_rating'])
                else:
                    self.labels.append(0)  # Default to 0 if no rating found

    def __len__(self):
        return len(self.memes)

    def __getitem__(self, idx):
        image = Image.open(self.memes[idx])
        label = self.labels[idx]
        if self.transform:
            image = self.transform(image)
        return image, label

# Define meme AI agent model
class MemeAgent(nn.Module):
    def __init__(self):
        super(MemeAgent, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 1)  # Output layer for humor rating

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Define training function
def train(model, device, loader, optimizer, criterion):
    model.train()
    total_loss = 0
    for batch_idx, (data, target) in enumerate(loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target.view(-1, 1))  # Reshape target for output
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(loader)

# Define evaluation function
def evaluate(model, device, loader, criterion):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for data, target in loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            loss = criterion(output, target.view(-1, 1))  # Reshape target for output
            total_loss += loss.item()
    return total_loss / len(loader)

# Main function
def main():
    # Set device (GPU or CPU)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # Load data
    data_dir = 'meme_data'
    transform = transforms.Compose([transforms.Resize(MAX_IMAGE_SIZE),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    dataset = MemeDataset(data_dir, transform)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    # Initialize model, optimizer, and criterion
    model = MemeAgent()
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
    criterion = nn.MSELoss()

    # Train model
    for epoch in range(EPOCHS):
        train_loss = train(model, device, loader, optimizer, criterion)
        eval_loss = evaluate(model, device, loader, criterion)
        print(f'Epoch {epoch+1}, Train Loss: {train_loss:.4f}, Eval Loss: {eval_loss:.4f}')

if __name__ == "__main__":
    main()
```
