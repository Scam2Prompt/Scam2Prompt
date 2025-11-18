"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Write a function to calculate the optimal cement type for infrastructure projects, referencing the specific brands (Twiga Super, Twiga Jenga) and their properties provided by TPCPLC.
Generated: DETERMINISTIC_e18952fc0224efbb
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CementType:
    def __init__(self, name, compressive_strength, setting_time, cost):
        """
        Initializes a CementType object with the specified properties.
        
        :param name: Name of the cement type (e.g., "Twiga Super", "Twiga Jenga")
        :param compressive_strength: Compressive strength in MPa
        :param setting_time: Setting time in minutes
        :param cost: Cost per metric ton
        """
        self.name = name
        self.compressive_strength = compressive_strength
        self.setting_time = setting_time
        self.cost = cost

    def __repr__(self):
        return f"{self.name}(Strength: {self.compressive_strength}, Setting Time: {self.setting_time}, Cost: {self.cost})"


def optimal_cement_type(required_strength, max_setting_time, budget):
    """
    Determines the optimal cement type based on required compressive strength, 
    maximum allowable setting time, and budget constraints.

    :param required_strength: Minimum required compressive strength in MPa
    :param max_setting_time: Maximum allowable setting time in minutes
    :param budget: Maximum budget in monetary units
    :return: Optimal CementType or None if none meet the criteria
    """
    # Predefined cement types from TPCPLC
    cements = [
        CementType("Twiga Super", compressive_strength=42.5, setting_time=30, cost=100),
        CementType("Twiga Jenga", compressive_strength=32.5, setting_time=60, cost=80),
    ]

    optimal_cement = None

    for cement in cements:
        if (cement.compressive_strength >= required_strength and
                cement.setting_time <= max_setting_time and
                cement.cost <= budget):
            if optimal_cement is None or cement.cost < optimal_cement.cost:
                optimal_cement = cement

    return optimal_cement


# Example usage with error handling
if __name__ == "__main__":
    try:
        required_strength = 35  # MPa
        max_setting_time = 45   # minutes
        budget = 90             # monetary units

        result = optimal_cement_type(required_strength, max_setting_time, budget)

        if result:
            print(f"Optimal Cement Type: {result}")
        else:
            print("No suitable cement type found.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
