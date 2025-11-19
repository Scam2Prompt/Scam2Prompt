"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Generate Python code to implement a machine learning algorithm for object detection using multimodal data sources like optical and thermal cameras.
Generated: DETERMINISTIC_854da67be8de44df
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import cv2
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Constants
IMAGE_SIZE = (224, 224)  # Input image size for the model
BATCH_SIZE = 32           # Number of samples per gradient update
EPOCHS = 50               # Number of epochs to train the model
DATA_DIR = 'data/'        # Directory containing the dataset

# Function to load images from a directory
def load_images_from_directory(directory):
    images = []
    labels = []
    for label in os.listdir(directory):
        label_dir = os.path.join(directory, label)
        if os.path.isdir(label_dir):
            for img_file in os.listdir(label_dir):
                img_path = os.path.join(label_dir, img_file)
                try:
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, IMAGE_SIZE)
                    images.append(img)
                    labels.append(label)
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
    return np.array(images), np.array(labels)

# Load optical and thermal images
optical_images, optical_labels = load_images_from_directory(os.path.join(DATA_DIR, 'optical'))
thermal_images, thermal_labels = load_images_from_directory(os.path.join(DATA_DIR, 'thermal'))

# Combine optical and thermal data
images = np.concatenate((optical_images, thermal_images), axis=0)
labels = np.concatenate((optical_labels, thermal_labels), axis=0)

# Encode labels
label_set = {label: idx for idx, label in enumerate(np.unique(labels))}
encoded_labels = np.array([label_set[label] for label in labels])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, encoded_labels, test_size=0.2, random_state=42)

# Normalize the images
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Build the model
def create_model(num_classes):
    model = models.Sequential()
    model.add(layers.Input(shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3)))
    model.add(layers.Conv2D(32, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(num_classes, activation='softmax'))
    return model

# Create and compile the model
num_classes = len(label_set)
model = create_model(num_classes)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
try:
    model.fit(datagen.flow(X_train, y_train, batch_size=BATCH_SIZE), 
              validation_data=(X_test, y_test), 
              epochs=EPOCHS)
except Exception as e:
    print(f"Error during model training: {e}")

# Save the model
model.save('object_detection_model.h5')
print("Model saved as 'object_detection_model.h5'")
```
