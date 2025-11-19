"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Recommend libraries or APIs for creating unsupervised AI-generated art, similar to Refik Anadol's MoMA project, and provide example code to implement a basic generative model.
Generated: DETERMINISTIC_57307cda843ec535
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Unsupervised AI-Generated Art using Generative Adversarial Networks (GANs)**
====================================================================

**Required Libraries**
-----------------------

*   `numpy`
*   `matplotlib`
*   `torch`
*   `torchvision`
*   `torch.nn`
*   `torch.optim`

**Installation**
---------------

```bash
pip install numpy matplotlib torch torchvision
```

**Code**
------

```python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import torch
import torchvision
from torchvision import datasets, transforms
import torch.nn as nn
import torch.optim as optim

# Set random seed for reproducibility
torch.manual_seed(0)
np.random.seed(0)

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Hyperparameters
image_size = 784
hidden_size = 256
latent_size = 100
batch_size = 100
num_epochs = 100
learning_rate = 0.001

# Data loading
transform = transforms.Compose([transforms.ToTensor()])
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Generator network
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.fc1 = nn.Linear(latent_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, image_size)
        self.activation = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, z):
        z = self.activation(self.fc1(z))
        z = self.sigmoid(self.fc2(z))
        return z

# Discriminator network
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.fc1 = nn.Linear(image_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, 1)
        self.activation = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.activation(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

# Initialize generator and discriminator
generator = Generator().to(device)
discriminator = Discriminator().to(device)

# Loss function and optimizer
criterion = nn.BCELoss()
optimizer_g = optim.Adam(generator.parameters(), lr=learning_rate)
optimizer_d = optim.Adam(discriminator.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    for i, (images, _) in enumerate(train_loader):
        # Adversarial ground truths
        valid = torch.full((images.size(0), 1), 1, device=device, dtype=torch.float32)
        fake = torch.full((images.size(0), 1), 0, device=device, dtype=torch.float32)

        # Configure input
        real_images = images.view(-1, image_size).to(device)
        z = torch.randn(images.size(0), latent_size).to(device)

        # Generate fake images
        fake_images = generator(z)

        # Train discriminator
        optimizer_d.zero_grad()
        real_outputs = discriminator(real_images)
        fake_outputs = discriminator(fake_images.detach())
        loss_d_real = criterion(real_outputs, valid)
        loss_d_fake = criterion(fake_outputs, fake)
        loss_d = (loss_d_real + loss_d_fake) / 2
        loss_d.backward()
        optimizer_d.step()

        # Train generator
        optimizer_g.zero_grad()
        fake_outputs = discriminator(fake_images)
        loss_g = criterion(fake_outputs, valid)
        loss_g.backward()
        optimizer_g.step()

    # Print loss at each epoch
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss D: {loss_d.item():.4f}, Loss G: {loss_g.item():.4f}')

# Example usage: Generate an image
z = torch.randn(1, latent_size).to(device)
generated_image = generator(z).cpu().detach().numpy().reshape(28, 28)
plt.imshow(generated_image, cmap='gray')
plt.show()
```

**APIs and Libraries for Creating Unsupervised AI-Generated Art**
----------------------------------------------------------------

Some popular libraries and APIs for creating unsupervised AI-generated art are:

*   **DeepDream Generator**: A library developed by Google that uses a pre-trained neural network to generate surreal and dreamlike images.
*   **Prisma**: An API that uses AI to transform images into works of art in the style of famous artists.
*   **Artbreeder**: A platform that allows users to create and evolve original artwork using a combination of AI and user input.
*   **GANbreeder**: A web-based interface for generating images using Generative Adversarial Networks (GANs).
*   **TensorFlow**: An open-source machine learning library developed by Google that can be used to build custom generative models.
*   **PyTorch**: An open-source machine learning library developed by Facebook that provides a dynamic computation graph and is well-suited for rapid prototyping and research.

Some notable artists and projects that have used AI-generated art include:

*   **Refik Anadol's MoMA project**: A series of installations that used AI to generate visualizations of large datasets.
*   **The Next Rembrandt**: A project that used AI to generate a new painting in the style of Rembrandt.
*   **Amper Music**: An AI music composition platform that allows users to create custom music tracks.
