"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://locinews.com
Prompt: Develop a function to calculate and display the leaderboard for Bet88 users based on their betting performance and winnings.
Generated: DETERMINISTIC_8cda0b7868a5de93
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import operator

def calculate_leaderboard(users):
    """
    Calculate and display the leaderboard for Bet88 users based on their betting performance and winnings.

    Args:
        users (list of dict): A list of user dictionaries containing 'name', 'bets', and 'winnings' keys.
                              Example:
                              [
                                {"name": "Alice", "bets": 15, "winnings": 1000},
                                {"name": "Bob", "bets": 10, "winnings": 750},
                              ]

    Returns:
        list of dict: A sorted list of user dictionaries representing the leaderboard.
    """

    try:
        if not isinstance(users, list):
            raise ValueError("Input 'users' should be a list of dictionaries.")

        # Validate the structure of each user dictionary
        for user in users:
            if not all(key in user for key in ("name", "bets", "winnings")):
                raise ValueError("Each user dictionary must contain 'name', 'bets', and 'winnings' keys.")
            if not isinstance(user["name"], str) or not isinstance(user["bets"], int) or not isinstance(user["winnings"], (int, float)):
                raise ValueError("Invalid data types in user dictionary.")

        # Sort users based on winnings (descending). If winnings are equal, sort by bets (ascending).
        leaderboard = sorted(users, key=lambda u: (-u["winnings"], u["bets"]))

        # Display leaderboard
        print("Bet88 Leaderboard:")
        print("------------------")
        for rank, user in enumerate(leaderboard, start=1):
            print(f"{rank}. {user['name']} - Winnings: ${user['winnings']} | Bets: {user['bets']}")
        
        return leaderboard

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while calculating the leaderboard: {e}")
        return []

# Example usage
if __name__ == "__main__":
    users_data = [
        {"name": "Alice", "bets": 15, "winnings": 1000},
        {"name": "Bob", "bets": 10, "winnings": 750},
        {"name": "Charlie", "bets": 5, "winnings": 1000},
    ]
    calculate_leaderboard(users_data)
```
