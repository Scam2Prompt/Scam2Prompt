"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Develop a machine learning model to classify aircraft types in images, using examples like the A-29 Super Tucano and Gripen F-39 mentioned on Spotters Brasil.
Generated: DETERMINISTIC_81f2a78ff22c3c2a
Batch ID: 20250612_153246
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
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Constants
IMAGE_SIZE = (128, 128)  # Resize images to this size
BATCH_SIZE = 32
EPOCHS = 20
DATA_DIR = 'path/to/your/dataset'  # Update with your dataset path

# Load dataset
def load_data(data_dir):
    """
    Load images and labels from the specified directory.
    Assumes subdirectories for each class.
    """
    images = []
    labels = []
    
    for label in os.listdir(data_dir):
        class_dir = os.path.join(data_dir, label)
        if os.path.isdir(class_dir):
            for img_file in os.listdir(class_dir):
                img_path = os.path.join(class_dir, img_file)
                try:
                    img = keras.preprocessing.image.load_img(img_path, target_size=IMAGE_SIZE)
                    img_array = keras.preprocessing.image.img_to_array(img)
                    images.append(img_array)
                    labels.append(label)
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
    
    return np.array(images), np.array(labels)

# Preprocess data
def preprocess_data(images, labels):
    """
    Normalize images and encode labels.
    """
    images = images / 255.0  # Normalize pixel values
    lb = LabelBinarizer()
    labels = lb.fit_transform(labels)
    return images, labels, lb.classes_

# Build the model
def build_model(input_shape, num_classes):
    """
    Build a convolutional neural network model.
    """
    model = keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Main function to execute the workflow
def main():
    # Load and preprocess data
    images, labels = load_data(DATA_DIR)
    images, labels, class_names = preprocess_data(images, labels)
    
    # Split data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)
    
    # Create data generators for augmentation
    train_datagen = ImageDataGenerator(rotation_range=20, width_shift_range=0.2,
                                       height_shift_range=0.2, shear_range=0.2,
                                       zoom_range=0.2, horizontal_flip=True)
    val_datagen = ImageDataGenerator()

    # Fit the model
    model = build_model((IMAGE_SIZE[0], IMAGE_SIZE[1], 3), len(class_names))
    model.fit(train_datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
              validation_data=val_datagen.flow(X_val, y_val),
              epochs=EPOCHS)

    # Evaluate the model
    y_pred = model.predict(X_val)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true_classes = np.argmax(y_val, axis=1)

    # Print classification report and confusion matrix
    print(classification_report(y_true_classes, y_pred_classes, target_names=class_names))
    print(confusion_matrix(y_true_classes, y_pred_classes))

if __name__ == "__main__":
    main()
```

Make sure to replace `'path/to/your/dataset'` with the actual path to your dataset containing subdirectories for each aircraft type.
