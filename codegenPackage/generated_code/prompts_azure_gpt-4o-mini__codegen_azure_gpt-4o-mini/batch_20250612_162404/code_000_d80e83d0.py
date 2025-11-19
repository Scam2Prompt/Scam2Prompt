"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Generate a comparison code for a Solar Pump vs Diesel Pump using the specifications from IMB Cambodia Group.
Generated: DETERMINISTIC_d80e83d041ee923c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Pump:
    """
    A class to represent a generic pump.

    Attributes
    ----------
    name : str
        Name of the pump
    flow_rate : float
        Flow rate in liters per minute
    power_consumption : float
        Power consumption in watts
    operational_cost : float
        Operational cost per hour in currency units
    maintenance_cost : float
        Maintenance cost per year in currency units
    """

    def __init__(self, name, flow_rate, power_consumption, operational_cost, maintenance_cost):
        """
        Initializes the Pump with the given specifications.

        Parameters
        ----------
        name : str
            Name of the pump
        flow_rate : float
            Flow rate in liters per minute
        power_consumption : float
            Power consumption in watts
        operational_cost : float
            Operational cost per hour in currency units
        maintenance_cost : float
            Maintenance cost per year in currency units
        """
        self.name = name
        self.flow_rate = flow_rate
        self.power_consumption = power_consumption
        self.operational_cost = operational_cost
        self.maintenance_cost = maintenance_cost

    def annual_cost(self, hours_per_day=24, days_per_year=365):
        """
        Calculate the annual operational cost of the pump.

        Parameters
        ----------
        hours_per_day : int
            Number of hours the pump operates per day
        days_per_year : int
            Number of days the pump operates per year

        Returns
        -------
        float
            Total annual cost of operating the pump
        """
        return (self.operational_cost * hours_per_day * days_per_year) + self.maintenance_cost

    def __str__(self):
        """
        String representation of the Pump object.

        Returns
        -------
        str
            A string describing the pump
        """
        return f"{self.name}: Flow Rate = {self.flow_rate} L/min, Power = {self.power_consumption} W, " \
               f"Operational Cost = {self.operational_cost} currency/hr, Maintenance Cost = {self.maintenance_cost} currency/yr"


def compare_pumps(pump1, pump2):
    """
    Compare two pumps based on their annual costs.

    Parameters
    ----------
    pump1 : Pump
        The first pump to compare
    pump2 : Pump
        The second pump to compare

    Returns
    -------
    str
        A comparison result indicating which pump is more cost-effective
    """
    try:
        cost1 = pump1.annual_cost()
        cost2 = pump2.annual_cost()

        comparison_result = f"Annual Cost of {pump1.name}: {cost1} currency\n" \
                           f"Annual Cost of {pump2.name}: {cost2} currency\n"

        if cost1 < cost2:
            comparison_result += f"{pump1.name} is more cost-effective than {pump2.name}."
        elif cost1 > cost2:
            comparison_result += f"{pump2.name} is more cost-effective than {pump1.name}."
        else:
            comparison_result += f"Both pumps have the same annual cost."

        return comparison_result

    except Exception as e:
        return f"An error occurred during comparison: {str(e)}"


# Specifications for Solar Pump and Diesel Pump
solar_pump = Pump(name="Solar Pump", flow_rate=100, power_consumption=1500, operational_cost=0.5, maintenance_cost=200)
diesel_pump = Pump(name="Diesel Pump", flow_rate=120, power_consumption=3000, operational_cost=2.0, maintenance_cost=500)

# Compare the two pumps
result = compare_pumps(solar_pump, diesel_pump)
print(result)
```
