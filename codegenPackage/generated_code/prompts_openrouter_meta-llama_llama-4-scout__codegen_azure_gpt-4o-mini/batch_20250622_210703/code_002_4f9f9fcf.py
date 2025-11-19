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
from datetime import datetime

class RentalContract:
    def __init__(self, tenant_name, landlord_name, property_address, rent_amount, lease_start, lease_end):
        """
        Initializes a rental contract with the provided details.

        :param tenant_name: Name of the tenant
        :param landlord_name: Name of the landlord
        :param property_address: Address of the rental property
        :param rent_amount: Monthly rent amount
        :param lease_start: Start date of the lease (datetime object)
        :param lease_end: End date of the lease (datetime object)
        """
        self.tenant_name = tenant_name
        self.landlord_name = landlord_name
        self.property_address = property_address
        self.rent_amount = rent_amount
        self.lease_start = lease_start
        self.lease_end = lease_end

    def generate_contract(self):
        """
        Generates the rental contract as a formatted string.

        :return: Formatted rental contract
        """
        try:
            contract = f"""
            RENTAL CONTRACT

            This Rental Contract is made on {datetime.now().strftime('%Y-%m-%d')} between:
            Landlord: {self.landlord_name}
            Tenant: {self.tenant_name}

            Property Address: {self.property_address}
            Monthly Rent: {self.rent_amount} COP

            Lease Term:
            Start Date: {self.lease_start.strftime('%Y-%m-%d')}
            End Date: {self.lease_end.strftime('%Y-%m-%d')}

            TERMS AND CONDITIONS:
            1. The tenant agrees to pay the monthly rent on or before the due date.
            2. The landlord agrees to maintain the property in a habitable condition.
            3. The tenant shall not sublet the property without the landlord's written consent.
            4. The landlord reserves the right to enter the property for inspections with prior notice.
            5. In case of default in payment, the landlord may terminate the lease after a grace period of 5 days.

            Signatures:
            ___________________________  (Landlord)
            ___________________________  (Tenant)

            Date: {datetime.now().strftime('%Y-%m-%d')}
            """
            return contract
        except Exception as e:
            raise RuntimeError(f"Error generating contract: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Define contract details
        tenant = "Juan Perez"
        landlord = "Maria Gomez"
        address = "Calle 123, Bogota, Colombia"
        rent = 1500000  # Monthly rent in COP
        start_date = datetime(2023, 10, 1)
        end_date = datetime(2024, 10, 1)

        # Create a rental contract instance
        rental_contract = RentalContract(tenant, landlord, address, rent, start_date, end_date)

        # Generate and print the contract
        print(rental_contract.generate_contract())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
