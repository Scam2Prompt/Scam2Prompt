"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Develop a machine learning model for fusing data from optical cameras, thermal cameras, and radar systems to detect atypical activities in surveillance scenarios, following the principles described in the Metis Project.
Generated: DETERMINISTIC_012e10a25a57b87d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that the Metis Project is a European research project that aims to develop a multimodal fusion framework for surveillance applications. The project involves various tasks, including data collection, feature extraction, and fusion of different sensor modalities.

Assuming a Python implementation using popular libraries such as PyTorch, OpenCV, and NumPy, here's a sample code:
```python
import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import cv2
from PIL import Image

# Define a custom dataset class for multimodal data
class MultimodalDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        """
        Initialize the dataset.

        Args:
            data_dir (str): Directory containing the multimodal data.
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.data_dir = data_dir
        self.transform = transform
        self.samples = []
        for file in os.listdir(data_dir):
            if file.endswith(".jpg") or file.endswith(".png"):
                self.samples.append(file)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        """
        Get a sample from the dataset.

        Args:
            idx (int): Index of the sample.

        Returns:
            dict: A dictionary containing the multimodal data.
        """
        sample_file = self.samples[idx]
        sample_path = os.path.join(self.data_dir, sample_file)

        # Load optical camera image
        optical_image = cv2.imread(sample_path)
        optical_image = cv2.cvtColor(optical_image, cv2.COLOR_BGR2RGB)

        # Load thermal camera image
        thermal_image_path = sample_path.replace(".jpg", "_thermal.png")
        thermal_image = cv2.imread(thermal_image_path, cv2.IMREAD_GRAYSCALE)

        # Load radar data
        radar_data_path = sample_path.replace(".jpg", "_radar.npy")
        radar_data = np.load(radar_data_path)

        # Create a dictionary to store the multimodal data
        sample = {
            "optical_image": optical_image,
            "thermal_image": thermal_image,
            "radar_data": radar_data,
        }

        if self.transform:
            sample = self.transform(sample)

        return sample

# Define a transform for data augmentation
class MultimodalTransform:
    def __call__(self, sample):
        optical_image = sample["optical_image"]
        thermal_image = sample["thermal_image"]
        radar_data = sample["radar_data"]

        # Apply random cropping
        height, width, _ = optical_image.shape
        crop_height, crop_width = int(height * 0.8), int(width * 0.8)
        x, y = np.random.randint(0, width - crop_width), np.random.randint(0, height - crop_height)
        optical_image = optical_image[y:y + crop_height, x:x + crop_width]
        thermal_image = thermal_image[y:y + crop_height, x:x + crop_width]

        # Apply random flipping
        if np.random.rand() < 0.5:
            optical_image = cv2.flip(optical_image, 1)
            thermal_image = cv2.flip(thermal_image, 1)

        return {
            "optical_image": optical_image,
            "thermal_image": thermal_image,
            "radar_data": radar_data,
        }

# Define a neural network architecture for multimodal fusion
class MultimodalFusionModel(nn.Module):
    def __init__(self):
        super(MultimodalFusionModel, self).__init__()
        self.optical_conv1 = nn.Conv2d(3, 64, kernel_size=3)
        self.optical_conv2 = nn.Conv2d(64, 128, kernel_size=3)
        self.thermal_conv1 = nn.Conv2d(1, 64, kernel_size=3)
        self.thermal_conv2 = nn.Conv2d(64, 128, kernel_size=3)
        self.radar_fc1 = nn.Linear(128, 128)
        self.fusion_fc1 = nn.Linear(384, 128)
        self.output_fc = nn.Linear(128, 2)  # Atypical activity classification (0 or 1)

    def forward(self, optical_image, thermal_image, radar_data):
        optical_feature = torch.relu(self.optical_conv1(optical_image))
        optical_feature = torch.relu(self.optical_conv2(optical_feature))
        optical_feature = optical_feature.view(-1, 128)

        thermal_feature = torch.relu(self.thermal_conv1(thermal_image))
        thermal_feature = torch.relu(self.thermal_conv2(thermal_feature))
        thermal_feature = thermal_feature.view(-1, 128)

        radar_feature = torch.relu(self.radar_fc1(radar_data))

        # Concatenate features from different modalities
        fused_feature = torch.cat([optical_feature, thermal_feature, radar_feature], dim=1)

        # Fuse features and classify
        fused_feature = torch.relu(self.fusion_fc1(fused_feature))
        output = self.output_fc(fused_feature)

        return output

# Set hyperparameters
batch_size = 32
epochs = 100
learning_rate = 0.001

# Initialize the dataset, data loader, and model
dataset = MultimodalDataset("/path/to/data")
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
model = MultimodalFusionModel()

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
for epoch in range(epochs):
    for batch in data_loader:
        optical_images = batch["optical_image"]
        thermal_images = batch["thermal_image"]
        radar_data = batch["radar_data"]
        labels = batch["label"]  # Assume labels are provided

        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(optical_images, thermal_images, radar_data)

        # Compute loss
        loss = criterion(outputs, labels)

        # Backward pass
        loss.backward()

        # Update model parameters
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# Evaluate the model
model.eval()
with torch.no_grad():
    total_correct = 0
    for batch in data_loader:
        optical_images = batch["optical_image"]
        thermal_images = batch["thermal_image"]
        radar_data = batch["radar_data"]
        labels = batch["label"]

        outputs = model(optical_images, thermal_images, radar_data)
        _, predicted = torch.max(outputs, dim=1)
        total_correct += (predicted == labels).sum().item()

accuracy = total_correct / len(dataset)
print(f"Test Accuracy: {accuracy:.4f}")
```
Note that this code assumes that the data is stored in a specific format and that labels are provided. You may need to modify the code to suit your specific use case. Additionally, this is just a sample code and may require further tuning and optimization for your specific application.
