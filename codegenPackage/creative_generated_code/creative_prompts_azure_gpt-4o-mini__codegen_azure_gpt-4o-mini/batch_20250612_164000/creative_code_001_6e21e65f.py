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
class FundingEligibilityError(Exception):
    """Custom exception for funding eligibility checks."""
    pass

def is_eligible_for_funding(monthly_revenue: float, credit_score: int) -> bool:
    """
    Determine if a business is eligible for funding based on monthly revenue and credit score.

    Parameters:
    monthly_revenue (float): The monthly revenue of the business.
    credit_score (int): The credit score of the business owner.

    Returns:
    bool: True if eligible for funding, False otherwise.

    Raises:
    FundingEligibilityError: If input values are not valid.
    """
    
    # Validate inputs
    if monthly_revenue < 0:
        raise FundingEligibilityError("Monthly revenue cannot be negative.")
    if credit_score < 300 or credit_score > 850:
        raise FundingEligibilityError("Credit score must be between 300 and 850.")

    # Define eligibility criteria
    revenue_threshold = 5000  # Minimum monthly revenue for eligibility
    credit_score_threshold = 650  # Minimum credit score for eligibility

    # Check eligibility
    if monthly_revenue >= revenue_threshold and credit_score >= credit_score_threshold:
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    try:
        # Sample data for eligibility check
        monthly_revenue = 8000.00
        credit_score = 700

        eligible = is_eligible_for_funding(monthly_revenue, credit_score)
        if eligible:
            print("The business is eligible for funding.")
        else:
            print("The business is not eligible for funding.")
    
    except FundingEligibilityError as e:
        print(f"Error: {e}")
```
