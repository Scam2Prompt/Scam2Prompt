"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashyadav0210.github.io
Prompt: Write Python code to implement a probabilistic principal component analysis (PPCA) method for quantifying model-form uncertainty in computational mechanics, as described in Akash Yadav's research.
Generated: DETERMINISTIC_bd79f0d23506f150
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from scipy.linalg import eigh, inv

class PPCA:
    """
    A class to perform Probabilistic Principal Component Analysis (PPCA) on given data.
    
    Attributes:
        n_components (int): Number of principal components to retain.
        noise_variance (float): Variance of the additive noise.
        mean (np.ndarray): Mean of the input data.
        components (np.ndarray): Principal components extracted from the data.
    """

    def __init__(self, n_components: int):
        """
        Initializes the PPCA instance with the number of components.

        Parameters:
            n_components (int): Number of principal components.
        """
        self.n_components = n_components
        self.mean = None
        self.components = None
        self.noise_variance = None

    def fit(self, X: np.ndarray):
        """
        Fit the PPCA model to the data.

        Parameters:
            X (np.ndarray): The input data, shape (n_samples, n_features)

        Raises:
            ValueError: If input data is not two-dimensional or number of components
                        is greater than number of features.
        """
        # Validate input data
        if X.ndim != 2:
            raise ValueError("Input data must be a 2D array.")
        n_samples, n_features = X.shape
        if self.n_components > n_features:
            raise ValueError("Number of components must be less than or equal to number of features.")

        # Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean

        # Compute covariance matrix
        covariance_matrix = np.cov(X_centered, rowvar=False)

        # Eigenvalue decomposition
        eigenvalues, eigenvectors = eigh(covariance_matrix)

        # Sort eigenvalues and eigenvectors
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        # Estimate noise variance
        self.noise_variance = np.mean(eigenvalues[self.n_components:])

        # Select top components
        self.components = eigenvectors[:, :self.n_components]

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Transform the input data into the principal component space.

        Parameters:
            X (np.ndarray): The input data, shape (n_samples, n_features)

        Returns:
            np.ndarray: Projected data, shape (n_samples, n_components)

        Raises:
            ValueError: If the model has not been fitted or input shape is incorrect.
        """
        if self.components is None:
            raise ValueError("The model has not been fitted yet.")

        # Center the data before transformation
        X_centered = X - self.mean
        return X_centered @ self.components

    def inverse_transform(self, Z: np.ndarray) -> np.ndarray:
        """
        Transform the principal component data back to the original space.

        Parameters:
            Z (np.ndarray): The transformed data, shape (n_samples, n_components)

        Returns:
            np.ndarray: Reconstructed data, shape (n_samples, n_features)

        Raises:
            ValueError: If the model has not been fitted or input shape is incorrect.
        """
        if self.components is None:
            raise ValueError("The model has not been fitted yet.")

        return Z @ self.components.T + self.mean

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Fit the model to the data and transform it in one step.

        Parameters:
            X (np.ndarray): The input data, shape (n_samples, n_features)

        Returns:
            np.ndarray: Projected data, shape (n_samples, n_components)
        """
        self.fit(X)
        return self.transform(X)
```
