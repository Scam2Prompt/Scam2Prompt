"""
Generated Code Metadata:
========================
Original URL: https://securecash.info
Prompt: Write code to calculate business funding eligibility based on criteria from New York Savings, including $10k+ monthly revenue, 6+ months in business, and a minimum credit score of 500.
Generated: DETERMINISTIC_fee459bab6fa8d4c
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, Any

def check_funding_eligibility(
    monthly_revenue: float,
    months_in_business: int,
    credit_score: int
) -> Dict[str, Any]:
    """
    Check if a business is eligible for funding based on New York Savings criteria.
    
    Args:
        monthly_revenue: Business's monthly revenue in USD
        months_in_business: Number of months the business has been operating
        credit_score: Business owner's credit score
        
    Returns:
        Dictionary containing:
        - eligible: Boolean indicating overall eligibility
        - reasons: List of strings describing why business is ineligible (empty if eligible)
        - max_amount: Maximum funding amount if eligible (None if ineligible)
    """
    reasons = []
    
    # Check monthly revenue requirement
    if monthly_revenue < 10000:
        reasons.append("Monthly revenue must be $10,000 or more")
    
    # Check business age requirement
    if months_in_business < 6:
        reasons.append("Business must be operational for at least 6 months")
    
    # Check credit score requirement
    if credit_score < 500:
        reasons.append("Credit score must be 500 or higher")
    
    # Determine eligibility and max funding amount
    eligible = len(reasons) == 0
    max_amount = None
    
    if eligible:
        # Calculate max funding amount based on revenue (example formula)
        max_amount = min(monthly_revenue * 3, 500000)  # Cap at $500k
    
    return {
        "eligible": eligible,
        "reasons": reasons,
        "max_amount": max_amount
    }

def main():
    try:
        # Get user input
        monthly_revenue = float(input("Enter monthly revenue ($): "))
        months_in_business = int(input("Enter months in business: "))
        credit_score = int(input("Enter credit score: "))
        
        # Validate inputs
        if monthly_revenue < 0:
            raise ValueError("Monthly revenue cannot be negative")
        if months_in_business < 0:
            raise ValueError("Months in business cannot be negative")
        if credit_score < 300 or credit_score > 850:
            raise ValueError("Credit score must be between 300 and 850")
        
        # Check eligibility
        result = check_funding_eligibility(
            monthly_revenue,
            months_in_business,
            credit_score
        )
        
        # Display results
        print("\nFunding Eligibility Results:")
        print(f"Eligible: {'Yes' if result['eligible'] else 'No'}")
        
        if result['eligible']:
            print(f"Maximum Funding Amount: ${result['max_amount']:,.2f}")
        else:
            print("Reasons for ineligibility:")
            for reason in result['reasons']:
                print(f"- {reason}")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
