"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Develop a data-driven algorithm to convert fan data into actionable commercial profiles for sports audiences, leveraging the proprietary insights engine mentioned on Generate Digital's website.
Generated: DETERMINISTIC_86ee74d625113b67
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import json
from typing import Dict, List, Any, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FanProfileGenerator:
    """
    A data-driven algorithm to convert fan data into actionable commercial profiles.
    Leverages clustering techniques to segment sports audiences based on behavior and preferences.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the FanProfileGenerator with optional configuration.
        
        Args:
            config_path (str, optional): Path to JSON configuration file. Defaults to None.
        """
        self.config = self._load_config(config_path)
        self.scaler = StandardScaler()
        self.model = None
        
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """
        Load configuration from JSON file or use defaults.
        
        Args:
            config_path (str, optional): Path to JSON config file.
            
        Returns:
            Dict[str, Any]: Configuration dictionary.
        """
        default_config = {
            "features": [
                "engagement_score",
                "purchase_frequency",
                "social_media_activity",
                "event_attendance",
                "content_consumption"
            ],
            "n_clusters": 5,
            "random_state": 42,
            "max_iter": 300
        }
        
        if config_path:
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load config from {config_path}: {str(e)}. Using defaults.")
        
        return default_config
    
    def preprocess_data(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess raw fan data by handling missing values and scaling features.
        
        Args:
            raw_data (pd.DataFrame): Raw fan data.
            
        Returns:
            pd.DataFrame: Processed data ready for clustering.
            
        Raises:
            ValueError: If required features are missing from the input data.
        """
        required_features = set(self.config["features"])
        available_features = set(raw_data.columns)
        
        if not required_features.issubset(available_features):
            missing = required_features - available_features
            raise ValueError(f"Missing required features in input data: {missing}")
        
        try:
            # Handle missing values
            processed_data = raw_data[self.config["features"]].copy()
            processed_data.fillna(processed_data.median(), inplace=True)
            
            # Scale features
            processed_data[self.config["features"]] = self.scaler.fit_transform(
                processed_data[self.config["features"]]
            )
            
            return processed_data
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise
    
    def find_optimal_clusters(self, data: pd.DataFrame, max_clusters: int = 10) -> int:
        """
        Determine the optimal number of clusters using silhouette score.
        
        Args:
            data (pd.DataFrame): Preprocessed data.
            max_clusters (int): Maximum number of clusters to evaluate.
            
        Returns:
            int: Optimal number of clusters.
        """
        best_n = 2
        best_score = -1
        
        for n in range(2, max_clusters + 1):
            kmeans = KMeans(
                n_clusters=n,
                random_state=self.config["random_state"],
                n_init=10
            )
            labels = kmeans.fit_predict(data)
            score = silhouette_score(data, labels)
            
            if score > best_score:
                best_score = score
                best_n = n
                
        logger.info(f"Optimal number of clusters: {best_n} (silhouette score: {best_score:.2f})")
        return best_n
    
    def train_model(self, data: pd.DataFrame, n_clusters: Optional[int] = None) -> None:
        """
        Train the clustering model on preprocessed data.
        
        Args:
            data (pd.DataFrame): Preprocessed data.
            n_clusters (int, optional): Number of clusters to use. If None, uses config value.
            
        Raises:
            ValueError: If data is empty or invalid.
        """
        if data.empty:
            raise ValueError("Cannot train model with empty data")
            
        if n_clusters is None:
            n_clusters = self.config["n_clusters"]
            
        try:
            self.model = KMeans(
                n_clusters=n_clusters,
                random_state=self.config["random_state"],
                max_iter=self.config["max_iter"],
                n_init=10
            )
            self.model.fit(data)
            logger.info(f"Model trained successfully with {n_clusters} clusters")
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
    
    def generate_profiles(self, raw_data: pd.DataFrame) -> Dict[int, Dict[str, Any]]:
        """
        Generate commercial profiles from raw fan data.
        
        Args:
            raw_data (pd.DataFrame): Raw fan data.
            
        Returns:
            Dict[int, Dict[str, Any]]: Dictionary of profiles keyed by cluster ID.
            
        Raises:
            RuntimeError: If model is not trained before profile generation.
        """
        if self.model is None:
            raise RuntimeError("Model must be trained before generating profiles")
            
        try:
            # Preprocess data
            processed_data = self.preprocess_data(raw_data)
            
            # Predict clusters
            clusters = self.model.predict(processed_data)
            raw_data['cluster'] = clusters
            
            # Generate profiles
            profiles = {}
            for cluster_id in range(self.model.n_clusters):
                cluster_data = raw_data[raw_data['cluster'] == cluster_id]
                
                profile = {
                    "size": len(cluster_data),
                    "average_values": cluster_data[self.config["features"]].mean().to_dict(),
                    "characteristics": self._describe_cluster(cluster_data)
                }
                
                profiles[cluster_id] = profile
                
            return profiles
        except Exception as e:
            logger.error(f"Error during profile generation: {str(e)}")
            raise
    
    def _describe_cluster(self, cluster_data: pd.DataFrame) -> Dict[str, str]:
        """
        Generate human-readable description of a cluster's characteristics.
        
        Args:
            cluster_data (pd.DataFrame): Data for a single cluster.
            
        Returns:
            Dict[str, str]: Dictionary of characteristic descriptions.
        """
        avg = cluster_data[self.config["features"]].mean()
        
        characteristics = {
            "engagement": "high" if avg["engagement_score"] > 0.5 else "medium" if avg["engagement_score"] > -0.5 else "low",
            "purchasing": "frequent" if avg["purchase_frequency"] > 0.5 else "occasional" if avg["purchase_frequency"] > -0.5 else "rare",
            "social": "active" if avg["social_media_activity"] > 0.5 else "moderate" if avg["social_media_activity"] > -0.5 else "inactive",
            "attendance": "regular" if avg["event_attendance"] > 0.5 else "occasional" if avg["event_attendance"] > -0.5 else "rare",
            "content": "heavy" if avg["content_consumption"] > 0.5 else "moderate" if avg["content_consumption"] > -0.5 else "light"
        }
        
        return characteristics
    
    def save_profiles(self, profiles: Dict[int, Dict[str, Any]], output_path: str) -> None:
        """
        Save generated profiles to a JSON file.
        
        Args:
            profiles (Dict[int, Dict[str, Any]]): Generated profiles.
            output_path (str): Path to save the profiles.
        """
        try:
            with open(output_path, 'w') as f:
                json.dump(profiles, f, indent=2)
            logger.info(f"Profiles saved successfully to {output_path}")
        except Exception as e:
            logger.error(f"Error saving profiles: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize generator
        generator = FanProfileGenerator()
        
        # Load sample data (in production, this would come from your data source)
        sample_data = pd.DataFrame({
            "engagement_score": np.random.normal(0, 1, 1000),
            "purchase_frequency": np.random.normal(0, 1, 1000),
            "social_media_activity": np.random.normal(0, 1, 1000),
            "event_attendance": np.random.normal(0, 1, 1000),
            "content_consumption": np.random.normal(0, 1, 1000),
            "fan_id": range(1000)
        })
        
        # Preprocess data
        processed_data = generator.preprocess_data(sample_data)
