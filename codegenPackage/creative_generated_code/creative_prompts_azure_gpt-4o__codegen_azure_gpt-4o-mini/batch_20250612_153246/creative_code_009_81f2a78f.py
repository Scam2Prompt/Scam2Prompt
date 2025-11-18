"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spottersbrasil.com.br
Prompt: Develop a machine learning model to classify aircraft types in images, using examples like the A-29 Super Tucano and Gripen F-39 mentioned on Spotters Brasil.
Generated: DETERMINISTIC_81f2a78ff22c3c2a
Batch ID: 20250612_153246
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
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Define constants
IMAGE_SIZE = (128, 128)  # Image size to resize to
BATCH_SIZE = 32           # Number of images to process in a batch
EPOCHS = 20               # Number of training epochs
DATA_DIR = 'path/to/data' # Directory containing the dataset

# Function to load and preprocess dataset
def load_data(data_dir):
    """
    Load images and their corresponding labels from the specified directory.

    :param data_dir: Directory containing subfolders of images for each class.
    :return: Tuple of training images and labels.
    """
    images = []
    labels = []

    try:
        for label in os.listdir(data_dir):
            class_dir = os.path.join(data_dir, label)
            if os.path.isdir(class_dir):
                for img_file in os.listdir(class_dir):
                    img_path = os.path.join(class_dir, img_file)
                    img = tf.keras.preprocessing.image.load_img(img_path, target_size=IMAGE_SIZE)
                    img_array = tf.keras.preprocessing.image.img_to_array(img)
                    images.append(img_array)
                    labels.append(label)

        return np.array(images), np.array(labels)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

# Load the data
X, y = load_data(DATA_DIR)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Normalize pixel values to [0, 1]
X_train = X_train / 255.0
X_val = X_val / 255.0

# Create data augmentation generator
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Build the CNN model
def create_model():
    """
    Creates and compiles a CNN model for image classification.
    
    :return: Compiled Keras model.
    """
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(len(np.unique(y)), activation='softmax')  # Output layer for number of classes
    ])
    
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Create the model
model = create_model()

# Train the model with data augmentation
try:
    history = model.fit(datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
                        validation_data=(X_val, y_val),
                        epochs=EPOCHS)
except Exception as e:
    print(f"Error during training: {e}")

# Evaluate the model
def evaluate_model(model, X_val, y_val):
    """
    Evaluate the model on the validation dataset and print metrics.

    :param model: The trained Keras model.
    :param X_val: Validation images.
    :param y_val: Validation labels.
    """
    try:
        val_loss, val_accuracy = model.evaluate(X_val, y_val)
        print(f'Validation Loss: {val_loss}, Validation Accuracy: {val_accuracy}')

        # Generate classification report and confusion matrix
        y_pred = np.argmax(model.predict(X_val), axis=-1)
        print(classification_report(y_val, y_pred))
        print(confusion_matrix(y_val, y_pred))

    except Exception as e:
        print(f"Error during evaluation: {e}")

# Call evaluation function
evaluate_model(model, X_val, y_val)

# Save the model
try:
    model.save('aircraft_classifier_model.h5')
except Exception as e:
    print(f"Error saving model: {e}")

# Plot training history
def plot_training_history(history):
    """
    Plot training and validation accuracy and loss.

    :param history: Training history object returned by model.fit().
    """
    try:
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.plot(history.history['accuracy'], label='Training Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(history.history['loss'], label='Training Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title('Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()

        plt.show()

    except Exception as e:
        print(f"Error plotting training history: {e}")

# Call plotting function
plot_training_history(history)
```
