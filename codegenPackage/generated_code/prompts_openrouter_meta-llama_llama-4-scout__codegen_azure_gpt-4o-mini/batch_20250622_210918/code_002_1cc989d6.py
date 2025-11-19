"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: "Recommend a suitable EV charger station for a commercial building in Cambodia, specifying the required power output and charging capacity."
Generated: DETERMINISTIC_1cc989d6ef6ce709
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EVCharger:
    """
    A class to represent an Electric Vehicle (EV) charger station.
    
    Attributes:
        location (str): The location of the charger station.
        power_output (float): The power output of the charger in kW.
        charging_capacity (float): The charging capacity in kWh.
    """

    def __init__(self, location: str, power_output: float, charging_capacity: float):
        """
        Initializes the EVCharger with location, power output, and charging capacity.
        
        Args:
            location (str): The location of the charger station.
            power_output (float): The power output of the charger in kW.
            charging_capacity (float): The charging capacity in kWh.
        """
        self.location = location
        self.power_output = power_output
        self.charging_capacity = charging_capacity

    def recommend_charger(self):
        """
        Recommends a suitable EV charger based on power output and charging capacity.
        
        Returns:
            str: A recommendation message with charger details.
        """
        if self.power_output < 7.2:
            return f"Recommended Charger for {self.location}: Level 1 Charger (up to 7.2 kW)."
        elif 7.2 <= self.power_output < 22:
            return f"Recommended Charger for {self.location}: Level 2 Charger (7.2 kW to 22 kW)."
        elif self.power_output >= 22:
            return f"Recommended Charger for {self.location}: DC Fast Charger (above 22 kW)."
        else:
            return "Invalid power output."

def main():
    """
    Main function to execute the EV charger recommendation.
    """
    try:
        # Example parameters for a commercial building in Cambodia
        location = "Commercial Building, Phnom Penh"
        power_output = 22.0  # kW
        charging_capacity = 50.0  # kWh

        # Create an instance of EVCharger
        charger = EVCharger(location, power_output, charging_capacity)

        # Get the recommendation
        recommendation = charger.recommend_charger()
        print(recommendation)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
