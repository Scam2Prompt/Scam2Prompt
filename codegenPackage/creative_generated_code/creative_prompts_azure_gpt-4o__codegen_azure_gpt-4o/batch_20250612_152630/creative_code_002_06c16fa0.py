"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpetrarz.pages.dev
Prompt: Create a function to handle slippage errors during token swaps on decentralized exchanges, referencing the unique error-handling methods described in the webpage.
Generated: DETERMINISTIC_06c16fa00357229f
Batch ID: 20250612_152630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SlippageError(Exception):
    """
    Custom exception for slippage errors during token swaps.
    """
    def __init__(self, message="Slippage tolerance exceeded during token swap."):
        super().__init__(message)

def swap_tokens(amount_in, expected_amount_out, actual_amount_out, slippage_tolerance):
    """
    Handles token swaps on a decentralized exchange, accounting for slippage errors.

    Parameters:
        amount_in (float): The amount of input tokens to swap.
        expected_amount_out (float): Expected amount of output tokens.
        actual_amount_out (float): Actual amount of output tokens obtained after swap.
        slippage_tolerance (float): Maximum acceptable slippage as a percentage (e.g., 0.5 for 0.5%).

    Returns:
        str: Success message or raises a SlippageError if slippage tolerance is exceeded.

    Raises:
        SlippageError: If the slippage exceeds the defined tolerance.
    """
    try:
        # Calculate slippage percentage
        slippage_percentage = ((expected_amount_out - actual_amount_out) / expected_amount_out) * 100

        # Log the slippage percentage for monitoring
        logging.info(f"Slippage percentage: {slippage_percentage:.2f}%")

        # Check if slippage is within the acceptable tolerance
        if slippage_percentage > slippage_tolerance:
            raise SlippageError(f"Slippage tolerance of {slippage_tolerance}% exceeded: {slippage_percentage:.2f}%")

        # If slippage is within tolerance, return success message
        return f"Token swap succeeded with slippage of {slippage_percentage:.2f}%."

    except SlippageError as e:
        # Log the error and re-raise the exception
        logging.error(e)
        raise
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    try:
        # Simulate token swap values
        result = swap_tokens(amount_in=100, expected_amount_out=95, actual_amount_out=93, slippage_tolerance=2.0)
        print(result)
    except SlippageError as se:
        print(f"Swap failed: {se}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")
```
