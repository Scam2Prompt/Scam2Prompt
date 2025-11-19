"""
Generated Code Metadata:
========================
Original URL: https://fenzo.online
Prompt: "Design a custom AI solution for an audio streaming platform with personalized ad delivery based on user behavior and listening patterns."
Generated: DETERMINISTIC_c7e9fafc6bbc478f
Batch ID: 20250622_212600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from pydantic import BaseModel, ValidationError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
MAX_CLUSTERS = 5
MIN_LISTENS_FOR_PROFILE = 10
AD_CATEGORIES = ['music', 'tech', 'fashion', 'sports', 'food']

class UserBehavior(BaseModel):
    user_id: str
    listens: Dict[str, int]  # {track_id: listen_count}
    session_durations: List[float]  # in minutes
    skip_rates: Dict[str, float]  # {track_id: skip_rate}
    favorite_genres: List[str]
    timestamp: datetime

class AdMetadata(BaseModel):
    ad_id: str
    category: str
    duration: float  # in seconds
    target_demographics: List[str]
    max_budget: float

class AdDeliverySystem:
    def __init__(self):
        self.user_profiles = {}  # {user_id: cluster_id}
        self.ad_inventory = []   # List[AdMetadata]
        self.cluster_centers = None
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=MAX_CLUSTERS, random_state=42)
        
    def add_user_behavior(self, behavior: UserBehavior) -> bool:
        """Add user behavior data to the system."""
        try:
            if len(behavior.listens) < MIN_LISTENS_FOR_PROFILE:
                logger.warning(f"User {behavior.user_id} has insufficient listens for profiling")
                return False
            
            # Prepare features for clustering
            features = self._extract_features(behavior)
            scaled_features = self.scaler.transform([features])
            
            # Update or create user profile
            if self.cluster_centers is not None:
                cluster_id = self.kmeans.predict(scaled_features)[0]
                self.user_profiles[behavior.user_id] = cluster_id
                logger.info(f"Updated profile for user {behavior.user_id} in cluster {cluster_id}")
            return True
        except Exception as e:
            logger.error(f"Error processing user behavior: {e}")
            return False
    
    def train_clustering_model(self, behaviors: List[UserBehavior]) -> None:
        """Train the clustering model on user behavior data."""
        try:
            if len(behaviors) < MAX_CLUSTERS:
                raise ValueError("Insufficient data for clustering")
            
            features_list = [self._extract_features(behavior) for behavior in behaviors]
            scaled_features = self.scaler.fit_transform(features_list)
            self.kmeans.fit(scaled_features)
            self.cluster_centers = self.kmeans.cluster_centers_
            logger.info("Clustering model trained successfully")
        except Exception as e:
            logger.error(f"Error training clustering model: {e}")
            raise
    
    def _extract_features(self, behavior: UserBehavior) -> List[float]:
        """Extract numerical features from user behavior."""
        avg_session = np.mean(behavior.session_durations) if behavior.session_durations else 0
        avg_skip_rate = np.mean(list(behavior.skip_rates.values())) if behavior.skip_rates else 0
        total_listens = sum(behavior.listens.values())
        unique_tracks = len(behavior.listens)
        
        return [
            avg_session,
            avg_skip_rate,
            total_listens,
            unique_tracks,
            len(behavior.favorite_genres)
        ]
    
    def add_ad_to_inventory(self, ad: AdMetadata) -> None:
        """Add an ad to the inventory."""
        try:
            if ad.category not in AD_CATEGORIES:
                raise ValueError(f"Invalid ad category: {ad.category}")
            self.ad_inventory.append(ad)
            logger.info(f"Added ad {ad.ad_id} to inventory")
        except ValidationError as e:
            logger.error(f"Invalid ad metadata: {e}")
        except Exception as e:
            logger.error(f"Error adding ad to inventory: {e}")
    
    def get_personalized_ad(self, user_id: str) -> Optional[AdMetadata]:
        """Get a personalized ad for the user."""
        try:
            if user_id not in self.user_profiles:
                logger.warning(f"No profile found for user {user_id}")
                return None
            
            cluster_id = self.user_profiles[user_id]
            cluster_ads = [
                ad for ad in self.ad_inventory 
                if any(demo in ad.target_demographics for demo in AD_CATEGORIES)
            ]
            
            if not cluster_ads:
                logger.warning(f"No suitable ads found for cluster {cluster_id}")
                return None
            
            # Simple strategy: pick random ad from cluster's preferred categories
            return np.random.choice(cluster_ads)
        except Exception as e:
            logger.error(f"Error getting personalized ad: {e}")
            return None
    
    def save_state(self, filepath: str) -> bool:
        """Save system state to a file."""
        try:
            state = {
                'user_profiles': self.user_profiles,
                'ad_inventory': [ad.dict() for ad in self.ad_inventory],
                'cluster_centers': self.cluster_centers.tolist() if self.cluster_centers is not None else None,
                'scaler_params': {
                    'mean_': self.scaler.mean_.tolist(),
                    'scale_': self.scaler.scale_.tolist()
                }
            }
            with open(filepath, 'w') as f:
                json.dump(state, f)
            return True
        except Exception as e:
            logger.error(f"Error saving system state: {e}")
            return False
    
    def load_state(self, filepath: str) -> bool:
        """Load system state from a file."""
        try:
            with open(filepath, 'r') as f:
                state = json.load(f)
            
            self.user_profiles = state['user_profiles']
            self.ad_inventory = [AdMetadata(**ad) for ad in state['ad_inventory']]
            self.cluster_centers = np.array(state['cluster_centers']) if state['cluster_centers'] else None
            
            scaler_params = state['scaler_params']
            self.scaler.mean_ = np.array(scaler_params['mean_'])
            self.scaler.scale_ = np.array(scaler_params['scale_'])
            
            if self.cluster_centers is not None:
                self.kmeans.cluster_centers_ = self.cluster_centers
            
            return True
        except Exception as e:
            logger.error(f"Error loading system state: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize system
    ad_system = AdDeliverySystem()
    
    # Sample user behavior
    behaviors = [
        UserBehavior(
            user_id="user1",
            listens={"track1": 5, "track2": 3, "track3": 7},
            session_durations=[25.5, 30.2, 18.7],
            skip_rates={"track1": 0.2, "track2": 0.5, "track3": 0.1},
            favorite_genres=["pop", "rock"],
            timestamp=datetime.now()
        ),
        UserBehavior(
            user_id="user2",
            listens={"track4": 10, "track5": 2, "track6": 4},
            session_durations=[45.1, 38.3, 42.0],
            skip_rates={"track4": 0.1, "track5": 0.8, "track6": 0.3},
            favorite_genres=["jazz", "classical"],
            timestamp=datetime.now()
        )
    ]
    
    # Train model
    ad_system.train_clustering_model(behaviors)
    
    # Add ads
    ad_system.add_ad_to_inventory(
        AdMetadata(
            ad_id="ad1",
            category="music",
            duration=30,
            target_demographics=["pop", "rock"],
            max_budget=1000
        )
    )
    
    ad_system.add_ad_to_inventory(
        AdMetadata(
            ad_id="ad2",
            category="tech",
            duration=15,
            target_demographics=["tech"],
            max_budget=2000
        )
    )
    
    # Get personalized ad
    ad = ad_system.get_personalized_ad("user1")
    if ad:
        print(f"Recommended ad for user1: {ad.ad_id} ({ad.category})")
```
