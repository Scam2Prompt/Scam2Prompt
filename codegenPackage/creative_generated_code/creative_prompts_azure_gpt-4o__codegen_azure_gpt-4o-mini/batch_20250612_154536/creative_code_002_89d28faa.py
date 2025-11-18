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
import numpy as np
import pandas as pd

class CoolingEfficiencyCalculator:
    """
    A class to calculate the cooling efficiency of a data center using Vertiv's CRAC solutions.
    """

    def __init__(self, sensor_data: pd.DataFrame):
        """
        Initializes the CoolingEfficiencyCalculator with sensor data.
        
        Parameters:
            sensor_data (pd.DataFrame): DataFrame containing sensor readings with columns 
                                         ['temperature_in', 'temperature_out', 'power_consumed'].
        """
        self.validate_sensor_data(sensor_data)
        self.sensor_data = sensor_data

    def validate_sensor_data(self, sensor_data: pd.DataFrame):
        """
        Validates the input sensor data.
        
        Parameters:
            sensor_data (pd.DataFrame): DataFrame to validate.
        
        Raises:
            ValueError: If the DataFrame does not contain the required columns or has invalid data types.
        """
        required_columns = ['temperature_in', 'temperature_out', 'power_consumed']
        for column in required_columns:
            if column not in sensor_data.columns:
                raise ValueError(f"Missing required column: {column}")
            if not np.issubdtype(sensor_data[column].dtype, np.number):
                raise ValueError(f"Column {column} must be numeric.")

    def calculate_cooling_efficiency(self) -> pd.Series:
        """
        Calculates the cooling efficiency for each row of sensor data.
        
        Returns:
            pd.Series: A series containing the calculated cooling efficiency for each entry.
        """
        # Calculate temperature difference
        temperature_difference = self.sensor_data['temperature_out'] - self.sensor_data['temperature_in']
        # Apply the formula for cooling efficiency: EER = Temperature Difference / Power Consumed
        self.sensor_data['cooling_efficiency'] = temperature_difference / self.sensor_data['power_consumed']
        
        # Handle division by zero and invalid values
        self.sensor_data['cooling_efficiency'].replace([np.inf, -np.inf], np.nan, inplace=True)
        self.sensor_data['cooling_efficiency'].fillna(0, inplace=True)
        
        return self.sensor_data['cooling_efficiency']

def main():
    # Example sensor data
    data = {
        'temperature_in': [20, 22, 19],
        'temperature_out': [30, 33, 28],
        'power_consumed': [700, 800, 750]
    }
    
    # Create a DataFrame from the example data
    sensor_data_df = pd.DataFrame(data)

    try:
        # Initialize the cooling efficiency calculator
        calculator = CoolingEfficiencyCalculator(sensor_data_df)

        # Calculate cooling efficiency
        efficiency = calculator.calculate_cooling_efficiency()

        # Display results
        print("Cooling Efficiency Results:")
        print(efficiency)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
