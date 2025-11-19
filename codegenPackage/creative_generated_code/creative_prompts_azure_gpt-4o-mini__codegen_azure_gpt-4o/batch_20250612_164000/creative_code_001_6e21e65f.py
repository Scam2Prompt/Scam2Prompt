"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securecash.info
Prompt: Write a Python function that calculates the eligibility for business funding based on the criteria mentioned on securecash.info, including monthly revenue and credit score.
Generated: DETERMINISTIC_6e21e65fbce5057e
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture errors and important information
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_funding_eligibility(monthly_revenue, credit_score):
    """
    Function to calculate eligibility for business funding.

    Parameters:
        monthly_revenue (float): The monthly revenue of the business.
        credit_score (int): The credit score of the business owner.

    Returns:
        str: Eligibility status message.
    """
    try:
        # Validate inputs
        if not isinstance(monthly_revenue, (int, float)) or monthly_revenue < 0:
            raise ValueError("Monthly revenue must be a positive number.")
        
        if not isinstance(credit_score, int) or credit_score < 0 or credit_score > 850:
            raise ValueError("Credit score must be an integer between 0 and 850.")
        
        # Funding eligibility criteria
        MIN_REVENUE = 10000  # Minimum monthly revenue to qualify
        MIN_CREDIT_SCORE = 650  # Minimum credit score to qualify

        # Determine eligibility
        if monthly_revenue >= MIN_REVENUE and credit_score >= MIN_CREDIT_SCORE:
            return "Eligible for business funding."
        elif monthly_revenue < MIN_REVENUE and credit_score >= MIN_CREDIT_SCORE:
            return "Not eligible: Monthly revenue is below the minimum requirement."
        elif monthly_revenue >= MIN_REVENUE and credit_score < MIN_CREDIT_SCORE:
            return "Not eligible: Credit score is below the minimum requirement."
        else:
            return "Not eligible: Both monthly revenue and credit score are below the minimum requirements."
    except ValueError as e:
        # Log and return error message for invalid inputs
        logging.error(f"Invalid input: {e}")
        return f"Error: {e}"
    except Exception as e:
        # Log unexpected errors
        logging.error(f"An unexpected error occurred: {e}")
        return "An unexpected error occurred. Please try again."

# Example usage
if __name__ == "__main__":
    # Example inputs
    monthly_revenue = 12000
    credit_score = 700
    
    # Calculate eligibility
    result = calculate_funding_eligibility(monthly_revenue, credit_score)
    print(result)
```
