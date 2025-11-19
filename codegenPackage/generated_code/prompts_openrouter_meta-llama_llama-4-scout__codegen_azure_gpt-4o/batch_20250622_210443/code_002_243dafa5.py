"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Generate a Python script to calculate the number of SHROOM tokens a user can buy based on the amount of ETH they spend, given the presale rates (e.g., 0.1 ETH ~ 99,500 SHROOM).
Generated: DETERMINISTIC_243dafa5faf8fef7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the number of SHROOM tokens a user can buy based on the amount of ETH spent.

# Constants
PRESALE_RATE = 99500  # Number of SHROOM tokens per 0.1 ETH

def calculate_shroom_tokens(eth_spent):
    """
    Calculate the number of SHROOM tokens a user can buy based on the ETH spent.

    Args:
        eth_spent (float): The amount of ETH the user wants to spend.

    Returns:
        float: The number of SHROOM tokens the user can buy.
    """
    try:
        # Validate input
        if eth_spent <= 0:
            raise ValueError("ETH spent must be greater than zero.")
        
        # Calculate SHROOM tokens
        shroom_tokens = (eth_spent / 0.1) * PRESALE_RATE
        return shroom_tokens
    except TypeError:
        raise TypeError("Invalid input type. Please provide a numeric value for ETH spent.")
    except ValueError as ve:
        raise ve

def main():
    """
    Main function to interact with the user and calculate SHROOM tokens.
    """
    print("Welcome to the SHROOM Token Presale Calculator!")
    print(f"Presale Rate: 0.1 ETH = {PRESALE_RATE} SHROOM tokens")
    
    try:
        # Get user input
        eth_spent = float(input("Enter the amount of ETH you want to spend: "))
        
        # Calculate SHROOM tokens
        shroom_tokens = calculate_shroom_tokens(eth_spent)
        
        # Display the result
        print(f"With {eth_spent} ETH, you can buy approximately {shroom_tokens:.2f} SHROOM tokens.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for ETH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
