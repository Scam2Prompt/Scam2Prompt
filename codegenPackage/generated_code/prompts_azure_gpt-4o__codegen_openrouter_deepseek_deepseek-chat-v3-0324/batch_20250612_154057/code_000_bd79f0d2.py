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
from scipy.linalg import svd, pinv
from scipy.stats import multivariate_normal
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted


class ProbabilisticPCA(BaseEstimator, TransformerMixin):
    """
    Probabilistic Principal Component Analysis (PPCA) implementation.
    
    Parameters
    ----------
    n_components : int, default=None
        Number of components to keep. If None, all components are kept.
        
    max_iter : int, default=100
        Maximum number of EM iterations.
        
    tol : float, default=1e-4
        Tolerance for convergence of EM algorithm.
        
    random_state : int, default=None
        Random seed for initialization.
        
    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        Principal axes in feature space.
        
    noise_variance_ : float
        Estimated noise variance.
        
    mean_ : ndarray of shape (n_features,)
        Per-feature empirical mean.
        
    n_components_ : int
        The estimated number of components.
        
    n_features_ : int
        Number of features in the training data.
        
    n_samples_ : int
        Number of samples in the training data.
    """
    
    def __init__(self, n_components=None, max_iter=100, tol=1e-4, random_state=None):
        self.n_components = n_components
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state
        
    def fit(self, X, y=None):
        """
        Fit the model with X.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data.
            
        y : Ignored
            Not used, present for API consistency.
            
        Returns
        -------
        self : object
            Returns the instance itself.
        """
        np.random.seed(self.random_state)
        X = self._validate_data(X, dtype=[np.float64, np.float32], ensure_min_samples=2)
        
        n_samples, n_features = X.shape
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        
        if self.n_components is None:
            n_components = min(n_samples, n_features)
        else:
            n_components = self.n_components
            
        self.n_components_ = n_components
        self.n_features_ = n_features
        self.n_samples_ = n_samples
        
        # Initialize parameters using SVD
        U, S, Vt = svd(X_centered, full_matrices=False)
        self.components_ = Vt[:n_components]
        
        # Initial noise variance (average of discarded eigenvalues)
        if n_components < min(n_samples, n_features):
            self.noise_variance_ = np.mean(S[n_components:] ** 2) / (n_features - n_components)
        else:
            self.noise_variance_ = 1e-6
            
        # EM algorithm
        prev_log_likelihood = -np.inf
        for i in range(self.max_iter):
            # E-step: compute posterior moments
            M = self.components_.T @ self.components_ + self.noise_variance_ * np.eye(n_components)
            Minv = pinv(M)
            X_transformed = X_centered @ self.components_.T @ Minv.T
            XXT = X_centered.T @ X_transformed
            
            # M-step: update parameters
            self.components_ = (XXT @ pinv(n_samples * Minv + X_transformed.T @ X_transformed)).T
            self.noise_variance_ = (np.sum(X_centered ** 2) - 
                                   np.trace(XXT @ self.components_)) / (n_samples * n_features)
            
            # Check convergence
            log_likelihood = self._log_likelihood(X_centered)
            if np.abs(log_likelihood - prev_log_likelihood) < self.tol:
                break
            prev_log_likelihood = log_likelihood
            
        return self
    
    def transform(self, X):
        """
        Apply dimensionality reduction to X.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            New data to transform.
            
        Returns
        -------
        X_transformed : ndarray of shape (n_samples, n_components)
            Transformed values.
        """
        check_is_fitted(self)
        X = self._validate_data(X, reset=False)
        X_centered = X - self.mean_
        
        M = self.components_.T @ self.components_ + self.noise_variance_ * np.eye(self.n_components_)
        Minv = pinv(M)
        return X_centered @ self.components_.T @ Minv.T
    
    def inverse_transform(self, X):
        """
        Transform data back to its original space.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_components)
            Transformed data.
            
        Returns
        -------
        X_original : ndarray of shape (n_samples, n_features)
            Data in original space.
        """
        check_is_fitted(self)
        return X @ self.components_ + self.mean_
    
    def _log_likelihood(self, X_centered):
        """
        Compute log-likelihood of the data.
        
        Parameters
        ----------
        X_centered : ndarray of shape (n_samples, n_features)
            Centered data.
            
        Returns
        -------
        log_likelihood : float
            Log-likelihood of the data.
        """
        n_samples, n_features = X_centered.shape
        C = self.components_.T @ self.components_ + self.noise_variance_ * np.eye(n_features)
        
        try:
            log_likelihood = -0.5 * (n_samples * n_features * np.log(2 * np.pi) +
                                    n_samples * np.log(np.linalg.det(C)) +
                                    np.trace(X_centered @ pinv(C) @ X_centered.T))
        except np.linalg.LinAlgError:
            log_likelihood = -np.inf
            
        return log_likelihood
    
    def sample(self, n_samples=1):
        """
        Generate random samples from the fitted PPCA model.
        
        Parameters
        ----------
        n_samples : int, default=1
            Number of samples to generate.
            
        Returns
        -------
        X : ndarray of shape (n_samples, n_features)
            Random samples from the fitted PPCA model.
        """
        check_is_fitted(self)
        
        # Sample latent variables
        z = np.random.normal(size=(n_samples, self.n_components_))
        
        # Transform to observed space
        X = z @ self.components_ + self.mean_
        
        # Add noise
        noise = np.random.normal(scale=np.sqrt(self.noise_variance_), 
                                size=(n_samples, self.n_features_))
        return X + noise
    
    def score_samples(self, X):
        """
        Compute log-likelihood of each sample under the current model.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Data to score.
            
        Returns
        -------
        log_prob : ndarray of shape (n_samples,)
            Log-likelihood of each sample.
        """
        check_is_fitted(self)
        X = self._validate_data(X, reset=False)
        X_centered = X - self.mean_
        
        C = self.components_.T @ self.components_ + self.noise_variance_ * np.eye(self.n_features_)
        return multivariate_normal.logpdf(X_centered, cov=C)
    
    def score(self, X, y=None):
        """
        Compute average log-likelihood of the data under the current model.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Data to score.
            
        y : Ignored
            Not used, present for API consistency.
            
        Returns
        -------
        log_prob : float
            Average log-likelihood of the data.
        """
        return np.mean(self.score_samples(X))
```
