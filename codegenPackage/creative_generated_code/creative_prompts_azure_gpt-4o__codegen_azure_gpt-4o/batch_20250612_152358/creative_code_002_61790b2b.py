"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc82mx10.pages.dev
Prompt: Develop a program that calculates the remaining Notcoin to be distributed based on the provided statistics ($85 million distributed, $15 million left).
Generated: DETERMINISTIC_61790b2bd0f65389
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate the remaining Notcoin to be distributed

def calculate_remaining_notcoin(distributed_amount, total_amount):
    """
    Calculate the remaining amount of Notcoin to be distributed.
    
    :param distributed_amount: Amount of Notcoin already distributed (in millions)
    :param total_amount: Total amount of Notcoin available for distribution (in millions)
    :return: Remaining amount of Notcoin to be distributed (in millions)
    """
    try:
        # Validate inputs
        if distributed_amount < 0 or total_amount < 0:
            raise ValueError("Amounts must be non-negative.")
        if distributed_amount > total_amount:
            raise ValueError("Distributed amount cannot exceed total amount.")
        
        # Calculate the remaining Notcoin
        remaining_amount = total_amount - distributed_amount
        return remaining_amount
        
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return None
    
if __name__ == "__main__":
    # Initial statistics
    distributed_notcoin = 85  # $85 million distributed
    total_notcoin = 100       # Total $100 million available (85 + 15)
    
    # Calculate the remaining Notcoin
    remaining_notcoin = calculate_remaining_notcoin(distributed_notcoin, total_notcoin)
    
    if remaining_notcoin is not None:
        # Display the result
        print(f"Remaining Notcoin to be distributed: ${remaining_notcoin} million")
```
