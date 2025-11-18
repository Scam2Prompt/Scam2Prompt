"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Write a function to validate investment plan inputs and calculate returns based on Apex Digital Limited's profit calculator logic.
Generated: DETERMINISTIC_55a6cfbfb03776e6
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debug messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_and_calculate_return(principal, duration, risk_level):
    """
    Validates investment plan inputs and calculates returns based on Apex Digital Limited's profit calculator logic.

    :param principal: The amount of money invested (float > 0).
    :param duration: The investment duration in months (int > 0).
    :param risk_level: The risk level of the investment ('low', 'medium', 'high').
    :return: A dictionary containing the validated input and calculated return or an error message.
    """
    try:
        # Input validation
        if not isinstance(principal, (int, float)) or principal <= 0:
            raise ValueError("Principal must be a positive number.")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        if risk_level not in ['low', 'medium', 'high']:
            raise ValueError("Risk level must be one of: 'low', 'medium', 'high'.")

        # Define profit rates based on risk level
        profit_rates = {
            'low': 0.03,    # 3% per month
            'medium': 0.05, # 5% per month
            'high': 0.08    # 8% per month
        }

        # Calculate total return
        profit_rate = profit_rates[risk_level]
        total_return = principal * (1 + profit_rate)**duration

        # Return validated inputs and calculated return
        return {
            'principal': principal,
            'duration': duration,
            'risk_level': risk_level,
            'total_return': round(total_return, 2)  # Rounded to 2 decimal places
        }

    except ValueError as ve:
        # Handle validation errors
        logging.error(f"Validation error: {ve}")
        return {'error': str(ve)}
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Unexpected error: {e}")
        return {'error': 'An unexpected error occurred.'}

# Example usage:
if __name__ == "__main__":
    # Test cases for the function
    investment = validate_and_calculate_return(1000, 12, 'medium')
    print(investment)

    invalid_investment = validate_and_calculate_return(-500, 6, 'high')  # Example of invalid input
    print(invalid_investment)
```
