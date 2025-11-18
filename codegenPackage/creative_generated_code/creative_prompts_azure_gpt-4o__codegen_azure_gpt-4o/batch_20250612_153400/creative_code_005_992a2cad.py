"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-dogio.pages.dev
Prompt: Create a function to calculate the number of DOG tokens received for a given ETH deposit amount, based on the presale exchange rate (e.g., 0.1 ETH = 99,500 DOG).
Generated: DETERMINISTIC_992a2cada522f906
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate the number of DOG tokens received for a given ETH deposit amount.
# Presale exchange rate: 0.1 ETH = 99,500 DOG

# Import necessary modules
from decimal import Decimal, InvalidOperation

def calculate_dog_tokens(eth_amount: float) -> int:
    """
    Calculate the number of DOG tokens received for a given ETH deposit amount.

    Args:
        eth_amount (float): The amount of ETH deposited.

    Returns:
        int: The number of DOG tokens received.
    
    Raises:
        ValueError: If the provided ETH amount is invalid or negative.
    """
    try:
        # Validate and convert the input to Decimal for precision
        eth_amount_decimal = Decimal(str(eth_amount))
        
        if eth_amount_decimal <= 0:
            raise ValueError("ETH amount must be greater than zero.")
        
        # Presale exchange rate constants
        exchange_rate_eth = Decimal("0.1")  # ETH equivalent for rate calculation
        exchange_rate_dog = Decimal("99500")  # DOG tokens received for 0.1 ETH
        
        # Calculate the DOG token amount
        dog_tokens = (eth_amount_decimal / exchange_rate_eth) * exchange_rate_dog
        
        # Return the DOG token amount as an integer (tokens are typically whole numbers)
        return int(dog_tokens)
    
    except InvalidOperation:
        # Handle invalid numeric input
        raise ValueError("Invalid ETH amount provided. Ensure it is a valid numeric value.")
    except Exception as e:
        # Handle unforeseen errors
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")


# Example usage (uncomment the lines below to test the function):
# try:
#     eth_input = 0.5  # Replace with user input or dynamic value
#     dog_tokens_received = calculate_dog_tokens(eth_input)
#     print(f"For {eth_input} ETH, you will receive {dog_tokens_received} DOG tokens.")
# except Exception as error:
#     print(f"Error: {error}")
```
