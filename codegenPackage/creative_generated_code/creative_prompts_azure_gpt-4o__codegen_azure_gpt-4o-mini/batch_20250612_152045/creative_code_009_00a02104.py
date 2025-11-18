"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Write a script to calculate the optimal time for snow removal after snowfall, using the guidelines provided by VIRCOMEM for frezare-based snow clearing.
Generated: DETERMINISTIC_00a021047a34c240
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SnowRemovalOptimizer:
    def __init__(self, snowfall_data, temperature_data):
        """
        Initialize the SnowRemovalOptimizer with snowfall and temperature data.
        
        :param snowfall_data: List of tuples containing (date_time, snowfall_amount)
        :param temperature_data: List of tuples containing (date_time, temperature)
        """
        self.snowfall_data = snowfall_data
        self.temperature_data = temperature_data

    def calculate_optimal_removal_time(self):
        """
        Calculate optimal snow removal times based on snowfall and temperature.

        :return: List of tuples containing (snowfall_time, optimal_removal_time)
        """
        optimal_times = []
        
        for snowfall_time, snowfall_amount in self.snowfall_data:
            # Convert strings to datetime objects for comparison
            snowfall_dt = self._parse_datetime(snowfall_time)
            removal_time = self._find_optimal_removal_time(snowfall_dt, snowfall_amount)
            if removal_time:
                optimal_times.append((snowfall_time, removal_time.strftime("%Y-%m-%d %H:%M")))
        
        return optimal_times

    def _find_optimal_removal_time(self, snowfall_dt, snowfall_amount):
        """
        Determine the optimal removal time based on snowfall amount and temperature.

        :param snowfall_dt: Datetime of the snowfall
        :param snowfall_amount: Amount of snowfall in centimeters
        :return: Datetime of the optimal removal time or None if conditions aren't met
        """
        # Check temperatures for the next hours
        for hour in range(1, 5):  # Checking next 4 hours
            check_time = snowfall_dt + datetime.timedelta(hours=hour)
            temperature = self._get_temperature_at_time(check_time)
            
            if temperature is not None:
                # Guidelines based on VIRCOMEM for freezing temperatures
                if temperature < 0:  # If temperature is below freezing
                    if snowfall_amount > 5:  # Significant snowfall
                        return check_time  # Remove after an hour
                    else:
                        continue  # Wait for a higher temperature
                else:
                    return check_time  # Remove when temperature is above freezing
        
        return None  # No optimal time found

    def _get_temperature_at_time(self, check_time):
        """
        Retrieve the temperature at a given datetime.

        :param check_time: Datetime to check for temperature
        :return: Temperature at the given datetime or None if not available
        """
        for time, temp in self.temperature_data:
            if self._parse_datetime(time) == check_time:
                return temp
        return None  # Temperature data not found

    def _parse_datetime(self, date_string):
        """
        Parse a datetime string into a datetime object.

        :param date_string: Datetime string in format '%Y-%m-%d %H:%M'
        :return: Corresponding datetime object
        """
        try:
            return datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')
        except ValueError as e:
            print(f"Error parsing date '{date_string}': {e}")
            return None  # Return None to handle the error gracefully

# Sample data for testing
snowfall_data = [
    ("2023-10-01 08:00", 6),  # 6 cm of snow at 8 AM
    ("2023-10-01 12:00", 3)   # 3 cm of snow at 12 PM
]

temperature_data = [
    ("2023-10-01 09:00", -1),  # -1°C at 9 AM
    ("2023-10-01 10:00", 2),   # 2°C at 10 AM
    ("2023-10-01 11:00", -2),  # -2°C at 11 AM
    ("2023-10-01 12:00", 0)    # 0°C at 12 PM
]

# Instantiate optimizer and calculate removal times
optimizer = SnowRemovalOptimizer(snowfall_data, temperature_data)
optimal_removal_times = optimizer.calculate_optimal_removal_time()

# Output the results
for snowfall_time, removal_time in optimal_removal_times:
    print(f"Optimal removal time for snow at {snowfall_time} is {removal_time}")
```
