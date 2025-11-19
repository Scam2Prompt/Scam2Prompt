"""
Generated Code Metadata:
========================
Original URL: https://evamobi.com
Prompt: How can I leverage laser-focused targeting in my in-app advertising to reach specific demographics effectively?
Generated: DETERMINISTIC_1fab2d7877b5b1b1
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# In-App Advertising Targeting System

```python
import json
from typing import Dict, List, Optional
from enum import Enum
import logging
from datetime import datetime, date
import pytz

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Demographics(Enum):
    """Enum for supported demographic categories"""
    AGE = "age"
    GENDER = "gender"
    LOCATION = "location"
    INCOME = "income"
    INTERESTS = "interests"
    DEVICE = "device"
    BEHAVIOR = "behavior"

class AdTargetingSystem:
    """
    A system for managing laser-focused in-app advertising targeting based on demographics.
    
    Attributes:
        ads (Dict): Dictionary storing ads with their targeting criteria
        user_profiles (Dict): Dictionary storing user demographic data
    """
    
    def __init__(self):
        self.ads = {}
        self.user_profiles = {}
    
    def add_ad(
        self,
        ad_id: str,
        content: str,
        targeting_criteria: Dict[Demographics, List],
        bid_price: float
    ) -> bool:
        """
        Add a new ad with targeting criteria to the system.
        
        Args:
            ad_id: Unique identifier for the ad
            content: Ad content to display
            targeting_criteria: Dictionary of demographic criteria
            bid_price: Maximum bid price for this ad
            
        Returns:
            bool: True if ad was added successfully
        """
        try:
            if ad_id in self.ads:
                logger.warning(f"Ad with ID {ad_id} already exists")
                return False
                
            # Validate targeting criteria
            for demo in targeting_criteria:
                if not isinstance(demo, Demographics):
                    raise ValueError(f"Invalid demographic category: {demo}")
            
            self.ads[ad_id] = {
                "content": content,
                "targeting_criteria": targeting_criteria,
                "bid_price": bid_price,
                "impressions": 0,
                "clicks": 0,
                "created_at": datetime.now(pytz.UTC)
            }
            return True
        except Exception as e:
            logger.error(f"Error adding ad {ad_id}: {str(e)}")
            return False
    
    def add_user_profile(
        self,
        user_id: str,
        demographics: Dict[Demographics, any]
    ) -> bool:
        """
        Add or update a user profile with demographic information.
        
        Args:
            user_id: Unique identifier for the user
            demographics: Dictionary of demographic information
            
        Returns:
            bool: True if profile was added/updated successfully
        """
        try:
            # Validate demographics
            for demo in demographics:
                if not isinstance(demo, Demographics):
                    raise ValueError(f"Invalid demographic category: {demo}")
            
            self.user_profiles[user_id] = demographics
            return True
        except Exception as e:
            logger.error(f"Error adding user profile {user_id}: {str(e)}")
            return False
    
    def get_targeted_ads(
        self,
        user_id: str,
        limit: int = 5
    ) -> Optional[List[Dict]]:
        """
        Get ads targeted for a specific user based on their demographics.
        
        Args:
            user_id: User to target ads for
            limit: Maximum number of ads to return
            
        Returns:
            List of matching ads (sorted by bid price) or None if error
        """
        try:
            if user_id not in self.user_profiles:
                logger.warning(f"No profile found for user {user_id}")
                return None
                
            user_demo = self.user_profiles[user_id]
            matching_ads = []
            
            for ad_id, ad in self.ads.items():
                matches = True
                
                # Check each targeting criterion
                for demo, target_values in ad["targeting_criteria"].items():
                    if demo in user_demo:
                        user_value = user_demo[demo]
                        
                        # Handle different demographic types
                        if demo == Demographics.AGE:
                            if not (target_values[0] <= user_value <= target_values[1]):
                                matches = False
                                break
                        elif demo == Demographics.LOCATION:
                            if user_value not in target_values:
                                matches = False
                                break
                        else:
                            if user_value not in target_values:
                                matches = False
                                break
                
                if matches:
                    matching_ads.append({
                        "ad_id": ad_id,
                        "content": ad["content"],
                        "bid_price": ad["bid_price"],
                        "score": self._calculate_relevance_score(ad, user_demo)
                    })
            
            # Sort by relevance score (descending) then bid price (descending)
            matching_ads.sort(key=lambda x: (-x["score"], -x["bid_price"]))
            
            # Update impressions for returned ads
            for ad in matching_ads[:limit]:
                self.ads[ad["ad_id"]]["impressions"] += 1
            
            return matching_ads[:limit]
        except Exception as e:
            logger.error(f"Error getting targeted ads for user {user_id}: {str(e)}")
            return None
    
    def _calculate_relevance_score(self, ad: Dict, user_demo: Dict) -> float:
        """
        Calculate a relevance score between 0-1 for an ad based on user demographics.
        
        Args:
            ad: Ad dictionary
            user_demo: User demographic data
            
        Returns:
            float: Relevance score (higher is more relevant)
        """
        score = 0.0
        total_weight = 0
        
        # Define weights for different demographics
        weights = {
            Demographics.AGE: 0.3,
            Demographics.GENDER: 0.2,
            Demographics.LOCATION: 0.25,
            Demographics.INTERESTS: 0.15,
            Demographics.BEHAVIOR: 0.1
        }
        
        for demo, target_values in ad["targeting_criteria"].items():
            if demo in user_demo:
                user_value = user_demo[demo]
                
                # Calculate match score for this demographic
                if demo == Demographics.AGE:
                    # Normalize age match (closer to middle of range is better)
                    age_range = target_values[1] - target_values[0]
                    distance = min(abs(user_value - target_values[0]), 
                                  abs(user_value - target_values[1]))
                    demo_score = 1 - (distance / age_range)
                else:
                    demo_score = 1.0 if user_value in target_values else 0.0
                
                # Apply weight
                weight = weights.get(demo, 0.05)
                score += demo_score * weight
                total_weight += weight
        
        # Normalize score if any weights were applied
        if total_weight > 0:
            score /= total_weight
        
        return round(score, 2)
    
    def record_click(self, ad_id: str) -> bool:
        """
        Record a click event for an ad.
        
        Args:
            ad_id: ID of the ad that was clicked
            
        Returns:
            bool: True if click was recorded successfully
        """
        try:
            if ad_id not in self.ads:
                logger.warning(f"Ad {ad_id} not found")
                return False
                
            self.ads[ad_id]["clicks"] += 1
            return True
        except Exception as e:
            logger.error(f"Error recording click for ad {ad_id}: {str(e)}")
            return False
    
    def get_performance_metrics(self, ad_id: str) -> Optional[Dict]:
        """
        Get performance metrics for an ad.
        
        Args:
            ad_id: ID of the ad to get metrics for
            
        Returns:
            Dictionary with performance metrics or None if error
        """
        try:
            if ad_id not in self.ads:
                logger.warning(f"Ad {ad_id} not found")
                return None
                
            ad = self.ads[ad_id]
            impressions = ad["impressions"]
            clicks = ad["clicks"]
            
            return {
                "ad_id": ad_id,
                "impressions": impressions,
                "clicks": clicks,
                "ctr": round(clicks / impressions, 4) if impressions > 0 else 0,
                "created_at": ad["created_at"].isoformat(),
                "bid_price": ad["bid_price"]
            }
        except Exception as e:
            logger.error(f"Error getting metrics for ad {ad_id}: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    targeting_system = AdTargetingSystem()
    
    # Add some ads with targeting criteria
    targeting_system.add_ad(
        ad_id="ad1",
        content="Summer Sale - 50% off swimwear!",
        targeting_criteria={
            Demographics.AGE: [18, 35],
            Demographics.GENDER: ["female"],
            Demographics.LOCATION: ["CA", "FL", "TX"],
            Demographics.INTERESTS: ["fashion", "beach"]
        },
        bid_price=1.20
    )
    
    targeting_system.add_ad(
        ad_id="ad2
