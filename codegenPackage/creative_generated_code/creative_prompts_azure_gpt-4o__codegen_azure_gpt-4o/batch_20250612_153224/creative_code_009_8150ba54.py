"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Recommend a machine learning library for classifying foot and ankle injuries based on X-ray or MRI data, with a focus on conditions like hallux valgus and Achilles tendon ruptures.
Generated: DETERMINISTIC_8150ba54dd084449
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a machine learning pipeline using TensorFlow/Keras to classify 
foot and ankle injuries such as hallux valgus and Achilles tendon ruptures based on 
X-ray or MRI data. TensorFlow is chosen as it is widely used, production-ready, and 
has robust support for image-based classification tasks.
"""

import tensorflow as tf
from tensorflow.keras import layers, models, callbacks, optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Ensure the TensorFlow library is properly installed
try:
    import tensorflow as tf
except ImportError as e:
    raise ImportError("TensorFlow is not installed. Install it via pip: pip install tensorflow") from e

# Set up key directories
DATA_DIR = "path/to/dataset"  # Replace with the path to your dataset
TRAIN_DIR = os.path.join(DATA_DIR, "train")
VALIDATION_DIR = os.path.join(DATA_DIR, "validation")
TEST_DIR = os.path.join(DATA_DIR, "test")

# Parameters
IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 32
EPOCHS = 25
LEARNING_RATE = 0.001

# Data Preprocessing
# Use ImageDataGenerator for data augmentation and proper normalization
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255.0,      # Normalize pixel values
    rotation_range=20,        # Random rotation
    width_shift_range=0.2,    # Random width shift
    height_shift_range=0.2,   # Random height shift
    shear_range=0.2,          # Random shearing
    zoom_range=0.2,           # Random zoom
    horizontal_flip=True      # Random horizontal flip
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

# Load training and validation datasets
train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'  # Use 'categorical' for multi-class classification
)

validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Model Architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),  # Prevent overfitting
    layers.Dense(train_generator.num_classes, activation='softmax')  # Output layer
])

# Compile the model
model.compile(
    optimizer=optimizers.Adam(learning_rate=LEARNING_RATE),
    loss='categorical_crossentropy',  # Loss function suitable for multi-class classification
    metrics=['accuracy']  # Monitor accuracy
)

# Callbacks
early_stopping = callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,  # Stop training if no improvement for 5 epochs
    restore_best_weights=True
)

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // BATCH_SIZE,
    callbacks=[early_stopping]
)

# Save the trained model
MODEL_SAVE_PATH = "path/to/save/model.h5"
model.save(MODEL_SAVE_PATH)

# Load and test the model on unseen data
test_datagen = ImageDataGenerator(rescale=1.0 / 255.0)
test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_generator)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

# Note: Ensure your dataset is organized with separate directories for training, validation, and test data,
# with subdirectories for each class containing the respective images.
```
