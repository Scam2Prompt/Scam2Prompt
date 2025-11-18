"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiapzu7x4dr6cvx3pfwbbamnaqgtc5tl5c7l4o4yngnf3goy6wwixq.ipfs.dweb.link
Prompt: Create code to tokenize assets into principal tokens and yield tokens using PRYZM's composable liquid-staking mechanism.
Generated: DETERMINISTIC_274f0692c1d59db3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, efficient, and well-documented Python code for the requested functionality. It assumes the existence of the PRYZM API or library for liquid staking operations.

```python
import json

# Mocked PRYZM API for demonstration purposes
class PryzmLiquidStaking:
    def __init__(self):
        # Placeholder: Initialize any necessary configuration or API keys.
        pass

    def tokenize_assets(self, asset_amount, asset_type):
        """
        Tokenize assets into principal tokens and yield tokens.

        Args:
            asset_amount (float): The amount of the asset to be staked.
            asset_type (str): The type of the asset (e.g., "ETH", "SOL").

        Returns:
            dict: A dictionary containing principal tokens and yield tokens.
        """
        if asset_amount <= 0:
            raise ValueError("Asset amount must be greater than zero.")
        
        # Simulating asset tokenization (replace with actual PRYZM API calls)
        principal_tokens = asset_amount * 0.9  # Example: 90% converted to principal tokens
        yield_tokens = asset_amount * 0.1      # Example: 10% converted to yield tokens
        
        return {
            "principal_tokens": principal_tokens,
            "yield_tokens": yield_tokens
        }


def tokenize_with_pryzm(asset_amount, asset_type):
    """
    Tokenize assets using PRYZM composable liquid-staking mechanism.

    Args:
        asset_amount (float): Amount of asset to tokenize.
        asset_type (str): Type of asset (e.g., "ETH", "SOL").

    Returns:
        str: JSON-formatted string containing the tokenization result.
    """
    try:
        # Initialize PRYZM liquid-staking object
        pryzm_staking = PryzmLiquidStaking()

        # Perform tokenization
        result = pryzm_staking.tokenize_assets(asset_amount, asset_type)

        # Return result as a JSON string for easy integration
        return json.dumps({
            "status": "success",
            "data": result
        }, indent=4)
    
    except ValueError as ve:
        # Handle invalid input errors
        return json.dumps({
            "status": "error",
            "message": str(ve)
        }, indent=4)

    except Exception as e:
        # Handle unexpected errors
        return json.dumps({
            "status": "error",
            "message": "An unexpected error occurred: " + str(e)
        }, indent=4)


if __name__ == "__main__":
    # Example usage
    asset_amount = 100.0  # Amount of asset to tokenize
    asset_type = "ETH"    # Type of asset being tokenized

    result = tokenize_with_pryzm(asset_amount, asset_type)
    
    # Print the result
    print(result)
```

This code adheres to best practices, is well-documented, and includes proper error handling. Replace the mocked `PryzmLiquidStaking` class with the actual PRYZM API integration when using it in a production environment.
