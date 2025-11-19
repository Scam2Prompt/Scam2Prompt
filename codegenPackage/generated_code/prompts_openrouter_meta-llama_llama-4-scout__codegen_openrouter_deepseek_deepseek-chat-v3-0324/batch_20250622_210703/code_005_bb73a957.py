"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Develop a code snippet to calculate the total cost of ownership of an electric vehicle, considering factors like purchase price, charging time, and maintenance costs, as mentioned on the eControl SA website."
Generated: DETERMINISTIC_bb73a957c2e83839
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electric_vehicle_tco_calculator.py
"""
Electric Vehicle Total Cost of Ownership (TCO) Calculator.
This script calculates the total cost of ownership for an electric vehicle
based on purchase price, charging costs, maintenance costs, and other factors.
"""

class ElectricVehicleTCOCalculator:
    """
    A class to calculate the Total Cost of Ownership (TCO) for an electric vehicle.
    
    Attributes:
        purchase_price (float): Initial purchase price of the vehicle
        annual_mileage (float): Miles driven per year
        electricity_cost_per_kwh (float): Cost per kWh in local currency
        charging_efficiency (float): Efficiency of charging (0 to 1)
        battery_capacity_kwh (float): Battery capacity in kWh
        range_miles (float): Vehicle range on full charge in miles
        annual_maintenance_cost (float): Estimated annual maintenance cost
        insurance_cost (float): Annual insurance cost
        years_owned (int): Number of years the vehicle will be owned
        resale_value (float): Estimated resale value after ownership period
        tax_credits (float): Any applicable tax credits or incentives
    """
    
    def __init__(
        self,
        purchase_price: float,
        annual_mileage: float,
        electricity_cost_per_kwh: float,
        charging_efficiency: float = 0.9,
        battery_capacity_kwh: float = 0,
        range_miles: float = 0,
        annual_maintenance_cost: float = 0,
        insurance_cost: float = 0,
        years_owned: int = 5,
        resale_value: float = 0,
        tax_credits: float = 0
    ):
        """
        Initialize the calculator with vehicle and cost parameters.
        
        Args:
            purchase_price: Initial purchase price of the vehicle
            annual_mileage: Miles driven per year
            electricity_cost_per_kwh: Cost per kWh in local currency
            charging_efficiency: Efficiency of charging (default: 0.9)
            battery_capacity_kwh: Battery capacity in kWh
            range_miles: Vehicle range on full charge in miles
            annual_maintenance_cost: Estimated annual maintenance cost
            insurance_cost: Annual insurance cost
            years_owned: Number of years the vehicle will be owned (default: 5)
            resale_value: Estimated resale value after ownership period
            tax_credits: Any applicable tax credits or incentives
        """
        self.purchase_price = purchase_price
        self.annual_mileage = annual_mileage
        self.electricity_cost_per_kwh = electricity_cost_per_kwh
        self.charging_efficiency = charging_efficiency
        self.battery_capacity_kwh = battery_capacity_kwh
        self.range_miles = range_miles
        self.annual_maintenance_cost = annual_maintenance_cost
        self.insurance_cost = insurance_cost
        self.years_owned = years_owned
        self.resale_value = resale_value
        self.tax_credits = tax_credits
        
        # Validate inputs
        if any(value < 0 for value in [
            purchase_price, annual_mileage, electricity_cost_per_kwh,
            battery_capacity_kwh, range_miles, annual_maintenance_cost,
            insurance_cost, resale_value, tax_credits
        ]):
            raise ValueError("All monetary values must be non-negative")
        if years_owned <= 0:
            raise ValueError("Years owned must be greater than zero")
        if not 0 < charging_efficiency <= 1:
            raise ValueError("Charging efficiency must be between 0 and 1")
    
    def calculate_energy_cost(self) -> float:
        """
        Calculate the total energy cost over the ownership period.
        
        Returns:
            float: Total energy cost in local currency
        """
        if self.range_miles <= 0 or self.battery_capacity_kwh <= 0:
            raise ValueError("Battery capacity and range must be positive values")
            
        kwh_per_mile = self.battery_capacity_kwh / self.range_miles
        annual_kwh = self.annual_mileage * kwh_per_mile / self.charging_efficiency
        return annual_kwh * self.electricity_cost_per_kwh * self.years_owned
    
    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of ownership.
        
        Returns:
            float: Total cost of ownership in local currency
        """
        try:
            energy_cost = self.calculate_energy_cost()
            total_cost = (
                self.purchase_price
                + energy_cost
                + (self.annual_maintenance_cost * self.years_owned)
                + (self.insurance_cost * self.years_owned)
                - self.resale_value
                - self.tax_credits
            )
            return total_cost
        except Exception as e:
            raise ValueError(f"Error calculating total cost: {str(e)}")
    
    def calculate_annual_cost(self) -> float:
        """
        Calculate the annual cost of ownership.
        
        Returns:
            float: Annual cost of ownership in local currency
        """
        try:
            return self.calculate_total_cost() / self.years_owned
        except Exception as e:
            raise ValueError(f"Error calculating annual cost: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Example parameters (values should be replaced with actual data)
        calculator = ElectricVehicleTCOCalculator(
            purchase_price=45000,
            annual_mileage=12000,
            electricity_cost_per_kwh=0.12,
            battery_capacity_kwh=75,
            range_miles=250,
            annual_maintenance_cost=500,
            insurance_cost=1200,
            years_owned=5,
            resale_value=20000,
            tax_credits=7500
        )
        
        total_cost = calculator.calculate_total_cost()
        annual_cost = calculator.calculate_annual_cost()
        
        print(f"Total Cost of Ownership: ${total_cost:,.2f}")
        print(f"Annual Cost: ${annual_cost:,.2f}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
```
