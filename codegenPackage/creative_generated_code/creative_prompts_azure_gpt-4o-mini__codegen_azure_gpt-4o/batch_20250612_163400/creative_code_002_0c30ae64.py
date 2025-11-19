"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gdg-1i3.pages.dev
Prompt: Generate a function to handle slippage errors during token swaps based on the guidance from the GDG-1I3 webpage.
Generated: DETERMINISTIC_0c30ae64123845a8
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SlippageError(Exception):
    """
    Custom exception for slippage errors during token swaps.
    """
    pass


def handle_slippage_error(expected_amount: float, actual_amount: float, tolerance: float) -> bool:
    """
    Handles slippage errors during token swaps by comparing expected and actual amounts.
    
    Args:
        expected_amount (float): The expected token amount from the swap.
        actual_amount (float): The actual token amount received from the swap.
        tolerance (float): The acceptable tolerance percentage (e.g., 0.05 for 5% tolerance).

    Returns:
        bool: True if the slippage is within the tolerance, False otherwise.

    Raises:
        SlippageError: If the slippage is outside the acceptable tolerance.
    """
    try:
        # Validate input data
        if tolerance < 0 or tolerance > 1:
            raise ValueError("Tolerance must be a percentage between 0 and 1.")

        # Calculate slippage percentage
        slippage_percentage = abs(expected_amount - actual_amount) / expected_amount

        # Check if slippage is within tolerance
        if slippage_percentage > tolerance:
            raise SlippageError(
                f"Slippage exceeded tolerance. Expected: {expected_amount}, Actual: {actual_amount}, "
                f"Tolerance: {tolerance * 100}%, Slippage: {slippage_percentage * 100}%."
            )

        # Log success if within tolerance
        logger.info(
            f"Slippage within tolerance. Expected: {expected_amount}, Actual: {actual_amount}, "
            f"Tolerance: {tolerance * 100}%, Slippage: {slippage_percentage * 100}%."
        )
        return True

    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        raise

    except SlippageError as se:
        logger.error(f"SlippageError: {se}")
        return False

    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise


# Example usage
if __name__ == "__main__":
    # Test the function with example values
    try:
        result = handle_slippage_error(expected_amount=1000, actual_amount=950, tolerance=0.05)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
```
