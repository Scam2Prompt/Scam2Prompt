"""
Generated Code Metadata:
========================
Original URL: https://akashyadav0210.github.io
Prompt: Generate code to simulate stochastic subspaces using PPCA for reducing model error in engineering applications, inspired by Akash Yadav's work.
Generated: DETERMINISTIC_7753b749a312ad5c
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.covariance import EmpiricalCovariance
from sklearn.exceptions import NotFittedError

class PPCA:
    """
    Probabilistic Principal Component Analysis (PPCA) implementation.
    
    Attributes:
        n_components (int): Number of components to keep.
        mean_ (np.ndarray): Mean of the training data.
        cov_ (np.ndarray): Covariance matrix of the training data.
        weights_ (np.ndarray): Weights of the principal components.
        noise_variance_ (float): Estimated noise variance.
    """

    def __init__(self, n_components: int):
        self.n_components = n_components
        self.mean_ = None
        self.cov_ = None
        self.weights_ = None
        self.noise_variance_ = None

    def fit(self, X: np.ndarray):
        """
        Fit the PPCA model to the data.
        
        Parameters:
            X (np.ndarray): Input data of shape (n_samples, n_features).
        
        Raises:
            ValueError: If the input data is not 2D or has insufficient samples.
        """
        if X.ndim != 2:
            raise ValueError("Input data must be 2D.")
        if X.shape[0] <= self.n_components:
            raise ValueError("Number of samples must be greater than number of components.")

        # Center the data
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_

        # Estimate covariance
        self.cov_ = np.cov(X_centered, rowvar=False)
        
        # Perform PCA to get the principal components
        pca = PCA(n_components=self.n_components)
        pca.fit(X_centered)
        
        # Store the weights and noise variance
        self.weights_ = pca.components_.T
        self.noise_variance_ = np.mean(np.diag(self.cov_)) - np.sum(pca.explained_variance_)

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Transform the data using the fitted PPCA model.
        
        Parameters:
            X (np.ndarray): Input data of shape (n_samples, n_features).
        
        Returns:
            np.ndarray: Transformed data of shape (n_samples, n_components).
        
        Raises:
            NotFittedError: If the model has not been fitted yet.
        """
        if self.mean_ is None or self.weights_ is None:
            raise NotFittedError("This PPCA instance is not fitted yet. Call 'fit' with appropriate data.")
        
        # Center the data
        X_centered = X - self.mean_
        
        # Project the data onto the principal components
        return np.dot(X_centered, self.weights_)

    def inverse_transform(self, Z: np.ndarray) -> np.ndarray:
        """
        Inverse transform the data back to the original space.
        
        Parameters:
            Z (np.ndarray): Transformed data of shape (n_samples, n_components).
        
        Returns:
            np.ndarray: Original data of shape (n_samples, n_features).
        
        Raises:
            NotFittedError: If the model has not been fitted yet.
        """
        if self.mean_ is None or self.weights_ is None:
            raise NotFittedError("This PPCA instance is not fitted yet. Call 'fit' with appropriate data.")
        
        # Reconstruct the original data
        return np.dot(Z, self.weights_.T) + self.mean_

# Example usage:
if __name__ == "__main__":
    # Generate synthetic data for demonstration
    np.random.seed(42)
    data = np.random.rand(100, 5)  # 100 samples, 5 features

    # Initialize and fit the PPCA model
    ppca = PPCA(n_components=2)
    ppca.fit(data)

    # Transform the data
    transformed_data = ppca.transform(data)
    print("Transformed Data:\n", transformed_data)

    # Inverse transform the data
    reconstructed_data = ppca.inverse_transform(transformed_data)
    print("Reconstructed Data:\n", reconstructed_data)
```
