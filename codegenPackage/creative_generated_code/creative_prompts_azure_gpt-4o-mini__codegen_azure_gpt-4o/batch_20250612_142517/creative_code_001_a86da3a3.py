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
# Import necessary modules
import json

def filter_microloan_offers(offers, min_amount, max_amount):
    """
    Filters microloan offers based on the minimum and maximum loan amounts.

    Parameters:
    - offers (list of dict): List of microloan offers as dictionaries.
    - min_amount (float): Minimum loan amount.
    - max_amount (float): Maximum loan amount.
    
    Returns:
    - list of dict: Filtered list of offers that fall within the specified range.
    """
    # Validate inputs
    if not isinstance(offers, list):
        raise ValueError("Offers must be a list of dictionaries.")
    
    if not all(isinstance(offer, dict) for offer in offers):
        raise ValueError("Each offer must be a dictionary.")
    
    if not isinstance(min_amount, (int, float)) or not isinstance(max_amount, (int, float)):
        raise ValueError("Minimum and maximum amounts must be numeric.")
    
    if min_amount > max_amount:
        raise ValueError("Minimum amount cannot be greater than maximum amount.")

    # Filter offers based on the specified loan amounts
    filtered_offers = [
        offer for offer in offers
        if min_amount <= offer.get("loan_amount", 0) <= max_amount
    ]

    return filtered_offers


# Example usage
if __name__ == "__main__":
    # Sample microloan offers (in Kazakhstan)
    microloan_offers = [
        {"offer_id": 1, "loan_amount": 50000, "currency": "KZT"},
        {"offer_id": 2, "loan_amount": 150000, "currency": "KZT"},
        {"offer_id": 3, "loan_amount": 300000, "currency": "KZT"},
        {"offer_id": 4, "loan_amount": 450000, "currency": "KZT"}
    ]

    try:
        # Define minimum and maximum loan amounts for filtering
        min_loan_amount = 100000
        max_loan_amount = 400000

        # Filter offers
        filtered_offers = filter_microloan_offers(microloan_offers, min_loan_amount, max_loan_amount)

        # Print results in JSON format for better readability
        print(json.dumps(filtered_offers, indent=4))
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error: {e}")
```
