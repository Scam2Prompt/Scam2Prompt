"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorswap.shop
Prompt: Create a script to track trade volume and user metrics for an NFT trading platform, inspired by Grailswap's reported statistics (e.g., 4.7k+ swaps, $258K+ trade volume).
Generated: DETERMINISTIC_8ca8993cbe38cbf6
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script for tracking trade volume and user metrics for an NFT trading platform:

```python
import json
from datetime import datetime
from typing import List, Dict

class NFTTradingPlatform:
    """
    A class to track trade volume and user metrics for an NFT trading platform.
    """

    def __init__(self):
        """
        Initializes the platform with empty metrics.
        """
        self.total_swaps = 0  # Total number of swaps performed
        self.total_trade_volume = 0.0  # Total trade volume in USD
        self.user_metrics = {}  # Stores user-specific metrics: {user_id: {"swaps": int, "trade_volume": float}}

    def record_swap(self, user_id: str, trade_volume: float):
        """
        Records a trade (swap) and updates metrics for both the platform and the user.

        Args:
        - user_id (str): Unique identifier for the user performing the swap.
        - trade_volume (float): The monetary value of the trade in USD.

        Raises:
        - ValueError: If trade_volume is not positive.
        """
        if trade_volume <= 0:
            raise ValueError("Trade volume must be a positive value.")

        # Update overall metrics
        self.total_swaps += 1
        self.total_trade_volume += trade_volume

        # Update user-specific metrics
        if user_id not in self.user_metrics:
            self.user_metrics[user_id] = {"swaps": 0, "trade_volume": 0.0}
        self.user_metrics[user_id]["swaps"] += 1
        self.user_metrics[user_id]["trade_volume"] += trade_volume

    def get_platform_metrics(self) -> Dict[str, float]:
        """
        Returns the overall metrics for the platform.

        Returns:
        - Dict[str, float]: Dictionary containing total swaps and trade volume.
        """
        return {
            "total_swaps": self.total_swaps,
            "total_trade_volume": self.total_trade_volume,
        }

    def get_user_metrics(self, user_id: str) -> Dict[str, float]:
        """
        Returns the metrics for a specific user.

        Args:
        - user_id (str): Unique identifier for the user.

        Returns:
        - Dict[str, float]: Dictionary containing user's swap count and trade volume.

        Raises:
        - KeyError: If the user_id does not exist in the user metrics.
        """
        if user_id not in self.user_metrics:
            raise KeyError(f"No metrics found for user_id: {user_id}")
        return self.user_metrics[user_id]

    def export_metrics_to_json(self, file_path: str):
        """
        Exports the metrics to a JSON file.

        Args:
        - file_path (str): Path to the JSON file where metrics will be saved.
        """
        data = {
            "platform_metrics": self.get_platform_metrics(),
            "user_metrics": self.user_metrics,
        }
        try:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
        except IOError as e:
            print(f"Error exporting metrics to JSON: {e}")

    def import_metrics_from_json(self, file_path: str):
        """
        Imports metrics from a JSON file and updates the platform's data.

        Args:
        - file_path (str): Path to the JSON file containing metrics.

        Raises:
        - FileNotFoundError: If the file does not exist.
        - ValueError: If the file format is invalid.
        """
        try:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
                self.total_swaps = data["platform_metrics"]["total_swaps"]
                self.total_trade_volume = data["platform_metrics"]["total_trade_volume"]
                self.user_metrics = data["user_metrics"]
        except FileNotFoundError:
            raise FileNotFoundError(f"No file found at {file_path}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid file format: {e}")


# Example usage
if __name__ == "__main__":
    platform = NFTTradingPlatform()

    # Record a few swaps
    try:
        platform.record_swap("user1", 150.75)
        platform.record_swap("user2", 107.50)
        platform.record_swap("user1", 200.25)

        # Display platform metrics
        print("Platform Metrics:", platform.get_platform_metrics())

        # Display user metrics
        print("User1 Metrics:", platform.get_user_metrics("user1"))
        print("User2 Metrics:", platform.get_user_metrics("user2"))

        # Export metrics to a JSON file
        platform.export_metrics_to_json("metrics.json")

        # Import metrics back from the JSON file
        platform.import_metrics_from_json("metrics.json")
        print("Metrics successfully imported from JSON file.")
    except Exception as e:
        print(f"Error: {e}")
```

This script is a complete solution that tracks NFT trading metrics, handles errors gracefully, and allows exporting/importing data.
