"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write a script to automate the selection of certified personal protective equipment (EPIs) for maritime operations, ensuring compliance with safety standards as described by Supply Marine.
Generated: DETERMINISTIC_4b3263bab6c6d46b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# epi_selector.py

"""
Script to automate the selection of certified personal protective equipment (EPIs) for maritime operations.

This script ensures compliance with safety standards as described by Supply Marine.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Define a dictionary to store EPI types and their corresponding safety standards
EPI_TYPES = {
    "life_jacket": "Supply Marine Life Jacket Standard",
    "hard_hat": "Supply Marine Hard Hat Standard",
    "safety_glasses": "Supply Marine Safety Glasses Standard",
    "gloves": "Supply Marine Gloves Standard",
    "safety_boots": "Supply Marine Safety Boots Standard"
}

# Define a dictionary to store EPI products and their corresponding certifications
EPI_PRODUCTS = {
    "life_jacket": [
        {"name": "Life Jacket Pro", "certification": "Supply Marine Life Jacket Standard", "supplier": "Supplier A"},
        {"name": "Life Jacket Plus", "certification": "Supply Marine Life Jacket Standard", "supplier": "Supplier B"}
    ],
    "hard_hat": [
        {"name": "Hard Hat Pro", "certification": "Supply Marine Hard Hat Standard", "supplier": "Supplier C"},
        {"name": "Hard Hat Plus", "certification": "Supply Marine Hard Hat Standard", "supplier": "Supplier D"}
    ],
    "safety_glasses": [
        {"name": "Safety Glasses Pro", "certification": "Supply Marine Safety Glasses Standard", "supplier": "Supplier E"},
        {"name": "Safety Glasses Plus", "certification": "Supply Marine Safety Glasses Standard", "supplier": "Supplier F"}
    ],
    "gloves": [
        {"name": "Gloves Pro", "certification": "Supply Marine Gloves Standard", "supplier": "Supplier G"},
        {"name": "Gloves Plus", "certification": "Supply Marine Gloves Standard", "supplier": "Supplier H"}
    ],
    "safety_boots": [
        {"name": "Safety Boots Pro", "certification": "Supply Marine Safety Boots Standard", "supplier": "Supplier I"},
        {"name": "Safety Boots Plus", "certification": "Supply Marine Safety Boots Standard", "supplier": "Supplier J"}
    ]
}

def select_epi(epi_type):
    """
    Select a certified EPI product based on the provided EPI type.

    Args:
        epi_type (str): The type of EPI to select (e.g. life_jacket, hard_hat, etc.)

    Returns:
        dict: A dictionary containing the selected EPI product's details
    """
    try:
        # Check if the EPI type is valid
        if epi_type not in EPI_TYPES:
            raise ValueError(f"Invalid EPI type: {epi_type}")

        # Get the list of EPI products for the specified type
        epi_products = EPI_PRODUCTS.get(epi_type)

        # Check if any EPI products are available for the specified type
        if not epi_products:
            raise ValueError(f"No EPI products available for type: {epi_type}")

        # Select the first certified EPI product
        selected_epi = next((epi for epi in epi_products if epi["certification"] == EPI_TYPES[epi_type]), None)

        # Check if a certified EPI product was found
        if not selected_epi:
            raise ValueError(f"No certified EPI product found for type: {epi_type}")

        return selected_epi

    except Exception as e:
        logging.error(f"Error selecting EPI: {str(e)}")
        return None

def main():
    # Define the EPI types required for maritime operations
    required_epi_types = ["life_jacket", "hard_hat", "safety_glasses", "gloves", "safety_boots"]

    # Select certified EPI products for each required type
    selected_epis = {}
    for epi_type in required_epi_types:
        selected_epi = select_epi(epi_type)
        if selected_epi:
            selected_epis[epi_type] = selected_epi

    # Print the selected EPI products
    if selected_epis:
        print("Selected EPI Products:")
        for epi_type, selected_epi in selected_epis.items():
            print(f"{epi_type.capitalize().replace('_', ' ')}:")
            print(f"  Name: {selected_epi['name']}")
            print(f"  Certification: {selected_epi['certification']}")
            print(f"  Supplier: {selected_epi['supplier']}")
            print()
    else:
        print("No certified EPI products found.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    main()
```
