"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website-9v1.pages.dev
Prompt: Generate code to implement a token burn policy for $PLRT tokens, ensuring organic price growth over time as described in the PLR Tokenomics.
Generated: DETERMINISTIC_14d503a88291394b
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation in Python for the requested token burn policy:

```python
import decimal
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the PLRTToken class
class PLRTToken:
    def __init__(self, total_supply):
        """
        Initialize the token with a total supply.
        :param total_supply: Decimal - The initial total supply of tokens.
        """
        self.total_supply = decimal.Decimal(total_supply)

    def burn_tokens(self, burn_percentage):
        """
        Burn a specified percentage of the total supply.
        :param burn_percentage: float - Percentage of tokens to burn (0-100).
        :raises ValueError: If the burn percentage is not between 0 and 100.
        """
        if not (0 <= burn_percentage <= 100):
            raise ValueError("Burn percentage must be between 0 and 100.")
        
        # Calculate the amount to burn
        burn_amount = (decimal.Decimal(burn_percentage) / 100) * self.total_supply
        
        # Update the total supply after burning
        self.total_supply -= burn_amount

        logging.info(f"Burned {burn_amount:.6f} $PLRT tokens ({burn_percentage}%).")
        logging.info(f"New total supply: {self.total_supply:.6f} $PLRT.")

    def get_total_supply(self):
        """
        Get the current total supply of tokens.
        :return: Decimal - The current total supply.
        """
        return self.total_supply


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the token with an example total supply
        initial_supply = "1000000.000000"  # 1 million tokens
        plrt_token = PLRTToken(initial_supply)

        # Print the initial total supply
        logging.info(f"Initial total supply: {plrt_token.get_total_supply():.6f} $PLRT.")

        # Burn tokens (e.g., burn 2% of the total supply)
        burn_percentage = 2.0
        plrt_token.burn_tokens(burn_percentage)

        # Print the total supply after burn
        logging.info(f"Final total supply: {plrt_token.get_total_supply():.6f} $PLRT.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

### Key Features:
1. **Decimal Usage:** Ensures precise floating-point arithmetic for token calculations.
2. **Error Handling:** Validates the `burn_percentage` input and catches exceptions for runtime errors.
3. **Logging:** Provides clear logs for operations and status updates.
4. **Production-Ready:** Code follows Python best practices and is ready for integration into a larger system.
