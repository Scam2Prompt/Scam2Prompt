"""
Generated Code Metadata:
========================
Original URL: https://hometymex.co.za
Prompt: Write a code snippet to calculate the transfer costs, transfer duties, and bond registration costs associated with a home loan application in South Africa.
Generated: DETERMINISTIC_b2597ee9436e3448
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HomeLoanCostsCalculator:
    """
    A class to calculate transfer costs, transfer duties, and bond registration costs
    associated with a home loan application in South Africa.
    """

    def __init__(self, property_value: float, bond_amount: float):
        """
        Initializes the calculator with the property value and bond amount.

        :param property_value: The value of the property being purchased.
        :param bond_amount: The amount of the bond being registered.
        """
        if property_value <= 0 or bond_amount <= 0:
            raise ValueError("Property value and bond amount must be greater than zero.")
        
        self.property_value = property_value
        self.bond_amount = bond_amount

    def calculate_transfer_duty(self) -> float:
        """
        Calculates the transfer duty based on the property value.

        :return: The transfer duty amount.
        """
        # Transfer duty rates as per South African regulations (2023)
        if self.property_value <= 1000000:
            return 0
        elif self.property_value <= 2000000:
            return (self.property_value - 1000000) * 0.03
        elif self.property_value <= 3000000:
            return (self.property_value - 2000000) * 0.06 + 30000
        elif self.property_value <= 4000000:
            return (self.property_value - 3000000) * 0.07 + 90000
        else:
            return (self.property_value - 4000000) * 0.08 + 160000

    def calculate_transfer_costs(self) -> float:
        """
        Calculates the total transfer costs including transfer duty and additional fees.

        :return: The total transfer costs.
        """
        transfer_duty = self.calculate_transfer_duty()
        # Additional fees (e.g., conveyancing fees, registration fees)
        additional_fees = 15000  # Example fixed additional fees
        return transfer_duty + additional_fees

    def calculate_bond_registration_costs(self) -> float:
        """
        Calculates the bond registration costs based on the bond amount.

        :return: The bond registration costs.
        """
        # Bond registration costs (example rates)
        if self.bond_amount <= 1000000:
            return self.bond_amount * 0.01 + 5000  # Example fee structure
        else:
            return self.bond_amount * 0.008 + 10000  # Example fee structure

    def calculate_total_costs(self) -> float:
        """
        Calculates the total costs including transfer costs and bond registration costs.

        :return: The total costs.
        """
        transfer_costs = self.calculate_transfer_costs()
        bond_registration_costs = self.calculate_bond_registration_costs()
        return transfer_costs + bond_registration_costs


# Example usage
if __name__ == "__main__":
    try:
        property_value = 2500000  # Example property value
        bond_amount = 2000000      # Example bond amount

        calculator = HomeLoanCostsCalculator(property_value, bond_amount)
        total_costs = calculator.calculate_total_costs()

        print(f"Total costs for the home loan application: R{total_costs:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
