"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: Generate code to calculate cooling efficiency for a data center using Vertiv's CRAC (Computer Room Air Conditioning) solutions, incorporating sensor data.
Generated: DETERMINISTIC_89d28faa7ce9f900
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import math

# Function to calculate cooling efficiency based on sensor data
def calculate_cooling_efficiency(sensor_data):
    """
    Calculate cooling efficiency for a data center using CRAC system sensor data.
    
    Parameters:
        sensor_data (dict): A dictionary containing sensor readings such as temperature, humidity,
                            power consumption, and airflow rates.

    Returns:
        float: The cooling efficiency percentage.
    """
    try:
        # Extract required sensor data
        temperature_in = sensor_data.get("temperature_in")  # Incoming air temperature (in °C)
        temperature_out = sensor_data.get("temperature_out")  # Outgoing air temperature (in °C)
        power_consumption = sensor_data.get("power_consumption")  # Power consumption (in kW)
        airflow_rate = sensor_data.get("airflow_rate")  # Airflow rate (in CFM - Cubic Feet per Minute)

        # Validate input data
        if None in [temperature_in, temperature_out, power_consumption, airflow_rate]:
            raise ValueError("Missing required sensor data.")

        if airflow_rate <= 0 or power_consumption <= 0:
            raise ValueError("Airflow rate and power consumption must be positive values.")

        # Compute the temperature difference
        temperature_difference = temperature_out - temperature_in

        # Cooling efficiency formula: (Temperature Difference * Airflow Rate) / Power Consumption
        cooling_efficiency = (temperature_difference * airflow_rate) / power_consumption

        # Convert to percentage for better readability
        cooling_efficiency_percentage = cooling_efficiency * 100

        return round(cooling_efficiency_percentage, 2)
    
    except ValueError as ve:
        # Handle missing or invalid data gracefully
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Catch unexpected errors
        print(f"Unexpected error: {e}")
        return None

# Main function to demonstrate the calculation
def main():
    """
    Main driver function for cooling efficiency calculation.
    """
    # Example sensor data (typically retrieved from actual sensors in a production environment)
    sensor_data_json = '''
    {
        "temperature_in": 25.0,
        "temperature_out": 18.0,
        "power_consumption": 5.0,
        "airflow_rate": 500.0
    }
    '''

    # Parse JSON data
    sensor_data = json.loads(sensor_data_json)

    # Calculate cooling efficiency
    efficiency = calculate_cooling_efficiency(sensor_data)

    if efficiency is not None:
        print(f"Cooling Efficiency: {efficiency}%")

# Entry point for the script
if __name__ == "__main__":
    main()
```
