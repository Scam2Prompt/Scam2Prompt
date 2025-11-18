"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Generate a script to estimate the cost and energy savings for installing solar panels and EV charging stations, using the services described on Technische Installatiebedrijf van Boxtel's website.
Generated: DETERMINISTIC_3c1f97071191b610
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class EnergyCostEstimator:
    def __init__(self, solar_panel_cost_per_kw, ev_charger_cost, energy_savings_percentage):
        """
        Initializes the EnergyCostEstimator with the necessary parameters.

        :param solar_panel_cost_per_kw: Cost of solar panels per kW
        :param ev_charger_cost: Cost of installing an EV charging station
        :param energy_savings_percentage: Estimated energy savings percentage from solar panels
        """
        self.solar_panel_cost_per_kw = solar_panel_cost_per_kw
        self.ev_charger_cost = ev_charger_cost
        self.energy_savings_percentage = energy_savings_percentage
    
    def estimate_solar_panel_cost(self, kw_needed):
        """
        Estimates the total cost of installing solar panels based on the required kW.

        :param kw_needed: The number of kilowatts needed for the solar panel installation
        :return: Total cost of solar panel installation
        """
        if kw_needed <= 0:
            raise ValueError("kw_needed must be greater than zero.")
        
        total_cost = kw_needed * self.solar_panel_cost_per_kw
        return total_cost

    def estimate_energy_savings(self, annual_energy_cost):
        """
        Estimates the annual energy savings based on the energy savings percentage.

        :param annual_energy_cost: The total annual cost of energy before savings
        :return: Estimated annual energy savings
        """
        if annual_energy_cost < 0:
            raise ValueError("annual_energy_cost must be non-negative.")
        
        savings = annual_energy_cost * (self.energy_savings_percentage / 100)
        return savings

    def total_estimate(self, kw_needed, annual_energy_cost):
        """
        Calculates the total estimate including solar panel installation and energy savings.

        :param kw_needed: The number of kilowatts needed for solar panel installation
        :param annual_energy_cost: The total annual cost of energy
        :return: A dictionary containing the total cost of solar panels, energy savings, and total estimate
        """
        try:
            solar_cost = self.estimate_solar_panel_cost(kw_needed)
            energy_savings = self.estimate_energy_savings(annual_energy_cost)
            total_estimate = solar_cost + self.ev_charger_cost - energy_savings
            
            return {
                "solar_cost": solar_cost,
                "energy_savings": energy_savings,
                "total_estimate": total_estimate
            }
        except ValueError as e:
            return {"error": str(e)}

def main():
    # Example parameters (These values should ideally come from a configuration file or user input)
    SOLAR_PANEL_COST_PER_KW = 1500  # Cost per kW of solar panels
    EV_CHARGER_COST = 1000           # Cost of EV charger installation
    ENERGY_SAVINGS_PERCENTAGE = 30   # Estimated energy savings percentage

    estimator = EnergyCostEstimator(SOLAR_PANEL_COST_PER_KW, EV_CHARGER_COST, ENERGY_SAVINGS_PERCENTAGE)

    # Example inputs for estimation
    kw_needed = 5   # kW needed for the solar panel installation
    annual_energy_cost = 1200  # Total annual energy cost in currency

    # Calculate estimates
    result = estimator.total_estimate(kw_needed, annual_energy_cost)

    # Print the results
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
```
