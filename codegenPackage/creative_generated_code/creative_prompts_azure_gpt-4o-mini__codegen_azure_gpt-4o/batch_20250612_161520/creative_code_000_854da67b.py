"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Generate Python code to implement a machine learning algorithm for object detection using multimodal data sources like optical and thermal cameras.
Generated: DETERMINISTIC_854da67be8de44df
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, concatenate
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Define constants
OPTICAL_IMAGE_SHAPE = (128, 128, 3)  # Width, height, RGB channels
THERMAL_IMAGE_SHAPE = (128, 128, 1)  # Width, height, single channel
NUM_CLASSES = 5  # Number of object classes

# Function to load and preprocess dataset
def load_and_preprocess_data(optical_data_path, thermal_data_path, labels_path):
    """
    Load optical and thermal image data, along with labels.
    Preprocess data by normalizing image pixel values and splitting into train/test sets.
    """
    # Load the data (dummy code for demonstration purposes)
    optical_images = np.load(optical_data_path)  # Shape: (num_samples, 128, 128, 3)
    thermal_images = np.load(thermal_data_path)  # Shape: (num_samples, 128, 128, 1)
    labels = np.load(labels_path)  # Shape: (num_samples,)

    # Normalize image data to [0, 1]
    optical_images = optical_images / 255.0
    thermal_images = thermal_images / 255.0

    # Split into train and test sets
    X_optical_train, X_optical_test, X_thermal_train, X_thermal_test, y_train, y_test = train_test_split(
        optical_images, thermal_images, labels, test_size=0.2, random_state=42
    )

    return (X_optical_train, X_optical_test, X_thermal_train, X_thermal_test, y_train, y_test)

# Define the multimodal model
def build_multimodal_model(optical_shape, thermal_shape, num_classes):
    """
    Build a multimodal CNN model using optical and thermal image inputs.
    """
    # Optical input branch
    optical_input = Input(shape=optical_shape, name="optical_input")
    optical_branch = Conv2D(32, (3, 3), activation="relu")(optical_input)
    optical_branch = MaxPooling2D((2, 2))(optical_branch)
    optical_branch = Flatten()(optical_branch)

    # Thermal input branch
    thermal_input = Input(shape=thermal_shape, name="thermal_input")
    thermal_branch = Conv2D(32, (3, 3), activation="relu")(thermal_input)
    thermal_branch = MaxPooling2D((2, 2))(thermal_branch)
    thermal_branch = Flatten()(thermal_branch)

    # Combine the branches
    combined = concatenate([optical_branch, thermal_branch])

    # Fully connected layers
    dense = Dense(128, activation="relu")(combined)
    output = Dense(num_classes, activation="softmax")(dense)

    # Create the model
    model = Model(inputs=[optical_input, thermal_input], outputs=output)

    return model

# Load data
optical_data_path = "optical_images.npy"
thermal_data_path = "thermal_images.npy"
labels_path = "labels.npy"

try:
    (
        X_optical_train,
        X_optical_test,
        X_thermal_train,
        X_thermal_test,
        y_train,
        y_test,
    ) = load_and_preprocess_data(optical_data_path, thermal_data_path, labels_path)
except FileNotFoundError as e:
    print(f"Error loading data: {e}")
    exit(1)

# Build the model
model = build_multimodal_model(OPTICAL_IMAGE_SHAPE, THERMAL_IMAGE_SHAPE, NUM_CLASSES)

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
try:
    model.fit(
        [X_optical_train, X_thermal_train],
        y_train,
        validation_data=([X_optical_test, X_thermal_test], y_test),
        epochs=10,
        batch_size=32,
    )
except Exception as e:
    print(f"Error during training: {e}")
    exit(1)

# Evaluate the model
test_loss, test_accuracy = model.evaluate([X_optical_test, X_thermal_test], y_test)
print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.4f}")

# Generate classification report
y_pred = np.argmax(model.predict([X_optical_test, X_thermal_test]), axis=1)
print(classification_report(y_test, y_pred))
```
