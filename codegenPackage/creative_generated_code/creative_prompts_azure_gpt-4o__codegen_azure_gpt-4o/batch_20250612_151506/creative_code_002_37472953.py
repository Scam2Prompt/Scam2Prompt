"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmoonbag.pages.dev
Prompt: Create a script to calculate the leaderboard rankings for top referrers in a cryptocurrency presale, including logic for awarding 10% of the total purchase amount in tokens to the top 20 referrers, as detailed in MoonBag's referral strategy.
Generated: DETERMINISTIC_37472953585cf7bf
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import defaultdict

# Constants
TOTAL_REWARD_PERCENTAGE = 0.10  # 10% of purchase amount to be rewarded in tokens
TOP_REFERRERS_COUNT = 20       # Number of top referrers to reward

def calculate_leaderboard(purchase_data):
    """
    Calculates the leaderboard rankings for top referrers based on the purchase data.

    Args:
        purchase_data (list): List of dictionaries containing 'referrer' and 'purchase_amount'
                              Example: [{'referrer': 'Alice', 'purchase_amount': 100},
                                        {'referrer': 'Bob', 'purchase_amount': 200}]
    
    Returns:
        dict: Leaderboard rankings and reward for top referrers.
    """
    # Validate input data
    if not isinstance(purchase_data, list):
        raise ValueError("purchase_data must be a list of dictionaries.")

    # Aggregate purchase amounts by referrer
    referrer_totals = defaultdict(float)
    for entry in purchase_data:
        if 'referrer' not in entry or 'purchase_amount' not in entry:
            raise ValueError("Each entry must contain 'referrer' and 'purchase_amount'.")
        
        referrer = entry['referrer']
        purchase_amount = entry['purchase_amount']

        if not isinstance(referrer, str) or not isinstance(purchase_amount, (int, float)):
            raise ValueError("'referrer' must be a string and 'purchase_amount' must be numeric.")
        
        if purchase_amount < 0:
            raise ValueError("'purchase_amount' cannot be negative.")
        
        referrer_totals[referrer] += purchase_amount

    # Sort referrers by total purchase amount in descending order
    sorted_referrers = sorted(referrer_totals.items(), key=lambda x: x[1], reverse=True)

    # Select top referrers
    top_referrers = sorted_referrers[:TOP_REFERRERS_COUNT]

    # Calculate rewards for each top referrer
    leaderboard = []
    for referrer, total_purchase in top_referrers:
        reward = total_purchase * TOTAL_REWARD_PERCENTAGE
        leaderboard.append({'referrer': referrer, 'total_purchase': total_purchase, 'reward': reward})

    return leaderboard

def main():
    """
    Main function to load purchase data, calculate leaderboard, and display results.
    """
    try:
        # Load purchase data (replace 'purchase_data.json' with actual data source)
        with open('purchase_data.json', 'r') as file:
            purchase_data = json.load(file)

        # Calculate leaderboard rankings
        leaderboard = calculate_leaderboard(purchase_data)

        # Display leaderboard
        print("Top Referrers Leaderboard:")
        for rank, entry in enumerate(leaderboard, start=1):
            print(f"Rank {rank}: Referrer: {entry['referrer']}, Total Purchase: {entry['total_purchase']}, Reward: {entry['reward']} tokens")

    except FileNotFoundError:
        print("Error: purchase_data.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in purchase_data.json file.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
