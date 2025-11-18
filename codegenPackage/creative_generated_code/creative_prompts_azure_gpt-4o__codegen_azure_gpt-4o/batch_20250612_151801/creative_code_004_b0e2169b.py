"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitoadworld.pages.dev
Prompt: Write a script to calculate weekly giveaway winners for DigiToads based on interactions in Discord, Telegram, and Twitter, ensuring fair selection from the prize pool.
Generated: DETERMINISTIC_b0e2169b6af0e361
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import csv
from collections import Counter

# Constants
DISCORD_INTERACTIONS_FILE = "discord_interactions.csv"
TELEGRAM_INTERACTIONS_FILE = "telegram_interactions.csv"
TWITTER_INTERACTIONS_FILE = "twitter_interactions.csv"
PRIZE_POOL = ["Prize1", "Prize2", "Prize3", "Prize4", "Prize5"]  # Example prize pool
NUM_WINNERS = 5  # Number of weekly winners

def load_interactions(file_path):
    """
    Load interactions from a CSV file. 
    Assumes the file has a "username" column.

    :param file_path: Path to the CSV file
    :return: List of usernames
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row['username'] for row in reader if 'username' in row]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except KeyError:
        print(f"Error: 'username' column not found in the file {file_path}")
        return []

def merge_interactions(*interaction_lists):
    """
    Merge multiple interaction lists into a single list.

    :param interaction_lists: Lists of usernames from different platforms
    :return: Combined list of usernames
    """
    return [username for interaction_list in interaction_lists for username in interaction_list]

def select_winners(interactions, num_winners):
    """
    Select fair giveaway winners based on interaction frequency.

    :param interactions: List of usernames
    :param num_winners: Number of winners to select
    :return: List of selected winner usernames
    """
    if not interactions:
        print("Error: No interactions provided.")
        return []

    # Count interactions per user
    user_counts = Counter(interactions)

    # Create a weighted list based on interaction counts
    weighted_list = []
    for user, count in user_counts.items():
        weighted_list.extend([user] * count)

    # Select unique winners randomly
    try:
        winners = random.sample(set(weighted_list), min(num_winners, len(set(weighted_list))))
        return winners
    except ValueError:
        print("Error: Unable to select winners. Interaction list might be empty.")
        return []

def assign_prizes(winners, prize_pool):
    """
    Assign prizes to winners.

    :param winners: List of winner usernames
    :param prize_pool: List of prizes
    :return: Dictionary of winners and their assigned prizes
    """
    return {winner: prize_pool[i % len(prize_pool)] for i, winner in enumerate(winners)}

def main():
    """
    Main function to calculate weekly giveaway winners for DigiToads.
    """
    print("Loading interactions...")
    discord_interactions = load_interactions(DISCORD_INTERACTIONS_FILE)
    telegram_interactions = load_interactions(TELEGRAM_INTERACTIONS_FILE)
    twitter_interactions = load_interactions(TWITTER_INTERACTIONS_FILE)

    print("Merging interactions across platforms...")
    all_interactions = merge_interactions(discord_interactions, telegram_interactions, twitter_interactions)

    print("Selecting winners...")
    winners = select_winners(all_interactions, NUM_WINNERS)

    if winners:
        print("Assigning prizes...")
        winner_prizes = assign_prizes(winners, PRIZE_POOL)

        print("Weekly Giveaway Winners:")
        for winner, prize in winner_prizes.items():
            print(f"{winner}: {prize}")
    else:
        print("No winners selected.")

if __name__ == "__main__":
    main()
```
