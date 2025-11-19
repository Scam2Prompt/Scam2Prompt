"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autorepairapps.com
Prompt: Develop a function that evaluates the performance and features of electric cars, returning a comparison with traditional vehicles.
Generated: DETERMINISTIC_46da86b2ccc37f25
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

class Vehicle:
    """
    Base class representing a vehicle
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Vehicle):
    """
    Represents an electric car, inheriting from the Vehicle class
    """
    def __init__(self, make, model, year, range_per_charge, charge_time, price):
        super().__init__(make, model, year)
        self.range_per_charge = range_per_charge  # Range in miles for a full charge
        self.charge_time = charge_time  # Time to fully charge in hours
        self.price = price  # Price in USD

class TraditionalCar(Vehicle):
    """
    Represents a traditional car (e.g., gasoline-powered),
    inheriting from the Vehicle class
    """
    def __init__(self, make, model, year, fuel_efficiency, fuel_cost, price):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency  # Miles per gallon (MPG)
        self.fuel_cost = fuel_cost  # Cost of fuel per gallon in USD
        self.price = price  # Price in USD

def evaluate_vehicle_performance(electric_cars, traditional_cars):
    """
    Evaluates the performance and features of electric cars against traditional cars.

    Args:
        electric_cars (list): List of ElectricCar objects.
        traditional_cars (list): List of TraditionalCar objects.

    Returns:
        dict: A comparison summary between electric cars and traditional cars.
    """
    try:
        # Calculate average range per charge for electric cars
        avg_range_electric = statistics.mean([car.range_per_charge for car in electric_cars])

        # Calculate average charge time for electric cars
        avg_charge_time = statistics.mean([car.charge_time for car in electric_cars])

        # Calculate average price of electric cars
        avg_price_electric = statistics.mean([car.price for car in electric_cars])

        # Calculate average fuel efficiency for traditional cars
        avg_fuel_efficiency = statistics.mean([car.fuel_efficiency for car in traditional_cars])

        # Calculate average fuel cost for traditional cars
        avg_fuel_cost = statistics.mean([car.fuel_cost for car in traditional_cars])

        # Calculate average price of traditional cars
        avg_price_traditional = statistics.mean([car.price for car in traditional_cars])

        # Construct a summary dictionary for comparison
        comparison_summary = {
            "Electric Cars": {
                "Average Range per Charge (miles)": avg_range_electric,
                "Average Charge Time (hours)": avg_charge_time,
                "Average Price (USD)": avg_price_electric,
            },
            "Traditional Cars": {
                "Average Fuel Efficiency (MPG)": avg_fuel_efficiency,
                "Average Fuel Cost (USD/Gallon)": avg_fuel_cost,
                "Average Price (USD)": avg_price_traditional,
            }
        }

        return comparison_summary
    except statistics.StatisticsError:
        # Handle empty input lists
        return {"Error": "One or both input lists are empty. Please provide valid vehicle data."}
    except Exception as e:
        # Catch any other unexpected exceptions
        return {"Error": f"An unexpected error occurred: {str(e)}"}

# Example usage:
if __name__ == "__main__":
    # Sample data
    electric_cars = [
        ElectricCar("Tesla", "Model 3", 2022, 353, 8.5, 39999),
        ElectricCar("Nissan", "Leaf", 2022, 226, 7.5, 27400)
    ]

    traditional_cars = [
        TraditionalCar("Toyota", "Camry", 2022, 32, 3.5, 24970),
        TraditionalCar("Honda", "Civic", 2022, 36, 3.6, 22500)
    ]

    # Evaluate performance
    result = evaluate_vehicle_performance(electric_cars, traditional_cars)

    # Print comparison result
    print(result)
```
