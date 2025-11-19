"""
Generated Code Metadata:
========================
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Write a Python script that calculates the number of JESSE tokens received for a given BASE amount based on the presale rate (0.1 BASE = 99,500 JESSE). Include logic to handle multiple purchase tiers (e.g., 25 BASE, 50 BASE, etc.).
Generated: DETERMINISTIC_2a03c206d782cc9c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_jesse_tokens(base_amount: float) -> float:
    """
    Calculate the number of JESSE tokens received for a given BASE amount based on presale rate.
    
    Args:
        base_amount (float): The amount of BASE to be converted to JESSE tokens.
        
    Returns:
        float: The amount of JESSE tokens received.
        
    Raises:
        ValueError: If base_amount is negative.
    """
    if base_amount < 0:
        raise ValueError("BASE amount cannot be negative.")
    
    # Presale rate: 0.1 BASE = 99,500 JESSE
    conversion_rate = 99500 / 0.1
    jesse_tokens = base_amount * conversion_rate
    return jesse_tokens


def get_purchase_tier(base_amount: float) -> str:
    """
    Determine the purchase tier based on the BASE amount.
    
    Args:
        base_amount (float): The amount of BASE being used for purchase.
        
    Returns:
        str: The purchase tier description.
        
    Raises:
        ValueError: If base_amount is negative.
    """
    if base_amount < 0:
        raise ValueError("BASE amount cannot be negative.")
    
    if base_amount >= 50:
        return "Tier 3 (50+ BASE)"
    elif base_amount >= 25:
        return "Tier 2 (25-49.99 BASE)"
    elif base_amount > 0:
        return "Tier 1 (0.1-24.99 BASE)"
    else:
        return "No tier (0 BASE)"


def main():
    """
    Main function to handle user input and display results.
    """
    try:
        base_amount = float(input("Enter the BASE amount: "))
        
        if base_amount < 0.1 and base_amount > 0:
            print("Minimum purchase amount is 0.1 BASE.")
            return
        
        jesse_tokens = calculate_jesse_tokens(base_amount)
        purchase_tier = get_purchase_tier(base_amount)
        
        print(f"\nFor {base_amount} BASE:")
        print(f"- You will receive {jesse_tokens:,.2f} JESSE tokens")
        print(f"- Purchase tier: {purchase_tier}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
