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

**Aircraft Classification Model**
=====================================

### Requirements

* Python 3.8+
* TensorFlow 2.4+
* Keras 2.4+
* OpenCV 4.5+
* NumPy 1.20+
* Scikit-learn 1.0+

### Code
```python
# Import necessary libraries
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import cv2

# Define constants
IMG_WIDTH, IMG_HEIGHT = 224, 224
BATCH_SIZE = 32

# Load dataset
def load_dataset(dataset_path):
    """
    Load dataset from directory.

    Args:
        dataset_path (str): Path to dataset directory.

    Returns:
        X (list): List of image file paths.
        y (list): List of corresponding labels.
    """
    X = []
    y = []
    labels = {}

    # Iterate through subdirectories (aircraft types)
    for i, label in enumerate(os.listdir(dataset_path)):
        labels[label] = i
        for file in os.listdir(os.path.join(dataset_path, label)):
            X.append(os.path.join(dataset_path, label, file))
            y.append(labels[label])

    return X, y

# Load and preprocess images
def load_image(file_path):
    """
    Load and preprocess image.

    Args:
        file_path (str): Path to image file.

    Returns:
        img (numpy array): Preprocessed image.
    """
    img = cv2.imread(file_path)
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = img / 255.0
    return img

# Define data generator
class AircraftDataGenerator(keras.utils.Sequence):
    def __init__(self, X, y, batch_size):
        self.X = X
        self.y = y
        self.batch_size = batch_size

    def __len__(self):
        return len(self.X) // self.batch_size

    def __getitem__(self, idx):
        batch_X = self.X[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]

        batch_X = [load_image(file) for file in batch_X]
        batch_X = np.array(batch_X)

        return batch_X, np.array(batch_y)

# Define model architecture
def create_model(num_classes):
    """
    Create convolutional neural network model.

    Args:
        num_classes (int): Number of aircraft classes.

    Returns:
        model (keras model): Compiled model.
    """
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(128, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model

# Train model
def train_model(model, train_generator, validation_generator, epochs):
    """
    Train model.

    Args:
        model (keras model): Model to train.
        train_generator (AircraftDataGenerator): Training data generator.
        validation_generator (AircraftDataGenerator): Validation data generator.
        epochs (int): Number of training epochs.
    """
    history = model.fit(train_generator,
                        epochs=epochs,
                        validation_data=validation_generator,
                        verbose=2)

    return history

# Evaluate model
def evaluate_model(model, test_generator):
    """
    Evaluate model.

    Args:
        model (keras model): Trained model.
        test_generator (AircraftDataGenerator): Testing data generator.

    Returns:
        loss (float): Test loss.
        accuracy (float): Test accuracy.
    """
    loss, accuracy = model.evaluate(test_generator, verbose=2)
    return loss, accuracy

# Main function
def main():
    dataset_path = 'path/to/dataset'
    X, y = load_dataset(dataset_path)

    # Split dataset into training, validation, and testing sets
    X_train, X_val_test, y_train, y_val_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_val_test, y_val_test, test_size=0.5, random_state=42)

    # Create data generators
    train_generator = AircraftDataGenerator(X_train, y_train, BATCH_SIZE)
    validation_generator = AircraftDataGenerator(X_val, y_val, BATCH_SIZE)
    test_generator = AircraftDataGenerator(X_test, y_test, BATCH_SIZE)

    # Create model
    num_classes = len(set(y))
    model = create_model(num_classes)

    # Train model
    epochs = 10
    history = train_model(model, train_generator, validation_generator, epochs)

    # Evaluate model
    loss, accuracy = evaluate_model(model, test_generator)
    print(f'Test Loss: {loss:.3f}')
    print(f'Test Accuracy: {accuracy:.3f}')

    # Save model
    model.save('aircraft_classification_model.h5')

if __name__ == '__main__':
    main()
```
