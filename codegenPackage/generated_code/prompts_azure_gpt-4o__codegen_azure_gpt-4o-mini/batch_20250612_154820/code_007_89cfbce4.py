"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Create a Python function to calculate potential savings when switching health insurance providers, based on data like premium costs and benefits, as discussed on the Health Insurance Shop blog.
Generated: DETERMINISTIC_89cfbce49f8180a2
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InsuranceProvider:
    def __init__(self, name, monthly_premium, annual_deductible, out_of_pocket_max):
        """
        Initialize an InsuranceProvider instance.

        :param name: Name of the insurance provider
        :param monthly_premium: Monthly premium cost
        :param annual_deductible: Annual deductible amount
        :param out_of_pocket_max: Maximum out-of-pocket expenses per year
        """
        self.name = name
        self.monthly_premium = monthly_premium
        self.annual_deductible = annual_deductible
        self.out_of_pocket_max = out_of_pocket_max

    def annual_cost(self):
        """
        Calculate the total annual cost for the insurance provider.

        :return: Total annual cost (monthly premium * 12 + annual deductible)
        """
        return (self.monthly_premium * 12) + self.annual_deductible


def calculate_savings(current_provider, new_provider):
    """
    Calculate potential savings when switching health insurance providers.

    :param current_provider: Instance of InsuranceProvider for the current provider
    :param new_provider: Instance of InsuranceProvider for the new provider
    :return: Potential savings if switching, or a message if no savings
    """
    try:
        current_cost = current_provider.annual_cost()
        new_cost = new_provider.annual_cost()

        savings = current_cost - new_cost

        if savings > 0:
            return f"Potential savings by switching to {new_provider.name}: ${savings:.2f} per year."
        else:
            return f"No savings by switching to {new_provider.name}. You would spend an additional ${-savings:.2f} per year."
    except Exception as e:
        return f"An error occurred while calculating savings: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Current insurance provider details
    current_provider = InsuranceProvider("Current Health Co", monthly_premium=300, annual_deductible=1500, out_of_pocket_max=5000)

    # New insurance provider details
    new_provider = InsuranceProvider("New Health Inc", monthly_premium=250, annual_deductible=1200, out_of_pocket_max=4000)

    # Calculate and print potential savings
    result = calculate_savings(current_provider, new_provider)
    print(result)
```
