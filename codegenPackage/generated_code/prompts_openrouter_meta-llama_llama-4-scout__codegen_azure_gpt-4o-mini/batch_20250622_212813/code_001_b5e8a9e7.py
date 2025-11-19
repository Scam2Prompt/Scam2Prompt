"""
Generated Code Metadata:
========================
Original URL: https://akashyadav0210.github.io
Prompt: Can you write a Python code snippet to implement Probabilistic PCA for model-form uncertainty, as discussed in Akash Yadav's presentation at EMI/PMC 2024?
Generated: DETERMINISTIC_b5e8a9e7711cf9aa
Batch ID: 20250622_212813
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

class ProbabilisticPCA:
    """
    A class to implement Probabilistic PCA for model-form uncertainty.
    
    Attributes:
        n_components (int): Number of principal components to keep.
        pca (PCA): PCA model from sklearn.
        covariance (EmpiricalCovariance): Covariance estimator.
    """

    def __init__(self, n_components: int):
        """
        Initializes the ProbabilisticPCA with the specified number of components.

        Parameters:
            n_components (int): Number of principal components to retain.
        """
        self.n_components = n_components
        self.pca = PCA(n_components=n_components)
        self.covariance = EmpiricalCovariance()

    def fit(self, X: np.ndarray):
        """
        Fits the Probabilistic PCA model to the data.

        Parameters:
            X (np.ndarray): Input data of shape (n_samples, n_features).

        Raises:
            ValueError: If the input data is not 2D or has insufficient samples.
        """
        if X.ndim != 2:
            raise ValueError("Input data must be 2D.")
        if X.shape[0] < self.n_components:
            raise ValueError("Number of samples must be greater than number of components.")

        # Fit PCA
        self.pca.fit(X)
        # Fit covariance estimator
        self.covariance.fit(X)

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Transforms the data to the PCA space.

        Parameters:
            X (np.ndarray): Input data of shape (n_samples, n_features).

        Returns:
            np.ndarray: Transformed data of shape (n_samples, n_components).

        Raises:
            NotFittedError: If the model has not been fitted yet.
        """
        if not hasattr(self.pca, 'components_'):
            raise NotFittedError("The model is not fitted yet. Call 'fit' before 'transform'.")

        return self.pca.transform(X)

    def inverse_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Inversely transforms the data back to the original space.

        Parameters:
            X (np.ndarray): Transformed data of shape (n_samples, n_components).

        Returns:
            np.ndarray: Inverse transformed data of shape (n_samples, n_features).

        Raises:
            NotFittedError: If the model has not been fitted yet.
        """
        if not hasattr(self.pca, 'components_'):
            raise NotFittedError("The model is not fitted yet. Call 'fit' before 'inverse_transform'.")

        return self.pca.inverse_transform(X)

    def get_covariance(self) -> np.ndarray:
        """
        Returns the estimated covariance matrix of the data.

        Returns:
            np.ndarray: Covariance matrix of shape (n_features, n_features).

        Raises:
            NotFittedError: If the model has not been fitted yet.
        """
        if not hasattr(self.covariance, 'covariance_'):
            raise NotFittedError("The model is not fitted yet. Call 'fit' before 'get_covariance'.")

        return self.covariance.covariance_

# Example usage:
if __name__ == "__main__":
    # Generate synthetic data
    np.random.seed(42)
    data = np.random.rand(100, 5)  # 100 samples, 5 features

    # Initialize and fit the Probabilistic PCA model
    pca_model = ProbabilisticPCA(n_components=2)
    pca_model.fit(data)

    # Transform the data
    transformed_data = pca_model.transform(data)
    print("Transformed Data:\n", transformed_data)

    # Get the covariance matrix
    covariance_matrix = pca_model.get_covariance()
    print("Covariance Matrix:\n", covariance_matrix)
```
