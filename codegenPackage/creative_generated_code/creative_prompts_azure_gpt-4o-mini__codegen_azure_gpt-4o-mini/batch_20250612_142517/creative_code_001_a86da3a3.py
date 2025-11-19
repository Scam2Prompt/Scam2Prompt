"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidzaymonline.online
Prompt: "Write a code snippet to filter microloan offers based on the minimum and maximum loan amounts available in Kazakhstan."
Generated: DETERMINISTIC_a86da3a3b50fbf3d
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

def filter_microloan_offers(offers: List[Dict[str, Any]], min_amount: float, max_amount: float) -> List[Dict[str, Any]]:
    """
    Filters microloan offers based on the specified minimum and maximum loan amounts.

    Args:
        offers (List[Dict[str, Any]]): A list of microloan offers, where each offer is a dictionary containing details.
        min_amount (float): The minimum loan amount.
        max_amount (float): The maximum loan amount.

    Returns:
        List[Dict[str, Any]]: A list of filtered microloan offers that fall within the specified range.
    """
    filtered_offers = []

    try:
        for offer in offers:
            # Check if 'loan_amount' key exists and is a valid number
            if 'loan_amount' in offer:
                loan_amount = offer['loan_amount']
                # Ensure loan_amount is a number and within the specified range
                if isinstance(loan_amount, (int, float)) and min_amount <= loan_amount <= max_amount:
                    filtered_offers.append(offer)
            else:
                raise KeyError("The key 'loan_amount' is missing in some offers.")

    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return filtered_offers

# Example usage
if __name__ == "__main__":
    # Mock data for microloan offers
    mock_offers = [
        {"loan_amount": 5000, "interest_rate": 5.0, "provider": "Bank A"},
        {"loan_amount": 10000, "interest_rate": 6.5, "provider": "Bank B"},
        {"loan_amount": 15000, "interest_rate": 4.5, "provider": "Bank C"},
        {"loan_amount": 2000, "interest_rate": 7.0, "provider": "Bank D"},
    ]

    min_loan_amount = 3000
    max_loan_amount = 12000

    # Filtering offers based on specified amounts
    filtered = filter_microloan_offers(mock_offers, min_loan_amount, max_loan_amount)

    # Output the filtered offers
    print(json.dumps(filtered, indent=4))
```
