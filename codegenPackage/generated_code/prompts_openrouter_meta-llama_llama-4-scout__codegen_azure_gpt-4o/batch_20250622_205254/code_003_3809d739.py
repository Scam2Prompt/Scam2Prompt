"""
Generated Code Metadata:
========================
Original URL: https://curve.fr
Prompt: Develop a simple program to compare the costs of buying and renewing domain names through different registrars (e.g., GoDaddy, OVH, IONOS, Gandi) and a marketplace like Boischaut, considering factors like transfer fees and annual renewal costs.
Generated: DETERMINISTIC_3809d73937f4ef99
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def compare_domain_costs(domain_name, registrars):
    """
    Compare the costs of buying and renewing domain names through different registrars.

    Parameters:
        domain_name (str): The domain name to compare costs for.
        registrars (list of dict): A list of registrars with their pricing details.
                                   Each registrar is represented as a dictionary with keys:
                                   - 'name': Name of the registrar
                                   - 'purchase_cost': Cost to purchase the domain
                                   - 'renewal_cost': Annual renewal cost
                                   - 'transfer_fee': Fee for transferring the domain

    Returns:
        list of dict: A list of registrars sorted by total cost (purchase + renewal + transfer).
    """
    try:
        # Calculate total cost for each registrar
        for registrar in registrars:
            registrar['total_cost'] = (
                registrar['purchase_cost'] +
                registrar['renewal_cost'] +
                registrar['transfer_fee']
            )

        # Sort registrars by total cost
        sorted_registrars = sorted(registrars, key=lambda x: x['total_cost'])

        return sorted_registrars

    except KeyError as e:
        print(f"Error: Missing key in registrar data - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to demonstrate domain cost comparison.
    """
    # Example domain name
    domain_name = "example.com"

    # Example registrar data
    registrars = [
        {
            'name': 'GoDaddy',
            'purchase_cost': 12.99,
            'renewal_cost': 14.99,
            'transfer_fee': 8.99
        },
        {
            'name': 'OVH',
            'purchase_cost': 10.99,
            'renewal_cost': 11.99,
            'transfer_fee': 7.99
        },
        {
            'name': 'IONOS',
            'purchase_cost': 9.99,
            'renewal_cost': 12.99,
            'transfer_fee': 6.99
        },
        {
            'name': 'Gandi',
            'purchase_cost': 11.99,
            'renewal_cost': 13.99,
            'transfer_fee': 7.49
        },
        {
            'name': 'Boischaut',
            'purchase_cost': 15.99,
            'renewal_cost': 16.99,
            'transfer_fee': 9.99
        }
    ]

    # Compare costs
    sorted_registrars = compare_domain_costs(domain_name, registrars)

    # Display results
    print(f"Cost comparison for domain: {domain_name}")
    print("Registrar | Purchase Cost | Renewal Cost | Transfer Fee | Total Cost")
    print("-" * 65)
    for registrar in sorted_registrars:
        print(f"{registrar['name']:10} | ${registrar['purchase_cost']:12.2f} | "
              f"${registrar['renewal_cost']:11.2f} | ${registrar['transfer_fee']:11.2f} | "
              f"${registrar['total_cost']:10.2f}")


if __name__ == "__main__":
    main()
```
