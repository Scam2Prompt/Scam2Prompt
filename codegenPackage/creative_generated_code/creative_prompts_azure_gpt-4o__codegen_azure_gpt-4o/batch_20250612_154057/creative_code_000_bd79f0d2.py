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
from scipy.linalg import svd
from scipy.stats import multivariate_normal

class PPCA:
    """
    Probabilistic Principal Component Analysis (PPCA) implementation.

    Attributes:
        latent_dim: Dimension of the latent space (principal components).
        mean: Mean vector of the data.
        W: Projection matrix mapping latent space to observed space.
        sigma2: Variance of the isotropic noise.
    """
    def __init__(self, latent_dim):
        """
        Initialize the PPCA model.

        Parameters:
            latent_dim (int): Number of principal components to retain.
        """
        self.latent_dim = latent_dim
        self.mean = None
        self.W = None
        self.sigma2 = None

    def fit(self, X, max_iter=100, tol=1e-6):
        """
        Fit the PPCA model to the data.

        Parameters:
            X (ndarray): Input data matrix of shape (n_samples, n_features).
            max_iter (int): Maximum number of iterations for EM algorithm.
            tol (float): Tolerance for convergence.

        Returns:
            None
        """
        # Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean

        # Step 1: Initialize parameters using SVD
        n_samples, n_features = X.shape
        U, S, Vt = svd(X_centered, full_matrices=False)
        self.W = Vt[:self.latent_dim].T * S[:self.latent_dim]
        self.sigma2 = np.mean(S[self.latent_dim:]**2) / n_features

        # EM algorithm for PPCA
        for iteration in range(max_iter):
            # E-Step: Compute expected latent variables
            M = self.W.T @ self.W + self.sigma2 * np.eye(self.latent_dim)
            M_inv = np.linalg.inv(M)
            Ez = X_centered @ self.W @ M_inv
            Ezz = n_samples * self.sigma2 * M_inv + Ez.T @ Ez

            # M-Step: Update parameters
            new_W = X_centered.T @ Ez @ np.linalg.inv(Ezz)
            new_sigma2 = (
                np.sum((X_centered - Ez @ new_W.T)**2) / (n_samples * n_features)
            )

            # Check convergence
            if np.linalg.norm(self.W - new_W) < tol and abs(self.sigma2 - new_sigma2) < tol:
                break

            self.W = new_W
            self.sigma2 = new_sigma2

    def transform(self, X):
        """
        Project data into the latent space.

        Parameters:
            X (ndarray): Input data matrix of shape (n_samples, n_features).

        Returns:
            ndarray: Projected data in latent space.
        """
        if self.mean is None or self.W is None:
            raise ValueError("The model must be fitted before transforming data.")
        X_centered = X - self.mean
        M = self.W.T @ self.W + self.sigma2 * np.eye(self.latent_dim)
        M_inv = np.linalg.inv(M)
        return X_centered @ self.W @ M_inv

    def reconstruct(self, X_latent):
        """
        Reconstruct data from the latent space.

        Parameters:
            X_latent (ndarray): Latent space representation.

        Returns:
            ndarray: Reconstructed data in original space.
        """
        if self.mean is None or self.W is None:
            raise ValueError("The model must be fitted before reconstructing data.")
        return X_latent @ self.W.T + self.mean

    def log_likelihood(self, X):
        """
        Compute the log-likelihood of the data under the PPCA model.

        Parameters:
            X (ndarray): Input data matrix of shape (n_samples, n_features).

        Returns:
            float: Log-likelihood of the data.
        """
        if self.mean is None or self.W is None:
            raise ValueError("The model must be fitted before computing log-likelihood.")
        X_centered = X - self.mean
        cov_matrix = self.W @ self.W.T + self.sigma2 * np.eye(X.shape[1])
        return np.sum(multivariate_normal.logpdf(X_centered, mean=np.zeros(X.shape[1]), cov=cov_matrix))

# Example usage
if __name__ == "__main__":
    # Generate synthetic data
    np.random.seed(42)
    X = np.random.rand(100, 5)  # 100 samples, 5 features

    # Fit PPCA model with 2 principal components
    ppca = PPCA(latent_dim=2)
    ppca.fit(X)

    # Transform data to latent space
    X_latent = ppca.transform(X)

    # Reconstruct data from latent space
    X_reconstructed = ppca.reconstruct(X_latent)

    # Compute log-likelihood
    log_likelihood = ppca.log_likelihood(X)

    print("Log-likelihood:", log_likelihood)
```
