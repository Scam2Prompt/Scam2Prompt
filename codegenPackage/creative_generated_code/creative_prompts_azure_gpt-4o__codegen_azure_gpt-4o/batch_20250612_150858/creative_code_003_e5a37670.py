"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-tumbler.to
Prompt: Develop a Python program that calculates the random commission (0.5% to 1%) charged by the ETH Tumbler service for a given Ether transaction amount.
Generated: DETERMINISTIC_e5a37670b3b230c2
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_tumbler_commission(ether_amount):
    """
    Calculate the commission charged by the ETH Tumbler service.

    The commission is randomized between 0.5% and 1%.
    
    Args:
        ether_amount (float): The amount of Ether to calculate commission for.
    
    Returns:
        float: The commission charged in Ether.
    """
    try:
        # Ensure the input amount is valid
        if ether_amount <= 0:
            raise ValueError("Ether amount must be greater than zero.")
        
        # Randomize the commission percentage between 0.5% (0.005) and 1% (0.01)
        commission_rate = random.uniform(0.005, 0.01)
        
        # Calculate the commission in Ether
        commission = ether_amount * commission_rate
        return commission
    
    except TypeError:
        raise TypeError("Invalid input. Please enter a numeric value for Ether amount.")

def main():
    """
    Main function to run the ETH Tumbler commission calculation program.
    """
    try:
        # Prompt user for Ether transaction amount
        ether_amount = float(input("Enter the Ether amount for the transaction: "))
        
        # Calculate the commission
        commission = calculate_tumbler_commission(ether_amount)
        
        # Display the results
        print(f"Transaction Amount: {ether_amount:.6f} ETH")
        print(f"Random Commission Rate: {commission / ether_amount:.4%}")
        print(f"Commission Charged: {commission:.6f} ETH")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
