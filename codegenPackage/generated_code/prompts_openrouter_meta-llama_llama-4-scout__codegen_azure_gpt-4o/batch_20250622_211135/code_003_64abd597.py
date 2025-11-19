"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Design a simple AI-powered NFT generator using a library like TensorFlow or PyTorch, inspired by the "Fuck OpenSea" AI Generator.
Generated: DETERMINISTIC_64abd5972bd00bd5
Batch ID: 20250622_211135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.utils import save_image
from torchvision.transforms import transforms
from PIL import Image
import random

# Set device (GPU if available, otherwise CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the Generator model
class Generator(nn.Module):
    def __init__(self, latent_dim):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 3 * 64 * 64),  # Output size: 3 channels (RGB), 64x64 image
            nn.Tanh()  # Normalize output to [-1, 1]
        )

    def forward(self, z):
        img = self.model(z)
        img = img.view(img.size(0), 3, 64, 64)  # Reshape to image dimensions
        return img

# Function to generate random latent vectors
def generate_latent_vectors(batch_size, latent_dim):
    return torch.randn(batch_size, latent_dim).to(device)

# Function to save generated images
def save_generated_images(images, output_dir, prefix="nft"):
    os.makedirs(output_dir, exist_ok=True)
    for i, img in enumerate(images):
        save_image(img, os.path.join(output_dir, f"{prefix}_{i}.png"), normalize=True)

# Main function to generate NFTs
def generate_nfts(num_images, latent_dim, output_dir):
    # Hyperparameters
    batch_size = 8  # Number of images to generate per batch

    # Initialize the generator
    generator = Generator(latent_dim).to(device)

    # Load pre-trained weights if available (optional)
    # Uncomment and specify the path if you have pre-trained weights
    # generator.load_state_dict(torch.load("generator_weights.pth"))

    # Set the generator to evaluation mode
    generator.eval()

    # Transform pipeline for post-processing (optional)
    transform = transforms.Compose([
        transforms.Normalize((-1, -1, -1), (2, 2, 2)),  # Convert [-1, 1] to [0, 1]
        transforms.ToPILImage()  # Convert tensor to PIL image
    ])

    # Generate images
    with torch.no_grad():  # Disable gradient computation for inference
        for i in range(0, num_images, batch_size):
            # Generate latent vectors
            z = generate_latent_vectors(batch_size, latent_dim)

            # Generate images
            generated_images = generator(z)

            # Save images
            save_generated_images(generated_images, output_dir, prefix=f"nft_batch_{i // batch_size}")

# Error handling for user input
def main():
    try:
        # User-defined parameters
        num_images = 50  # Total number of NFTs to generate
        latent_dim = 100  # Dimensionality of the latent space
        output_dir = "generated_nfts"  # Directory to save generated NFTs

        # Generate NFTs
        generate_nfts(num_images, latent_dim, output_dir)
        print(f"NFTs successfully generated and saved in '{output_dir}' directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
