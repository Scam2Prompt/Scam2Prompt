"""
Generated Code Metadata:
========================
Original URL: https://usdt-mixer-mix.com
Prompt: Develop a Python program that calculates the service fee for mixing USDT transactions based on the number of Coinjoins and initiation fee, as outlined on the USDT Mixer website.
Generated: DETERMINISTIC_0e9269d4cd633ed9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_service_fee(num_coinjoins, initiation_fee):
    """
    Calculate the service fee for mixing USDT transactions based on the number of Coinjoins and initiation fee.
    
    Args:
        num_coinjoins (int): Number of Coinjoins in the transaction.
        initiation_fee (float): Initiation fee in percentage (e.g., 0.5 for 0.5%).
        
    Returns:
        float: Total service fee in percentage.
        
    Raises:
        ValueError: If num_coinjoins is not a positive integer or initiation_fee is negative.
    """
    # Validate inputs
    if not isinstance(num_coinjoins, int) or num_coinjoins <= 0:
        raise ValueError("Number of Coinjoins must be a positive integer.")
    if initiation_fee < 0:
        raise ValueError("Initiation fee cannot be negative.")
    
    # Calculate the service fee based on the number of Coinjoins
    if num_coinjoins == 1:
        service_fee = 0.01  # 1%
    elif num_coinjoins == 2:
        service_fee = 0.02  # 2%
    elif num_coinjoins == 3:
        service_fee = 0.03  # 3%
    else:
        service_fee = 0.05  # 5% for 4 or more Coinjoins
    
    # Add the initiation fee
    total_fee = service_fee + (initiation_fee / 100)  # Convert initiation_fee from percentage to decimal
    
    # Round to 2 decimal places for percentage representation
    return round(total_fee * 100, 2)

# Example usage
if __name__ == "__main__":
    try:
        num_coinjoins = int(input("Enter the number of Coinjoins: "))
        initiation_fee = float(input("Enter the initiation fee percentage (e.g., 0.5 for 0.5%): "))
        
        total_fee = calculate_service_fee(num_coinjoins, initiation_fee)
        print(f"Total service fee: {total_fee}%")
    except ValueError as e:
        print(f"Error: {e}")
```
