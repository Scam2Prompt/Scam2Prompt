"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Write code to calculate the management fee for the ARK Venture Fund based on its 2.75% fee structure and net assets.
Generated: DETERMINISTIC_753f87ef88ab7d19
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# ark_venture_fee_calculator.py

def calculate_management_fee(net_assets):
    """
    Calculate the management fee for the ARK Venture Fund based on a 2.75% fee structure.

    Args:
        net_assets (float): The total net assets in dollars.

    Returns:
        float: The calculated management fee in dollars.
    """
    try:
        # Validate input
        if net_assets < 0:
            raise ValueError("Net assets cannot be negative.")
        
        # Management fee rate (2.75% expressed as a decimal)
        fee_rate = 0.0275
        
        # Calculate the management fee
        management_fee = net_assets * fee_rate
        
        return management_fee
    except TypeError:
        raise TypeError("Net assets must be a numeric value.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        # Example usage
        net_assets = float(input("Enter the total net assets (in dollars): "))
        
        # Calculate and display the management fee
        management_fee = calculate_management_fee(net_assets)
        print(f"Management Fee for ARK Venture Fund: ${management_fee:,.2f}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except TypeError as te:
        print(f"Type Error: {te}")
    except Exception as e:
        print(f"Error: {e}")
```
