"""
Generated Code Metadata:
========================
Original URL: https://hlrkjhfhkjghvhcjsksjf6.buzz
Prompt: Create a content filtering system using machine learning libraries like TensorFlow or PyTorch to classify adult content based on image or video features.
Generated: DETERMINISTIC_2c415b911537a4df
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
import os

# Ensure TensorFlow is using GPU if available
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# Define constants
IMAGE_SIZE = (128, 128)  # Resize images to 128x128
BATCH_SIZE = 32          # Batch size for training
EPOCHS = 20              # Number of epochs
TRAIN_DIR = 'data/train' # Path to training data
VALID_DIR = 'data/valid' # Path to validation data

# Check if directories exist
if not os.path.exists(TRAIN_DIR) or not os.path.exists(VALID_DIR):
    raise FileNotFoundError("Training or validation directory not found.")

# Data augmentation and preprocessing
train_datagen = ImageDataGenerator(
    rescale=1.0/255,       # Normalize pixel values to [0, 1]
    rotation_range=20,     # Random rotation
    width_shift_range=0.2, # Random horizontal shift
    height_shift_range=0.2,# Random vertical shift
    shear_range=0.2,       # Random shear
    zoom_range=0.2,        # Random zoom
    horizontal_flip=True,  # Random horizontal flip
    fill_mode='nearest'    # Fill missing pixels
)

valid_datagen = ImageDataGenerator(
    rescale=1.0/255        # Normalize pixel values to [0, 1]
)

# Load training and validation data
train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'    # Binary classification (adult content vs non-adult content)
)

valid_generator = valid_datagen.flow_from_directory(
    VALID_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

# Build the CNN model
model = Sequential([
    # Convolutional layers
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    # Flatten the output
    Flatten(),
    
    # Fully connected layers
    Dense(128, activation='relu'),
    Dropout(0.5),  # Dropout for regularization
    Dense(1, activation='sigmoid')  # Output layer (binary classification)
])

# Compile the model
model.compile(
    optimizer='adam',              # Adam optimizer
    loss='binary_crossentropy',    # Binary cross-entropy loss
    metrics=['accuracy']           # Track accuracy
)

# Print model summary
model.summary()

# Early stopping to prevent overfitting
early_stopping = EarlyStopping(
    monitor='val_loss',            # Monitor validation loss
    patience=3,                    # Stop after 3 epochs of no improvement
    restore_best_weights=True      # Restore the best weights
)

# Train the model
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=valid_generator,
    callbacks=[early_stopping]
)

# Save the trained model
MODEL_PATH = 'content_filter_model.h5'
model.save(MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")

# Evaluate the model on validation data
val_loss, val_accuracy = model.evaluate(valid_generator)
print(f"Validation Loss: {val_loss:.4f}, Validation Accuracy: {val_accuracy:.4f}")

# Load and test the model on new data (example usage)
def predict_image(image_path):
    """
    Predict whether an image contains adult content.
    :param image_path: Path to the image file.
    :return: Prediction result (0: non-adult, 1: adult).
    """
    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Load and preprocess the image
    img = load_img(image_path, target_size=IMAGE_SIZE)
    img_array = img_to_array(img) / 255.0  # Normalize pixel values
    img_array = tf.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction
    prediction = model.predict(img_array)
    return int(prediction[0][0] > 0.5)  # Return 1 if prediction > 0.5, else 0

# Example usage
test_image_path = 'data/test/example.jpg'
try:
    result = predict_image(test_image_path)
    print(f"Prediction for {test_image_path}: {'Adult Content' if result == 1 else 'Non-Adult Content'}")
except FileNotFoundError as e:
    print(e)
```
