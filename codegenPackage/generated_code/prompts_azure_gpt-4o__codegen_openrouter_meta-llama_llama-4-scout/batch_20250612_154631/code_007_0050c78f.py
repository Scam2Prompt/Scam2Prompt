"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Write a program to calculate the cost-effectiveness of using Econopure's LFnano filtration systems for brackish water treatment compared to conventional RO systems.
Generated: DETERMINISTIC_0050c78ff7902e67
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# econopure_cost_effectiveness.py

class FiltrationSystem:
    def __init__(self, name, capital_cost, operating_cost, lifespan, flow_rate):
        """
        Initialize a filtration system.

        Args:
            name (str): Name of the filtration system.
            capital_cost (float): Capital cost of the filtration system.
            operating_cost (float): Operating cost per unit of water treated.
            lifespan (int): Lifespan of the filtration system in years.
            flow_rate (float): Flow rate of the filtration system in m3/day.
        """
        self.name = name
        self.capital_cost = capital_cost
        self.operating_cost = operating_cost
        self.lifespan = lifespan
        self.flow_rate = flow_rate

    def calculate_total_cost(self, years_of_operation):
        """
        Calculate the total cost of the filtration system over a given period.

        Args:
            years_of_operation (int): Number of years of operation.

        Returns:
            float: Total cost of the filtration system.
        """
        # Calculate the annualized capital cost
        annualized_capital_cost = self.capital_cost / self.lifespan

        # Calculate the total operating cost
        total_operating_cost = self.operating_cost * self.flow_rate * 365 * years_of_operation

        # Calculate the total cost
        total_cost = annualized_capital_cost * years_of_operation + total_operating_cost

        return total_cost


class EconopureLFnano(FiltrationSystem):
    def __init__(self, capital_cost, operating_cost, lifespan, flow_rate):
        """
        Initialize an Econopure LFnano filtration system.

        Args:
            capital_cost (float): Capital cost of the Econopure LFnano filtration system.
            operating_cost (float): Operating cost per unit of water treated.
            lifespan (int): Lifespan of the Econopure LFnano filtration system in years.
            flow_rate (float): Flow rate of the Econopure LFnano filtration system in m3/day.
        """
        super().__init__("Econopure LFnano", capital_cost, operating_cost, lifespan, flow_rate)


class ConventionalRO(FiltrationSystem):
    def __init__(self, capital_cost, operating_cost, lifespan, flow_rate):
        """
        Initialize a conventional RO filtration system.

        Args:
            capital_cost (float): Capital cost of the conventional RO filtration system.
            operating_cost (float): Operating cost per unit of water treated.
            lifespan (int): Lifespan of the conventional RO filtration system in years.
            flow_rate (float): Flow rate of the conventional RO filtration system in m3/day.
        """
        super().__init__("Conventional RO", capital_cost, operating_cost, lifespan, flow_rate)


def calculate_cost_effectiveness(econopure_system, conventional_ro_system, years_of_operation, water_treated):
    """
    Calculate the cost-effectiveness of the Econopure LFnano filtration system compared to the conventional RO system.

    Args:
        econopure_system (EconopureLFnano): Econopure LFnano filtration system.
        conventional_ro_system (ConventionalRO): Conventional RO filtration system.
        years_of_operation (int): Number of years of operation.
        water_treated (float): Total amount of water treated in m3.

    Returns:
        dict: Cost-effectiveness results.
    """
    try:
        # Calculate the total cost of both systems
        econopure_total_cost = econopure_system.calculate_total_cost(years_of_operation)
        conventional_ro_total_cost = conventional_ro_system.calculate_total_cost(years_of_operation)

        # Calculate the cost per unit of water treated
        econopure_cost_per_unit = econopure_total_cost / (water_treated)
        conventional_ro_cost_per_unit = conventional_ro_total_cost / (water_treated)

        # Calculate the cost savings
        cost_savings = conventional_ro_cost_per_unit - econopure_cost_per_unit

        # Return the cost-effectiveness results
        return {
            "econopure_total_cost": econopure_total_cost,
            "conventional_ro_total_cost": conventional_ro_total_cost,
            "econopure_cost_per_unit": econopure_cost_per_unit,
            "conventional_ro_cost_per_unit": conventional_ro_cost_per_unit,
            "cost_savings": cost_savings,
        }

    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None


def main():
    # Define the filtration systems
    econopure_system = EconopureLFnano(
        capital_cost=100000,
        operating_cost=0.05,
        lifespan=10,
        flow_rate=100,
    )

    conventional_ro_system = ConventionalRO(
        capital_cost=150000,
        operating_cost=0.10,
        lifespan=8,
        flow_rate=100,
    )

    # Define the operation parameters
    years_of_operation = 5
    water_treated = 182500  # 500 m3/day * 365 days/year * 5 years

    # Calculate the cost-effectiveness
    results = calculate_cost_effectiveness(
        econopure_system, conventional_ro_system, years_of_operation, water_treated
    )

    if results:
        print("Cost-Effectiveness Results:")
        print(f"Econopure LFnano Total Cost: ${results['econopure_total_cost']:.2f}")
        print(f"Conventional RO Total Cost: ${results['conventional_ro_total_cost']:.2f}")
        print(f"Econopure LFnano Cost per Unit: ${results['econopure_cost_per_unit']:.2f}/m3")
        print(f"Conventional RO Cost per Unit: ${results['conventional_ro_cost_per_unit']:.2f}/m3")
        print(f"Cost Savings: ${results['cost_savings']:.2f}/m3")


if __name__ == "__main__":
    main()
```
