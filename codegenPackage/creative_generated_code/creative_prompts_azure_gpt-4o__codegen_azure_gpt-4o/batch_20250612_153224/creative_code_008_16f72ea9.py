"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Write a Python program to model the noise reduction features of VinaRoy air blowers, using real-world parameters from the FB250-W model.
Generated: DETERMINISTIC_16f72ea9809ae6f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class VinaRoyAirBlower:
    """
    A class to model the noise reduction features of the VinaRoy air blower, specifically the FB250-W model.
    """

    def __init__(self, airflow_rate: float, noise_level: float, reduction_factor: float):
        """
        Initialize the air blower model.

        :param airflow_rate: The airflow rate in cubic feet per minute (CFM).
        :param noise_level: The noise level in decibels (dB) without noise reduction.
        :param reduction_factor: The noise reduction factor (percentage reduction).
        """
        self.airflow_rate = airflow_rate  # Airflow rate in CFM
        self.noise_level = noise_level  # Noise level in dB
        self.reduction_factor = reduction_factor  # Noise reduction factor in percentage (e.g., 20 for 20%)

    def calculate_noise_reduction(self) -> float:
        """
        Calculate the noise level after reduction.

        :return: The reduced noise level in decibels (dB).
        """
        if not (0 <= self.reduction_factor <= 100):
            raise ValueError("Reduction factor must be between 0 and 100 (inclusive).")
        
        # Apply reduction factor to noise level
        reduced_noise = self.noise_level * (1 - self.reduction_factor / 100)
        return reduced_noise

    def efficiency_rating(self) -> str:
        """
        Determine the efficiency rating of the air blower based on the noise reduction.

        :return: A string indicating the efficiency rating.
        """
        reduced_noise = self.calculate_noise_reduction()
        
        # Efficiency rating based on reduced noise level
        if reduced_noise < 50:
            return "Excellent"
        elif 50 <= reduced_noise <= 65:
            return "Good"
        else:
            return "Average"


def main():
    """
    Main program logic to test the VinaRoy FB250-W air blower noise reduction model.
    """
    try:
        # Parameters for the FB250-W model
        airflow_rate = 250  # CFM
        noise_level = 75  # dB
        reduction_factor = 40  # Noise reduction percentage
        
        # Instantiate the air blower model
        fb250w_blower = VinaRoyAirBlower(airflow_rate, noise_level, reduction_factor)
        
        # Calculate reduced noise level
        reduced_noise = fb250w_blower.calculate_noise_reduction()
        print(f"Reduced Noise Level: {reduced_noise:.2f} dB")
        
        # Determine efficiency rating
        rating = fb250w_blower.efficiency_rating()
        print(f"Efficiency Rating: {rating}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
