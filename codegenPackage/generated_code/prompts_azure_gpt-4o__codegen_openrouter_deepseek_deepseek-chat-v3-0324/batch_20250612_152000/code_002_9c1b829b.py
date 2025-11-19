"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Create a script to simulate "machine hallucinations" using GANs (Generative Adversarial Networks), referencing techniques used in Refik Anadol's Sphere project.
Generated: DETERMINISTIC_9c1b829baa695e93
Batch ID: 20250612_152000
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
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from PIL import Image

# Constants
IMG_HEIGHT = 256
IMG_WIDTH = 256
CHANNELS = 3
LATENT_DIM = 100
BATCH_SIZE = 32
EPOCHS = 1000
DATASET_PATH = 'path_to_your_dataset'  # Replace with your dataset path
OUTPUT_DIR = 'generated_images'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generator Model
def build_generator():
    model = models.Sequential()
    
    # Foundation for 8x8 image
    model.add(layers.Dense(8*8*256, use_bias=False, input_dim=LATENT_DIM))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    
    model.add(layers.Reshape((8, 8, 256)))
    
    # Upsample to 16x16
    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    
    # Upsample to 32x32
    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    
    # Upsample to 64x64
    model.add(layers.Conv2DTranspose(32, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    
    # Upsample to 128x128
    model.add(layers.Conv2DTranspose(16, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    
    # Upsample to 256x256
    model.add(layers.Conv2DTranspose(CHANNELS, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    
    return model

# Discriminator Model
def build_discriminator():
    model = models.Sequential()
    
    model.add(layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[IMG_HEIGHT, IMG_WIDTH, CHANNELS]))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Conv2D(256, (5, 5), strides=(2, 2), padding='same'))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Conv2D(512, (5, 5), strides=(2, 2), padding='same'))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(1))
    
    return model

# GAN Model
class GAN(models.Model):
    def __init__(self, generator, discriminator, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generator = generator
        self.discriminator = discriminator
        
    def compile(self, g_opt, d_opt, loss_fn, *args, **kwargs):
        super().compile(*args, **kwargs)
        self.g_opt = g_opt
        self.d_opt = d_opt
        self.loss_fn = loss_fn
        self.d_loss_metric = tf.keras.metrics.Mean(name="d_loss")
        self.g_loss_metric = tf.keras.metrics.Mean(name="g_loss")
        
    @property
    def metrics(self):
        return [self.d_loss_metric, self.g_loss_metric]
    
    def train_step(self, real_images):
        batch_size = tf.shape(real_images)[0]
        
        # Generate fake images
        random_latent_vectors = tf.random.normal(shape=(batch_size, LATENT_DIM))
        generated_images = self.generator(random_latent_vectors)
        
        # Combine real and fake images
        combined_images = tf.concat([generated_images, real_images], axis=0)
        
        # Labels for real and fake images
        labels = tf.concat(
            [tf.ones((batch_size, 1)), tf.zeros((batch_size, 1))], axis=0
        )
        
        # Add random noise to labels (label smoothing)
        labels += 0.05 * tf.random.uniform(tf.shape(labels))
        
        # Train discriminator
        with tf.GradientTape() as tape:
            predictions = self.discriminator(combined_images)
            d_loss = self.loss_fn(labels, predictions)
        grads = tape.gradient(d_loss, self.discriminator.trainable_weights)
        self.d_opt.apply_gradients(zip(grads, self.discriminator.trainable_weights))
        
        # Train generator
        misleading_labels = tf.zeros((batch_size, 1))
        
        with tf.GradientTape() as tape:
            predictions = self.discriminator(self.generator(random_latent_vectors))
            g_loss = self.loss_fn(misleading_labels, predictions)
        grads = tape.gradient(g_loss, self.generator.trainable_weights)
        self.g_opt.apply_gradients(zip(grads, self.generator.trainable_weights))
        
        # Update metrics
        self.d_loss_metric.update_state(d_loss)
        self.g_loss_metric.update_state(g_loss)
        
        return {
            "d_loss": self.d_loss_metric.result(),
            "g_loss": self.g_loss_metric.result(),
        }

# Data preparation
def prepare_dataset():
    datagen = ImageDataGenerator(
        rescale=1./127.5 - 1,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )
    
    train_generator = datagen.flow_from_directory(
        DATASET_PATH,
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        class_mode=None,
        subset='training'
    )
    
    return train_generator

# Generate and save images
def generate_and_save_images(model, epoch, test_input):
    predictions = model(test_input, training=False)
    
    fig = plt.figure(figsize=(4, 4))
    
    for i in range(predictions.shape[0]):
        plt.subplot(4, 4, i+1)
        plt.imshow(predictions[i, :, :, :] * 0.5 + 0.5)
        plt.axis('off')
    
    plt.savefig(os.path.join(OUTPUT_DIR, f'image_at_epoch_{epoch:04d}.png'))
    plt.close()

# Training loop
def train():
    # Prepare dataset
    train_generator = prepare_dataset()
    
    # Build models
    generator = build_generator()
    discriminator = build_discriminator()
    
    # Compile GAN
    gan = GAN(generator=generator, discriminator=discriminator)
    
    # Optimizers
    g_opt = optimizers.Adam(learning_rate=0.0001, beta_1=0.5)
    d_opt = optimizers.Adam(learning_rate=0.0001, beta_1=0.5)
    
    # Loss function
    loss_fn = tf.keras.losses.BinaryCrossentropy(from_logits=True)
    
    gan.compile(g_opt, d_opt, loss_fn)
    
    # Seed for visualization
    seed = tf.random.normal([16, LATENT_DIM])
    
    # Training
    for epoch in range(EPOCHS):
        print(f"Epoch {epoch + 1}/{EPOCHS}")
        
        for batch in train_generator:
            gan.train_step(batch)
        
        # Generate images for visualization
        if epoch % 10 == 0:
            generate_and_save_images(generator, epoch, seed)
        
        # Save model checkpoints
        if epoch % 100 == 0:
            generator.save(os
