"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: What are some key examples of artificial intelligence applications in Python mentioned in the "Inteligencia artificial basico" presentations on the Ejecutor Tecnico site?
Generated: DETERMINISTIC_b354dd8a170ed472
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides examples of artificial intelligence applications in Python.
The examples are inspired by common AI topics such as natural language processing,
image recognition, and predictive analytics. These examples are generic and do not
reference specific content from the "Inteligencia artificial basico" presentations
on the Ejecutor Tecnico site, as the content is not directly accessible.
"""

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist
import cv2

# Example 1: Predictive Analytics using Linear Regression
def predictive_analytics_example():
    """
    Demonstrates predictive analytics using a simple linear regression model.
    """
    try:
        # Generate synthetic data
        np.random.seed(42)
        X = np.random.rand(100, 1) * 10  # Feature: Random numbers between 0 and 10
        y = 2.5 * X + np.random.randn(100, 1)  # Target: Linear relationship with noise

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict on the test set
        y_pred = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse:.2f}")
    except Exception as e:
        print(f"Error in predictive_analytics_example: {e}")

# Example 2: Natural Language Processing (NLP) using Text Vectorization
def nlp_example():
    """
    Demonstrates text vectorization using CountVectorizer for NLP tasks.
    """
    try:
        # Sample text data
        text_data = [
            "Artificial intelligence is fascinating.",
            "Machine learning is a subset of AI.",
            "Deep learning is a subset of machine learning."
        ]

        # Convert text data into numerical features
        vectorizer = CountVectorizer()
        text_vectors = vectorizer.fit_transform(text_data)

        # Display the feature names and vectorized data
        print("Feature Names:", vectorizer.get_feature_names_out())
        print("Vectorized Data:\n", text_vectors.toarray())
    except Exception as e:
        print(f"Error in nlp_example: {e}")

# Example 3: Image Recognition using Convolutional Neural Networks (CNNs)
def image_recognition_example():
    """
    Demonstrates image recognition using a simple neural network on the MNIST dataset.
    """
    try:
        # Load the MNIST dataset
        (X_train, y_train), (X_test, y_test) = mnist.load_data()

        # Normalize the data
        X_train = X_train / 255.0
        X_test = X_test / 255.0

        # Flatten the images for input into a dense neural network
        X_train = X_train.reshape(-1, 28 * 28)
        X_test = X_test.reshape(-1, 28 * 28)

        # Build a simple neural network model
        model = Sequential([
            Dense(128, activation='relu', input_shape=(28 * 28,)),
            Dense(64, activation='relu'),
            Dense(10, activation='softmax')  # Output layer for 10 classes
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        # Train the model
        model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

        # Evaluate the model
        test_loss, test_accuracy = model.evaluate(X_test, y_test)
        print(f"Test Accuracy: {test_accuracy:.2f}")
    except Exception as e:
        print(f"Error in image_recognition_example: {e}")

# Example 4: Clustering using K-Means
def clustering_example():
    """
    Demonstrates clustering using K-Means algorithm.
    """
    try:
        # Generate synthetic data
        np.random.seed(42)
        data = np.random.rand(100, 2)  # 100 points in 2D space

        # Apply K-Means clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(data)

        # Display cluster centers and labels
        print("Cluster Centers:\n", kmeans.cluster_centers_)
        print("Cluster Labels:\n", kmeans.labels_)
    except Exception as e:
        print(f"Error in clustering_example: {e}")

# Main function to run all examples
if __name__ == "__main__":
    print("Running Predictive Analytics Example...")
    predictive_analytics_example()

    print("\nRunning NLP Example...")
    nlp_example()

    print("\nRunning Image Recognition Example...")
    image_recognition_example()

    print("\nRunning Clustering Example...")
    clustering_example()
```
