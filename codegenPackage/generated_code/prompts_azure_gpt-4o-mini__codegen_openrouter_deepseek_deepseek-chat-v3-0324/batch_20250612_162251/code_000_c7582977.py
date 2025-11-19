"""
Generated Code Metadata:
========================
Original URL: https://eigenlab.io
Prompt: Generate a Python script that utilizes Eigen Lab's unique features for data analysis.
Generated: DETERMINISTIC_c7582977b2195e55
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.linalg import eig
import pandas as pd
from typing import Optional, Tuple

class EigenLabAnalyzer:
    """
    A class for performing data analysis using Eigen decomposition.
    Provides methods for PCA, variance analysis, and dimensionality reduction.
    """
    
    def __init__(self, data: np.ndarray):
        """
        Initialize the analyzer with input data.
        
        Args:
            data: Input data matrix (samples x features)
        """
        if not isinstance(data, np.ndarray):
            raise TypeError("Input data must be a numpy array")
        if len(data.shape) != 2:
            raise ValueError("Input data must be 2-dimensional")
            
        self.data = data
        self.mean = None
        self.std = None
        self.eigenvalues = None
        self.eigenvectors = None
        self.explained_variance = None
        
    def standardize_data(self) -> np.ndarray:
        """
        Standardize the data (zero mean, unit variance).
        
        Returns:
            Standardized data matrix
        """
        self.mean = np.mean(self.data, axis=0)
        self.std = np.std(self.data, axis=0)
        standardized_data = (self.data - self.mean) / self.std
        return standardized_data
    
    def compute_covariance_matrix(self, standardized_data: np.ndarray) -> np.ndarray:
        """
        Compute the covariance matrix of standardized data.
        
        Args:
            standardized_data: Data matrix after standardization
            
        Returns:
            Covariance matrix
        """
        return np.cov(standardized_data, rowvar=False)
    
    def perform_eigen_decomposition(self, covariance_matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Perform eigen decomposition on the covariance matrix.
        
        Args:
            covariance_matrix: The covariance matrix to decompose
            
        Returns:
            Tuple of (eigenvalues, eigenvectors)
        """
        eigenvalues, eigenvectors = eig(covariance_matrix)
        
        # Ensure eigenvalues are real (covariance matrix is symmetric)
        if not np.all(np.isreal(eigenvalues)):
            raise ValueError("Complex eigenvalues encountered - check input matrix")
            
        eigenvalues = np.real(eigenvalues)
        eigenvectors = np.real(eigenvectors)
        
        # Sort eigenvalues and eigenvectors in descending order
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        self.eigenvalues = eigenvalues
        self.eigenvectors = eigenvectors
        
        return eigenvalues, eigenvectors
    
    def compute_explained_variance(self) -> np.ndarray:
        """
        Compute the explained variance ratio for each principal component.
        
        Returns:
            Array of explained variance ratios
        """
        if self.eigenvalues is None:
            raise ValueError("Eigenvalues not computed - perform decomposition first")
            
        total_variance = np.sum(self.eigenvalues)
        self.explained_variance = self.eigenvalues / total_variance
        return self.explained_variance
    
    def perform_pca(self, n_components: Optional[int] = None) -> np.ndarray:
        """
        Perform Principal Component Analysis on the data.
        
        Args:
            n_components: Number of principal components to keep. If None, keep all.
            
        Returns:
            Transformed data in principal component space
        """
        # Standardize the data
        standardized_data = self.standardize_data()
        
        # Compute covariance matrix
        covariance_matrix = self.compute_covariance_matrix(standardized_data)
        
        # Perform eigen decomposition
        eigenvalues, eigenvectors = self.perform_eigen_decomposition(covariance_matrix)
        
        # Compute explained variance
        explained_variance = self.compute_explained_variance()
        
        # Determine number of components to keep
        if n_components is None:
            n_components = len(eigenvalues)
        elif n_components > len(eigenvalues):
            raise ValueError(f"n_components ({n_components}) cannot be larger than number of features ({len(eigenvalues)})")
        
        # Project data onto principal components
        principal_components = eigenvectors[:, :n_components]
        transformed_data = np.dot(standardized_data, principal_components)
        
        return transformed_data
    
    def get_optimal_components(self, variance_threshold: float = 0.95) -> int:
        """
        Determine the optimal number of components to explain a given variance threshold.
        
        Args:
            variance_threshold: Desired cumulative explained variance (0-1)
            
        Returns:
            Number of components needed to reach the threshold
        """
        if self.explained_variance is None:
            self.compute_explained_variance()
            
        cumulative_variance = np.cumsum(self.explained_variance)
        n_components = np.argmax(cumulative_variance >= variance_threshold) + 1
        return n_components
    
    def get_feature_importance(self) -> pd.DataFrame:
        """
        Get the importance of each original feature based on PCA loadings.
        
        Returns:
            DataFrame with feature importance scores
        """
        if self.eigenvectors is None:
            raise ValueError("Eigenvectors not computed - perform decomposition first")
            
        # Calculate absolute loadings across all components
        loadings = np.abs(self.eigenvectors)
        feature_importance = np.sum(loadings, axis=1)
        
        # Create DataFrame with feature names if available
        try:
            feature_names = [f"Feature_{i}" for i in range(self.data.shape[1])]
            return pd.DataFrame({
                'Feature': feature_names,
                'Importance': feature_importance
            }).sort_values('Importance', ascending=False)
        except Exception:
            return pd.DataFrame({
                'Feature': range(self.data.shape[1]),
                'Importance': feature_importance
            }).sort_values('Importance', ascending=False)


# Example usage
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(42)
    data = np.random.randn(100, 5)  # 100 samples, 5 features
    
    try:
        # Initialize analyzer
        analyzer = EigenLabAnalyzer(data)
        
        # Perform PCA
        transformed_data = analyzer.perform_pca(n_components=2)
        print("Transformed data shape:", transformed_data.shape)
        
        # Get optimal components
        optimal_components = analyzer.get_optimal_components(variance_threshold=0.9)
        print(f"Optimal components for 90% variance: {optimal_components}")
        
        # Get feature importance
        feature_importance = analyzer.get_feature_importance()
        print("\nFeature Importance:")
        print(feature_importance.head())
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
```
