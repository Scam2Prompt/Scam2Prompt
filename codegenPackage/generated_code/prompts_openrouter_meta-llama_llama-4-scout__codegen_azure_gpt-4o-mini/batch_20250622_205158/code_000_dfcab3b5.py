"""
Generated Code Metadata:
========================
Original URL: https://alphagrowth.fund
Prompt: What are the key factors to consider when investing in a fund for alpha growth?
Generated: DETERMINISTIC_dfcab3b5ec189c06
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentFund:
    """
    A class to represent an investment fund focused on alpha growth.

    Attributes:
        name (str): The name of the fund.
        management_fee (float): The annual management fee as a percentage.
        performance_fee (float): The performance fee as a percentage of profits.
        historical_returns (list): A list of historical annual returns.
    """

    def __init__(self, name, management_fee, performance_fee, historical_returns):
        """
        Initializes the InvestmentFund with the given parameters.

        Args:
            name (str): The name of the fund.
            management_fee (float): The annual management fee as a percentage.
            performance_fee (float): The performance fee as a percentage of profits.
            historical_returns (list): A list of historical annual returns.

        Raises:
            ValueError: If any of the fees are negative or if historical returns are not a list of floats.
        """
        if management_fee < 0 or performance_fee < 0:
            raise ValueError("Management and performance fees must be non-negative.")
        if not all(isinstance(r, float) for r in historical_returns):
            raise ValueError("Historical returns must be a list of floats.")

        self.name = name
        self.management_fee = management_fee
        self.performance_fee = performance_fee
        self.historical_returns = historical_returns

    def calculate_average_return(self):
        """
        Calculates the average annual return of the fund.

        Returns:
            float: The average annual return.
        """
        return sum(self.historical_returns) / len(self.historical_returns)

    def calculate_net_return(self):
        """
        Calculates the net return after management and performance fees.

        Returns:
            float: The net return after fees.
        """
        average_return = self.calculate_average_return()
        net_return = average_return - self.management_fee

        # Assuming performance fee is applied only on profits
        if average_return > 0:
            net_return -= (average_return * self.performance_fee)

        return net_return

    def __str__(self):
        """
        Returns a string representation of the InvestmentFund.

        Returns:
            str: A string describing the fund.
        """
        return (f"Investment Fund: {self.name}\n"
                f"Management Fee: {self.management_fee}%\n"
                f"Performance Fee: {self.performance_fee}%\n"
                f"Average Return: {self.calculate_average_return():.2f}%\n"
                f"Net Return: {self.calculate_net_return():.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        # Creating an instance of InvestmentFund
        fund = InvestmentFund(
            name="Alpha Growth Fund",
            management_fee=1.5,
            performance_fee=20,
            historical_returns=[0.10, 0.15, 0.12, 0.08, 0.20]
        )

        # Displaying fund information
        print(fund)

    except ValueError as e:
        print(f"Error: {e}")
```
