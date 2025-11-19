"""
Generated Code Metadata:
========================
Original URL: https://immediategrowth.site
Prompt: What are the key differences between various investment vehicles, such as stocks, bonds, and commodities, and how does Coin Growth help users understand these differences?
Generated: DETERMINISTIC_f08d2ce33db86497
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentVehicle:
    """
    A base class for different types of investment vehicles.
    """

    def __init__(self, name, risk_level, return_potential):
        """
        Initializes an investment vehicle with a name, risk level, and return potential.

        :param name: str - The name of the investment vehicle
        :param risk_level: str - The risk level associated with the investment
        :param return_potential: float - The potential return on investment
        """
        self.name = name
        self.risk_level = risk_level
        self.return_potential = return_potential

    def get_info(self):
        """
        Returns a summary of the investment vehicle's characteristics.

        :return: str - Summary of the investment vehicle
        """
        return f"{self.name}: Risk Level - {self.risk_level}, Return Potential - {self.return_potential}%"


class Stock(InvestmentVehicle):
    """
    Represents a stock investment vehicle.
    """

    def __init__(self, name, risk_level, return_potential, dividend_yield):
        """
        Initializes a stock with additional dividend yield information.

        :param name: str - The name of the stock
        :param risk_level: str - The risk level associated with the stock
        :param return_potential: float - The potential return on investment
        :param dividend_yield: float - The dividend yield of the stock
        """
        super().__init__(name, risk_level, return_potential)
        self.dividend_yield = dividend_yield

    def get_info(self):
        """
        Returns a summary of the stock's characteristics.

        :return: str - Summary of the stock
        """
        base_info = super().get_info()
        return f"{base_info}, Dividend Yield - {self.dividend_yield}%"


class Bond(InvestmentVehicle):
    """
    Represents a bond investment vehicle.
    """

    def __init__(self, name, risk_level, return_potential, maturity_years):
        """
        Initializes a bond with additional maturity information.

        :param name: str - The name of the bond
        :param risk_level: str - The risk level associated with the bond
        :param return_potential: float - The potential return on investment
        :param maturity_years: int - The number of years until maturity
        """
        super().__init__(name, risk_level, return_potential)
        self.maturity_years = maturity_years

    def get_info(self):
        """
        Returns a summary of the bond's characteristics.

        :return: str - Summary of the bond
        """
        base_info = super().get_info()
        return f"{base_info}, Maturity - {self.maturity_years} years"


class Commodity(InvestmentVehicle):
    """
    Represents a commodity investment vehicle.
    """

    def __init__(self, name, risk_level, return_potential, market_demand):
        """
        Initializes a commodity with additional market demand information.

        :param name: str - The name of the commodity
        :param risk_level: str - The risk level associated with the commodity
        :param return_potential: float - The potential return on investment
        :param market_demand: str - The current market demand for the commodity
        """
        super().__init__(name, risk_level, return_potential)
        self.market_demand = market_demand

    def get_info(self):
        """
        Returns a summary of the commodity's characteristics.

        :return: str - Summary of the commodity
        """
        base_info = super().get_info()
        return f"{base_info}, Market Demand - {self.market_demand}"


class CoinGrowth:
    """
    A class to help users understand the differences between investment vehicles.
    """

    @staticmethod
    def compare_investments(investments):
        """
        Compares a list of investment vehicles and returns their information.

        :param investments: list - A list of InvestmentVehicle objects
        :return: str - Summary of all investment vehicles
        """
        try:
            comparison_summary = "\n".join(investment.get_info() for investment in investments)
            return comparison_summary
        except Exception as e:
            return f"An error occurred while comparing investments: {str(e)}"


# Example usage
if __name__ == "__main__":
    investments = [
        Stock("Tech Corp", "High", 15.0, 2.5),
        Bond("Government Bond", "Low", 3.0, 10),
        Commodity("Gold", "Medium", 5.0, "High")
    ]

    comparison = CoinGrowth.compare_investments(investments)
    print(comparison)
```
