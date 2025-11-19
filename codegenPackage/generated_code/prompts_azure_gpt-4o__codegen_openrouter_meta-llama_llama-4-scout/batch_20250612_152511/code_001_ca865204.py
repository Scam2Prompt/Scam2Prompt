"""
Generated Code Metadata:
========================
Original URL: https://everyworld-started.pages.dev
Prompt: Create a function in Python to calculate the total points pledged to environmental charities based on Everyworld's payout data.
Generated: DETERMINISTIC_ca86520484720b3e
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Module to calculate total points pledged to environmental charities based on Everyworld's payout data.
"""

import logging

def calculate_environmental_charity_points(payout_data):
    """
    Calculate the total points pledged to environmental charities.

    Args:
        payout_data (list): A list of dictionaries containing payout data.
            Each dictionary should have the following keys:
                - 'charity_category' (str): The category of the charity.
                - 'points_pledged' (int): The number of points pledged.

    Returns:
        int: The total points pledged to environmental charities.

    Raises:
        ValueError: If payout_data is not a list or if a dictionary in payout_data is missing required keys.
    """

    # Initialize total points to 0
    total_points = 0

    # Check if payout_data is a list
    if not isinstance(payout_data, list):
        logging.error("payout_data must be a list")
        raise ValueError("payout_data must be a list")

    # Define environmental charity categories
    environmental_categories = ['environmental', 'conservation', 'animal_welfare']

    # Iterate over each payout in payout_data
    for payout in payout_data:
        # Check if payout is a dictionary
        if not isinstance(payout, dict):
            logging.error("Each payout in payout_data must be a dictionary")
            raise ValueError("Each payout in payout_data must be a dictionary")

        # Check if payout has required keys
        required_keys = ['charity_category', 'points_pledged']
        if not all(key in payout for key in required_keys):
            logging.error("Each payout dictionary must have 'charity_category' and 'points_pledged' keys")
            raise ValueError("Each payout dictionary must have 'charity_category' and 'points_pledged' keys")

        # Check if charity category is environmental
        if payout['charity_category'].lower() in environmental_categories:
            # Add points pledged to total
            total_points += payout['points_pledged']

    return total_points


def main():
    # Example usage
    payout_data = [
        {'charity_category': 'environmental', 'points_pledged': 100},
        {'charity_category': 'health', 'points_pledged': 50},
        {'charity_category': 'conservation', 'points_pledged': 200},
        {'charity_category': 'education', 'points_pledged': 150},
        {'charity_category': 'animal_welfare', 'points_pledged': 300}
    ]

    try:
        total_points = calculate_environmental_charity_points(payout_data)
        print(f"Total points pledged to environmental charities: {total_points}")
    except ValueError as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    main()
```
