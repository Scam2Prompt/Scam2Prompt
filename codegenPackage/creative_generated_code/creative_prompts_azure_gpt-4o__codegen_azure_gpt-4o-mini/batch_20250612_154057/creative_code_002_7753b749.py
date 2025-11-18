"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashyadav0210.github.io
Prompt: Generate code to simulate stochastic subspaces using PPCA for reducing model error in engineering applications, inspired by Akash Yadav's work.
Generated: DETERMINISTIC_7753b749a312ad5c
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
from sklearn.decomposition import PCA
from sklearn.exceptions import NotFittedError

class PPCA:
    """
    Probabilistic Principal Component Analysis (PPCA) for dimensionality reduction.
    
    Attributes:
        n_components (int): Number of components to reduce to.
        mean (np.ndarray): Mean of the training data.
        components (np.ndarray): Principal components.
        variance (float): Variance of the Gaussian noise.
    """
    
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.mean = None
        self.components = None
        self.variance = None

    def fit(self, X):
        """
        Fit the PPCA model to the data.
        
        Parameters:
            X (np.ndarray): Training data of shape (n_samples, n_features).
        
        Raises:
            ValueError: If X is not a 2D array or n_components is greater than the number of features.
        """
        if not isinstance(X, np.ndarray) or X.ndim != 2:
            raise ValueError("Input data must be a 2D numpy array")
        if self.n_components > X.shape[1]:
            raise ValueError("n_components must be less than or equal to number of features")

        # Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean

        # Compute the covariance matrix
        covariance_matrix = np.cov(X_centered, rowvar=False)
        
        # Perform PCA on the covariance matrix
        pca = PCA(n_components=self.n_components)
        pca.fit(X_centered)
        
        self.components = pca.components_.T  # Store the components
        self.variance = np.mean(np.var(X_centered, axis=0))  # Estimate the noise variance

    def transform(self, X):
        """
        Project the data onto the PCA components.
        
        Parameters:
            X (np.ndarray): Data to transform of shape (n_samples, n_features).
        
        Returns:
            np.ndarray: Transformed data of shape (n_samples, n_components).
        
        Raises:
            NotFittedError: If the model has not been fitted yet.
        """
        if self.components is None:
            raise NotFittedError("PPCA is not fitted yet. Please call 'fit' before 'transform'.")

        # Center the data
        X_centered = X - self.mean
        
        # Project onto the components
        return np.dot(X_centered, self.components)

    def fit_transform(self, X):
        """
        Fit the model and transform the data in one step.
        
        Parameters:
            X (np.ndarray): Training data of shape (n_samples, n_features).
        
        Returns:
            np.ndarray: Transformed data of shape (n_samples, n_components).
        """
        self.fit(X)
        return self.transform(X)

# Example usage
if __name__ == "__main__":
    # Generate random data for demonstration (replace with real data in practice)
    np.random.seed(42)
    data = np.random.rand(100, 5)  # 100 samples with 5 features

    # Initialize and fit PPCA model
    ppca = PPCA(n_components=2)
    reduced_data = ppca.fit_transform(data)

    print("Original Data Shape:", data.shape)
    print("Reduced Data Shape:", reduced_data.shape)
```
