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
from PIL import Image
import torchvision.transforms as transforms
from torchvision.models import vgg16
from tqdm import tqdm

# Set seed for reproducibility
torch.manual_seed(42)
np.random.seed(42)

# Define device (GPU or CPU)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Define dataset class for our creative data
class CreativeDataset(Dataset):
    def __init__(self, data_dir, transform):
        """
        Args:
            data_dir (str): Path to the directory containing the data.
            transform (callable): Optional transform to be applied on a sample.
        """
        self.data_dir = data_dir
        self.transform = transform
        self.data = [f for f in os.listdir(data_dir) if f.endswith('.jpg')]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path = os.path.join(self.data_dir, self.data[idx])
        image = Image.open(img_path)
        if self.transform:
            image = self.transform(image)
        return image

# Define data transforms
data_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Load dataset
dataset = CreativeDataset('./creative_data', data_transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Define generator model
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.fc1 = nn.Linear(100, 128)  # input layer (100) -> hidden layer (128)
        self.fc2 = nn.Linear(128, 256)  # hidden layer (128) -> hidden layer (256)
        self.fc3 = nn.Linear(256, 512)  # hidden layer (256) -> hidden layer (512)
        self.fc4 = nn.Linear(512, 784)  # hidden layer (512) -> output layer (784)

    def forward(self, x):
        x = torch.relu(self.fc1(x))      # activation function for hidden layer
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.tanh(self.fc4(x))      # activation function for output layer
        return x.view(-1, 1, 28, 28)

# Define discriminator model
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.fc1 = nn.Linear(784, 512)  # input layer (784) -> hidden layer (512)
        self.fc2 = nn.Linear(512, 256)  # hidden layer (512) -> hidden layer (256)
        self.fc3 = nn.Linear(256, 128)  # hidden layer (256) -> hidden layer (128)
        self.fc4 = nn.Linear(128, 1)   # hidden layer (128) -> output layer (1)

    def forward(self, x):
        x = x.view(-1, 784)
        x = torch.relu(self.fc1(x))      # activation function for hidden layer
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.sigmoid(self.fc4(x))  # activation function for output layer
        return x

# Initialize generator and discriminator
generator = Generator().to(device)
discriminator = Discriminator().to(device)

# Define loss function and optimizer
criterion = nn.BCELoss()
optimizer_g = optim.Adam(generator.parameters(), lr=0.001)
optimizer_d = optim.Adam(discriminator.parameters(), lr=0.001)

# Train the generator and discriminator
for epoch in range(100):  # loop over the dataset multiple times
    for i, data in tqdm(enumerate(dataloader), total=len(dataloader)):
        # Train discriminator
        optimizer_d.zero_grad()
        real_data = data.to(device)
        real_output = discriminator(real_data)
        real_label = torch.ones_like(real_output)
        real_loss = criterion(real_output, real_label)

        fake_data = generator(torch.randn(32, 100).to(device))
        fake_output = discriminator(fake_data.detach())
        fake_label = torch.zeros_like(fake_output)
        fake_loss = criterion(fake_output, fake_label)

        d_loss = real_loss + fake_loss
        d_loss.backward()
        optimizer_d.step()

        # Train generator
        optimizer_g.zero_grad()
        fake_data = generator(torch.randn(32, 100).to(device))
        fake_output = discriminator(fake_data)
        fake_label = torch.ones_like(fake_output)
        g_loss = criterion(fake_output, fake_label)
        g_loss.backward()
        optimizer_g.step()

    print(f'Epoch [{epoch+1}/100], D loss: {d_loss.item():.4f}, G loss: {g_loss.item():.4f}')

# Save the trained generator and discriminator
torch.save(generator.state_dict(), 'generator.pth')
torch.save(discriminator.state_dict(), 'discriminator.pth')
```
