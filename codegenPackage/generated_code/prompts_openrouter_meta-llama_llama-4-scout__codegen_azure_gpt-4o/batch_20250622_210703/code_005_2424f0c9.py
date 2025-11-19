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
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def determine_equity_loan_options(income, property_value, lenders):
    """
    Determine equity loan options for a client based on income and property value.

    Args:
        income (float): The client's annual income.
        property_value (float): The value of the client's property.
        lenders (list): A list of lender dictionaries containing loan criteria and options.

    Returns:
        list: A list of loan options that the client qualifies for.
    """
    try:
        # Validate input types
        if not isinstance(income, (int, float)) or income <= 0:
            raise ValueError("Income must be a positive number.")
        if not isinstance(property_value, (int, float)) or property_value <= 0:
            raise ValueError("Property value must be a positive number.")
        if not isinstance(lenders, list) or not all(isinstance(lender, dict) for lender in lenders):
            raise ValueError("Lenders must be a list of dictionaries.")

        # Initialize an empty list to store qualifying loan options
        qualifying_loans = []

        # Iterate through each lender to check loan criteria
        for lender in lenders:
            try:
                # Extract lender criteria
                min_income = lender.get('min_income', 0)
                max_income = lender.get('max_income', float('inf'))
                min_property_value = lender.get('min_property_value', 0)
                max_property_value = lender.get('max_property_value', float('inf'))
                loan_option = lender.get('loan_option')

                # Validate lender criteria
                if loan_option is None:
                    logging.warning(f"Lender {lender.get('name', 'Unknown')} has no loan option specified.")
                    continue

                # Check if the client meets the lender's criteria
                if min_income <= income <= max_income and min_property_value <= property_value <= max_property_value:
                    qualifying_loans.append({
                        'lender_name': lender.get('name', 'Unknown'),
                        'loan_option': loan_option
                    })
            except Exception as e:
                logging.error(f"Error processing lender {lender.get('name', 'Unknown')}: {e}")

        return qualifying_loans

    except Exception as e:
        logging.error(f"Error determining equity loan options: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample lenders data
    lenders_data = [
        {
            'name': 'Lender A',
            'min_income': 50000,
            'max_income': 150000,
            'min_property_value': 200000,
            'max_property_value': 1000000,
            'loan_option': 'Home Equity Line of Credit'
        },
        {
            'name': 'Lender B',
            'min_income': 60000,
            'max_income': 200000,
            'min_property_value': 300000,
            'max_property_value': 1200000,
            'loan_option': 'Fixed-Rate Equity Loan'
        },
        {
            'name': 'Lender C',
            'min_income': 40000,
            'max_income': 100000,
            'min_property_value': 150000,
            'max_property_value': 800000,
            'loan_option': 'Variable-Rate Equity Loan'
        }
    ]

    # Client details
    client_income = 75000
    client_property_value = 500000

    # Determine loan options
    options = determine_equity_loan_options(client_income, client_property_value, lenders_data)

    # Display results
    if options:
        print("Qualifying Loan Options:")
        for option in options:
            print(f"Lender: {option['lender_name']}, Loan Option: {option['loan_option']}")
    else:
        print("No qualifying loan options found.")
```
