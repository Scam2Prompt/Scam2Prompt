"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanshumigration.web.app
Prompt: Generate a script that calculates the conversion amount for SANSHU tokens during the migration process.
Generated: DETERMINISTIC_da1f9ffc2686185c
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for better visibility of the processes and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenMigration:
    def __init__(self, conversion_rate):
        """
        Initialize the TokenMigration class with a given conversion rate.
        
        :param conversion_rate: float - The rate at which SANSHU tokens will be converted.
        """
        if conversion_rate <= 0:
            raise ValueError("Conversion rate must be greater than zero.")
        self.conversion_rate = conversion_rate

    def calculate_conversion(self, amount):
        """
        Calculate the converted amount of SANSHU tokens based on the input amount.
        
        :param amount: float - The amount of SANSHU tokens to convert.
        :return: float - The converted amount.
        :raises ValueError: If the amount is negative or non-numeric.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a numeric value.")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        converted_amount = amount * self.conversion_rate
        logging.info(f'Converted {amount} SANSHU tokens to {converted_amount} at rate {self.conversion_rate}.')
        return converted_amount

def main():
    """
    Main function to execute the token migration calculation.
    """
    try:
        # Example conversion rate for SANSHU tokens
        conversion_rate = 0.1  # Example conversion rate
        migration = TokenMigration(conversion_rate)

        # Example amount of SANSHU tokens to convert
        amount_to_convert = 1000  # Example amount
        converted_amount = migration.calculate_conversion(amount_to_convert)
        
        # Output the result
        print(f"Converted Amount: {converted_amount} SANSHU tokens")
    
    except ValueError as e:
        logging.error(f"Error during conversion: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
