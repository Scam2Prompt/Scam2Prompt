"""
Generated Code Metadata:
========================
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: Create a program to track and display rewards for advertisers based on their engagement with the Rivalz AI-powered data and attention economy.
Generated: DETERMINISTIC_200e98b2eedf1c0d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class AdvertiserRewardTracker:
    """
    A class to track and manage rewards for advertisers based on their engagement metrics.
    """

    def __init__(self, storage_file: str = "advertiser_rewards.json"):
        """
        Initialize the reward tracker with a storage file.
        
        Args:
            storage_file: Path to JSON file for persistent storage
        """
        self.storage_file = storage_file
        self.rewards_data = self._load_data()

    def _load_data(self) -> Dict:
        """
        Load advertiser rewards data from storage file.
        Creates new file if it doesn't exist.
        
        Returns:
            Dictionary containing rewards data
        """
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"advertisers": {}}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in storage file")
        except Exception as e:
            raise RuntimeError(f"Error loading data: {str(e)}")

    def _save_data(self) -> None:
        """
        Save current rewards data to storage file.
        """
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.rewards_data, f, indent=2)
        except Exception as e:
            raise RuntimeError(f"Error saving data: {str(e)}")

    def register_advertiser(self, advertiser_id: str, name: str) -> None:
        """
        Register a new advertiser in the system.
        
        Args:
            advertiser_id: Unique identifier for the advertiser
            name: Display name of the advertiser
        """
        if advertiser_id in self.rewards_data["advertisers"]:
            raise ValueError("Advertiser already exists")
        
        self.rewards_data["advertisers"][advertiser_id] = {
            "name": name,
            "engagement_metrics": {
                "impressions": 0,
                "clicks": 0,
                "conversions": 0,
                "attention_time": 0  # in seconds
            },
            "rewards": 0,
            "transactions": []
        }
        self._save_data()

    def update_engagement(self, advertiser_id: str, metrics: Dict) -> None:
        """
        Update engagement metrics for an advertiser.
        
        Args:
            advertiser_id: ID of the advertiser to update
            metrics: Dictionary containing metrics to update
                    Supported keys: impressions, clicks, conversions, attention_time
        """
        if advertiser_id not in self.rewards_data["advertisers"]:
            raise ValueError("Advertiser not found")
        
        valid_metrics = ["impressions", "clicks", "conversions", "attention_time"]
        for metric, value in metrics.items():
            if metric not in valid_metrics:
                raise ValueError(f"Invalid metric: {metric}")
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(f"Invalid value for {metric}")
            
            self.rewards_data["advertisers"][advertiser_id]["engagement_metrics"][metric] += value
        
        self._calculate_rewards(advertiser_id)
        self._save_data()

    def _calculate_rewards(self, advertiser_id: str) -> None:
        """
        Calculate rewards based on engagement metrics.
        Reward formula:
        - Base reward per impression: 0.1 points
        - Bonus per click: 1 point
        - Bonus per conversion: 10 points
        - Attention time bonus: 0.01 points per second
        
        Args:
            advertiser_id: ID of the advertiser to calculate rewards for
        """
        metrics = self.rewards_data["advertisers"][advertiser_id]["engagement_metrics"]
        
        impression_rewards = metrics["impressions"] * 0.1
        click_rewards = metrics["clicks"] * 1
        conversion_rewards = metrics["conversions"] * 10
        attention_rewards = metrics["attention_time"] * 0.01
        
        total_rewards = impression_rewards + click_rewards + conversion_rewards + attention_rewards
        
        # Record transaction
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "rewards_earned": total_rewards - self.rewards_data["advertisers"][advertiser_id]["rewards"],
            "new_balance": total_rewards,
            "metrics": metrics.copy()
        }
        
        self.rewards_data["advertisers"][advertiser_id]["rewards"] = total_rewards
        self.rewards_data["advertisers"][advertiser_id]["transactions"].append(transaction)

    def get_advertiser_info(self, advertiser_id: str) -> Dict:
        """
        Get all information for a specific advertiser.
        
        Args:
            advertiser_id: ID of the advertiser to retrieve
        
        Returns:
            Dictionary containing advertiser information
        """
        if advertiser_id not in self.rewards_data["advertisers"]:
            raise ValueError("Advertiser not found")
        
        return self.rewards_data["advertisers"][advertiser_id]

    def get_top_advertisers(self, limit: int = 10) -> List[Tuple[str, float]]:
        """
        Get top advertisers by reward points.
        
        Args:
            limit: Maximum number of advertisers to return
        
        Returns:
            List of tuples (advertiser_id, rewards) sorted by rewards descending
        """
        advertisers = [
            (adv_id, data["rewards"])
            for adv_id, data in self.rewards_data["advertisers"].items()
        ]
        return sorted(advertisers, key=lambda x: x[1], reverse=True)[:limit]

    def redeem_rewards(self, advertiser_id: str, amount: float) -> float:
        """
        Redeem reward points for an advertiser.
        
        Args:
            advertiser_id: ID of the advertiser redeeming points
            amount: Amount of points to redeem
        
        Returns:
            New reward balance after redemption
        """
        if advertiser_id not in self.rewards_data["advertisers"]:
            raise ValueError("Advertiser not found")
        
        current_balance = self.rewards_data["advertisers"][advertiser_id]["rewards"]
        if amount > current_balance:
            raise ValueError("Insufficient reward balance")
        
        self.rewards_data["advertisers"][advertiser_id]["rewards"] -= amount
        
        # Record redemption transaction
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "rewards_redeemed": amount,
            "new_balance": current_balance - amount,
            "type": "redemption"
        }
        self.rewards_data["advertisers"][advertiser_id]["transactions"].append(transaction)
        
        self._save_data()
        return current_balance - amount


# Example usage
if __name__ == "__main__":
    try:
        tracker = AdvertiserRewardTracker()
        
        # Register advertisers
        tracker.register_advertiser("adv1", "Brand X")
        tracker.register_advertiser("adv2", "Company Y")
        
        # Update engagement metrics
        tracker.update_engagement("adv1", {"impressions": 1000, "clicks": 50, "attention_time": 500})
        tracker.update_engagement("adv2", {"impressions": 2000, "clicks": 30, "conversions": 5})
        
        # Display top advertisers
        print("Top Advertisers:")
        for adv_id, rewards in tracker.get_top_advertisers():
            info = tracker.get_advertiser_info(adv_id)
            print(f"{info['name']}: {rewards:.2f} points")
        
        # Redeem rewards
        new_balance = tracker.redeem_rewards("adv1", 50)
        print(f"Advertiser 1 new balance: {new_balance:.2f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
