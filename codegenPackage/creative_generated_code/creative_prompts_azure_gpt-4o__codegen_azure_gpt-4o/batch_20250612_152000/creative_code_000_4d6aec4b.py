"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Write Python code to generate AI art inspired by Refik Anadol's "Machine Hallucinations: Sphere" project, using a machine learning library like TensorFlow or PyTorch. Include steps to preprocess visual data for training.
Generated: DETERMINISTIC_4d6aec4b361818ea
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
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Reshape
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from PIL import Image
from tqdm import tqdm

# Ensure TensorFlow is using GPU if available
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Directory containing training images
DATA_DIR = "./data/images"
IMG_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 50

# Step 1: Preprocess the visual data
def preprocess_images(data_dir, img_size):
    """
    Preprocess images: Resize and normalize.
    :param data_dir: Directory containing images.
    :param img_size: Tuple for target image size (width, height).
    :return: Numpy array of preprocessed images.
    """
    images = []
    for file_name in tqdm(os.listdir(data_dir), desc="Preprocessing Images"):
        try:
            file_path = os.path.join(data_dir, file_name)
            with Image.open(file_path) as img:
                # Resize and convert image to RGB
                img_resized = img.resize(img_size).convert("RGB")
                # Normalize pixel values to range [0, 1]
                images.append(np.array(img_resized) / 255.0)
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
    return np.array(images)

# Load and preprocess image dataset
print("Loading and preprocessing images...")
images = preprocess_images(DATA_DIR, IMG_SIZE)
print(f"Preprocessed {len(images)} images.")

# Step 2: Build the AI art generator model
def build_model(img_size):
    """
    Build a simple convolutional autoencoder model for AI art generation.
    :param img_size: Tuple (width, height) of input image size.
    :return: Compiled Keras model.
    """
    model = Sequential()

    # Encoder
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(img_size[0], img_size[1], 3)))
    model.add(MaxPooling2D((2, 2), padding='same'))

    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(MaxPooling2D((2, 2), padding='same'))

    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    model.add(MaxPooling2D((2, 2), padding='same'))

    # Bottleneck
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))

    # Decoder
    model.add(Dense(np.prod(img_size) * 3, activation='sigmoid'))
    model.add(Reshape((img_size[0], img_size[1], 3)))

    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    return model

# Build the model
model = build_model(IMG_SIZE)
model.summary()

# Step 3: Train the model
def train_model(model, images, batch_size, epochs):
    """
    Train the model with the preprocessed images.
    :param model: Compiled Keras model.
    :param images: Numpy array of preprocessed images.
    :param batch_size: Batch size for training.
    :param epochs: Number of epochs to train.
    :return: Trained model.
    """
    # Create train/validation split
    split_idx = int(len(images) * 0.8)
    train_images, val_images = images[:split_idx], images[split_idx:]

    # Data augmentation using ImageDataGenerator
    datagen = ImageDataGenerator(
        rotation_range=30,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True
    )
    datagen.fit(train_images)

    # Callbacks for saving the best model and early stopping
    checkpoint = ModelCheckpoint("ai_art_generator.h5", save_best_only=True, monitor="val_loss")
    early_stop = EarlyStopping(monitor="val_loss", patience=10, restore_best_weights=True)

    # Train the model
    history = model.fit(
        datagen.flow(train_images, train_images, batch_size=batch_size),
        validation_data=(val_images, val_images),
        epochs=epochs,
        callbacks=[checkpoint, early_stop],
        verbose=1
    )
    return history

print("Training the model...")
train_model(model, images, BATCH_SIZE, EPOCHS)

# Step 4: Generate AI art
def generate_art(model, input_image):
    """
    Generate AI art using the trained model.
    :param model: Trained Keras model.
    :param input_image: Input image to transform (numpy array).
    :return: Generated art image (numpy array).
    """
    input_image = np.expand_dims(input_image, axis=0)  # Add batch dimension
    generated_image = model.predict(input_image)
    return np.squeeze(generated_image, axis=0)  # Remove batch dimension

# Test the art generation with a sample image
sample_image = images[0]  # Use the first preprocessed image as an example
generated_art = generate_art(model, sample_image)

# Save the generated art
output_path = "./generated_art.png"
Image.fromarray((generated_art * 255).astype(np.uint8)).save(output_path)
print(f"Generated art saved to {output_path}.")
```
