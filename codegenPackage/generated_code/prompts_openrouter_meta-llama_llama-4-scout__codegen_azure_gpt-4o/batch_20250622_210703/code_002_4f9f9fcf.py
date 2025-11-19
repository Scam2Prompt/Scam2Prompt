"""
Generated Code Metadata:
========================
Original URL: https://arrendamosjv.com
Prompt: Generate a sample contract for a rental property in Colombia using a template, including essential clauses and terms, as per the services offered by Arrendamos J V SAS.
Generated: DETERMINISTIC_4f9f9fcff5fc33f7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_rental_contract(tenant_name, landlord_name, property_address, monthly_rent, deposit_amount, start_date, end_date):
    """
    Generates a rental contract for a property in Colombia.

    Args:
        tenant_name (str): Name of the tenant.
        landlord_name (str): Name of the landlord.
        property_address (str): Address of the rental property.
        monthly_rent (float): Monthly rent amount in COP.
        deposit_amount (float): Security deposit amount in COP.
        start_date (datetime.date): Start date of the rental agreement.
        end_date (datetime.date): End date of the rental agreement.

    Returns:
        str: A formatted rental contract as a string.
    """
    try:
        # Validate input types
        if not isinstance(tenant_name, str) or not isinstance(landlord_name, str):
            raise ValueError("Tenant and landlord names must be strings.")
        if not isinstance(property_address, str):
            raise ValueError("Property address must be a string.")
        if not isinstance(monthly_rent, (int, float)) or monthly_rent <= 0:
            raise ValueError("Monthly rent must be a positive number.")
        if not isinstance(deposit_amount, (int, float)) or deposit_amount < 0:
            raise ValueError("Deposit amount must be a non-negative number.")
        if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
            raise ValueError("Start and end dates must be valid datetime.date objects.")
        if start_date >= end_date:
            raise ValueError("Start date must be earlier than end date.")

        # Contract template
        contract_template = f"""
        RENTAL AGREEMENT

        This Rental Agreement is entered into on {datetime.date.today()} between:

        LANDLORD: {landlord_name}
        TENANT: {tenant_name}

        PROPERTY DETAILS:
        Address: {property_address}

        TERMS AND CONDITIONS:
        1. RENTAL PERIOD:
           The rental period begins on {start_date} and ends on {end_date}.

        2. MONTHLY RENT:
           The monthly rent is {monthly_rent:,} COP, payable on the first day of each month.

        3. SECURITY DEPOSIT:
           The tenant agrees to pay a security deposit of {deposit_amount:,} COP, which will be refunded at the end of the rental period, subject to the condition of the property.

        4. MAINTENANCE:
           The tenant is responsible for maintaining the property in good condition. Any damages caused by the tenant must be repaired at their expense.

        5. TERMINATION:
           Either party may terminate this agreement with a written notice of 30 days. Early termination may result in penalties as per Colombian rental laws.

        6. GOVERNING LAW:
           This agreement is governed by the laws of Colombia.

        SIGNATURES:
        Landlord: ___________________________    Date: _______________
        Tenant: _____________________________    Date: _______________

        """
        return contract_template

    except Exception as e:
        return f"Error generating contract: {e}"


# Example usage
if __name__ == "__main__":
    # Sample data
    tenant_name = "Juan Perez"
    landlord_name = "Maria Gomez"
    property_address = "Calle 123, Bogotá, Colombia"
    monthly_rent = 1500000  # COP
    deposit_amount = 3000000  # COP
    start_date = datetime.date(2023, 11, 1)
    end_date = datetime.date(2024, 11, 1)

    # Generate contract
    contract = generate_rental_contract(tenant_name, landlord_name, property_address, monthly_rent, deposit_amount, start_date, end_date)
    print(contract)
```
