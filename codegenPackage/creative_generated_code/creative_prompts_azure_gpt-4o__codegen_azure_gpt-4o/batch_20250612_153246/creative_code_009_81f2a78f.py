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
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Ensure TensorFlow is using GPU if available
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Directories for data
data_dir = "path/to/dataset"  # Update this path to your dataset containing aircraft images
output_model_path = "aircraft_classifier.h5"

# Parameters
IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
BATCH_SIZE = 32
EPOCHS = 20

# Data preprocessing
data_gen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2,  # 80% training, 20% validation
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

# Training data generator
train_gen = data_gen.flow_from_directory(
    data_dir,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)

# Validation data generator
val_gen = data_gen.flow_from_directory(
    data_dir,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)

# Model architecture
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(train_gen.num_classes, activation="softmax")  # Output layer matches number of classes
])

# Compile the model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Early stopping to prevent overfitting
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

# Train the model
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS,
    callbacks=[early_stopping]
)

# Save the trained model
model.save(output_model_path)
print(f"Model saved to {output_model_path}")

# Evaluate the model
val_loss, val_accuracy = model.evaluate(val_gen)
print(f"Validation Loss: {val_loss:.4f}, Validation Accuracy: {val_accuracy:.4f}")

# Generate classification report
val_gen.reset()
y_true = val_gen.classes
y_pred = np.argmax(model.predict(val_gen), axis=1)
class_labels = list(train_gen.class_indices.keys())

print("Classification Report:")
print(classification_report(y_true, y_pred, target_names=class_labels))

# Plot training history
plt.figure(figsize=(12, 6))
plt.plot(history.history["accuracy"], label="Training Accuracy", color="blue")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy", color="orange")
plt.plot(history.history["loss"], label="Training Loss", color="green")
plt.plot(history.history["val_loss"], label="Validation Loss", color="red")
plt.legend()
plt.title("Training History")
plt.xlabel("Epochs")
plt.show()

# Notes:
# - Ensure the dataset structure is suitable for `ImageDataGenerator` (e.g., images grouped by class in subdirectories).
# - Replace `path/to/dataset` with the actual path to your dataset.
```
