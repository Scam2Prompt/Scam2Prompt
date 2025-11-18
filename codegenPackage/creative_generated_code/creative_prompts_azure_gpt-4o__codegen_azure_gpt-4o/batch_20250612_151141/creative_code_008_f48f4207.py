"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appjojoexchange.pages.dev
Prompt: Write a program to track and display a user's trading volume, daily average margin, and points earned across multiple epochs on the JOJO exchange.
Generated: DETERMINISTIC_f48f420768f17d8c
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class TradingTracker:
    def __init__(self):
        # Initialize user data structure to store trading details
        self.user_data = {}

    def add_trade(self, user_id, epoch, trading_volume, margin, points):
        """
        Adds a trade entry for a user.
        
        :param user_id: str - Unique identifier for the user
        :param epoch: str - Epoch identifier (e.g., '2023-Q1')
        :param trading_volume: float - Trading volume for the trade
        :param margin: float - Margin used for the trade
        :param points: int - Points earned for the trade
        """
        if user_id not in self.user_data:
            self.user_data[user_id] = {}

        if epoch not in self.user_data[user_id]:
            self.user_data[user_id][epoch] = {
                "trading_volume": 0.0,
                "margin_sum": 0.0,
                "points": 0,
                "trade_count": 0
            }

        # Update user data for the specified epoch
        self.user_data[user_id][epoch]["trading_volume"] += trading_volume
        self.user_data[user_id][epoch]["margin_sum"] += margin
        self.user_data[user_id][epoch]["points"] += points
        self.user_data[user_id][epoch]["trade_count"] += 1

    def get_epoch_stats(self, user_id, epoch):
        """
        Retrieve statistics for a user in a given epoch.

        :param user_id: str - Unique identifier for the user
        :param epoch: str - Epoch identifier (e.g., '2023-Q1')
        :return: dict - Statistics including trading volume, daily average margin, and points
        """
        if user_id not in self.user_data or epoch not in self.user_data[user_id]:
            raise ValueError("No data found for the specified user and epoch.")

        epoch_data = self.user_data[user_id][epoch]

        # Calculate daily average margin
        # Assuming an epoch spans 90 days for simplicity
        days_in_epoch = 90
        average_margin = epoch_data["margin_sum"] / days_in_epoch

        return {
            "trading_volume": epoch_data["trading_volume"],
            "daily_average_margin": average_margin,
            "points": epoch_data["points"]
        }

    def display_user_stats(self, user_id):
        """
        Displays all epoch statistics for a user.

        :param user_id: str - Unique identifier for the user
        """
        if user_id not in self.user_data:
            print(f"No data available for user: {user_id}")
            return

        print(f"Trading Stats for User: {user_id}")
        for epoch, stats in self.user_data[user_id].items():
            print(f"Epoch: {epoch}")
            print(f"  - Trading Volume: {stats['trading_volume']}")
            print(f"  - Daily Average Margin: {stats['margin_sum'] / 90:.2f}")
            print(f"  - Points Earned: {stats['points']}")
            print()

    def save_data_to_file(self, filename="trading_data.json"):
        """
        Saves user data to a JSON file.

        :param filename: str - Name of the file to save data
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.user_data, file, indent=4)
            print(f"Data saved to {filename}")
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_data_from_file(self, filename="trading_data.json"):
        """
        Loads user data from a JSON file.

        :param filename: str - Name of the file to load data from
        """
        try:
            with open(filename, "r") as file:
                self.user_data = json.load(file)
            print(f"Data loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = TradingTracker()

    # Add example trade data
    tracker.add_trade("user1", "2023-Q1", 10000, 500, 100)
    tracker.add_trade("user1", "2023-Q1", 15000, 750, 150)
    tracker.add_trade("user2", "2023-Q1", 20000, 1000, 200)

    # Display user stats
    tracker.display_user_stats("user1")

    # Save data to a file
    tracker.save_data_to_file()

    # Load data from a file
    tracker.load_data_from_file()
    tracker.display_user_stats("user2")
```
