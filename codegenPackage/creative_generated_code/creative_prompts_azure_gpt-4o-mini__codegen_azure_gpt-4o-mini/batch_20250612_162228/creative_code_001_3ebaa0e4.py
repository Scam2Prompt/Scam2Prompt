"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogdog.pages.dev
Prompt: Write a Python script that calculates the number of DOG tokens received for different ETH amounts during the presale, given the conversion rate of 0.1 ETH for 99,500 DOG.
Generated: DETERMINISTIC_3ebaa0e49aa8dbef
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# dog_token_calculator.py

def calculate_dog_tokens(eth_amount: float, conversion_rate: float = 0.1, dog_tokens_per_eth: int = 99500) -> int:
    """
    Calculate the number of DOG tokens received for a given amount of ETH.
    
    Parameters:
    eth_amount (float): The amount of ETH to convert to DOG tokens.
    conversion_rate (float): The rate of ETH to DOG tokens. Default is 0.1 ETH for 99,500 DOG.
    dog_tokens_per_eth (int): The number of DOG tokens received per conversion rate of ETH. Default is 99,500 DOG.
    
    Returns:
    int: The number of DOG tokens received.
    
    Raises:
    ValueError: If eth_amount is negative or conversion_rate is non-positive.
    """
    # Validate inputs
    if eth_amount < 0:
        raise ValueError("ETH amount must be non-negative.")
    if conversion_rate <= 0:
        raise ValueError("Conversion rate must be positive.")

    # Calculate DOG tokens received based on the ETH amount
    dog_tokens_received = (eth_amount / conversion_rate) * dog_tokens_per_eth
    return int(dog_tokens_received)


def main():
    """
    Main function to run the DOG token calculation based on user input.
    """
    try:
        # Get ETH amount from user input
        eth_amount = float(input("Enter the amount of ETH to convert to DOG tokens: "))
        
        # Calculate DOG tokens
        dog_tokens = calculate_dog_tokens(eth_amount)
        
        # Display the result
        print(f"For {eth_amount} ETH, you will receive {dog_tokens} DOG tokens.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
