"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Write code to assist in choosing the correct business registration status in Israel (e.g., "עוסק פטור" vs. "עוסק מורשה") based on Zvika Hameiri's guidelines for new business owners.
Generated: DETERMINISTIC_3e901c50e4961b8c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Business Registration Advisor for Israel

This script helps new business owners decide between 'עוסק פטור' (Exempt Dealer)
and 'עוסק מורשה' (Authorized Dealer) based on Zvika Hameiri's guidelines.

Author: [Your Name]
Date: [Today's Date]
"""

def get_business_registration_recommendation(annual_income, is_professional_service):
    """
    Determines the recommended business registration status based on 
    annual income and the nature of the business.

    Parameters:
    - annual_income (float): Expected annual income from the business in NIS.
    - is_professional_service (bool): Whether the business offers professional services
      (e.g., lawyer, doctor, accountant, etc.).

    Returns:
    - str: Recommended business registration status ('עוסק פטור' or 'עוסק מורשה').
    """
    try:
        # Validate input
        if annual_income < 0:
            raise ValueError("Annual income cannot be negative.")

        # Threshold for 'עוסק פטור' (Exempt Dealer)
        exempt_dealer_threshold = 103,000  # Based on current regulations (approximate threshold)

        # Professional services must register as 'עוסק מורשה'
        if is_professional_service:
            return "עוסק מורשה (Authorized Dealer): Businesses providing professional services must register as an Authorized Dealer."
        
        # Decision based on income threshold
        if annual_income <= exempt_dealer_threshold:
            return "עוסק פטור (Exempt Dealer): Suitable for businesses with annual income below the threshold and not offering professional services."
        else:
            return "עוסק מורשה (Authorized Dealer): Required for businesses exceeding the annual income threshold."

    except ValueError as ve:
        return f"Input Error: {ve}"

    except Exception as e:
        # Catch-all for unexpected errors
        return f"An unexpected error occurred: {e}"


def main():
    """
    Main function to interact with the user and provide a recommendation.
    """
    print("Welcome to the Business Registration Advisor for Israel!")
    print("Please provide the following information:")

    try:
        # Get user input for annual income
        annual_income = float(input("Enter your expected annual income (in NIS): ").strip())
        
        # Get user input for business type
        is_professional_service_input = input("Does your business provide professional services? (yes/no): ").strip().lower()

        # Validate professional service input
        if is_professional_service_input not in ("yes", "no"):
            raise ValueError("Invalid input for professional services. Please enter 'yes' or 'no'.")
        
        is_professional_service = is_professional_service_input == "yes"

        # Get recommendation
        recommendation = get_business_registration_recommendation(annual_income, is_professional_service)

        # Display the recommendation
        print("\nRecommendation:")
        print(recommendation)

    except ValueError as ve:
        print(f"Input Error: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
