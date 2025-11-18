"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://universalsolar1.com
Prompt: Generate code to model the financial profitability of solar projects using Universal Solar's approach to financing partnerships with major investment groups worldwide.
Generated: DETERMINISTIC_8611e5f05ae84c36
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class SolarProjectProfitability:
    """
    A class to model the financial profitability of solar projects.
    This includes calculations related to initial investment, operational costs, 
    revenue from energy generation, and profit sharing with investment partners.
    """

    def __init__(self, project_name, capacity_kw, cost_per_kw, energy_price, operational_cost, investment_split):
        """
        Initialize the solar project profitability model.

        :param project_name: Name of the solar project.
        :param capacity_kw: Capacity of the solar project in kilowatts (kW).
        :param cost_per_kw: Total cost per kW of capacity ($).
        :param energy_price: Price per kWh of energy generated ($).
        :param operational_cost: Annual operational cost ($).
        :param investment_split: Dictionary containing the percentage split of profits
                                 with investment partners. Example: {"Universal Solar": 0.6, "Investor Group A": 0.4}
        """
        self.project_name = project_name
        self.capacity_kw = capacity_kw
        self.cost_per_kw = cost_per_kw
        self.energy_price = energy_price
        self.operational_cost = operational_cost
        self.investment_split = investment_split

        # Calculate initial investment cost
        self.initial_investment = self.capacity_kw * self.cost_per_kw

    def annual_energy_generation(self, sun_hours_per_day):
        """
        Calculate the annual energy generation based on capacity and average sun hours per day.

        :param sun_hours_per_day: Average daily sun hours.
        :return: Annual energy generation in kWh.
        """
        # Energy generation = capacity * sun hours per day * days in year
        return self.capacity_kw * sun_hours_per_day * 365

    def annual_revenue(self, sun_hours_per_day):
        """
        Calculate annual revenue from energy generation.

        :param sun_hours_per_day: Average daily sun hours.
        :return: Annual revenue ($).
        """
        return self.annual_energy_generation(sun_hours_per_day) * self.energy_price

    def annual_profit(self, sun_hours_per_day):
        """
        Calculate annual profit after operational costs.

        :param sun_hours_per_day: Average daily sun hours.
        :return: Annual profit ($).
        """
        revenue = self.annual_revenue(sun_hours_per_day)
        return revenue - self.operational_cost

    def profitability_distribution(self, sun_hours_per_day):
        """
        Calculate the profit distribution between Universal Solar and investment partners.

        :param sun_hours_per_day: Average daily sun hours.
        :return: Dictionary with profit distribution.
        """
        total_profit = self.annual_profit(sun_hours_per_day)
        distribution = {}
        for partner, percentage in self.investment_split.items():
            distribution[partner] = round(total_profit * percentage, 2)
        return distribution

    def summary(self, sun_hours_per_day):
        """
        Generate a summary of the project's financial data.

        :param sun_hours_per_day: Average daily sun hours.
        :return: Dictionary summarizing the financial data.
        """
        summary = {
            "Project Name": self.project_name,
            "Capacity (kW)": self.capacity_kw,
            "Initial Investment ($)": self.initial_investment,
            "Annual Energy Generation (kWh)": self.annual_energy_generation(sun_hours_per_day),
            "Annual Revenue ($)": self.annual_revenue(sun_hours_per_day),
            "Annual Operational Cost ($)": self.operational_cost,
            "Annual Profit ($)": self.annual_profit(sun_hours_per_day),
            "Profit Distribution ($)": self.profitability_distribution(sun_hours_per_day),
        }
        return summary


# Error handling and input validation would be implemented in real-world usage scenarios
if __name__ == "__main__":
    try:
        # Example solar project
        solar_project = SolarProjectProfitability(
            project_name="Sunny Fields Solar",
            capacity_kw=500,
            cost_per_kw=1200,
            energy_price=0.12,
            operational_cost=30000,
            investment_split={"Universal Solar": 0.6, "Investor Group A": 0.4}
        )

        # Average sun hours per day for the location
        average_sun_hours = 6

        # Generate the summary of financial data
        financial_summary = solar_project.summary(average_sun_hours)

        # Print the summary
        for key, value in financial_summary.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
