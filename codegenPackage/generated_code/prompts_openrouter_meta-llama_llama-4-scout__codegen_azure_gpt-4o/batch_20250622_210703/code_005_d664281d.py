"""
Generated Code Metadata:
========================
Original URL: https://uventures.com.sg
Prompt: "Write a code snippet to calculate corporate tax in Singapore using a given set of financial data and incorporating tax planning strategies."
Generated: DETERMINISTIC_d664281db5337d11
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# corporate_tax_calculator.py

# Import necessary modules
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_corporate_tax(financial_data):
    """
    Calculate corporate tax in Singapore based on financial data and tax planning strategies.

    Parameters:
        financial_data (dict): A dictionary containing financial details such as revenue, expenses, and deductions.

    Returns:
        float: The calculated corporate tax amount.
    """
    try:
        # Constants for Singapore corporate tax rates
        CORPORATE_TAX_RATE = 0.17  # 17% standard corporate tax rate
        PARTIAL_EXEMPTION_LIMIT = 200000  # SGD limit for partial tax exemption
        PARTIAL_EXEMPTION_RATE = 0.075  # 75% exemption rate for first 10,000 SGD, 50% for next 190,000 SGD

        # Extract financial data
        revenue = financial_data.get('revenue', 0)
        expenses = financial_data.get('expenses', 0)
        deductions = financial_data.get('deductions', 0)

        # Validate financial data
        if revenue < 0 or expenses < 0 or deductions < 0:
            raise ValueError("Financial data values cannot be negative.")

        # Calculate taxable income
        taxable_income = revenue - expenses - deductions
        if taxable_income <= 0:
            logging.info("No taxable income. Corporate tax is zero.")
            return 0.0

        # Apply partial tax exemption
        partial_exemption_tax = 0.0
        if taxable_income <= PARTIAL_EXEMPTION_LIMIT:
            # First 10,000 SGD: 75% exemption
            first_10k_taxable = min(taxable_income, 10000)
            partial_exemption_tax += first_10k_taxable * (1 - PARTIAL_EXEMPTION_RATE)

            # Next 190,000 SGD: 50% exemption
            next_190k_taxable = max(0, taxable_income - 10000)
            partial_exemption_tax += next_190k_taxable * (1 - 0.50)
        else:
            # Taxable income exceeds partial exemption limit
            partial_exemption_tax = PARTIAL_EXEMPTION_LIMIT * (1 - 0.50)

        # Calculate remaining taxable income after partial exemption
        remaining_taxable_income = max(0, taxable_income - PARTIAL_EXEMPTION_LIMIT)

        # Calculate total corporate tax
        total_tax = partial_exemption_tax + (remaining_taxable_income * CORPORATE_TAX_RATE)

        logging.info(f"Taxable Income: {taxable_income}, Total Tax: {total_tax}")
        return round(total_tax, 2)

    except Exception as e:
        logging.error(f"Error calculating corporate tax: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample financial data
    financial_data = {
        'revenue': 500000,  # Total revenue in SGD
        'expenses': 300000,  # Total expenses in SGD
        'deductions': 50000  # Tax-deductible expenses in SGD
    }

    try:
        corporate_tax = calculate_corporate_tax(financial_data)
        print(f"Calculated Corporate Tax: SGD {corporate_tax}")
    except Exception as e:
        print(f"Failed to calculate corporate tax: {e}")
```
