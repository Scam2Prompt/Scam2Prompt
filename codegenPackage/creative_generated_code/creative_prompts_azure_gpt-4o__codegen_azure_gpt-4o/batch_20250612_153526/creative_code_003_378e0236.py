"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenafinance.vercel.app
Prompt: Create a leaderboard system for tracking weekly challenge participation in the $PLENA Road to TGE campaign using Galxe data.
Generated: DETERMINISTIC_378e0236962561ea
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

# Simulated data for demonstration purposes
# In production, this function should connect to the Galxe API or database to fetch real participation data.
def fetch_galxe_data():
    """
    Fetch mock data from Galxe database (replace with actual API integration).
    Returns:
        List[Dict]: List of participant data.
    """
    return [
        {"username": "Alice", "activity_points": 120, "last_participation_date": "2023-10-01"},
        {"username": "Bob", "activity_points": 150, "last_participation_date": "2023-10-03"},
        {"username": "Charlie", "activity_points": 80, "last_participation_date": "2023-09-30"},
        {"username": "Diana", "activity_points": 200, "last_participation_date": "2023-10-02"},
    ]


class Leaderboard:
    """
    Leaderboard system for tracking weekly challenge participation.
    """
    def __init__(self):
        self.participants = []

    def calculate_weekly_leaderboard(self):
        """
        Calculate the leaderboard based on weekly participation data.
        Filters participants who participated within the last week and sorts them by activity points.

        Returns:
            List[Dict]: Sorted leaderboard data.
        """
        self.participants = fetch_galxe_data()
        
        # Calculate the current week date range
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())  # Start of the week (Monday)
        week_end = week_start + timedelta(days=6)            # End of the week (Sunday)
        
        # Filter participants based on last participation date within the current week
        weekly_participants = [
            p for p in self.participants
            if week_start <= datetime.strptime(p['last_participation_date'], "%Y-%m-%d") <= week_end
        ]
        
        # Sort participants by activity points (descending)
        leaderboard = sorted(weekly_participants, key=lambda x: x['activity_points'], reverse=True)
        return leaderboard

    def display_leaderboard(self):
        """
        Display the leaderboard in a user-friendly format.
        """
        leaderboard = self.calculate_weekly_leaderboard()
        if not leaderboard:
            print("No participants found for this week's leaderboard.")
            return

        print("Leaderboard - Weekly Challenge Participation")
        print("-------------------------------------------")
        for rank, participant in enumerate(leaderboard, 1):
            print(f"Rank {rank}: {participant['username']} - {participant['activity_points']} points")
        print("-------------------------------------------")


def main():
    """
    Main function to run the leaderboard system.
    """
    try:
        leaderboard_system = Leaderboard()
        leaderboard_system.display_leaderboard()
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
