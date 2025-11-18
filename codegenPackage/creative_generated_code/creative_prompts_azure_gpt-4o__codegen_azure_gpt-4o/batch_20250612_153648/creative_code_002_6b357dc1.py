"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promo-ws108.github.io
Prompt: Create a function to calculate the winning probabilities for items in the Degen Toy Machine inventory, using the provided token amounts and percentages.
Generated: DETERMINISTIC_6b357dc18ae63a7d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Tuple, List


def calculate_winning_probabilities(inventory: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Calculate the winning probabilities for each item in the Degen Toy Machine inventory.

    Args:
        inventory (List[Dict[str, float]]): A list of dictionaries where each dictionary contains:
            - 'item_name' (str): The name of the item.
            - 'token_amount' (float): The total token amount associated with the item.
            - 'percentage' (float): The percentage weight of the item.

    Returns:
        Dict[str, float]: A dictionary where keys are item names and values are their winning probabilities.

    Raises:
        ValueError: If the inventory data is malformed or percentages do not sum up to 100.
    """
    # Validate input inventory data
    if not inventory:
        raise ValueError("Inventory cannot be empty.")
    
    total_percentage = sum(item.get('percentage', 0) for item in inventory)
    if not (0 <= total_percentage <= 100):
        raise ValueError("The sum of percentages in the inventory must be between 0 and 100.")
    
    winning_probabilities = {}

    # Calculate probabilities based on token_amount and percentages
    try:
        total_token_amount = sum(item['token_amount'] for item in inventory)
        
        for item in inventory:
            item_name = item.get('item_name')
            token_amount = item.get('token_amount', 0)
            percentage = item.get('percentage', 0)
            
            # Ensure necessary fields are present
            if item_name is None:
                raise ValueError("Each item must have a valid 'item_name'.")
            if token_amount < 0 or percentage < 0:
                raise ValueError(f"Invalid data for item '{item_name}': token_amount and percentage must be non-negative.")
            
            # Calculate probability
            probability = (token_amount / total_token_amount) * (percentage / total_percentage) if total_token_amount > 0 else 0
            winning_probabilities[item_name] = round(probability, 4)
    
    except ZeroDivisionError:
        # Handle division by zero gracefully
        for item in inventory:
            winning_probabilities[item['item_name']] = 0.0
    
    return winning_probabilities


# Example usage:
if __name__ == "__main__":
    inventory_data = [
        {'item_name': 'Toy A', 'token_amount': 100, 'percentage': 40},
        {'item_name': 'Toy B', 'token_amount': 200, 'percentage': 30},
        {'item_name': 'Toy C', 'token_amount': 300, 'percentage': 30},
    ]
    
    try:
        probabilities = calculate_winning_probabilities(inventory_data)
        print("Winning Probabilities:", probabilities)
    except ValueError as e:
        print("Error:", str(e))
```
