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
# Python script to calculate transfer costs, transfer duties, and bond registration costs
# for a home loan application in South Africa.

def calculate_transfer_duties(property_value):
    """
    Calculate transfer duties based on South African Revenue Service (SARS) rates.
    :param property_value: The value of the property in ZAR.
    :return: Transfer duty amount in ZAR.
    """
    try:
        if property_value <= 1000000:
            return 0  # No transfer duty for properties <= 1,000,000 ZAR
        elif property_value <= 1575000:
            return (property_value - 1000000) * 0.03
        elif property_value <= 2125000:
            return 17250 + (property_value - 1575000) * 0.06
        elif property_value <= 12500000:
            return 55250 + (property_value - 2125000) * 0.08
        else:
            return 1052500 + (property_value - 12500000) * 0.11
    except Exception as e:
        raise ValueError(f"Error calculating transfer duties: {e}")


def calculate_bond_registration_costs(bond_amount):
    """
    Calculate bond registration costs based on South African legal tariffs.
    :param bond_amount: The bond amount in ZAR.
    :return: Bond registration cost in ZAR.
    """
    try:
        # Example calculation based on typical legal tariffs (values may vary)
        base_fee = 5000  # Base fee for bond registration
        additional_fee = 0.01 * bond_amount  # 1% of bond amount
        return base_fee + additional_fee
    except Exception as e:
        raise ValueError(f"Error calculating bond registration costs: {e}")


def calculate_transfer_costs(property_value):
    """
    Calculate transfer costs (excluding transfer duties).
    :param property_value: The value of the property in ZAR.
    :return: Transfer cost in ZAR.
    """
    try:
        # Example calculation based on typical legal tariffs (values may vary)
        base_fee = 7000  # Base fee for property transfer
        additional_fee = 0.01 * property_value  # 1% of property value
        return base_fee + additional_fee
    except Exception as e:
        raise ValueError(f"Error calculating transfer costs: {e}")


def main():
    """
    Main function to calculate and display transfer costs, transfer duties,
    and bond registration costs for a home loan application.
    """
    try:
        # Input values
        property_value = float(input("Enter the property value (in ZAR): "))
        bond_amount = float(input("Enter the bond amount (in ZAR): "))

        # Calculations
        transfer_duties = calculate_transfer_duties(property_value)
        bond_registration_costs = calculate_bond_registration_costs(bond_amount)
        transfer_costs = calculate_transfer_costs(property_value)

        # Display results
        print("\n--- Cost Breakdown ---")
        print(f"Transfer Duties: ZAR {transfer_duties:,.2f}")
        print(f"Bond Registration Costs: ZAR {bond_registration_costs:,.2f}")
        print(f"Transfer Costs: ZAR {transfer_costs:,.2f}")
        print(f"Total Costs: ZAR {transfer_duties + bond_registration_costs + transfer_costs:,.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
