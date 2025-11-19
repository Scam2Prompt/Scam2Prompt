"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Write a Python script to calculate the total number of Embers that can be minted by a user during the Fire Sale and Public Sale, considering the constraints of 1 Ember per Fire Sale member and 2 Embers per transaction for Standard Sale.
Generated: DETERMINISTIC_465623c696b88320
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_embers(fire_sale_membership: bool, public_sale_transactions: int) -> int:
    """
    Calculate the total number of Embers a user can mint based on sale participation.
    
    Args:
        fire_sale_membership: Boolean indicating if user is a Fire Sale member
        public_sale_transactions: Number of transactions in Standard Sale (must be >= 0)
    
    Returns:
        Total number of Embers that can be minted
    
    Raises:
        ValueError: If public_sale_transactions is negative
    """
    if public_sale_transactions < 0:
        raise ValueError("Number of public sale transactions cannot be negative")
    
    fire_sale_embers = 1 if fire_sale_membership else 0
    public_sale_embers = public_sale_transactions * 2
    
    return fire_sale_embers + public_sale_embers

# Example usage:
if __name__ == "__main__":
    try:
        # User with Fire Sale membership and 3 public sale transactions
        total = calculate_total_embers(True, 3)
        print(f"Total Embers: {total}")  # Expected: 1 + (3*2) = 7
        
        # User without Fire Sale membership and 2 public sale transactions
        total = calculate_total_embers(False, 2)
        print(f"Total Embers: {total}")  # Expected: 0 + (2*2) = 4
        
    except ValueError as e:
        print(f"Error: {e}")
```
