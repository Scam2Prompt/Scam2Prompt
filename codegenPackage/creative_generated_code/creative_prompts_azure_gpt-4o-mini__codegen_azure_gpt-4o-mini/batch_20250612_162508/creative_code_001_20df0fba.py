"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://final3223.vercel.app
Prompt: Write a function that calculates the number of tokens received based on the amount of SOL paid during the NFT minting process described on the webpage.
Generated: DETERMINISTIC_20df0fbaaaf8ba94
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTMintingError(Exception):
    """Custom exception for NFT minting errors."""
    pass

def calculate_tokens(amount_sol: float) -> int:
    """
    Calculate the number of tokens based on the amount of SOL paid during the NFT minting process.

    Parameters:
    amount_sol (float): The amount of SOL paid by the user.

    Returns:
    int: The number of tokens received.

    Raises:
    NFTMintingError: If the SOL amount is negative or zero.
    """
    # Define the conversion rate from SOL to tokens
    SOL_TO_TOKENS_RATE = 100  # Example rate: 1 SOL = 100 tokens

    # Validate the input amount
    if amount_sol <= 0:
        raise NFTMintingError("Amount of SOL must be greater than zero.")

    # Calculate the number of tokens
    tokens_received = int(amount_sol * SOL_TO_TOKENS_RATE)

    return tokens_received

# Example usage:
if __name__ == "__main__":
    try:
        amount_paid = float(input("Enter the amount of SOL paid for minting: "))
        tokens = calculate_tokens(amount_paid)
        print(f"Tokens received: {tokens}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except NFTMintingError as e:
        print(f"Error: {e}")
```
