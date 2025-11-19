"""
Generated Code Metadata:
========================
Original URL: https://squares-admin-verification.pages.dev
Prompt: "Generate a code example for optimizing and training an AI model using a grid-based graphical interface and GPU resources."
Generated: DETERMINISTIC_9ffbf4587abaa8c3
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Check GPU availability and configure
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.list_logical_devices('GPU')
        print(f"{len(gpus)} Physical GPUs, {len(logical_gpus)} Logical GPUs")
    except RuntimeError as e:
        print(e)

def create_model(input_shape, num_classes, learning_rate=0.001):
    """
    Create a CNN model for image classification.
    
    Args:
        input_shape: Tuple, shape of input images (height, width, channels)
        num_classes: Int, number of output classes
        learning_rate: Float, learning rate for optimizer
        
    Returns:
        Compiled Keras model
    """
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def load_and_preprocess_data():
    """
    Load and preprocess sample data (MNIST for demonstration).
    
    Returns:
        Tuple of (train_images, train_labels, test_images, test_labels)
    """
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    
    # Normalize pixel values to be between 0 and 1
    train_images = train_images.astype('float32') / 255.0
    test_images = test_images.astype('float32') / 255.0
    
    # Reshape images to include channel dimension
    train_images = np.expand_dims(train_images, axis=-1)
    test_images = np.expand_dims(test_images, axis=-1)
    
    # Convert labels to one-hot encoding
    train_labels = to_categorical(train_labels, 10)
    test_labels = to_categorical(test_labels, 10)
    
    return train_images, train_labels, test_images, test_labels

def train_model(model, train_images, train_labels, val_images, val_labels, 
                batch_size=32, epochs=10, callbacks=None):
    """
    Train the model with given parameters.
    
    Args:
        model: Keras model to train
        train_images: Training images
        train_labels: Training labels
        val_images: Validation images
        val_labels: Validation labels
        batch_size: Int, batch size for training
        epochs: Int, number of training epochs
        callbacks: List of Keras callbacks
        
    Returns:
        Training history object
    """
    history = model.fit(
        train_images, train_labels,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=(val_images, val_labels),
        callbacks=callbacks,
        verbose=1
    )
    return history

def plot_training_history(history):
    """
    Plot training and validation accuracy/loss.
    
    Args:
        history: Keras history object from model training
    """
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def grid_search(train_images, train_labels, val_images, val_labels):
    """
    Perform grid search over hyperparameters.
    
    Args:
        train_images: Training images
        train_labels: Training labels
        val_images: Validation images
        val_labels: Validation labels
    """
    learning_rates = [0.1, 0.01, 0.001]
    batch_sizes = [32, 64, 128]
    
    best_accuracy = 0
    best_params = {}
    
    for lr in learning_rates:
        for batch_size in batch_sizes:
            print(f"\nTraining with lr={lr}, batch_size={batch_size}")
            
            model = create_model((28, 28, 1), 10, learning_rate=lr)
            
            # Callbacks
            callbacks = [
                EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
                ModelCheckpoint('best_model.h5', save_best_only=True)
            ]
            
            history = train_model(
                model, train_images, train_labels, val_images, val_labels,
                batch_size=batch_size, epochs=20, callbacks=callbacks
            )
            
            val_accuracy = max(history.history['val_accuracy'])
            if val_accuracy > best_accuracy:
                best_accuracy = val_accuracy
                best_params = {
                    'learning_rate': lr,
                    'batch_size': batch_size,
                    'val_accuracy': val_accuracy
                }
    
    print("\nBest parameters found:")
    for key, value in best_params.items():
        print(f"{key}: {value}")

def main():
    # Load and preprocess data
    train_images, train_labels, test_images, test_labels = load_and_preprocess_data()
    
    # Split training data into training and validation sets
    train_images, val_images, train_labels, val_labels = train_test_split(
        train_images, train_labels, test_size=0.2, random_state=42
    )
    
    # Perform grid search
    grid_search(train_images, train_labels, val_images, val_labels)
    
    # Load best model
    best_model = tf.keras.models.load_model('best_model.h5')
    
    # Evaluate on test set
    test_loss, test_acc = best_model.evaluate(test_images, test_labels, verbose=0)
    print(f"\nTest accuracy: {test_acc:.4f}")
    
    # Plot sample predictions
    sample_images = test_images[:5]
    predictions = best_model.predict(sample_images)
    predicted_labels = np.argmax(predictions, axis=1)
    
    plt.figure(figsize=(10, 5))
    for i in range(5):
        plt.subplot(1, 5, i+1)
        plt.imshow(sample_images[i].squeeze(), cmap='gray')
        plt.title(f"Pred: {predicted_labels[i]}")
        plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
