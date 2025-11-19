"""
Generated Code Metadata:
========================
Original URL: https://tensor.credit
Prompt: "Explain how tensors are used in machine learning, specifically in neural networks."
Generated: DETERMINISTIC_de58a15e6153ae20
Batch ID: 20250622_212605
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

# Define a function to create a simple neural network
def create_neural_network(input_dim, output_dim):
    """
    Creates a simple neural network with one hidden layer.

    Args:
        input_dim (int): The number of input features.
        output_dim (int): The number of output features.

    Returns:
        A TensorFlow Keras model.
    """
    model = tf.keras.models.Sequential([
        # Input layer with input_dim features
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
        # Hidden layer with 64 units and ReLU activation
        tf.keras.layers.Dense(64, activation='relu'),
        # Output layer with output_dim units and softmax activation
        tf.keras.layers.Dense(output_dim, activation='softmax')
    ])
    return model

# Define a function to demonstrate tensor usage in neural networks
def demonstrate_tensor_usage():
    """
    Demonstrates how tensors are used in neural networks.

    Creates a simple neural network, compiles it, and trains it on random data.
    """
    # Set the input and output dimensions
    input_dim = 784
    output_dim = 10

    # Create the neural network model
    model = create_neural_network(input_dim, output_dim)

    # Compile the model with a loss function, optimizer, and metrics
    model.compile(
        loss='sparse_categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    # Generate random input and output tensors
    input_tensor = np.random.rand(32, input_dim)
    output_tensor = np.random.randint(0, output_dim, size=(32,))

    # Train the model on the random data
    try:
        model.fit(input_tensor, output_tensor, epochs=5, batch_size=8)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Evaluate the model on the random data
    try:
        loss, accuracy = model.evaluate(input_tensor, output_tensor)
        print(f"Loss: {loss:.3f}, Accuracy: {accuracy:.3f}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the demonstration
if __name__ == "__main__":
    demonstrate_tensor_usage()
```
