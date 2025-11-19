"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Write a Python script that utilizes machine learning to generate AI art similar to Refik Anadol's "Machine Hallucinations" project.
Generated: DETERMINISTIC_c553d9b7f6cb4255
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import matplotlib.pyplot as plt

# Ensure TensorFlow is using GPU if available
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Define constants
IMAGE_SIZE = (128, 128)  # Size of images for training
LATENT_DIM = 128         # Dimensionality of the latent space
BATCH_SIZE = 32          # Batch size for training
EPOCHS = 100             # Number of training epochs
DATA_DIR = './data'      # Directory containing training images
OUTPUT_DIR = './output'  # Directory to save generated images

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load and preprocess the dataset
def load_images(data_dir, image_size):
    """
    Load images from the specified directory and preprocess them.
    """
    images = []
    for file_name in os.listdir(data_dir):
        try:
            img_path = os.path.join(data_dir, file_name)
            img = Image.open(img_path).convert('RGB')
            img = img.resize(image_size)
            images.append(np.array(img) / 255.0)  # Normalize pixel values to [0, 1]
        except Exception as e:
            print(f"Error loading image {file_name}: {e}")
    return np.array(images)

# Load training data
print("Loading training data...")
train_images = load_images(DATA_DIR, IMAGE_SIZE)
if len(train_images) == 0:
    raise ValueError("No images found in the specified data directory.")

# Build the generator model
def build_generator(latent_dim):
    """
    Build the generator model.
    """
    model = models.Sequential([
        layers.Dense(8 * 8 * 256, input_dim=latent_dim),
        layers.Reshape((8, 8, 256)),
        layers.Conv2DTranspose(128, (5, 5), strides=(2, 2), padding='same', activation='relu'),
        layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', activation='relu'),
        layers.Conv2DTranspose(32, (5, 5), strides=(2, 2), padding='same', activation='relu'),
        layers.Conv2DTranspose(3, (5, 5), strides=(1, 1), padding='same', activation='sigmoid')  # Output RGB image
    ])
    return model

# Build the discriminator model
def build_discriminator(image_size):
    """
    Build the discriminator model.
    """
    model = models.Sequential([
        layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=(image_size[0], image_size[1], 3)),
        layers.LeakyReLU(alpha=0.2),
        layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'),
        layers.LeakyReLU(alpha=0.2),
        layers.Conv2D(256, (5, 5), strides=(2, 2), padding='same'),
        layers.LeakyReLU(alpha=0.2),
        layers.Flatten(),
        layers.Dense(1, activation='sigmoid')  # Output probability
    ])
    return model

# Build GAN model
def build_gan(generator, discriminator):
    """
    Combine generator and discriminator into a GAN model.
    """
    discriminator.trainable = False  # Freeze discriminator during generator training
    model = models.Sequential([generator, discriminator])
    return model

# Instantiate models
print("Building models...")
generator = build_generator(LATENT_DIM)
discriminator = build_discriminator(IMAGE_SIZE)
gan = build_gan(generator, discriminator)

# Compile models
discriminator.compile(optimizer=Adam(learning_rate=0.0002, beta_1=0.5), loss='binary_crossentropy', metrics=['accuracy'])
gan.compile(optimizer=Adam(learning_rate=0.0002, beta_1=0.5), loss='binary_crossentropy')

# Training function
def train_gan(generator, discriminator, gan, train_images, latent_dim, epochs, batch_size):
    """
    Train the GAN model.
    """
    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}/{epochs}")
        for _ in range(len(train_images) // batch_size):
            # Train discriminator
            real_images = train_images[np.random.randint(0, len(train_images), batch_size)]
            fake_images = generator.predict(np.random.normal(0, 1, (batch_size, latent_dim)))
            labels_real = np.ones((batch_size, 1))
            labels_fake = np.zeros((batch_size, 1))
            d_loss_real = discriminator.train_on_batch(real_images, labels_real)
            d_loss_fake = discriminator.train_on_batch(fake_images, labels_fake)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            # Train generator
            noise = np.random.normal(0, 1, (batch_size, latent_dim))
            labels_gan = np.ones((batch_size, 1))  # Generator wants discriminator to think images are real
            g_loss = gan.train_on_batch(noise, labels_gan)

        print(f"Discriminator Loss: {d_loss[0]:.4f}, Accuracy: {d_loss[1]:.4f}")
        print(f"Generator Loss: {g_loss:.4f}")

        # Save generated images for visualization
        if (epoch + 1) % 10 == 0 or epoch == epochs - 1:
            save_generated_images(generator, latent_dim, epoch + 1)

# Save generated images
def save_generated_images(generator, latent_dim, epoch):
    """
    Save generated images to the output directory.
    """
    noise = np.random.normal(0, 1, (10, latent_dim))
    generated_images = generator.predict(noise)
    for i, img_array in enumerate(generated_images):
        img = Image.fromarray((img_array * 255).astype(np.uint8))
        img.save(os.path.join(OUTPUT_DIR, f"epoch_{epoch}_image_{i + 1}.png"))

# Train the GAN
print("Starting training...")
train_gan(generator, discriminator, gan, train_images, LATENT_DIM, EPOCHS, BATCH_SIZE)

print("Training complete. Generated images saved to output directory.")
```
