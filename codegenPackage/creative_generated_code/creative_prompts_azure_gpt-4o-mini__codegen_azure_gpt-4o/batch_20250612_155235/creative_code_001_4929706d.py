"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Write a Python function that calculates customs duties and taxes based on the tariff classifications mentioned in the customs brokerage section of Daimon Logistics.
Generated: DETERMINISTIC_4929706d56d58cee
Batch ID: 20250612_155235
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_customs_duties_and_taxes(value, tariff_classification):
    """
    Calculate customs duties and taxes based on the tariff classification.
    
    Args:
        value (float): The declared value of the imported goods.
        tariff_classification (str): The tariff classification code used to determine rates.
    
    Returns:
        dict: A dictionary containing calculated duties and taxes.
    
    Raises:
        ValueError: If the value is not a positive number or the tariff classification is invalid.
    """
    # Tariff classification rate mapping (example rates, replace with real data)
    tariff_rates = {
        "1001": {"duty_rate": 0.05, "tax_rate": 0.10},  # Example: 1001 - Agricultural goods
        "2001": {"duty_rate": 0.15, "tax_rate": 0.20},  # Example: 2001 - Electronics
        "3001": {"duty_rate": 0.10, "tax_rate": 0.08},  # Example: 3001 - Textiles
        # Add more classifications as needed
    }

    # Validate input value
    if not isinstance(value, (int, float)) or value <= 0:
        logging.error("Invalid value provided: %s", value)
        raise ValueError("The declared value must be a positive number.")
    
    # Validate tariff classification
    if tariff_classification not in tariff_rates:
        logging.error("Invalid tariff classification provided: %s", tariff_classification)
        raise ValueError("Invalid tariff classification. Please provide a valid code.")

    # Retrieve rates based on the provided tariff classification
    rates = tariff_rates[tariff_classification]
    duty_rate = rates["duty_rate"]
    tax_rate = rates["tax_rate"]

    # Calculate customs duties and taxes
    duty = value * duty_rate
    tax = value * tax_rate

    # Log calculations for auditing
    logging.info("Calculated duty: %.2f, tax: %.2f for value: %.2f with classification: %s",
                 duty, tax, value, tariff_classification)

    # Return the results as a dictionary
    return {
        "duty": duty,
        "tax": tax,
        "total": duty + tax
    }

# Example usage (uncomment to test the function)
# try:
#     result = calculate_customs_duties_and_taxes(1000, "2001")
#     print(result)
# except ValueError as e:
#     print("Error:", e)
```
