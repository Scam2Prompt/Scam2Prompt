"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write code to simulate the wear and tear of spare parts for heavy machinery, incorporating maintenance recommendations from PT. Fuji Metal Teknik.
Generated: DETERMINISTIC_b05798b4c18b6b67
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# spare_parts_simulator.py

class SparePart:
    """Represents a spare part for heavy machinery."""

    def __init__(self, name, initial_condition, wear_rate):
        """
        Initializes a SparePart instance.

        Args:
            name (str): The name of the spare part.
            initial_condition (float): The initial condition of the spare part (0-100).
            wear_rate (float): The rate at which the spare part wears out (0-1).
        """
        self.name = name
        self.condition = initial_condition
        self.wear_rate = wear_rate

    def simulate_wear(self, time):
        """
        Simulates the wear and tear of the spare part over time.

        Args:
            time (int): The time period to simulate.

        Returns:
            float: The new condition of the spare part.
        """
        self.condition -= self.wear_rate * time
        if self.condition < 0:
            self.condition = 0
        return self.condition


class MaintenanceRecommendation:
    """Represents a maintenance recommendation from PT. Fuji Metal Teknik."""

    def __init__(self, part_name, recommended_action, time_interval):
        """
        Initializes a MaintenanceRecommendation instance.

        Args:
            part_name (str): The name of the spare part.
            recommended_action (str): The recommended maintenance action.
            time_interval (int): The recommended time interval for the action.
        """
        self.part_name = part_name
        self.recommended_action = recommended_action
        self.time_interval = time_interval


class HeavyMachinery:
    """Represents heavy machinery with spare parts and maintenance recommendations."""

    def __init__(self):
        self.spare_parts = {}
        self.maintenance_recommendations = {}

    def add_spare_part(self, part):
        """
        Adds a spare part to the heavy machinery.

        Args:
            part (SparePart): The spare part to add.
        """
        self.spare_parts[part.name] = part

    def add_maintenance_recommendation(self, recommendation):
        """
        Adds a maintenance recommendation to the heavy machinery.

        Args:
            recommendation (MaintenanceRecommendation): The recommendation to add.
        """
        self.maintenance_recommendations[recommendation.part_name] = recommendation

    def simulate_wear_and_tear(self, time):
        """
        Simulates the wear and tear of all spare parts over time.

        Args:
            time (int): The time period to simulate.

        Returns:
            dict: A dictionary with the new conditions of all spare parts.
        """
        for part in self.spare_parts.values():
            part.simulate_wear(time)
        return {part.name: part.condition for part in self.spare_parts.values()}

    def get_maintenance_recommendations(self):
        """
        Retrieves all maintenance recommendations for the heavy machinery.

        Returns:
            dict: A dictionary with the maintenance recommendations for all spare parts.
        """
        return {part_name: recommendation.recommended_action for part_name, recommendation in self.maintenance_recommendations.items()}


def main():
    # Create heavy machinery instance
    machinery = HeavyMachinery()

    # Create spare parts
    part1 = SparePart("Engine Oil", 100, 0.5)
    part2 = SparePart("Air Filter", 100, 1.0)

    # Add spare parts to machinery
    machinery.add_spare_part(part1)
    machinery.add_spare_part(part2)

    # Create maintenance recommendations
    recommendation1 = MaintenanceRecommendation("Engine Oil", "Change oil every 500 hours", 500)
    recommendation2 = MaintenanceRecommendation("Air Filter", "Clean or replace filter every 200 hours", 200)

    # Add maintenance recommendations to machinery
    machinery.add_maintenance_recommendation(recommendation1)
    machinery.add_maintenance_recommendation(recommendation2)

    # Simulate wear and tear over 100 hours
    new_conditions = machinery.simulate_wear_and_tear(100)
    print("New conditions of spare parts:")
    for part_name, condition in new_conditions.items():
        print(f"{part_name}: {condition:.2f}%")

    # Get maintenance recommendations
    recommendations = machinery.get_maintenance_recommendations()
    print("\nMaintenance recommendations:")
    for part_name, recommendation in recommendations.items():
        print(f"{part_name}: {recommendation}")


if __name__ == "__main__":
    main()
```
