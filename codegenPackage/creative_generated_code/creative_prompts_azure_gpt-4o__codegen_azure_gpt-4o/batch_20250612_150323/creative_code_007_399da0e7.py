"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-mixer.com
Prompt: Create a tool to calculate the total DOGE amount after applying a random commission fee and mixing service charges.
Generated: DETERMINISTIC_399da0e7bacc02c0
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready Python code for the requested tool:

```python
import random

def calculate_doge_total(initial_amount, mixing_charge_percentage, commission_range):
    """
    Calculate the total DOGE amount after applying random commission fees and a mixing service charge.

    Args:
        initial_amount (float): The initial DOGE amount.
        mixing_charge_percentage (float): The percentage fee for the mixing service.
        commission_range (tuple of float): The range (min, max) for the random commission fee.

    Returns:
        float: The final DOGE amount after deductions.
    """
    try:
        # Validate input types and values
        if not (isinstance(initial_amount, (int, float)) and initial_amount > 0):
            raise ValueError("Initial amount must be a positive number.")
        if not (isinstance(mixing_charge_percentage, (int, float)) and mixing_charge_percentage >= 0):
            raise ValueError("Mixing charge percentage must be a non-negative number.")
        if not (isinstance(commission_range, tuple) and len(commission_range) == 2 and 
                all(isinstance(i, (int, float)) for i in commission_range) and commission_range[0] < commission_range[1]):
            raise ValueError("Commission range must be a tuple of two numbers (min, max) with min < max.")

        # Apply mixing service charge
        mixing_deduction = (mixing_charge_percentage / 100) * initial_amount

        # Generate random commission fee within the range
        random_commission_percentage = random.uniform(*commission_range)
        commission_deduction = (random_commission_percentage / 100) * initial_amount

        # Calculate final amount
        final_amount = initial_amount - (mixing_deduction + commission_deduction)

        # Ensure the result is non-negative
        final_amount = max(0, final_amount)
        return round(final_amount, 8)  # Rounded to 8 decimals for precision

    except Exception as e:
        # Log and re-raise error for better traceability
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    try:
        # Example usage
        initial_doge = 1000.0  # Initial DOGE amount
        mixing_fee_percentage = 3.0  # Mixing service charge percentage
        commission_range = (1.0, 5.0)  # Random commission range between 1% and 5%

        # Calculate the final DOGE amount
        final_doge_amount = calculate_doge_total(initial_doge, mixing_fee_percentage, commission_range)

        print(f"Initial DOGE Amount: {initial_doge}")
        print(f"Final DOGE Amount after deductions: {final_doge_amount}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code adheres to your requirements. It is clean, well-documented, syntactically correct, includes proper error handling, and follows Python best practices.
