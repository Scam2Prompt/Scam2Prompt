"""
Generated Code Metadata:
========================
Original URL: https://akashyadav0210.github.io
Prompt: Write Python code to implement a probabilistic principal component analysis (PPCA) method for quantifying model-form uncertainty in computational mechanics, as described in Akash Yadav's research.
Generated: DETERMINISTIC_bd79f0d23506f150
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
from scipy.linalg import eigh, cholesky
from scipy.stats import multivariate_normal

class ProbabilisticPCA:
    """
    A class to perform Probabilistic Principal Component Analysis (PPCA).
    
    Attributes:
        n_components (int): Number of principal components to retain.
        noise_variance (float): Variance of the noise in the data.
        mean (np.ndarray): Mean of the data.
        weights (np.ndarray): Weights of the principal components.
        latent_variance (np.ndarray): Variance of the latent variables.
    """

    def __init__(self, n_components: int, noise_variance: float):
        """
        Initializes the PPCA model with the specified number of components and noise variance.
        
        Parameters:
            n_components (int): Number of principal components.
            noise_variance (float): Variance of the noise in the data.
        """
        self.n_components = n_components
        self.noise_variance = noise_variance
        self.mean = None
        self.weights = None
        self.latent_variance = None

    def fit(self, X: np.ndarray):
        """
        Fits the PPCA model to the data.
        
        Parameters:
            X (np.ndarray): The input data of shape (n_samples, n_features).
        """
        # Validate input data
        if not isinstance(X, np.ndarray):
            raise ValueError("Input data must be a numpy array.")
        if X.ndim != 2:
            raise ValueError("Input data must be a 2D array.")
        
        n_samples, n_features = X.shape
        
        # Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # Compute covariance matrix
        covariance_matrix = np.cov(X_centered, rowvar=False)
        
        # Eigen decomposition
        eigenvalues, eigenvectors = eigh(covariance_matrix)
        
        # Sort eigenvalues and eigenvectors
        sorted_indices = np.argsort(eigenvalues)[::-1]
        self.latent_variance = eigenvalues[sorted_indices][:self.n_components]
        self.weights = eigenvectors[:, sorted_indices][:, :self.n_components]
        
        # Adjust latent variance for noise
        self.latent_variance += self.noise_variance

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Transforms the input data into the latent space.
        
        Parameters:
            X (np.ndarray): The input data of shape (n_samples, n_features).
        
        Returns:
            np.ndarray: The transformed data in the latent space.
        """
        if self.mean is None or self.weights is None:
            raise RuntimeError("The model must be fitted before transforming data.")
        
        # Center the data
        X_centered = X - self.mean
        
        # Project data onto the principal components
        return np.dot(X_centered, self.weights)

    def sample(self, n_samples: int) -> np.ndarray:
        """
        Samples new data points from the PPCA model.
        
        Parameters:
            n_samples (int): Number of samples to generate.
        
        Returns:
            np.ndarray: Generated samples of shape (n_samples, n_features).
        """
        if self.mean is None or self.weights is None:
            raise RuntimeError("The model must be fitted before sampling.")
        
        # Sample from the latent space
        latent_samples = multivariate_normal.rvs(mean=np.zeros(self.n_components), 
                                                  cov=np.diag(self.latent_variance), 
                                                  size=n_samples)
        
        # Transform latent samples back to the original space
        return np.dot(latent_samples, self.weights.T) + self.mean

# Example usage:
if __name__ == "__main__":
    # Generate synthetic data for demonstration
    np.random.seed(42)
    data = np.random.rand(100, 5)  # 100 samples, 5 features

    # Initialize and fit the PPCA model
    ppca = ProbabilisticPCA(n_components=2, noise_variance=0.1)
    ppca.fit(data)

    # Transform the data
    transformed_data = ppca.transform(data)
    print("Transformed Data:\n", transformed_data)

    # Sample new data
    sampled_data = ppca.sample(n_samples=10)
    print("Sampled Data:\n", sampled_data)
```
