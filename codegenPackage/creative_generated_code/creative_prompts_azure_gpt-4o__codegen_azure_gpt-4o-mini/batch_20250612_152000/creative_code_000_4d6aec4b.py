"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Write Python code to generate AI art inspired by Refik Anadol's "Machine Hallucinations: Sphere" project, using a machine learning library like TensorFlow or PyTorch. Include steps to preprocess visual data for training.
Generated: DETERMINISTIC_4d6aec4b361818ea
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import numpy as np
import torch
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchvision import models
import matplotlib.pyplot as plt
from PIL import Image

# Set device for PyTorch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define constants
IMAGE_SIZE = (256, 256)  # Size to which images will be resized
BATCH_SIZE = 16           # Number of images per batch

class CustomDataset(Dataset):
    """Custom dataset for loading and preprocessing images."""
    
    def __init__(self, directory):
        self.directory = directory
        self.image_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png')]
        self.transform = transforms.Compose([
            transforms.Resize(IMAGE_SIZE),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normalization
        ])

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_path = self.image_files[idx]
        image = Image.open(img_path).convert('RGB')
        image = self.transform(image)
        return image

def create_dataloader(directory):
    """Creates a DataLoader for the dataset."""
    dataset = CustomDataset(directory)
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)
    return dataloader

def generate_art_model():
    """Generates a model for creating art inspired by Refik Anadol's style."""
    # For simplicity, we use a pre-trained model and modify it.
    model = models.resnet18(pretrained=True)
    model.fc = torch.nn.Linear(model.fc.in_features, 256)  # Change output size for our task
    return model.to(device)

def train_model(model, dataloader, num_epochs=10):
    """Trains the model using the provided DataLoader."""
    criterion = torch.nn.MSELoss()  # Example loss function
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    model.train()  # Set model to training mode
    for epoch in range(num_epochs):
        for images in dataloader:
            images = images.to(device)
            optimizer.zero_grad()  # Zero the gradients

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, torch.randn_like(outputs))  # Dummy target for illustration
            
            loss.backward()  # Backward pass
            optimizer.step()  # Update weights

        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

def generate_art_images(model, num_images=5):
    """Generates and saves art images using the trained model."""
    model.eval()  # Set model to evaluation mode
    with torch.no_grad():
        for i in range(num_images):
            noise = torch.randn(1, 3, IMAGE_SIZE[0], IMAGE_SIZE[1]).to(device)
            generated_image = model(noise).cpu().squeeze(0).numpy()
            generated_image = (generated_image * 0.5 + 0.5)  # Undo normalization
            plt.imsave(f'generated_art_{i+1}.png', np.transpose(generated_image, (1, 2, 0)))

def main(image_directory):
    """Main function to run the art generation process."""
    try:
        dataloader = create_dataloader(image_directory)
        model = generate_art_model()
        train_model(model, dataloader, num_epochs=10)
        generate_art_images(model, num_images=5)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Execute the script with the directory containing images
if __name__ == "__main__":
    # Provide the path to the directory containing your images
    IMAGE_DIRECTORY = 'path/to/your/images'
    main(IMAGE_DIRECTORY)
```
