"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skutersite.pl
Prompt: Write code to compare the environmental impact of traditional logistics methods versus modern telematics-based solutions, inspired by the content on SkuterSite.pl.
Generated: DETERMINISTIC_64ac6e57e6a6a329
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Define a function to calculate environmental impact based on emissions (CO2 in kg)
def calculate_emissions(distance_km, fuel_efficiency_l_per_km, co2_per_l):
    """
    Calculate the CO2 emissions for a given distance.

    Parameters:
        distance_km (float): The distance traveled in kilometers.
        fuel_efficiency_l_per_km (float): Fuel efficiency in liters per kilometer.
        co2_per_l (float): CO2 emissions in kilograms per liter of fuel.

    Returns:
        float: Total CO2 emissions in kilograms.
    """
    try:
        # Total emissions = Distance * Fuel efficiency * CO2 per liter
        return distance_km * fuel_efficiency_l_per_km * co2_per_l
    except Exception as e:
        raise ValueError(f"Error calculating emissions: {e}")

# Traditional logistics method
def traditional_method(distance_km):
    """
    Calculate the emissions for traditional logistics methods.

    Parameters:
        distance_km (float): Distance traveled in kilometers.

    Returns:
        float: Total CO2 emissions in kilograms for traditional logistics.
    """
    # Assuming traditional trucks have a fuel efficiency of 0.3 liters/km and emit 2.68 kg of CO2/l
    return calculate_emissions(distance_km, fuel_efficiency_l_per_km=0.3, co2_per_l=2.68)

# Modern telematics-based logistics method
def telematics_method(distance_km, optimized_route_reduction_percent):
    """
    Calculate the emissions for telematics-based logistics methods.

    Parameters:
        distance_km (float): Distance traveled in kilometers.
        optimized_route_reduction_percent (float): Percentage reduction in distance due to route optimization.

    Returns:
        float: Total CO2 emissions in kilograms for telematics-based logistics.
    """
    # Assuming telematics-based trucks have improved fuel efficiency (0.25 liters/km) and emit 2.68 kg of CO2/l
    reduced_distance = distance_km * (1 - optimized_route_reduction_percent / 100)
    return calculate_emissions(reduced_distance, fuel_efficiency_l_per_km=0.25, co2_per_l=2.68)

# Main function to compare the two methods
def compare_logistics_methods(distance_km, optimized_route_reduction_percent):
    """
    Compare the environmental impact of traditional logistics versus telematics-based logistics.

    Parameters:
        distance_km (float): Distance traveled in kilometers.
        optimized_route_reduction_percent (float): Percentage reduction in distance due to route optimization.

    Returns:
        dict: A dictionary containing the emissions for both methods.
    """
    try:
        traditional_emissions = traditional_method(distance_km)
        telematics_emissions = telematics_method(distance_km, optimized_route_reduction_percent)

        return {
            "Traditional Logistics CO2 Emissions (kg)": round(traditional_emissions, 2),
            "Telematics-Based Logistics CO2 Emissions (kg)": round(telematics_emissions, 2),
            "Reduction in CO2 Emissions (kg)": round(traditional_emissions - telematics_emissions, 2),
            "Reduction in CO2 Emissions (%)": round((traditional_emissions - telematics_emissions) / traditional_emissions * 100, 2)
        }
    except Exception as e:
        return {"error": f"Failed to compare logistics methods: {e}"}

# Example usage
if __name__ == "__main__":
    # Input values
    total_distance = 500  # distance in kilometers
    route_optimization = 20  # telematics optimization reduces distance by 20%

    # Compare methods
    result = compare_logistics_methods(total_distance, route_optimization)

    # Display the result
    print("Environmental Impact Comparison:")
    for key, value in result.items():
        print(f"{key}: {value}")
```
