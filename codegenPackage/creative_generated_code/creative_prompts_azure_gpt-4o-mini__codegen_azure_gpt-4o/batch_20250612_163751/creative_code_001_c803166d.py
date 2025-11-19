"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogleonidas.pages.dev
Prompt: Write a function to calculate the amount of DOG tokens received based on the ETH amount invested during the DOG token presale.
Generated: DETERMINISTIC_c803166d1b28f648
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate the amount of DOG tokens received based on invested ETH during the presale.

def calculate_dog_tokens(eth_amount, exchange_rate):
    """
    Calculate the number of DOG tokens received based on ETH investment.

    Args:
    eth_amount (float): The amount of ETH invested.
    exchange_rate (float): The rate of DOG tokens per ETH.

    Returns:
    float: The number of DOG tokens received.
    """
    try:
        # Validate inputs
        if eth_amount < 0:
            raise ValueError("ETH amount must be non-negative.")
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be greater than zero.")

        # Calculate the DOG tokens
        dog_tokens = eth_amount * exchange_rate
        return dog_tokens

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Define the ETH investment and exchange rate
    eth_invested = 2.5  # Example: 2.5 ETH
    dog_exchange_rate = 3000  # Example: 3000 DOG tokens per ETH

    # Calculate the DOG tokens
    received_tokens = calculate_dog_tokens(eth_invested, dog_exchange_rate)

    if received_tokens is not None:
        print(f"ETH Invested: {eth_invested}, Exchange Rate: {dog_exchange_rate}")
        print(f"DOG Tokens Received: {received_tokens}")
```
