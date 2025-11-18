"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Write a program to simulate "seeing like a machine" by training a neural network to generate artistic interpretations of visual data, inspired by Refik Anadol's TED Talk.
Generated: DETERMINISTIC_788e5c358cc10581
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
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import random

# Ensure TensorFlow logs less verbose output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Set random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Constants
DATA_DIR = "./images"  # Directory where images are stored
IMG_WIDTH = 128
IMG_HEIGHT = 128
BATCH_SIZE = 32
EPOCHS = 50
LATENT_DIM = 128  # Dimension of the latent space

# Verify data directory exists
if not os.path.exists(DATA_DIR):
    raise FileNotFoundError(f"Data directory '{DATA_DIR}' not found.")

# Data preprocessing using ImageDataGenerator
data_gen = ImageDataGenerator(rescale=1.0 / 255.0)
train_generator = data_gen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode=None,
    shuffle=True,
)

# Build the neural network: Autoencoder architecture
def build_autoencoder(img_shape, latent_dim):
    """
    Builds an autoencoder model with the specified image shape and latent dimension.

    Parameters:
    img_shape (tuple): Input image shape (height, width, channels).
    latent_dim (int): Dimension of the latent space.

    Returns:
    autoencoder (tf.keras.Model): The compiled autoencoder model.
    """
    # Encoder
    encoder_input = layers.Input(shape=img_shape, name="encoder_input")
    x = layers.Conv2D(32, (3, 3), activation="relu", padding="same")(encoder_input)
    x = layers.MaxPooling2D((2, 2), padding="same")(x)
    x = layers.Conv2D(64, (3, 3), activation="relu", padding="same")(x)
    x = layers.MaxPooling2D((2, 2), padding="same")(x)
    x = layers.Flatten()(x)
    latent_output = layers.Dense(latent_dim, activation="relu", name="latent_output")(x)

    encoder = models.Model(encoder_input, latent_output, name="encoder")

    # Decoder
    decoder_input = layers.Input(shape=(latent_dim,), name="decoder_input")
    x = layers.Dense((IMG_WIDTH // 4) * (IMG_HEIGHT // 4) * 64, activation="relu")(decoder_input)
    x = layers.Reshape((IMG_WIDTH // 4, IMG_HEIGHT // 4, 64))(x)
    x = layers.Conv2DTranspose(64, (3, 3), activation="relu", padding="same")(x)
    x = layers.UpSampling2D((2, 2))(x)
    x = layers.Conv2DTranspose(32, (3, 3), activation="relu", padding="same")(x)
    x = layers.UpSampling2D((2, 2))(x)
    decoder_output = layers.Conv2DTranspose(3, (3, 3), activation="sigmoid", padding="same", name="decoder_output")(x)

    decoder = models.Model(decoder_input, decoder_output, name="decoder")

    # Autoencoder
    autoencoder_input = encoder_input
    encoded = encoder(autoencoder_input)
    decoded = decoder(encoded)
    autoencoder = models.Model(autoencoder_input, decoded, name="autoencoder")

    return autoencoder, encoder, decoder


# Build and compile the autoencoder
img_shape = (IMG_WIDTH, IMG_HEIGHT, 3)
autoencoder, encoder, decoder = build_autoencoder(img_shape, LATENT_DIM)

autoencoder.compile(optimizer=optimizers.Adam(learning_rate=0.001), loss="mse")

# Summary of the model
autoencoder.summary()

# Training the autoencoder
print("Starting training...")
history = autoencoder.fit(
    train_generator,
    epochs=EPOCHS,
    steps_per_epoch=len(train_generator),
    verbose=1,
)

# Save the model
MODEL_DIR = "./models"
os.makedirs(MODEL_DIR, exist_ok=True)
autoencoder.save(os.path.join(MODEL_DIR, "autoencoder.h5"))
encoder.save(os.path.join(MODEL_DIR, "encoder.h5"))
decoder.save(os.path.join(MODEL_DIR, "decoder.h5"))
print(f"Models saved to {MODEL_DIR}")

# Visualize results
def visualize_results(autoencoder, generator, num_images=5):
    """
    Visualizes original images and their reconstructed counterparts.

    Parameters:
    autoencoder (tf.keras.Model): Trained autoencoder model.
    generator (tf.keras.preprocessing.image.ImageDataGenerator): Image generator for loading images.
    num_images (int): Number of images to visualize.
    """
    images = next(generator)
    selected_images = images[:num_images]
    reconstructed_images = autoencoder.predict(selected_images)

    plt.figure(figsize=(10, 5))
    for i in range(num_images):
        # Original image
        plt.subplot(2, num_images, i + 1)
        plt.imshow(selected_images[i])
        plt.title("Original")
        plt.axis("off")

        # Reconstructed image
        plt.subplot(2, num_images, i + 1 + num_images)
        plt.imshow(reconstructed_images[i])
        plt.title("Reconstructed")
        plt.axis("off")

    plt.tight_layout()
    plt.show()


# Visualize a few example reconstructions
visualize_results(autoencoder, train_generator)
```
