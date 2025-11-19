"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Develop a program that calculates property division according to Swedish "Sambolagen" (cohabitation law), as described on juridiskklinik.se.
Generated: DETERMINISTIC_dd93f00a41f91664
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropertyDivision:
    """
    A class to represent the property division according to Swedish 'Sambolagen' (Cohabitation Law).
    """

    def __init__(self, assets, debts):
        """
        Initializes the PropertyDivision with assets and debts.

        :param assets: A dictionary where keys are asset names and values are their values.
        :param debts: A dictionary where keys are debt names and values are their values.
        """
        self.assets = assets
        self.debts = debts

    def total_assets(self):
        """
        Calculates the total value of assets.

        :return: Total value of assets.
        """
        return sum(self.assets.values())

    def total_debts(self):
        """
        Calculates the total value of debts.

        :return: Total value of debts.
        """
        return sum(self.debts.values())

    def net_property(self):
        """
        Calculates the net property value by subtracting total debts from total assets.

        :return: Net property value.
        """
        return self.total_assets() - self.total_debts()

    def division(self):
        """
        Calculates the division of property according to 'Sambolagen'.

        :return: A tuple containing the net property value and the share for each partner.
        """
        net_value = self.net_property()
        if net_value < 0:
            raise ValueError("Net property value cannot be negative. Consider reviewing assets and debts.")

        # Each partner gets half of the net property value
        share = net_value / 2
        return net_value, share

    def display_results(self):
        """
        Displays the results of the property division.

        :return: None
        """
        try:
            net_value, share = self.division()
            print(f"Total Assets: {self.total_assets()} SEK")
            print(f"Total Debts: {self.total_debts()} SEK")
            print(f"Net Property Value: {net_value} SEK")
            print(f"Each partner's share: {share} SEK")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Define assets and debts
    assets = {
        "House": 3000000,
        "Car": 200000,
        "Savings": 500000
    }
    debts = {
        "Mortgage": 2500000,
        "Car Loan": 100000
    }

    # Create a PropertyDivision instance
    property_division = PropertyDivision(assets, debts)

    # Display the results
    property_division.display_results()
```
