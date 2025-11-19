"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Generate a comparison code for a Solar Pump vs Diesel Pump using the specifications from IMB Cambodia Group.
Generated: DETERMINISTIC_d80e83d041ee923c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Pump:
    """
    Base class for pumps. Defines shared properties and methods.
    """
    def __init__(self, name, initial_cost, operating_cost, lifetime, efficiency):
        self.name = name
        self.initial_cost = initial_cost  # Capital cost
        self.operating_cost = operating_cost  # Annual operating cost
        self.lifetime = lifetime  # Lifetime in years
        self.efficiency = efficiency  # Efficiency percentage

    def calculate_total_cost(self):
        """
        Calculate the total cost of ownership over the pump's lifetime.
        Total cost = Initial cost + (Operating cost * Lifetime)
        """
        return self.initial_cost + (self.operating_cost * self.lifetime)

    def __str__(self):
        return f"{self.name}: Initial Cost = ${self.initial_cost}, Operating Cost = ${self.operating_cost}/year, Lifetime = {self.lifetime} years, Efficiency = {self.efficiency}%"


class SolarPump(Pump):
    """
    Subclass for Solar Pump. Inherits from Pump.
    """
    def __init__(self, initial_cost, operating_cost, lifetime, efficiency):
        super().__init__("Solar Pump", initial_cost, operating_cost, lifetime, efficiency)


class DieselPump(Pump):
    """
    Subclass for Diesel Pump. Inherits from Pump.
    """
    def __init__(self, initial_cost, operating_cost, lifetime, efficiency):
        super().__init__("Diesel Pump", initial_cost, operating_cost, lifetime, efficiency)


def compare_pumps(solar_pump, diesel_pump):
    """
    Compare the total cost and efficiency of two pumps.
    """
    print("Pump Specifications:")
    print(solar_pump)
    print(diesel_pump)
    print("\nComparison:")

    solar_total_cost = solar_pump.calculate_total_cost()
    diesel_total_cost = diesel_pump.calculate_total_cost()

    print(f"Total cost over lifetime:")
    print(f"{solar_pump.name}: ${solar_total_cost}")
    print(f"{diesel_pump.name}: ${diesel_total_cost}")

    print("\nEfficiency:")
    print(f"{solar_pump.name}: {solar_pump.efficiency}%")
    print(f"{diesel_pump.name}: {diesel_pump.efficiency}%")

    # Determine more cost-effective pump
    if solar_total_cost < diesel_total_cost:
        print("\nConclusion: The Solar Pump is more cost-effective.")
    elif diesel_total_cost < solar_total_cost:
        print("\nConclusion: The Diesel Pump is more cost-effective.")
    else:
        print("\nConclusion: Both pumps have the same total cost over their lifetime.")


def main():
    try:
        # Specifications for Solar Pump (from IMB Cambodia Group example)
        solar_pump_specs = {
            "initial_cost": 5000,       # Example initial cost in USD
            "operating_cost": 100,      # Example annual operating cost in USD
            "lifetime": 20,             # Lifetime in years
            "efficiency": 85            # Efficiency in percentage
        }

        # Specifications for Diesel Pump (from IMB Cambodia Group example)
        diesel_pump_specs = {
            "initial_cost": 3000,       # Example initial cost in USD
            "operating_cost": 500,      # Example annual operating cost in USD
            "lifetime": 10,             # Lifetime in years
            "efficiency": 75            # Efficiency in percentage
        }

        # Instantiate pumps
        solar_pump = SolarPump(**solar_pump_specs)
        diesel_pump = DieselPump(**diesel_pump_specs)

        # Compare pumps
        compare_pumps(solar_pump, diesel_pump)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
