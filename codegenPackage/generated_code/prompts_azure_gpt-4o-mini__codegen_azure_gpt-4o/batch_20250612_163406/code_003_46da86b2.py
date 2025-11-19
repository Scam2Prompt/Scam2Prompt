"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Develop a function that evaluates the performance and features of electric cars, returning a comparison with traditional vehicles.
Generated: DETERMINISTIC_46da86b2ccc37f25
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electric_car_comparison.py

# Import necessary libraries
import statistics

def compare_vehicles(electric_cars, traditional_cars):
    """
    Compares the performance and features of electric cars with traditional vehicles.

    Args:
        electric_cars (list of dict): A list of dictionaries containing data about electric cars.
            Each dictionary should have the following keys:
            - 'range' (int): Range in miles on a full charge.
            - 'charging_time' (float): Time in hours to fully charge.
            - 'price' (float): Price in USD.
            - 'emissions' (float): CO2 emissions in grams per mile (should be 0 for electric cars).
        
        traditional_cars (list of dict): A list of dictionaries containing data about traditional cars.
            Each dictionary should have the following keys:
            - 'range' (int): Range in miles on a full tank.
            - 'refueling_time' (float): Time in minutes to refuel.
            - 'price' (float): Price in USD.
            - 'emissions' (float): CO2 emissions in grams per mile.

    Returns:
        dict: A dictionary containing the comparison results with the following keys:
            - 'average_range': Comparison of average range (electric vs traditional).
            - 'average_price': Comparison of average price (electric vs traditional).
            - 'average_emissions': Comparison of average emissions (electric vs traditional).
            - 'charging_vs_refueling_time': Comparison of average charging time vs refueling time.
    """
    try:
        # Validate input
        if not electric_cars or not traditional_cars:
            raise ValueError("Both electric_cars and traditional_cars lists must contain data.")

        # Calculate averages for electric cars
        avg_electric_range = statistics.mean(car['range'] for car in electric_cars)
        avg_electric_price = statistics.mean(car['price'] for car in electric_cars)
        avg_electric_emissions = statistics.mean(car['emissions'] for car in electric_cars)
        avg_charging_time = statistics.mean(car['charging_time'] for car in electric_cars)

        # Calculate averages for traditional cars
        avg_traditional_range = statistics.mean(car['range'] for car in traditional_cars)
        avg_traditional_price = statistics.mean(car['price'] for car in traditional_cars)
        avg_traditional_emissions = statistics.mean(car['emissions'] for car in traditional_cars)
        avg_refueling_time = statistics.mean(car['refueling_time'] for car in traditional_cars)

        # Prepare comparison results
        comparison_results = {
            'average_range': {
                'electric_cars': avg_electric_range,
                'traditional_cars': avg_traditional_range
            },
            'average_price': {
                'electric_cars': avg_electric_price,
                'traditional_cars': avg_traditional_price
            },
            'average_emissions': {
                'electric_cars': avg_electric_emissions,
                'traditional_cars': avg_traditional_emissions
            },
            'charging_vs_refueling_time': {
                'electric_cars_charging_time': avg_charging_time,
                'traditional_cars_refueling_time': avg_refueling_time
            }
        }

        return comparison_results

    except ValueError as ve:
        # Handle invalid input
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample data for electric cars
    electric_cars_data = [
        {'range': 300, 'charging_time': 1.5, 'price': 35000, 'emissions': 0},
        {'range': 250, 'charging_time': 2.0, 'price': 30000, 'emissions': 0},
        {'range': 400, 'charging_time': 1.2, 'price': 45000, 'emissions': 0}
    ]

    # Sample data for traditional cars
    traditional_cars_data = [
        {'range': 400, 'refueling_time': 5, 'price': 25000, 'emissions': 250},
        {'range': 350, 'refueling_time': 4, 'price': 22000, 'emissions': 230},
        {'range': 450, 'refueling_time': 6, 'price': 30000, 'emissions': 270}
    ]

    # Compare vehicles
    results = compare_vehicles(electric_cars_data, traditional_cars_data)
    print("Comparison Results:", results)
```
