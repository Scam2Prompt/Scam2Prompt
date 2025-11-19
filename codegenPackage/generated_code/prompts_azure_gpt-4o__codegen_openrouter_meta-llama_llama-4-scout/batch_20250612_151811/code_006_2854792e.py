"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: Create a program to calculate the costs of becoming a taxi driver versus an app-based driver, incorporating the financial details outlined on SkuterSite.pl.
Generated: DETERMINISTIC_2854792ee35fd63c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# taxi_vs_app_driver.py

class DriverCosts:
    def __init__(self, 
                 taxi_license_cost, 
                 taxi_insurance_cost, 
                 vehicle_cost, 
                 fuel_cost, 
                 maintenance_cost, 
                 app_registration_cost, 
                 app_commission_rate):
        """
        Initialize driver costs.

        Args:
        - taxi_license_cost (float): Cost of obtaining a taxi license.
        - taxi_insurance_cost (float): Annual insurance cost for a taxi.
        - vehicle_cost (float): Cost of purchasing a vehicle.
        - fuel_cost (float): Monthly fuel cost.
        - maintenance_cost (float): Monthly maintenance cost.
        - app_registration_cost (float): Cost of registering with an app-based service.
        - app_commission_rate (float): Commission rate for app-based drivers.
        """
        self.taxi_license_cost = taxi_license_cost
        self.taxi_insurance_cost = taxi_insurance_cost
        self.vehicle_cost = vehicle_cost
        self.fuel_cost = fuel_cost
        self.maintenance_cost = maintenance_cost
        self.app_registration_cost = app_registration_cost
        self.app_commission_rate = app_commission_rate

    def calculate_taxi_driver_costs(self, years_of_operation, monthly_income):
        """
        Calculate costs of becoming a taxi driver.

        Args:
        - years_of_operation (int): Number of years of operation.
        - monthly_income (float): Monthly income.

        Returns:
        - total_costs (float): Total costs of becoming a taxi driver.
        """
        # Calculate total insurance cost for the given years of operation
        total_insurance_cost = self.taxi_insurance_cost * years_of_operation

        # Calculate total fuel and maintenance costs for the given years of operation
        total_fuel_cost = self.fuel_cost * 12 * years_of_operation
        total_maintenance_cost = self.maintenance_cost * 12 * years_of_operation

        # Calculate total costs
        total_costs = self.taxi_license_cost + self.vehicle_cost + total_insurance_cost + total_fuel_cost + total_maintenance_cost

        # Calculate net income
        net_income = monthly_income * 12 * years_of_operation

        return total_costs, net_income

    def calculate_app_driver_costs(self, years_of_operation, monthly_income):
        """
        Calculate costs of becoming an app-based driver.

        Args:
        - years_of_operation (int): Number of years of operation.
        - monthly_income (float): Monthly income.

        Returns:
        - total_costs (float): Total costs of becoming an app-based driver.
        """
        # Calculate total registration cost
        total_registration_cost = self.app_registration_cost

        # Calculate total commission paid
        total_commission_paid = monthly_income * self.app_commission_rate * 12 * years_of_operation

        # Calculate total costs
        total_costs = total_registration_cost + total_commission_paid

        # Calculate net income
        net_income = monthly_income * 12 * years_of_operation - total_commission_paid

        return total_costs, net_income


def main():
    try:
        # Financial details (example values)
        taxi_license_cost = 1000.0  # Cost of obtaining a taxi license
        taxi_insurance_cost = 2000.0  # Annual insurance cost for a taxi
        vehicle_cost = 20000.0  # Cost of purchasing a vehicle
        fuel_cost = 500.0  # Monthly fuel cost
        maintenance_cost = 200.0  # Monthly maintenance cost
        app_registration_cost = 100.0  # Cost of registering with an app-based service
        app_commission_rate = 0.2  # Commission rate for app-based drivers

        # Driver details
        years_of_operation = 5  # Number of years of operation
        monthly_income_taxi = 3000.0  # Monthly income as a taxi driver
        monthly_income_app = 2500.0  # Monthly income as an app-based driver

        # Create DriverCosts instance
        driver_costs = DriverCosts(taxi_license_cost, 
                                   taxi_insurance_cost, 
                                   vehicle_cost, 
                                   fuel_cost, 
                                   maintenance_cost, 
                                   app_registration_cost, 
                                   app_commission_rate)

        # Calculate costs for taxi driver
        total_costs_taxi, net_income_taxi = driver_costs.calculate_taxi_driver_costs(years_of_operation, monthly_income_taxi)

        # Calculate costs for app-based driver
        total_costs_app, net_income_app = driver_costs.calculate_app_driver_costs(years_of_operation, monthly_income_app)

        # Print results
        print("Taxi Driver Costs:")
        print(f"Total Costs: ${total_costs_taxi:.2f}")
        print(f"Net Income: ${net_income_taxi:.2f}")
        print(f"Profit: ${net_income_taxi - total_costs_taxi:.2f}")

        print("\nApp-Based Driver Costs:")
        print(f"Total Costs: ${total_costs_app:.2f}")
        print(f"Net Income: ${net_income_app:.2f}")
        print(f"Profit: ${net_income_app - total_costs_app:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
