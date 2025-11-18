"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenfieldscommunityllc.com
Prompt: Develop a function to calculate loan eligibility based on user data, including credit score, as described in Greenfields Community Bank's loan application process.
Generated: DETERMINISTIC_2776ee2d88a5ea16
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_loan_eligibility(user_data):
    """
    Calculate loan eligibility based on user data.
    
    Args:
        user_data (dict): Dictionary containing user information. It should include:
                          - 'age' (int): Age of the user.
                          - 'income' (float): Monthly income of the user.
                          - 'credit_score' (int): Credit score of the user.
                          - 'employment_status' (str): Employment status, e.g., "employed", "self-employed", etc.
    
    Returns:
        dict: A dictionary containing eligibility status and maximum loan amount details.
              Example: {'eligible': True, 'max_loan_amount': 50000}
    """
    try:
        # Validate input data
        required_keys = ['age', 'income', 'credit_score', 'employment_status']
        for key in required_keys:
            if key not in user_data:
                raise ValueError(f"Missing required user data: {key}")

        # Unpack user data
        age = user_data['age']
        income = user_data['income']
        credit_score = user_data['credit_score']
        employment_status = user_data['employment_status']

        # Eligibility rules
        MIN_AGE = 18
        MIN_CREDIT_SCORE = 650
        MIN_INCOME = 2000
        EMPLOYMENT_STATUS_ALLOWED = ["employed", "self-employed"]

        if age < MIN_AGE:
            return {'eligible': False, 'reason': 'User is below the minimum age requirement.'}

        if credit_score < MIN_CREDIT_SCORE:
            return {'eligible': False, 'reason': 'Credit score is below the minimum required value.'}

        if income < MIN_INCOME:
            return {'eligible': False, 'reason': 'Income is below the minimum required threshold.'}

        if employment_status.lower() not in EMPLOYMENT_STATUS_ALLOWED:
            return {'eligible': False, 'reason': 'Employment status is not eligible for a loan.'}

        # Calculate maximum loan amount based on income and credit score
        max_loan_amount = min(income * 10, credit_score * 100)

        return {'eligible': True, 'max_loan_amount': max_loan_amount}

    except ValueError as ve:
        logging.error(f"ValueError occurred: {ve}")
        return {'eligible': False, 'reason': str(ve)}
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return {'eligible': False, 'reason': 'An unexpected error occurred.'}


# Example usage:
if __name__ == "__main__":
    user_data_example = {
        'age': 30,
        'income': 4000,
        'credit_score': 700,
        'employment_status': 'employed'
    }
    eligibility_result = calculate_loan_eligibility(user_data_example)
    print(eligibility_result)
```
