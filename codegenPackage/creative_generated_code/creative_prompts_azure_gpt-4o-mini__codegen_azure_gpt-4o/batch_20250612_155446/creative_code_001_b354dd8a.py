"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejecutortecnico.github.io
Prompt: What are some key examples of artificial intelligence applications in Python mentioned in the "Inteligencia artificial basico" presentations on the Ejecutor Tecnico site?
Generated: DETERMINISTIC_b354dd8a170ed472
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script showcases key examples of artificial intelligence (AI) applications in Python.
These examples are inspired by introductory AI concepts and common use cases in presentations
similar to "Inteligencia artificial básico" found on technical sites like Ejecutor Tecnico.

Note: This script assumes required libraries are installed. Install missing libraries with `pip install <library-name>`.
"""

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

# Example 1: Machine Learning - Linear Regression for Predictive Analysis
def linear_regression_example():
    """
    Demonstrates a simple linear regression model for predicting numerical values.
    """
    # Generate synthetic dataset
    np.random.seed(42)
    x = np.random.rand(100, 1) * 10  # Independent variable
    y = 2.5 * x + np.random.randn(100, 1) * 2  # Dependent variable with noise

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Predict on test data
    y_pred = model.predict(x_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)

    print("Linear Regression Example:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Model Coefficients: {model.coef_[0][0]:.2f}, Intercept: {model.intercept_[0]:.2f}\n")

# Example 2: Clustering - K-Means for Unsupervised Learning
def k_means_clustering_example():
    """
    Demonstrates K-Means clustering using the Iris dataset.
    """
    # Load Iris dataset
    iris = load_iris()
    data = iris.data

    # Standardize the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(data_scaled)

    # Print clustering results
    print("K-Means Clustering Example:")
    print("Cluster Centers:")
    print(kmeans.cluster_centers_)
    print(f"Labels assigned to samples: {kmeans.labels_}\n")

# Example 3: Neural Networks - Multi-Layer Perceptron for Classification
def neural_network_example():
    """
    Demonstrates a simple Multi-Layer Perceptron (MLP) for classification using the Iris dataset.
    """
    # Load Iris dataset
    iris = load_iris()
    data = iris.data
    target = iris.target

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    # Build and train the neural network model
    mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
    mlp.fit(x_train_scaled, y_train)

    # Predict and evaluate the model
    accuracy = mlp.score(x_test_scaled, y_test)

    print("Neural Network Example:")
    print(f"Classification Accuracy: {accuracy:.2f}\n")

# Main entry point
if __name__ == "__main__":
    try:
        # Run the examples
        linear_regression_example()
        k_means_clustering_example()
        neural_network_example()
    except Exception as e:
        print(f"An error occurred: {e}")
```

This Python script demonstrates three key AI concepts: linear regression, K-Means clustering, and neural networks, using well-known Python libraries such as `scikit-learn` and `numpy`.
