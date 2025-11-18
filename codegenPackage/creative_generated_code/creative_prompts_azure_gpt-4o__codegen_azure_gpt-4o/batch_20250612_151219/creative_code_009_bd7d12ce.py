"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbbag.com
Prompt: Develop a program to calculate the monthly rewards for top 20 referrers in MoonBag's referral program, based on the total amount purchased using their referral codes.
Generated: DETERMINISTIC_bd7d12ce6edf1a39
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from decimal import Decimal

# Constants
TOP_REFERRER_COUNT = 20

# Database connection details
DB_PATH = "moonbag.db"

# Function to fetch referral data from the database
def fetch_referral_data():
    """
    Fetches the referral data from the database.

    Returns:
        list of tuples: Each tuple contains (referrer_id, total_amount).
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Query to calculate the total amount purchased using each referrer code
        query = """
        SELECT referrer_id, SUM(amount) as total_amount
        FROM purchases
        GROUP BY referrer_id
        ORDER BY total_amount DESC
        LIMIT ?
        """
        
        cursor.execute(query, (TOP_REFERRER_COUNT,))
        results = cursor.fetchall()
        
        conn.close()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

# Function to calculate rewards for each referrer
def calculate_rewards(referral_data, reward_percentage):
    """
    Calculates rewards based on referral data.

    Args:
        referral_data (list of tuples): Referral data with referrer_id and total_amount.
        reward_percentage (float): The percentage of total_amount given as rewards.

    Returns:
        list of tuples: Each tuple contains (referrer_id, reward_amount).
    """
    rewards = []
    for referrer_id, total_amount in referral_data:
        # Calculate reward based on percentage
        reward_amount = Decimal(total_amount) * Decimal(reward_percentage / 100)
        rewards.append((referrer_id, round(reward_amount, 2)))  # Round to 2 decimal places
    return rewards

# Function to display rewards
def display_rewards(rewards):
    """
    Displays rewards for top referrers.

    Args:
        rewards (list of tuples): Each tuple contains (referrer_id, reward_amount).
    """
    print(f"{'Referrer ID':<15} {'Reward Amount ($)':<15}")
    print("-" * 30)
    for referrer_id, reward_amount in rewards:
        print(f"{referrer_id:<15} {reward_amount:<15}")

def main():
    """
    Main function to execute the referral rewards calculation.
    """
    # Reward percentage (for example, 5%)
    reward_percentage = 5.0

    print("Fetching referral data...")
    referral_data = fetch_referral_data()

    if not referral_data:
        print("No referral data available or an error occurred.")
        return

    print("Calculating rewards...")
    rewards = calculate_rewards(referral_data, reward_percentage)

    print("Displaying rewards for top referrers...")
    display_rewards(rewards)

if __name__ == "__main__":
    main()
```
