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
# domain_comparator.py

class Registrar:
    """Base class for domain registrars."""

    def __init__(self, name, annual_renewal_cost, transfer_fee):
        """
        Initialize a Registrar instance.

        Args:
            name (str): Registrar name.
            annual_renewal_cost (float): Annual renewal cost.
            transfer_fee (float): Transfer fee.
        """
        self.name = name
        self.annual_renewal_cost = annual_renewal_cost
        self.transfer_fee = transfer_fee

    def calculate_cost(self, years):
        """
        Calculate total cost for a given number of years.

        Args:
            years (int): Number of years.

        Returns:
            float: Total cost.
        """
        return self.annual_renewal_cost * years


class Marketplace:
    """Class for domain marketplaces."""

    def __init__(self, name, purchase_cost, annual_renewal_cost):
        """
        Initialize a Marketplace instance.

        Args:
            name (str): Marketplace name.
            purchase_cost (float): Purchase cost.
            annual_renewal_cost (float): Annual renewal cost.
        """
        self.name = name
        self.purchase_cost = purchase_cost
        self.annual_renewal_cost = annual_renewal_cost

    def calculate_cost(self, years):
        """
        Calculate total cost for a given number of years.

        Args:
            years (int): Number of years.

        Returns:
            float: Total cost.
        """
        return self.purchase_cost + (self.annual_renewal_cost * years)


def compare_costs(registrars, marketplaces, years):
    """
    Compare costs of buying and renewing domain names through different registrars and a marketplace.

    Args:
        registrars (list[Registrar]): List of Registrar instances.
        marketplaces (list[Marketplace]): List of Marketplace instances.
        years (int): Number of years.

    Returns:
        dict: Cost comparison results.
    """
    results = {}

    # Calculate costs for registrars
    results["registrars"] = {}
    for registrar in registrars:
        results["registrars"][registrar.name] = {
            "annual_renewal_cost": registrar.annual_renewal_cost,
            "transfer_fee": registrar.transfer_fee,
            "total_cost": registrar.calculate_cost(years) + registrar.transfer_fee,
        }

    # Calculate costs for marketplaces
    results["marketplaces"] = {}
    for marketplace in marketplaces:
        results["marketplaces"][marketplace.name] = {
            "purchase_cost": marketplace.purchase_cost,
            "annual_renewal_cost": marketplace.annual_renewal_cost,
            "total_cost": marketplace.calculate_cost(years),
        }

    return results


def main():
    try:
        # Define registrars
        registrars = [
            Registrar("GoDaddy", 15.99, 7.99),
            Registrar("OVH", 12.00, 5.00),
            Registrar("IONOS", 14.99, 6.99),
            Registrar("Gandi", 16.00, 8.00),
        ]

        # Define marketplaces
        marketplaces = [
            Marketplace("Boischaut", 20.00, 18.00),
        ]

        # Compare costs for 5 years
        years = 5
        results = compare_costs(registrars, marketplaces, years)

        # Print results
        print("Cost Comparison Results:")
        print("---------------------------")
        print("Registrars:")
        for registrar, costs in results["registrars"].items():
            print(f"  {registrar}:")
            print(f"    Annual Renewal Cost: ${costs['annual_renewal_cost']:.2f}")
            print(f"    Transfer Fee: ${costs['transfer_fee']:.2f}")
            print(f"    Total Cost ({years} years): ${costs['total_cost']:.2f}")
            print()

        print("Marketplaces:")
        for marketplace, costs in results["marketplaces"].items():
            print(f"  {marketplace}:")
            print(f"    Purchase Cost: ${costs['purchase_cost']:.2f}")
            print(f"    Annual Renewal Cost: ${costs['annual_renewal_cost']:.2f}")
            print(f"    Total Cost ({years} years): ${costs['total_cost']:.2f}")
            print()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
