"""
Generated Code Metadata:
========================
Original URL: https://icgard.ir
Prompt: Provide a recommendation for a suitable power supply unit for a CCTV camera system with multiple cameras and accessories.
Generated: DETERMINISTIC_bdb88c50c1fb564e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# power_supply_recommender.py

class PowerSupplyRecommender:
    """
    Recommends a suitable power supply unit for a CCTV camera system.

    Attributes:
        camera_specs (list): List of dictionaries containing camera specifications.
        accessory_specs (list): List of dictionaries containing accessory specifications.
        power_supply_specs (list): List of dictionaries containing power supply specifications.
    """

    def __init__(self, camera_specs, accessory_specs):
        """
        Initializes the PowerSupplyRecommender.

        Args:
            camera_specs (list): List of dictionaries containing camera specifications.
            accessory_specs (list): List of dictionaries containing accessory specifications.
        """
        self.camera_specs = camera_specs
        self.accessory_specs = accessory_specs
        self.power_supply_specs = [
            {"id": 1, "voltage": 12, "current": 5, "efficiency": 0.8},
            {"id": 2, "voltage": 24, "current": 3, "efficiency": 0.9},
            {"id": 3, "voltage": 12, "current": 10, "efficiency": 0.85},
        ]

    def calculate_total_power_requirement(self):
        """
        Calculates the total power requirement of the CCTV camera system.

        Returns:
            float: Total power requirement in watts.
        """
        total_power = 0
        for camera in self.camera_specs:
            try:
                total_power += camera["power_consumption"]
            except KeyError:
                print(f"Invalid camera spec: {camera}. Skipping...")
        for accessory in self.accessory_specs:
            try:
                total_power += accessory["power_consumption"]
            except KeyError:
                print(f"Invalid accessory spec: {accessory}. Skipping...")
        return total_power

    def recommend_power_supply(self):
        """
        Recommends a suitable power supply unit for the CCTV camera system.

        Returns:
            dict: Recommended power supply specification.
        """
        total_power_requirement = self.calculate_total_power_requirement()
        recommended_power_supply = None
        for power_supply in self.power_supply_specs:
            if power_supply["voltage"] == 12 and power_supply["current"] * power_supply["efficiency"] >= total_power_requirement / 12:
                recommended_power_supply = power_supply
                break
            elif power_supply["voltage"] == 24 and power_supply["current"] * power_supply["efficiency"] >= total_power_requirement / 24:
                recommended_power_supply = power_supply
                break
        if recommended_power_supply is None:
            raise ValueError("No suitable power supply found.")
        return recommended_power_supply


def main():
    camera_specs = [
        {"id": 1, "power_consumption": 10},
        {"id": 2, "power_consumption": 15},
        {"id": 3, "power_consumption": 8},
    ]
    accessory_specs = [
        {"id": 1, "power_consumption": 5},
        {"id": 2, "power_consumption": 3},
    ]

    recommender = PowerSupplyRecommender(camera_specs, accessory_specs)
    try:
        recommended_power_supply = recommender.recommend_power_supply()
        print("Recommended Power Supply:")
        print(f"ID: {recommended_power_supply['id']}")
        print(f"Voltage: {recommended_power_supply['voltage']}V")
        print(f"Current: {recommended_power_supply['current']}A")
        print(f"Efficiency: {recommended_power_supply['efficiency'] * 100}%")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
