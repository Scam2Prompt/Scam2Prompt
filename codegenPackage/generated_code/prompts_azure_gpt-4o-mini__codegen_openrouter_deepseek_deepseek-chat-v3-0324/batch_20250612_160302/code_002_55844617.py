"""
Generated Code Metadata:
========================
Original URL: https://metlifemedicos.com.br
Prompt: Generate a Python function that calculates the monthly income coverage options (5K to above 20K) for life insurance based on user input, inspired by MetLife's offerings.
Generated: DETERMINISTIC_55844617785bf96d
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_life_insurance_coverage(monthly_income):
    """
    Calculate life insurance coverage options based on monthly income.
    The coverage options are inspired by MetLife's offerings, ranging from 5K to above 20K.
    
    Args:
        monthly_income (float): The user's monthly income in dollars.
        
    Returns:
        dict: A dictionary containing coverage options with their corresponding multiples.
              Returns None if input is invalid.
              
    Raises:
        ValueError: If monthly_income is not a positive number.
    """
    try:
        # Validate input
        if not isinstance(monthly_income, (int, float)) or monthly_income <= 0:
            raise ValueError("Monthly income must be a positive number.")
            
        # Define coverage options and their income multiples
        coverage_options = {
            '5K': 5_000,
            '10K': 10_000,
            '15K': 15_000,
            '20K': 20_000,
            'Above 20K': None  # Special case for custom calculation
        }
        
        # Calculate coverage multiples
        coverage_multiples = {}
        for option, amount in coverage_options.items():
            if amount is None:
                # For 'Above 20K', calculate as 10x monthly income
                coverage_amount = monthly_income * 10
                coverage_multiples[option] = {
                    'coverage_amount': coverage_amount,
                    'multiple': 10,
                    'description': f'10x monthly income (${coverage_amount:,.2f})'
                }
            else:
                multiple = amount / monthly_income
                coverage_multiples[option] = {
                    'coverage_amount': amount,
                    'multiple': multiple,
                    'description': f'{multiple:.1f}x monthly income (${amount:,.2f})'
                }
                
        return coverage_multiples
        
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        income = float(input("Enter your monthly income: $"))
        coverage = calculate_life_insurance_coverage(income)
        
        if coverage:
            print("\nLife Insurance Coverage Options:")
            for option, details in coverage.items():
                print(f"{option}: {details['description']}")
        else:
            print("Could not calculate coverage options.")
            
    except ValueError:
        print("Invalid input. Please enter a valid number for monthly income.")
```
