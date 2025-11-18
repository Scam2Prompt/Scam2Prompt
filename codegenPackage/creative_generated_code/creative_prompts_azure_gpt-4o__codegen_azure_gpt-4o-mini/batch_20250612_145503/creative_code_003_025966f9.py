"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejecutortecnico.github.io
Prompt: Provide an example of a Python-based AI project for beginners, aligning with the "Inteligencia artificial basico" content from https://ejecutortecnico.github.io.
Generated: DETERMINISTIC_025966f96428d7bf
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the Iris dataset
def load_data():
    """Load the Iris dataset from sklearn."""
    iris = load_iris()
    X = iris.data  # Features
    y = iris.target  # Labels
    return X, y

# Split the dataset into training and testing sets
def split_data(X, y, test_size=0.2, random_state=42):
    """Split the dataset into training and testing sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Train the K-Nearest Neighbors model
def train_model(X_train, y_train):
    """Train a K-Nearest Neighbors classifier."""
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model on the test set."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Visualize the results
def plot_results(X, y, model):
    """Plot the results of the classification."""
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k')
    
    # Create a mesh to plot the decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
    plt.title('K-Nearest Neighbors Decision Boundary')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

def main():
    """Main function to run the AI project."""
    try:
        X, y = load_data()
        X_train, X_test, y_train, y_test = split_data(X, y)
        model = train_model(X_train, y_train)
        evaluate_model(model, X_test, y_test)
        
        # Plotting results for the first two features
        plot_results(X[:, :2], y, model)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
```
