"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdiumclaim.pages.dev
Prompt: Create a program to evenly distribute 5% of the total Holdium supply among users who preordered Solana Mobile Chapter 2 before July 12th, as described on the website.
Generated: DETERMINISTIC_794dd3babd78292e
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
import datetime

# Constants
TOTAL_HOLDIUM_SUPPLY = 1_000_000_000  # Example total Holdium supply
DISTRIBUTION_PERCENTAGE = 0.05  # 5% distribution
PREORDER_CUTOFF_DATE = datetime.date(2023, 7, 12)  # Cutoff date for preorders

# Function to validate preorder eligibility
def is_preorder_eligible(preorder_date):
    """
    Checks if a preorder date is eligible for distribution.

    Args:
        preorder_date (datetime.date): Date of the user's preorder.

    Returns:
        bool: True if eligible, False otherwise.
    """
    return preorder_date <= PREORDER_CUTOFF_DATE

# Function to distribute Holdium evenly
def distribute_holdium(preorder_users):
    """
    Distributes 5% of the total Holdium supply evenly among eligible users.

    Args:
        preorder_users (list of dict): List of users with preorder information.
            Each user is represented as a dictionary with keys 'user_id' and 'preorder_date'.

    Returns:
        dict: Dictionary with user IDs as keys and distributed Holdium as values.
    """
    # Filter eligible users
    eligible_users = [
        user for user in preorder_users if is_preorder_eligible(user['preorder_date'])
    ]

    # Check if there are any eligible users
    if not eligible_users:
        raise ValueError("No eligible users found for distribution.")

    # Calculate the total Holdium to distribute
    total_distributed_holdium = TOTAL_HOLDIUM_SUPPLY * DISTRIBUTION_PERCENTAGE

    # Calculate the amount per user
    holdium_per_user = total_distributed_holdium / len(eligible_users)

    # Prepare the distribution result
    distribution_result = {
        user['user_id']: holdium_per_user for user in eligible_users
    }

    return distribution_result

# Example usage
if __name__ == "__main__":
    try:
        # Example list of users with preorder dates
        preorder_users = [
            {'user_id': 'user_1', 'preorder_date': datetime.date(2023, 7, 10)},
            {'user_id': 'user_2', 'preorder_date': datetime.date(2023, 6, 25)},
            {'user_id': 'user_3', 'preorder_date': datetime.date(2023, 7, 13)},  # Not eligible
            {'user_id': 'user_4', 'preorder_date': datetime.date(2023, 7, 5)},
        ]

        # Distribute Holdium
        distribution = distribute_holdium(preorder_users)

        # Print the distribution result
        print("Holdium Distribution:")
        for user_id, holdium_amount in distribution.items():
            print(f"User {user_id}: {holdium_amount:.2f} Holdium")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
