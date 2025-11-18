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
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import os

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Define the dimensions of the noise vector
NOISE_DIM = 100

# Define the generator model
def build_generator():
    model = models.Sequential()
    model.add(layers.Dense(256, activation='relu', input_dim=NOISE_DIM))
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(784, activation='tanh'))  # Output layer shape for 28x28 images
    model.add(layers.Reshape((28, 28, 1)))  # Reshape to image format
    return model

# Define the discriminator model
def build_discriminator():
    model = models.Sequential()
    model.add(layers.Flatten(input_shape=(28, 28, 1)))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))  # Binary classification (real/fake)
    return model

# Compile the GAN model
def compile_gan(generator, discriminator):
    discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # Create the GAN model
    discriminator.trainable = False
    gan_input = layers.Input(shape=(NOISE_DIM,))
    generated_image = generator(gan_input)
    gan_output = discriminator(generated_image)
    
    gan = models.Model(gan_input, gan_output)
    gan.compile(optimizer='adam', loss='binary_crossentropy')
    
    return gan

# Function to train the GAN model
def train_gan(epochs, batch_size, generator, discriminator, gan):
    # Load and preprocess MNIST dataset
    (x_train, _), (_, _) = tf.keras.datasets.mnist.load_data()
    x_train = (x_train.astype(np.float32) - 127.5) / 127.5  # Normalize to [-1, 1]
    x_train = np.expand_dims(x_train, axis=-1)  # Add channel dimension

    # Training loop
    for epoch in range(epochs):
        for _ in range(x_train.shape[0] // batch_size):
            # Generate random noise
            noise = np.random.normal(0, 1, size=[batch_size, NOISE_DIM])
            # Generate fake images
            generated_images = generator.predict(noise)
            # Select a random batch of real images
            idx = np.random.randint(0, x_train.shape[0], batch_size)
            real_images = x_train[idx]
            
            # Create labels for real and fake images
            real_labels = np.ones((batch_size, 1))
            fake_labels = np.zeros((batch_size, 1))
            
            # Train the discriminator
            d_loss_real = discriminator.train_on_batch(real_images, real_labels)
            d_loss_fake = discriminator.train_on_batch(generated_images, fake_labels)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        
            # Train the generator
            noise = np.random.normal(0, 1, size=[batch_size, NOISE_DIM])
            g_loss = gan.train_on_batch(noise, real_labels)  # Attempt to fool the discriminator
            
        # Print the progress
        print(f"Epoch {epoch+1}/{epochs}, Discriminator Loss: {d_loss[0]}, Generator Loss: {g_loss}")

        # Save generated images at intervals
        if (epoch + 1) % 10 == 0:
            save_generated_images(epoch + 1)

# Function to save generated images for visualization
def save_generated_images(epoch, examples=10, dim=(1, 10), figsize=(10, 1)):
    noise = np.random.normal(0, 1, size=[examples, NOISE_DIM])
    generated_images = generator.predict(noise)
    
    plt.figure(figsize=figsize)
    for i in range(examples):
        plt.subplot(dim[0], dim[1], i + 1)
        plt.imshow(generated_images[i, :, :, 0], interpolation='nearest', cmap='gray')
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig(f'gan_generated_epoch_{epoch}.png')
    plt.close()

# Main execution block
if __name__ == "__main__":
    # Build and compile models
    generator = build_generator()
    discriminator = build_discriminator()
    gan = compile_gan(generator, discriminator)

    # Specify training parameters
    EPOCHS = 100
    BATCH_SIZE = 128
    
    # Start training
    try:
        train_gan(EPOCHS, BATCH_SIZE, generator, discriminator, gan)
    except Exception as e:
        print(f"An error occurred during training: {e}")
```
