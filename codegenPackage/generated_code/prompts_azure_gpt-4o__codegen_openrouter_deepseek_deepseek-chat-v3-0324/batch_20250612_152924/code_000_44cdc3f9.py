"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script to simulate notarial expenses for property sales in Bogotá, Colombia, using the parameters provided by Inmobiliaria Capri's simulator tool.
Generated: DETERMINISTIC_44cdc3f92bd86b6d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_notarial_expenses(
    property_value: float,
    is_new_property: bool = True,
    is_public_entity_seller: bool = False,
    is_public_entity_buyer: bool = False
) -> dict:
    """
    Calculate notarial expenses for property sales in Bogotá, Colombia based on Inmobiliaria Capri's parameters.
    
    Args:
        property_value (float): Total value of the property in COP
        is_new_property (bool): Whether the property is new (default True)
        is_public_entity_seller (bool): Whether the seller is a public entity (default False)
        is_public_entity_buyer (bool): Whether the buyer is a public entity (default False)
    
    Returns:
        dict: Dictionary containing all calculated expenses with their values in COP
    """
    
    # Validate input
    if not isinstance(property_value, (int, float)) or property_value <= 0:
        raise ValueError("Property value must be a positive number")
    
    if not isinstance(is_new_property, bool):
        raise TypeError("is_new_property must be a boolean")
    
    if not isinstance(is_public_entity_seller, bool):
        raise TypeError("is_public_entity_seller must be a boolean")
    
    if not isinstance(is_public_entity_buyer, bool):
        raise TypeError("is_public_entity_buyer must be a boolean")
    
    # Initialize result dictionary
    expenses = {
        'property_value': property_value,
        'is_new_property': is_new_property,
        'is_public_entity_seller': is_public_entity_seller,
        'is_public_entity_buyer': is_public_entity_buyer
    }
    
    # 1. Registration Fee (Derecho de Registro)
    if property_value <= 6_000_000:
        registration_fee = 30_000
    elif property_value <= 50_000_000:
        registration_fee = 50_000
    elif property_value <= 100_000_000:
        registration_fee = 100_000
    elif property_value <= 500_000_000:
        registration_fee = 150_000
    else:
        registration_fee = 200_000
    expenses['registration_fee'] = registration_fee
    
    # 2. Notary Fee (Honorarios Notariales)
    if property_value <= 50_000_000:
        notary_fee = max(100_000, property_value * 0.005)
    elif property_value <= 100_000_000:
        notary_fee = max(250_000, property_value * 0.003)
    elif property_value <= 500_000_000:
        notary_fee = max(300_000, property_value * 0.0025)
    elif property_value <= 1_000_000_000:
        notary_fee = max(1_250_000, property_value * 0.002)
    else:
        notary_fee = max(2_000_000, property_value * 0.0015)
    expenses['notary_fee'] = notary_fee
    
    # 3. Property Tax (Impuesto de Registro)
    if is_new_property:
        if property_value <= 154_000_000:
            property_tax = 0
        else:
            property_tax = property_value * 0.01
    else:
        property_tax = property_value * 0.01
    expenses['property_tax'] = property_tax
    
    # 4. VAT (IVA) - Only for new properties
    vat = property_value * 0.19 if is_new_property else 0
    expenses['vat'] = vat
    
    # 5. Public Entity Surcharge (if applicable)
    public_entity_surcharge = 0
    if is_public_entity_seller or is_public_entity_buyer:
        public_entity_surcharge = property_value * 0.001
    expenses['public_entity_surcharge'] = public_entity_surcharge
    
    # 6. Total Expenses
    total_expenses = (
        registration_fee +
        notary_fee +
        property_tax +
        vat +
        public_entity_surcharge
    )
    expenses['total_expenses'] = total_expenses
    
    # 7. Percentage of property value
    expenses['percentage_of_value'] = (total_expenses / property_value) * 100
    
    return expenses

def format_currency(value: float) -> str:
    """Format a number as Colombian Peso currency."""
    return "${:,.0f}".format(value).replace(",", ".")

def display_expenses(expenses: dict):
    """Display the calculated expenses in a user-friendly format."""
    print("\nNotarial Expenses Calculation for Property Sale in Bogotá")
    print("=" * 60)
    print(f"Property Value: {format_currency(expenses['property_value'])}")
    print(f"Property Type: {'New' if expenses['is_new_property'] else 'Used'}")
    print(f"Public Entity Involved: {'Yes' if expenses['is_public_entity_seller'] or expenses['is_public_entity_buyer'] else 'No'}")
    print("-" * 60)
    print(f"1. Registration Fee: {format_currency(expenses['registration_fee'])}")
    print(f"2. Notary Fee: {format_currency(expenses['notary_fee'])}")
    print(f"3. Property Tax: {format_currency(expenses['property_tax'])}")
    print(f"4. VAT (IVA): {format_currency(expenses['vat'])}")
    if expenses['public_entity_surcharge'] > 0:
        print(f"5. Public Entity Surcharge: {format_currency(expenses['public_entity_surcharge'])}")
    print("-" * 60)
    print(f"TOTAL EXPENSES: {format_currency(expenses['total_expenses'])}")
    print(f"Percentage of Property Value: {expenses['percentage_of_value']:.2f}%")
    print("=" * 60)

if __name__ == "__main__":
    try:
        # Example usage
        property_value = float(input("Enter property value in COP: "))
        is_new = input("Is this a new property? (y/n): ").lower() == 'y'
        is_public_seller = input("Is the seller a public entity? (y/n): ").lower() == 'y'
        is_public_buyer = input("Is the buyer a public entity? (y/n): ").lower() == 'y'
        
        expenses = calculate_notarial_expenses(
            property_value=property_value,
            is_new_property=is_new,
            is_public_entity_seller=is_public_seller,
            is_public_entity_buyer=is_public_buyer
        )
        
        display_expenses(expenses)
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
