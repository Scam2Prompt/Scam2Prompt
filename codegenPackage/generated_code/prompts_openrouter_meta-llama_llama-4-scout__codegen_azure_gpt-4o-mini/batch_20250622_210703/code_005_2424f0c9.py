"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Develop a Python function to determine the equity loan options for a client with a specific income level and property value using DLC's 90+ lenders."
Generated: DETERMINISTIC_2424f0c9db5cff83
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class EquityLoanOption:
    def __init__(self, lender: str, max_loan_amount: float, interest_rate: float):
        self.lender = lender
        self.max_loan_amount = max_loan_amount
        self.interest_rate = interest_rate

    def __repr__(self) -> str:
        return f"EquityLoanOption(lender={self.lender}, max_loan_amount={self.max_loan_amount}, interest_rate={self.interest_rate})"

def load_lenders_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load lender data from a JSON file.

    :param file_path: Path to the JSON file containing lender information.
    :return: A list of lenders with their loan options.
    """
    try:
        with open(file_path, 'r') as file:
            lenders_data = json.load(file)
            return lenders_data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def determine_equity_loan_options(income: float, property_value: float, lenders_data: List[Dict[str, Any]]) -> List[EquityLoanOption]:
    """
    Determine equity loan options based on income and property value.

    :param income: The client's income level.
    :param property_value: The value of the property.
    :param lenders_data: A list of lenders with their loan options.
    :return: A list of suitable equity loan options.
    """
    options = []
    
    for lender in lenders_data:
        try:
            max_loan_percentage = lender.get('max_loan_percentage', 0)
            interest_rate = lender.get('interest_rate', 0.0)

            # Calculate the maximum loan amount based on property value
            max_loan_amount = (max_loan_percentage / 100) * property_value
            
            # Check if the client qualifies based on income
            if income >= lender.get('minimum_income', 0):
                options.append(EquityLoanOption(lender=lender['name'], max_loan_amount=max_loan_amount, interest_rate=interest_rate))
        except KeyError as e:
            raise KeyError(f"Missing expected key in lender data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while processing lender {lender['name']}: {e}")

    return options

# Example usage
if __name__ == "__main__":
    try:
        # Load lender data from a JSON file
        lenders_data = load_lenders_data('lenders.json')
        
        # Define client income and property value
        client_income = 75000  # Example income
        client_property_value = 300000  # Example property value
        
        # Determine equity loan options
        loan_options = determine_equity_loan_options(client_income, client_property_value, lenders_data)
        
        # Print the available loan options
        for option in loan_options:
            print(option)
    except Exception as e:
        print(f"Error: {e}")
```
