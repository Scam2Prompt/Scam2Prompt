"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Write a program to simulate "seeing like a machine" by training a neural network to generate artistic interpretations of visual data, inspired by Refik Anadol's TED Talk.
Generated: DETERMINISTIC_788e5c358cc10581
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import os
import warnings

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings('ignore')

class MachineVisionArtist:
    """
    A neural network that generates artistic interpretations of visual data.
    Inspired by Refik Anadol's work on machine creativity.
    """
    
    def __init__(self, input_shape=(256, 256, 3)):
        self.input_shape = input_shape
        self.generator = self._build_generator()
        self.discriminator = self._build_discriminator()
        self.gan = self._build_gan()
        
    def _build_generator(self):
        """Build the generator model that creates artistic images."""
        model = models.Sequential()
        
        # Encoder
        model.add(layers.Conv2D(64, (3, 3), padding='same', input_shape=self.input_shape))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization())
        
        model.add(layers.Conv2D(128, (3, 3), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization())
        
        model.add(layers.Conv2D(256, (3, 3), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization())
        
        # Transformer (creative interpretation)
        model.add(layers.Conv2D(512, (3, 3), padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization())
        
        # Decoder
        model.add(layers.Conv2DTranspose(256, (3, 3), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization())
        
        model.add(layers.Conv2DTranspose(128, (3, 3), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization())
        
        model.add(layers.Conv2D(3, (3, 3), activation='tanh', padding='same'))
        
        return model
    
    def _build_discriminator(self):
        """Build the discriminator model that evaluates generated images."""
        model = models.Sequential()
        
        model.add(layers.Conv2D(64, (3, 3), padding='same', input_shape=self.input_shape))
        model.add(layers.LeakyReLU(alpha=0.2))
        
        model.add(layers.Conv2D(128, (3, 3), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        
        model.add(layers.Conv2D(256, (3, 3), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        
        model.add(layers.Flatten())
        model.add(layers.Dropout(0.4))
        model.add(layers.Dense(1, activation='sigmoid'))
        
        opt = optimizers.Adam(learning_rate=0.0002, beta_1=0.5)
        model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
        
        return model
    
    def _build_gan(self):
        """Combine generator and discriminator into GAN."""
        self.discriminator.trainable = False
        model = models.Sequential()
        model.add(self.generator)
        model.add(self.discriminator)
        
        opt = optimizers.Adam(learning_rate=0.0002, beta_1=0.5)
        model.compile(loss='binary_crossentropy', optimizer=opt)
        
        return model
    
    def _load_dataset(self, data_dir, batch_size=32):
        """Load and preprocess training dataset."""
        datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True
        )
        
        dataset = datagen.flow_from_directory(
            data_dir,
            target_size=(self.input_shape[0], self.input_shape[1]),
            batch_size=batch_size,
            class_mode=None
        )
        
        return dataset
    
    def train(self, data_dir, epochs=100, batch_size=32):
        """Train the GAN model."""
        dataset = self._load_dataset(data_dir, batch_size)
        
        half_batch = batch_size // 2
        
        for epoch in range(epochs):
            # Train discriminator
            real_images = next(dataset)
            real_labels = np.ones((half_batch, 1))
            
            noise = np.random.normal(0, 1, (half_batch, *self.input_shape))
            fake_images = self.generator.predict(noise)
            fake_labels = np.zeros((half_batch, 1))
            
            d_loss_real = self.discriminator.train_on_batch(real_images, real_labels)
            d_loss_fake = self.discriminator.train_on_batch(fake_images, fake_labels)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
            
            # Train generator
            noise = np.random.normal(0, 1, (batch_size, *self.input_shape))
            valid_labels = np.ones((batch_size, 1))
            
            g_loss = self.gan.train_on_batch(noise, valid_labels)
            
            # Print progress
            print(f"Epoch {epoch + 1}/{epochs} [D loss: {d_loss[0]:.4f}, acc: {100*d_loss[1]:.2f}%] [G loss: {g_loss:.4f}]")
            
            # Save generated images periodically
            if (epoch + 1) % 10 == 0:
                self._save_generated_images(epoch + 1)
    
    def _save_generated_images(self, epoch, examples=5):
        """Save generated images for visualization."""
        noise = np.random.normal(0, 1, (examples, *self.input_shape))
        generated_images = self.generator.predict(noise)
        
        plt.figure(figsize=(10, 10))
        for i in range(examples):
            plt.subplot(1, examples, i + 1)
            plt.imshow((generated_images[i] + 1) / 2)  # Scale from [-1,1] to [0,1]
            plt.axis('off')
        
        if not os.path.exists('output'):
            os.makedirs('output')
        
        plt.savefig(f'output/generated_art_epoch_{epoch}.png')
        plt.close()
    
    def generate_art(self, input_image=None):
        """Generate artistic interpretation of input image or random noise."""
        if input_image is None:
            noise = np.random.normal(0, 1, (1, *self.input_shape))
            generated_image = self.generator.predict(noise)
        else:
            # Preprocess input image
            if isinstance(input_image, str):
                img = tf.keras.preprocessing.image.load_img(
                    input_image, target_size=self.input_shape[:2]
                )
                input_image = tf.keras.preprocessing.image.img_to_array(img)
                input_image = np.expand_dims(input_image, axis=0) / 255.0
            
            generated_image = self.generator.predict(input_image)
        
        return (generated_image[0] + 1) / 2  # Scale to [0,1] range

# Example usage
if __name__ == "__main__":
    artist = MachineVisionArtist()
    
    try:
        # Train on a dataset (replace with your image directory)
        artist.train(data_dir='path/to/your/images', epochs=50, batch_size=16)
        
        # Generate and save sample artwork
        artwork = artist.generate_art()
        plt.imshow(artwork)
        plt.axis('off')
        plt.savefig('output/final_artwork.png')
        plt.close()
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
