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
# Import necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Define constants
IMG_WIDTH, IMG_HEIGHT = 512, 512
LATENT_DIM = 100

# Load and preprocess dataset
def load_dataset(data_dir, img_width, img_height):
    """Loads and preprocesses dataset"""
    try:
        dataset = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            labels='inferred',
            label_mode='int',
            batch_size=32,
            image_size=(img_width, img_height)
        )
        return dataset
    except Exception as e:
        print(f"Error loading dataset: {e}")

# Define generator model
def define_generator(latent_dim):
    """Defines generator model"""
    model = keras.Sequential([
        keras.layers.Dense(7*7*256, use_bias=False, input_shape=(latent_dim,)),
        keras.layers.BatchNormalization(),
        keras.layers.LeakyReLU(),
        
        keras.layers.Reshape((7, 7, 256)),
        keras.layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False),
        keras.layers.BatchNormalization(),
        keras.layers.LeakyReLU(),
        
        keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False),
        keras.layers.BatchNormalization(),
        keras.layers.LeakyReLU(),
        
        keras.layers.Conv2DTranspose(3, (5, 5), strides=(2, 2), padding='same', activation='tanh', use_bias=False)
    ])
    return model

# Define discriminator model
def define_discriminator():
    """Defines discriminator model"""
    model = keras.Sequential([
        keras.layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[512, 512, 3]),
        keras.layers.LeakyReLU(),
        keras.layers.Dropout(0.3),
        
        keras.layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'),
        keras.layers.LeakyReLU(),
        keras.layers.Dropout(0.3),
        
        keras.layers.Flatten(),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

# Define GAN model
class GAN(keras.Model):
    """Defines GAN model"""
    def __init__(self, generator, discriminator, latent_dim):
        super(GAN, self).__init__()
        self.generator = generator
        self.discriminator = discriminator
        self.latent_dim = latent_dim

    def compile(self, g_optimizer, d_optimizer, loss_fn):
        super(GAN, self).compile()
        self.g_optimizer = g_optimizer
        self.d_optimizer = d_optimizer
        self.loss_fn = loss_fn

    def train_step(self, real_images):
        batch_size = tf.shape(real_images)[0]

        # Sample latent vectors
        latent_vectors = tf.random.normal(shape=(batch_size, self.latent_dim))

        # Generate fake images
        fake_images = self.generator(latent_vectors, training=True)

        # Combine real and fake images
        combined_images = tf.concat([real_images, fake_images], axis=0)

        # Create labels for real and fake images
        labels = tf.concat([tf.ones((batch_size, 1)), tf.zeros((batch_size, 1))], axis=0)

        # Train discriminator
        with tf.GradientTape() as tape:
            predictions = self.discriminator(combined_images, training=True)
            d_loss = self.loss_fn(labels, predictions)
        grads = tape.gradient(d_loss, self.discriminator.trainable_weights)
        self.d_optimizer.apply_gradients(zip(grads, self.discriminator.trainable_weights))

        # Sample new latent vectors
        latent_vectors = tf.random.normal(shape=(batch_size, self.latent_dim))

        # Generate fake images
        fake_images = self.generator(latent_vectors, training=True)

        # Create labels for fake images
        labels = tf.ones((batch_size, 1))

        # Train generator
        with tf.GradientTape() as tape:
            predictions = self.discriminator(fake_images, training=True)
            g_loss = self.loss_fn(labels, predictions)
        grads = tape.gradient(g_loss, self.generator.trainable_weights)
        self.g_optimizer.apply_gradients(zip(grads, self.generator.trainable_weights))

        return {"d_loss": d_loss, "g_loss": g_loss}

# Main function
def main():
    # Load dataset
    dataset = load_dataset('./data', IMG_WIDTH, IMG_HEIGHT)

    # Define generator and discriminator models
    generator = define_generator(LATENT_DIM)
    discriminator = define_discriminator()

    # Define GAN model
    gan = GAN(generator, discriminator, LATENT_DIM)

    # Compile GAN model
    gan.compile(
        g_optimizer=keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
        d_optimizer=keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
        loss_fn=keras.losses.BinaryCrossentropy(from_logits=True)
    )

    # Train GAN model
    history = gan.fit(dataset, epochs=100)

    # Save generator model
    generator.save('generator_model.h5')

    # Use generator to create AI art
    def create_art(generator, latent_dim):
        latent_vector = tf.random.normal(shape=(1, latent_dim))
        art = generator.predict(latent_vector)
        art = (art + 1) / 2
        return art

    art = create_art(generator, LATENT_DIM)
    art = Image.fromarray(np.uint8(art * 255))
    art.show()

if __name__ == "__main__":
    main()
```
