"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Write a Python code to generate AI art using machine learning, inspired by Refik Anadol's Machine Hallucinations project.
Generated: DETERMINISTIC_6ceddcac5a5bd560
Batch ID: 20250622_205623
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
from tensorflow.keras import layers
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
IMAGE_SIZE = 256
LATENT_DIM = 512
BATCH_SIZE = 16
EPOCHS = 50
CHECKPOINT_DIR = './training_checkpoints'
OUTPUT_DIR = './generated_art'

# Create directories if they don't exist
os.makedirs(CHECKPOINT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

class GAN:
    def __init__(self):
        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()
        self.gan = self.build_gan()
        
    def build_generator(self):
        model = tf.keras.Sequential()
        model.add(layers.Dense(8*8*256, use_bias=False, input_shape=(LATENT_DIM,)))
        model.add(layers.BatchNormalization())
        model.add(layers.LeakyReLU())
        
        model.add(layers.Reshape((8, 8, 256)))
        assert model.output_shape == (None, 8, 8, 256)
        
        model.add(layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
        assert model.output_shape == (None, 8, 8, 128)
        model.add(layers.BatchNormalization())
        model.add(layers.LeakyReLU())

        model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
        assert model.output_shape == (None, 16, 16, 64)
        model.add(layers.BatchNormalization())
        model.add(layers.LeakyReLU())

        model.add(layers.Conv2DTranspose(32, (5, 5), strides=(2, 2), padding='same', use_bias=False))
        assert model.output_shape == (None, 32, 32, 32)
        model.add(layers.BatchNormalization())
        model.add(layers.LeakyReLU())

        model.add(layers.Conv2DTranspose(3, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
        assert model.output_shape == (None, 64, 64, 3)
        
        return model
    
    def build_discriminator(self):
        model = tf.keras.Sequential()
        model.add(layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[64, 64, 3]))
        model.add(layers.LeakyReLU())
        model.add(layers.Dropout(0.3))

        model.add(layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU())
        model.add(layers.Dropout(0.3))

        model.add(layers.Flatten())
        model.add(layers.Dense(1))
        
        return model
    
    def build_gan(self):
        self.discriminator.trainable = False
        gan_input = layers.Input(shape=(LATENT_DIM,))
        gan_output = self.discriminator(self.generator(gan_input))
        gan = tf.keras.Model(gan_input, gan_output)
        gan.compile(optimizer=tf.keras.optimizers.Adam(0.0002, 0.5), loss='binary_crossentropy')
        return gan

def load_dataset(dataset_path):
    try:
        images = []
        for filename in os.listdir(dataset_path):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                img = Image.open(os.path.join(dataset_path, filename))
                img = img.resize((64, 64))
                img = np.array(img)
                images.append(img)
        images = np.array(images)
        images = (images - 127.5) / 127.5  # Normalize to [-1, 1]
        return images
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def train(gan, dataset, epochs=EPOCHS, batch_size=BATCH_SIZE):
    checkpoint_prefix = os.path.join(CHECKPOINT_DIR, "ckpt")
    checkpoint = tf.train.Checkpoint(
        generator_optimizer=tf.keras.optimizers.Adam(0.0002, 0.5),
        discriminator_optimizer=tf.keras.optimizers.Adam(0.0002, 0.5),
        generator=gan.generator,
        discriminator=gan.discriminator
    )
    
    real_labels = np.ones((batch_size, 1))
    fake_labels = np.zeros((batch_size, 1))
    
    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}/{epochs}")
        
        for i in range(dataset.shape[0] // batch_size):
            # Train discriminator
            real_images = dataset[i * batch_size : (i + 1) * batch_size]
            noise = np.random.normal(0, 1, (batch_size, LATENT_DIM))
            fake_images = gan.generator.predict(noise)
            
            d_loss_real = gan.discriminator.train_on_batch(real_images, real_labels)
            d_loss_fake = gan.discriminator.train_on_batch(fake_images, fake_labels)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
            
            # Train generator
            noise = np.random.normal(0, 1, (batch_size, LATENT_DIM))
            g_loss = gan.gan.train_on_batch(noise, real_labels)
            
            if i % 100 == 0:
                print(f"Batch {i}: D loss: {d_loss}, G loss: {g_loss}")
                generate_and_save_images(gan.generator, epoch, i)
        
        if (epoch + 1) % 5 == 0:
            checkpoint.save(file_prefix=checkpoint_prefix)

def generate_and_save_images(model, epoch, batch):
    predictions = model.predict(np.random.normal(0, 1, (4, LATENT_DIM)))
    fig = plt.figure(figsize=(10, 10))
    
    for i in range(predictions.shape[0]):
        plt.subplot(2, 2, i + 1)
        plt.imshow((predictions[i] * 0.5 + 0.5))  # Scale back to [0,1]
        plt.axis('off')
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"image_epoch_{epoch}_batch_{batch}_{timestamp}.png"
    plt.savefig(os.path.join(OUTPUT_DIR, filename))
    plt.close()

def main():
    # Initialize GAN
    gan = GAN()
    
    # Load dataset (replace with your dataset path)
    dataset_path = './dataset'
    dataset = load_dataset(dataset_path)
    
    if dataset is None:
        print("Failed to load dataset. Exiting.")
        return
    
    # Train GAN
    train(gan, dataset)
    
    # Generate final images
    generate_and_save_images(gan.generator, EPOCHS, 0)

if __name__ == "__main__":
    main()
```
