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
from scipy.linalg import svd
from sklearn.utils.validation import check_random_state

class ProbabilisticPCA:
    """
    Probabilistic Principal Component Analysis (PPCA) implementation.
    
    Parameters:
    -----------
    n_components : int, default=None
        Number of components to keep. If None, all components are kept.
    max_iter : int, default=100
        Maximum number of EM iterations.
    tol : float, default=1e-6
        Convergence tolerance for EM algorithm.
    random_state : int or RandomState, default=None
        Random number generator seed or instance.
    
    Attributes:
    -----------
    components_ : ndarray of shape (n_components, n_features)
        Principal axes in feature space.
    explained_variance_ : ndarray of shape (n_components,)
        Variance explained by each of the selected components.
    noise_variance_ : float
        Estimated noise variance.
    mean_ : ndarray of shape (n_features,)
        Per-feature empirical mean.
    n_iter_ : int
        Number of EM iterations run.
    """
    
    def __init__(self, n_components=None, max_iter=100, tol=1e-6, random_state=None):
        self.n_components = n_components
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state
        
    def fit(self, X):
        """
        Fit the model with X.
        
        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            Training data.
            
        Returns:
        --------
        self : object
            Returns the instance itself.
        """
        X = np.asarray(X)
        n_samples, n_features = X.shape
        
        # Initialize parameters
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        
        # Initialize using SVD
        U, S, Vt = svd(X_centered, full_matrices=False)
        if self.n_components is None:
            self.n_components = n_features
            
        # Initial values
        W = Vt[:self.n_components].T * S[:self.n_components]
        sigma2 = np.mean(S[self.n_components:]**2) if self.n_components < n_features else 1.0
        
        # EM algorithm
        rng = check_random_state(self.random_state)
        prev_log_likelihood = -np.inf
        self.n_iter_ = 0
        
        for i in range(self.max_iter):
            # E-step
            M = W.T @ W + sigma2 * np.eye(self.n_components)
            Minv = np.linalg.inv(M)
            X_hat = X_centered @ W @ Minv @ W.T
            
            # M-step
            W_new = X_centered.T @ X_hat @ np.linalg.inv(X_hat.T @ X_hat + n_samples * sigma2 * Minv)
            sigma2_new = np.mean(
                np.sum(X_centered**2, axis=1) - 2 * np.sum(X_hat @ W_new.T * X_centered, axis=1) +
                np.trace(X_hat.T @ X_hat @ W_new.T @ W_new)
            ) / n_features
            
            # Check convergence
            log_likelihood = self._log_likelihood(X_centered, W_new, sigma2_new)
            if np.abs(log_likelihood - prev_log_likelihood) < self.tol:
                break
                
            prev_log_likelihood = log_likelihood
            W = W_new
            sigma2 = sigma2_new
            self.n_iter_ += 1
            
        # Store results
        self.components_ = W.T
        self.explained_variance_ = np.sum(self.components_**2, axis=1)
        self.noise_variance_ = sigma2
        
        return self
    
    def transform(self, X):
        """
        Apply dimensionality reduction to X.
        
        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            New data.
            
        Returns:
        --------
        X_transformed : ndarray of shape (n_samples, n_components)
            Transformed values.
        """
        X = np.asarray(X)
        X_centered = X - self.mean_
        M = self.components_ @ self.components_.T + self.noise_variance_ * np.eye(self.components_.shape[0])
        Minv = np.linalg.inv(M)
        return X_centered @ self.components_.T @ Minv
    
    def inverse_transform(self, X_transformed):
        """
        Transform data back to its original space.
        
        Parameters:
        -----------
        X_transformed : array-like of shape (n_samples, n_components)
            Transformed data.
            
        Returns:
        --------
        X_original : ndarray of shape (n_samples, n_features)
            Data in original space.
        """
        X_transformed = np.asarray(X_transformed)
        return X_transformed @ self.components_ + self.mean_
    
    def _log_likelihood(self, X, W, sigma2):
        """
        Compute log-likelihood of the data.
        
        Parameters:
        -----------
        X : ndarray of shape (n_samples, n_features)
            Centered data.
        W : ndarray of shape (n_features, n_components)
            Current weight matrix.
        sigma2 : float
            Current noise variance.
            
        Returns:
        --------
        log_likelihood : float
            Log-likelihood of the data.
        """
        n_samples, n_features = X.shape
        C = W @ W.T + sigma2 * np.eye(n_features)
        Cinv = np.linalg.inv(C)
        log_det_C = np.log(np.linalg.det(C))
        return -0.5 * n_samples * (n_features * np.log(2 * np.pi) + log_det_C + np.trace(X.T @ X @ Cinv) / n_samples)
```
