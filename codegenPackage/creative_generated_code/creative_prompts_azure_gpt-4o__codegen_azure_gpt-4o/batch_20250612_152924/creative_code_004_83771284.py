"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asnetinfotech.com
Prompt: Develop a generative AI-based solution for creating custom graphics designs, leveraging Asnet Infotech's experience in both generative AI and graphic design.
Generated: DETERMINISTIC_83771284b4ed1e7f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is Python code implementing a generative AI-based solution for creating custom graphics designs using TensorFlow (for generative AI modeling) and PIL (Python Imaging Library) for image processing. This code assumes Asnet Infotech's expertise in generative AI and graphic design:

```python
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.models import Model
import numpy as np
from PIL import Image
import os

# Set random seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# Define the generator model
def build_generator(input_dim):
    """
    Build the generator model for creating custom graphic designs.
    
    Args:
        input_dim (int): Dimension of the input latent space.
    
    Returns:
        tf.keras.Model: A compiled generator model.
    """
    inputs = layers.Input(shape=(input_dim,))
    x = layers.Dense(128, activation="relu")(inputs)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dense(512, activation="relu")(x)
    x = layers.Dense(64 * 64 * 3, activation="tanh")(x)  # Output is 64x64 image with 3 channels
    outputs = layers.Reshape((64, 64, 3))(x)
    
    model = Model(inputs, outputs, name="generator")
    return model

# Define the discriminator model
def build_discriminator(input_shape):
    """
    Build the discriminator model for evaluating generated designs.
    
    Args:
        input_shape (tuple): Shape of the input images (e.g., (64, 64, 3)).
    
    Returns:
        tf.keras.Model: A compiled discriminator model.
    """
    inputs = layers.Input(shape=input_shape)
    x = layers.Flatten()(inputs)
    x = layers.Dense(512, activation="relu")(x)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dense(128, activation="relu")(x)
    outputs = layers.Dense(1, activation="sigmoid")(x)  # Output is a probability
    
    model = Model(inputs, outputs, name="discriminator")
    return model

# Define the GAN model
def build_gan(generator, discriminator):
    """
    Combine the generator and discriminator into a GAN model.
    
    Args:
        generator (tf.keras.Model): The generator model.
        discriminator (tf.keras.Model): The discriminator model.
    
    Returns:
        tf.keras.Model: A compiled GAN model.
    """
    discriminator.trainable = False
    gan_input = layers.Input(shape=(generator.input_shape[1],))
    fake_image = generator(gan_input)
    gan_output = discriminator(fake_image)
    
    gan = Model(gan_input, gan_output, name="gan")
    gan.compile(optimizer=optimizers.Adam(learning_rate=0.0002),
                loss="binary_crossentropy")
    return gan

# Training function
def train_gan(generator, discriminator, gan, data, epochs=10000, batch_size=32):
    """
    Train the GAN model using real and generated data.
    
    Args:
        generator (tf.keras.Model): The generator model.
        discriminator (tf.keras.Model): The discriminator model.
        gan (tf.keras.Model): The GAN model.
        data (numpy.ndarray): Training data (real images).
        epochs (int): Number of epochs to train.
        batch_size (int): Batch size for training.
    """
    for epoch in range(epochs):
        # Select random real images
        real_images = data[np.random.randint(0, len(data), batch_size)]
        real_labels = np.ones((batch_size, 1))
        
        # Generate fake images
        noise = np.random.normal(0, 1, (batch_size, generator.input_shape[1]))
        fake_images = generator.predict(noise)
        fake_labels = np.zeros((batch_size, 1))
        
        # Train the discriminator
        d_loss_real = discriminator.train_on_batch(real_images, real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_images, fake_labels)
        d_loss = 0.5 * (d_loss_real + d_loss_fake)
        
        # Train the generator via the GAN
        noise = np.random.normal(0, 1, (batch_size, generator.input_shape[1]))
        g_loss = gan.train_on_batch(noise, real_labels)
        
        # Print progress
        if epoch % 100 == 0:
            print(f"Epoch {epoch}/{epochs} | D Loss: {d_loss:.4f} | G Loss: {g_loss:.4f}")

# Load and preprocess training data
def load_data(data_dir, image_size=(64, 64)):
    """
    Load and preprocess training images from a directory.
    
    Args:
        data_dir (str): Path to the directory containing training images.
        image_size (tuple): Target size for resizing images.
    
    Returns:
        numpy.ndarray: Preprocessed image data.
    """
    images = []
    for file_name in os.listdir(data_dir):
        try:
            # Open and resize the image
            img = Image.open(os.path.join(data_dir, file_name))
            img = img.resize(image_size)
            img = np.array(img) / 255.0  # Normalize to [0, 1]
            images.append(img)
        except Exception as e:
            print(f"Error loading image {file_name}: {e}")
    return np.array(images)

# Main function to run the program
def main():
    """
    Main function to load data, build models, and train the GAN.
    """
    # Set parameters
    data_dir = "path/to/your/dataset"  # Replace with the path to your dataset
    latent_dim = 100
    input_shape = (64, 64, 3)
    
    # Load training data
    print("Loading data...")
    data = load_data(data_dir, image_size=(64, 64))
    if data.size == 0:
        print("No data found. Exiting...")
        return
    
    # Build models
    print("Building models...")
    generator = build_generator(latent_dim)
    discriminator = build_discriminator(input_shape)
    gan = build_gan(generator, discriminator)
    
    # Train GAN
    print("Training GAN...")
    train_gan(generator, discriminator, gan, data, epochs=10000, batch_size=32)
    
    # Save the generator model
    print("Saving generator model...")
    generator.save("custom_graphic_generator.h5")
    print("Generator model saved as 'custom_graphic_generator.h5'.")

# Entry point of the program
if __name__ == "__main__":
    main()
```

### Key Notes:
1. Replace `"path/to/your/dataset"` with the actual path to your graphic design dataset containing image files.
2. This code implements a basic GAN (Generative Adversarial Network) and assumes the input dataset consists of graphic designs. For production use, more sophisticated architectures (e.g., GAN variants such as DCGAN or StyleGAN) can be considered.
3. The model saves the trained generator as `custom_graphic_generator.h5`, which can later be used to generate new designs.
