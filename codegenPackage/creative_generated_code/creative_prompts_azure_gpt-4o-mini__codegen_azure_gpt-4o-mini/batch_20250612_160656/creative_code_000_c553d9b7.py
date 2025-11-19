"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Write a Python script that utilizes machine learning to generate AI art similar to Refik Anadol's "Machine Hallucinations" project.
Generated: DETERMINISTIC_c553d9b7f6cb4255
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from tensorflow.keras.applications import VGG16
from PIL import Image
import os

# Set constants
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
BATCH_SIZE = 32
EPOCHS = 50
DATASET_DIR = 'path/to/your/dataset'  # Specify path to your dataset

# Function to load images and preprocess them
def load_and_preprocess_images(data_dir):
    """
    Load images from a directory and preprocess them for training.
    
    Parameters:
        data_dir (str): Directory containing the images.

    Returns:
        np.array: Array of preprocessed images.
    """
    images = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(data_dir, filename)
            try:
                img = Image.open(img_path)
                img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
                img_array = np.array(img) / 255.0  # Normalize pixel values
                images.append(img_array)
            except Exception as e:
                print(f"Error loading image {filename}: {e}")
    return np.array(images)

# Load dataset
X_train = load_and_preprocess_images(DATASET_DIR)

# Data augmentation
data_gen = ImageDataGenerator(rotation_range=20,
                               width_shift_range=0.2,
                               height_shift_range=0.2,
                               shear_range=0.2,
                               zoom_range=0.2,
                               horizontal_flip=True,
                               fill_mode='nearest')

# Create the model using VGG16 as a base
def create_model():
    """
    Create a sequential model using VGG16 as a base.

    Returns:
        keras.Model: Compiled convolutional neural network model.
    """
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3))
    model = Sequential()
    model.add(base_model)
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3, activation='sigmoid'))  # Assuming 3 channels for output
    model.compile(optimizer=Adam(), loss='mean_squared_error')
    return model

# Create the model
model = create_model()

# Callbacks for early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model
try:
    model.fit(data_gen.flow(X_train, batch_size=BATCH_SIZE), 
              epochs=EPOCHS, 
              validation_split=0.2, 
              callbacks=[early_stopping])
except Exception as e:
    print(f"Error during training: {e}")

# Function to generate AI art
def generate_art(model, num_images=5):
    """
    Generate AI art using the trained model.

    Parameters:
        model (keras.Model): Trained model to generate art.
        num_images (int): Number of art images to generate.
    """
    for i in range(num_images):
        noise = np.random.normal(0, 1, (1, IMAGE_WIDTH, IMAGE_HEIGHT, 3))
        generated_image = model.predict(noise)
        generated_image = (generated_image.squeeze() * 255).astype(np.uint8)  # Convert to image format
        plt.imshow(generated_image)
        plt.axis('off')
        plt.savefig(f'generated_art_{i}.png', bbox_inches='tight')
        plt.show()

# Generate AI art
generate_art(model)
``` 

Make sure to replace `'path/to/your/dataset'` with the actual path where the dataset of images is located.
