"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateunity.org
Prompt: Generate a script to calculate the environmental benefits of investing in electric vehicle infrastructure in the UK, referencing Immediate Unity's article "What are the benefits of investing in electric vehicle infrastructure in the UK?"
Generated: DETERMINISTIC_503df705f0b760c7
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class ElectricVehicleInfrastructure:
    """
    A class to calculate the environmental benefits of investing in electric vehicle infrastructure.
    """

    def __init__(self, current_ev_count, target_ev_count, average_miles_per_ev, co2_per_mile):
        """
        Initializes the ElectricVehicleInfrastructure class.

        Args:
            current_ev_count (int): Current number of electric vehicles.
            target_ev_count (int): Target number of electric vehicles after infrastructure investment.
            average_miles_per_ev (float): Average miles driven per electric vehicle per year.
            co2_per_mile (float): CO2 emissions per mile for traditional vehicles.
        """
        self.current_ev_count = current_ev_count
        self.target_ev_count = target_ev_count
        self.average_miles_per_ev = average_miles_per_ev
        self.co2_per_mile = co2_per_mile

    def calculate_co2_emissions(self, ev_count):
        """
        Calculates the CO2 emissions avoided by electric vehicles.

        Args:
            ev_count (int): Number of electric vehicles.

        Returns:
            float: Total CO2 emissions avoided in metric tons.
        """
        # CO2 emissions avoided in metric tons
        emissions_avoided = (ev_count * self.average_miles_per_ev * self.co2_per_mile) / 2204.62  # Convert lbs to tons
        return emissions_avoided

    def calculate_environmental_benefits(self):
        """
        Calculates the environmental benefits of increasing electric vehicle infrastructure.

        Returns:
            dict: A dictionary containing the current and target emissions avoided.
        """
        results = {}
        try:
            # Calculate emissions avoided for current and target EV counts
            current_emissions_avoided = self.calculate_co2_emissions(self.current_ev_count)
            target_emissions_avoided = self.calculate_co2_emissions(self.target_ev_count)

            results['current_emissions_avoided'] = current_emissions_avoided
            results['target_emissions_avoided'] = target_emissions_avoided
            results['emissions_reduction'] = target_emissions_avoided - current_emissions_avoided

            return results
        except Exception as e:
            print(f"Error calculating environmental benefits: {e}")
            return None

def main():
    """
    Main function to run the environmental benefits calculation.
    """
    # Example data, these values would ideally come from a database or an API.
    current_ev_count = 300000  # Current EV count in the UK
    target_ev_count = 3000000   # Target EV count in the UK
    average_miles_per_ev = 12400 # Average miles driven per electric vehicle
    co2_per_mile = 404          # CO2 emissions per mile for traditional vehicles in lbs

    ev_infrastructure = ElectricVehicleInfrastructure(current_ev_count, target_ev_count, average_miles_per_ev, co2_per_mile)
    
    benefits = ev_infrastructure.calculate_environmental_benefits()
    
    if benefits:
        print("Environmental Benefits of EV Infrastructure Investment:")
        print(json.dumps(benefits, indent=4))

if __name__ == "__main__":
    main()
```
