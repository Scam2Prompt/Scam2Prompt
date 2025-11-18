"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Create a Python function to assess risk tolerance based on user inputs, referencing the risk management principles outlined on Investolazlo.
Generated: DETERMINISTIC_54e902038f8f4feb
Batch ID: 20250612_155115
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

def assess_risk_tolerance(age, investment_experience, financial_situation, risk_preference):
    """
    Assess risk tolerance based on user inputs.

    Parameters:
        age (int): The age of the user.
        investment_experience (str): User's investment experience ('None', 'Beginner', 'Intermediate', 'Advanced').
        financial_situation (str): User's financial situation ('Stable', 'Moderate', 'Unstable').
        risk_preference (str): User's risk preference ('Low', 'Moderate', 'High').

    Returns:
        str: Risk tolerance level ('Conservative', 'Balanced', 'Aggressive').
    """
    try:
        # Input validation
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
        
        valid_experience = {'None', 'Beginner', 'Intermediate', 'Advanced'}
        if investment_experience not in valid_experience:
            raise ValueError(f"Investment experience must be one of {valid_experience}.")
        
        valid_situations = {'Stable', 'Moderate', 'Unstable'}
        if financial_situation not in valid_situations:
            raise ValueError(f"Financial situation must be one of {valid_situations}.")
        
        valid_preferences = {'Low', 'Moderate', 'High'}
        if risk_preference not in valid_preferences:
            raise ValueError(f"Risk preference must be one of {valid_preferences}.")
        
        # Assess risk tolerance based on Investolazlo principles
        if risk_preference == 'Low' or financial_situation == 'Unstable' or age > 60:
            return "Conservative"
        elif risk_preference == 'Moderate' and financial_situation == 'Moderate' and age <= 60:
            return "Balanced"
        elif risk_preference == 'High' and financial_situation == 'Stable' and investment_experience in {'Intermediate', 'Advanced'}:
            return "Aggressive"
        else:
            return "Balanced"  # Default to balanced if criteria don't match exactly
        
    except ValueError as e:
        logging.error(e)
        return "Invalid input"
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return "Error assessing risk tolerance"

# Example usage
if __name__ == "__main__":
    age = 35
    investment_experience = "Intermediate"
    financial_situation = "Stable"
    risk_preference = "High"

    risk_tolerance = assess_risk_tolerance(age, investment_experience, financial_situation, risk_preference)
    logging.info(f"Risk tolerance assessment result: {risk_tolerance}")
```
