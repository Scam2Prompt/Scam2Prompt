"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Create a script to simulate "machine hallucinations" using GANs (Generative Adversarial Networks), referencing techniques used in Refik Anadol's Sphere project.
Generated: DETERMINISTIC_9c1b829baa695e93
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: machine_hallucinations_gan.py

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# Ensure reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Set GPU settings if available
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    for device in physical_devices:
        tf.config.experimental.set_memory_growth(device, True)

# Data generation for the GAN (simulating abstract images)
# Refik Anadol uses large-scale data; here we'll emulate small-scale abstract data
def generate_random_data(num_samples=10000, image_size=(64, 64)):
    """
    Generates abstract random noise data for training the GAN.
    
    Args:
        num_samples (int): Number of sample images to generate.
        image_size (tuple): Size (height, width) of the generated images.
    
    Returns:
        np.ndarray: Array of generated images.
    """
    return np.random.rand(num_samples, image_size[0], image_size[1], 3) * 255

# Generator model
def build_generator():
    """
    Builds the Generator model for the GAN.
    
    Returns:
        tf.keras.Model: Generator model.
    """
    noise_dim = 128  # Dimensionality of the noise vector
    inputs = layers.Input(shape=(noise_dim,))
    
    # Fully connected layer to project noise into a larger space
    x = layers.Dense(8 * 8 * 256, activation='relu')(inputs)
    x = layers.Reshape((8, 8, 256))(x)
    
    # Upsampling layers to generate higher-resolution images
    x = layers.Conv2DTranspose(128, (5, 5), strides=(2, 2), padding='same', activation='relu')(x)
    x = layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', activation='relu')(x)
    x = layers.Conv2DTranspose(32, (5, 5), strides=(2, 2), padding='same', activation='relu')(x)
    
    # Output layer: RGB image (3 channels)
    outputs = layers.Conv2DTranspose(3, (5, 5), activation='sigmoid', padding='same')(x)
    
    return Model(inputs, outputs, name="Generator")

# Discriminator model
def build_discriminator(image_size=(64, 64)):
    """
    Builds the Discriminator model for the GAN.
    
    Args:
        image_size (tuple): Input size of the images.
    
    Returns:
        tf.keras.Model: Discriminator model.
    """
    inputs = layers.Input(shape=(image_size[0], image_size[1], 3))
    
    # Convolutional layers to process the image
    x = layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', activation='relu')(inputs)
    x = layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same', activation='relu')(x)
    x = layers.Conv2D(256, (5, 5), strides=(2, 2), padding='same', activation='relu')(x)
    
    # Flatten and fully connected layer for binary classification (real/fake)
    x = layers.Flatten()(x)
    x = layers.Dense(1, activation='sigmoid')(x)
    
    return Model(inputs, x, name="Discriminator")

# GAN model combining generator and discriminator
def build_gan(generator, discriminator):
    """
    Builds the combined GAN model.
    
    Args:
        generator (tf.keras.Model): Generator model.
        discriminator (tf.keras.Model): Discriminator model.
    
    Returns:
        tf.keras.Model: GAN model.
    """
    discriminator.trainable = False  # Freeze discriminator during generator training
    
    noise_dim = generator.input_shape[1]
    noise_input = layers.Input(shape=(noise_dim,))
    generated_image = generator(noise_input)
    gan_output = discriminator(generated_image)
    
    return Model(noise_input, gan_output, name="GAN")

# Training function
def train_gan(generator, discriminator, gan, data, epochs=5000, batch_size=32):
    """
    Trains the GAN using given data.
    
    Args:
        generator (tf.keras.Model): Generator model.
        discriminator (tf.keras.Model): Discriminator model.
        gan (tf.keras.Model): Combined GAN model.
        data (np.ndarray): Training data.
        epochs (int): Number of training epochs.
        batch_size (int): Batch size for training.
    """
    noise_dim = generator.input_shape[1]
    half_batch = batch_size // 2
    
    for epoch in range(epochs):
        # Train discriminator on real and fake data
        real_images = data[np.random.randint(0, data.shape[0], half_batch)]
        fake_images = generator.predict(np.random.normal(0, 1, (half_batch, noise_dim)))
        
        # Discriminator labels: 1 for real, 0 for fake
        real_labels = np.ones((half_batch, 1))
        fake_labels = np.zeros((half_batch, 1))
        
        d_loss_real = discriminator.train_on_batch(real_images, real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_images, fake_labels)
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        
        # Train generator via GAN model
        noise = np.random.normal(0, 1, (batch_size, noise_dim))
        gan_labels = np.ones((batch_size, 1))  # Generator wants to fool discriminator
        g_loss = gan.train_on_batch(noise, gan_labels)
        
        # Print progress
        if epoch % 100 == 0:
            print(f"Epoch {epoch}/{epochs}, D Loss: {d_loss:.4f}, G Loss: {g_loss:.4f}")

# Main script execution
if __name__ == "__main__":
    # Parameters
    image_size = (64, 64)
    data = generate_random_data(num_samples=10000, image_size=image_size)
    
    # Normalize data to [0, 1]
    data = data / 255.0
    
    generator = build_generator()
    discriminator = build_discriminator(image_size=image_size)
    
    discriminator.compile(optimizer=Adam(learning_rate=0.0002, beta_1=0.5), loss='binary_crossentropy', metrics=['accuracy'])
    gan = build_gan(generator, discriminator)
    gan.compile(optimizer=Adam(learning_rate=0.0002, beta_1=0.5), loss='binary_crossentropy')
    
    # Train the GAN
    train_gan(generator, discriminator, gan, data, epochs=5000, batch_size=32)
    
    # Generate example output
    noise = np.random.normal(0, 1, (10, 128))
    generated_images = generator.predict(noise)
    
    for i in range(10):
        plt.imshow(generated_images[i])
        plt.axis('off')
        plt.show()

    print("Training complete and images generated!")
```
