"""
Generated Code Metadata:
========================
Original URL: https://namebudget.net
Prompt: Generate a script to calculate the cost of registering multiple domains using NameBudget.net's pricing structure and display the total in a user-friendly format.
Generated: DETERMINISTIC_14eef0524d1e7eab
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# namebudget_domain_calculator.py

class DomainRegistrar:
    def __init__(self):
        # Define NameBudget.net's pricing structure
        self.pricing_structure = {
            'com': 10.99,
            'net': 12.99,
            'io': 14.99,
            'org': 11.99,
            'biz': 13.99
        }

    def calculate_domain_cost(self, domain_name, extension):
        """
        Calculate the cost of registering a single domain.

        Args:
            domain_name (str): The domain name.
            extension (str): The domain extension (e.g., com, net, io).

        Returns:
            float: The cost of registering the domain.

        Raises:
            ValueError: If the domain extension is not supported.
        """
        if extension not in self.pricing_structure:
            raise ValueError(f"Unsupported domain extension: {extension}")

        return self.pricing_structure[extension]

    def calculate_total_cost(self, domains):
        """
        Calculate the total cost of registering multiple domains.

        Args:
            domains (list[tuple[str, str]]): A list of tuples containing domain names and extensions.

        Returns:
            float: The total cost of registering all domains.

        Raises:
            ValueError: If a domain extension is not supported.
        """
        total_cost = 0.0
        for domain_name, extension in domains:
            try:
                domain_cost = self.calculate_domain_cost(domain_name, extension)
                total_cost += domain_cost
            except ValueError as e:
                print(f"Error: {e}")

        return total_cost


def main():
    registrar = DomainRegistrar()

    # Example usage
    domains = [
        ('example', 'com'),
        ('test', 'net'),
        ('blog', 'io'),
        ('forum', 'org'),
        ('shop', 'biz')
    ]

    total_cost = registrar.calculate_total_cost(domains)

    print("Domain Registration Costs:")
    for i, (domain_name, extension) in enumerate(domains, start=1):
        try:
            domain_cost = registrar.calculate_domain_cost(domain_name, extension)
            print(f"{i}. {domain_name}.{extension}: ${domain_cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    print(f"\nTotal Cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
```
