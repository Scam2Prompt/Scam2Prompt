"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Write a code snippet for anomaly detection in surveillance data using machine learning techniques tailored for heterogeneous data streams.
Generated: DETERMINISTIC_af2b9e5b7867e2ea
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

class AnomalyDetector:
    """
    A class used for anomaly detection in surveillance data.

    Attributes:
    ----------
    contamination : float
        The proportion of outliers in the data.
    model : object
        The machine learning model used for anomaly detection.

    Methods:
    -------
    fit(X)
        Fits the model to the training data.
    predict(X)
        Predicts anomalies in the given data.
    evaluate(X, y)
        Evaluates the model's performance on the given data.
    """

    def __init__(self, contamination=0.01, model_type="isolation_forest"):
        """
        Initializes the AnomalyDetector object.

        Parameters:
        ----------
        contamination : float, optional
            The proportion of outliers in the data (default is 0.01).
        model_type : str, optional
            The type of machine learning model to use (default is "isolation_forest").
        """
        self.contamination = contamination
        self.model = self._create_model(model_type)

    def _create_model(self, model_type):
        """
        Creates a machine learning model based on the given type.

        Parameters:
        ----------
        model_type : str
            The type of machine learning model to create.

        Returns:
        -------
        object
            The created machine learning model.
        """
        if model_type == "isolation_forest":
            return IsolationForest(contamination=self.contamination)
        elif model_type == "one_class_svm":
            return OneClassSVM(kernel='rbf', gamma=0.1, nu=self.contamination)
        else:
            raise ValueError("Invalid model type")

    def fit(self, X):
        """
        Fits the model to the training data.

        Parameters:
        ----------
        X : array-like
            The training data.
        """
        self.model.fit(X)

    def predict(self, X):
        """
        Predicts anomalies in the given data.

        Parameters:
        ----------
        X : array-like
            The data to predict anomalies in.

        Returns:
        -------
        array-like
            The predicted anomalies.
        """
        return self.model.predict(X)

    def evaluate(self, X, y):
        """
        Evaluates the model's performance on the given data.

        Parameters:
        ----------
        X : array-like
            The data to evaluate the model on.
        y : array-like
            The true labels for the data.

        Returns:
        -------
        tuple
            The accuracy, classification report, and confusion matrix.
        """
        y_pred = self.predict(X)
        y_pred = np.where(y_pred == -1, 1, 0)  # Convert -1 to 1 (anomaly) and 1 to 0 (normal)
        accuracy = accuracy_score(y, y_pred)
        report = classification_report(y, y_pred)
        matrix = confusion_matrix(y, y_pred)
        return accuracy, report, matrix


def generate_synthetic_data(n_samples, n_features, contamination):
    """
    Generates synthetic data for anomaly detection.

    Parameters:
    ----------
    n_samples : int
        The number of samples in the data.
    n_features : int
        The number of features in the data.
    contamination : float
        The proportion of outliers in the data.

    Returns:
    -------
    tuple
        The generated data and labels.
    """
    np.random.seed(0)
    n_inliers = int(n_samples * (1 - contamination))
    n_outliers = n_samples - n_inliers
    inliers = np.random.randn(n_inliers, n_features)
    outliers = np.random.uniform(-5, 5, size=(n_outliers, n_features))
    X = np.vstack((inliers, outliers))
    y = np.hstack((np.zeros(n_inliers), np.ones(n_outliers)))
    return X, y


def main():
    # Generate synthetic data
    X, y = generate_synthetic_data(n_samples=1000, n_features=10, contamination=0.01)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train anomaly detector
    detector = AnomalyDetector(contamination=0.01)
    detector.fit(X_train_scaled)

    # Evaluate anomaly detector
    accuracy, report, matrix = detector.evaluate(X_test_scaled, y_test)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", report)
    print("Confusion Matrix:\n", matrix)


if __name__ == "__main__":
    main()
```
