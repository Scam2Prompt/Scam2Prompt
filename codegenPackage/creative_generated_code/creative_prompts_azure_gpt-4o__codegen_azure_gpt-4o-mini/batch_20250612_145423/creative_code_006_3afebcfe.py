"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslavision.us
Prompt: Provide an example of how to use machine learning to train an AI model for recognizing traffic signs and road conditions, similar to Tesla Vision's approach.
Generated: DETERMINISTIC_3afebcfee2b77d15
Batch ID: 20250612_145423
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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(42)

# Constants
IMG_HEIGHT = 64
IMG_WIDTH = 64
BATCH_SIZE = 32
EPOCHS = 20
DATA_DIR = 'path/to/traffic_signs_data'  # Adjust the path to your dataset

# Function to load and preprocess data
def load_data(data_dir):
    """
    Load traffic sign images and their labels from the specified directory.
    """
    images = []
    labels = []

    # Check if directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"The specified data directory does not exist: {data_dir}")

    # Loop through each class directory to load images
    for label in os.listdir(data_dir):
        class_dir = os.path.join(data_dir, label)
        
        if not os.path.isdir(class_dir):
            continue
        
        for img_name in os.listdir(class_dir):
            img_path = os.path.join(class_dir, img_name)
            try:
                img = tf.keras.preprocessing.image.load_img(img_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
                img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0  # Normalize to [0, 1]
                images.append(img_array)
                labels.append(label)
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")

    return np.array(images), np.array(labels)

# Load and preprocess the dataset
X, y = load_data(DATA_DIR)

# Encode labels to integers
label_binarizer = LabelBinarizer()
y_encoded = label_binarizer.fit_transform(y)

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Data augmentation to improve model generalization
datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Define the model architecture
def create_model():
    """
    Create a CNN model for traffic sign recognition.
    """
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(len(label_binarizer.classes_), activation='softmax')  # Output layer for multiclass classification
    ])
    
    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Create and train the model
model = create_model()
history = model.fit(datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
                    validation_data=(X_val, y_val),
                    epochs=EPOCHS)

# Save the trained model
model.save('traffic_sign_recognition_model.h5')

# Plot training history
def plot_training_history(history):
    """
    Plot training and validation accuracy and loss over epochs.
    """
    plt.figure(figsize=(12, 4))

    # Plot accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='train_accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    # Plot loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='train_loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

# Call the function to plot the training history
plot_training_history(history)

# Optionally, load the model and evaluate on new data
def load_and_evaluate_model(model_path, test_data):
    """
    Load a trained model and evaluate it on new data.
    """
    model = tf.keras.models.load_model(model_path)
    
    # Perform evaluation
    loss, accuracy = model.evaluate(test_data)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

# Example usage (uncomment below when you have test data)
# load_and_evaluate_model('traffic_sign_recognition_model.h5', X_test)
```
