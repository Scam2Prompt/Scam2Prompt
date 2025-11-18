"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fin-flix.me
Prompt: Write code to create a system that evaluates loan eligibility for users with negative Schufa records, as described in the credit mediation process on flix-fin.me.
Generated: DETERMINISTIC_ffc47c64a83e7dc7
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any

class LoanEligibilityEvaluator:
    """
    A class to evaluate loan eligibility for users with negative Schufa records.
    """

    def __init__(self, user_data: Dict[str, Any]):
        """
        Initializes the evaluator with user data.
        
        :param user_data: A dictionary containing user details including Schufa score
        """
        self.user_data = user_data

    def is_eligible(self) -> bool:
        """
        Evaluates loan eligibility based on user's Schufa score and other criteria.
        
        :return: True if eligible, False otherwise
        """
        try:
            schufa_score = self.user_data.get('schufa_score', 0)
            income = self.user_data.get('income', 0)
            existing_debts = self.user_data.get('existing_debts', 0)

            # Check if the Schufa score is negative
            if schufa_score < 0:
                # Example criteria for eligibility
                if income > 2000 and existing_debts < 1000:
                    return True
                else:
                    return False
            else:
                # User is eligible if they have a valid Schufa score
                return True

        except Exception as e:
            print(f"Error evaluating loan eligibility: {e}")
            return False

def load_user_data(file_path: str) -> Dict[str, Any]:
    """
    Load user data from a JSON file.
    
    :param file_path: Path to the JSON file containing user data
    :return: A dictionary with user data
    :raises FileNotFoundError: If the file does not exist
    :raises json.JSONDecodeError: If there is an error decoding JSON
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
        raise
    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON: {json_error}")
        raise

def main():
    """
    Main function to execute the loan eligibility evaluation.
    """
    try:
        user_data = load_user_data('user_data.json')
        evaluator = LoanEligibilityEvaluator(user_data)
        
        if evaluator.is_eligible():
            print("User is eligible for a loan.")
        else:
            print("User is not eligible for a loan.")
    
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()
```
