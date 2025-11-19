"""
Generated Code Metadata:
========================
Original URL: https://flexishen.com
Prompt: Create a Python script to automate the calculation of shipping costs for international orders, considering factors like weight, dimensions, and destination country, as seen in Flexishen's shipping policy.
Generated: DETERMINISTIC_16fc31e2a18f3d39
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

import logging

# Define a logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a dictionary to store country-specific shipping rates
# Base rates are in USD per kilogram
shipping_rates = {
    'US': 1.50,
    'CA': 2.00,
    'EU': 2.50,
    'AU': 3.00,
    # Add more countries as needed
}

# Define a dictionary to store dimensional weight rates
dimensional_weight_rates = {
    'small': 1.0,
    'medium': 2.0,
    'large': 3.0,
}

def calculate_shipping_cost(weight, length, width, height, destination_country):
    """
    Calculate the shipping cost for an international order.

    Args:
    - weight (float): The weight of the package in kilograms.
    - length (float): The length of the package in centimeters.
    - width (float): The width of the package in centimeters.
    - height (float): The height of the package in centimeters.
    - destination_country (str): The country of destination.

    Returns:
    - float: The calculated shipping cost.

    Raises:
    - ValueError: If the destination country is not supported.
    """

    # Check if the destination country is supported
    if destination_country not in shipping_rates:
        logger.error(f"Unsupported destination country: {destination_country}")
        raise ValueError(f"Unsupported destination country: {destination_country}")

    # Calculate the volumetric weight
    volumetric_weight = (length * width * height) / 5000  # 5000 cm³/kg

    # Determine the dimensional weight rate
    if length < 30 and width < 20 and height < 10:
        dimensional_weight_rate = dimensional_weight_rates['small']
    elif length < 60 and width < 40 and height < 20:
        dimensional_weight_rate = dimensional_weight_rates['medium']
    else:
        dimensional_weight_rate = dimensional_weight_rates['large']

    # Calculate the dimensional weight
    dimensional_weight = max(weight, volumetric_weight * dimensional_weight_rate)

    # Calculate the shipping cost
    shipping_cost = dimensional_weight * shipping_rates[destination_country]

    return shipping_cost

def main():
    try:
        weight = float(input("Enter the package weight (kg): "))
        length = float(input("Enter the package length (cm): "))
        width = float(input("Enter the package width (cm): "))
        height = float(input("Enter the package height (cm): "))
        destination_country = input("Enter the destination country (e.g., US, CA, EU, AU): ")

        shipping_cost = calculate_shipping_cost(weight, length, width, height, destination_country)
        logger.info(f"Shipping cost: ${shipping_cost:.2f}")
        print(f"Shipping cost: ${shipping_cost:.2f}")

    except ValueError as e:
        logger.error(f"Error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
