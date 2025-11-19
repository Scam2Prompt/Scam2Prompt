"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Write code to simulate the effects of Relivo’s ingredients (e.g., collagen, magnesium, probiotics) on various health metrics such as energy levels, immunity, and gut health.
Generated: DETERMINISTIC_934246863fc27166
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# relivo_simulator.py

class HealthMetric:
    """Represents a health metric with a value and a range of normal values."""

    def __init__(self, name, value, min_normal, max_normal):
        """
        Initializes a HealthMetric.

        Args:
            name (str): The name of the health metric.
            value (float): The current value of the health metric.
            min_normal (float): The minimum normal value of the health metric.
            max_normal (float): The maximum normal value of the health metric.
        """
        self.name = name
        self.value = value
        self.min_normal = min_normal
        self.max_normal = max_normal

    def is_normal(self):
        """Checks if the health metric value is within the normal range."""
        return self.min_normal <= self.value <= self.max_normal

    def __str__(self):
        return f"{self.name}: {self.value} ({self.min_normal}-{self.max_normal})"


class Ingredient:
    """Represents an ingredient with effects on health metrics."""

    def __init__(self, name):
        """
        Initializes an Ingredient.

        Args:
            name (str): The name of the ingredient.
        """
        self.name = name
        self.effects = {}

    def add_effect(self, health_metric_name, change):
        """
        Adds an effect on a health metric.

        Args:
            health_metric_name (str): The name of the health metric.
            change (float): The change in the health metric value.
        """
        self.effects[health_metric_name] = change

    def apply_effects(self, health_metrics):
        """
        Applies the effects of the ingredient on health metrics.

        Args:
            health_metrics (dict): A dictionary of health metrics.

        Returns:
            dict: The updated health metrics.
        """
        updated_health_metrics = health_metrics.copy()
        for health_metric_name, change in self.effects.items():
            if health_metric_name in updated_health_metrics:
                updated_health_metrics[health_metric_name].value += change
        return updated_health_metrics


class RelivoSimulator:
    """Simulates the effects of Relivo's ingredients on health metrics."""

    def __init__(self):
        self.ingredients = {}
        self.health_metrics = {
            "energy_levels": HealthMetric("Energy Levels", 50, 0, 100),
            "immunity": HealthMetric("Immunity", 50, 0, 100),
            "gut_health": HealthMetric("Gut Health", 50, 0, 100),
        }

    def add_ingredient(self, ingredient):
        """
        Adds an ingredient to the simulator.

        Args:
            ingredient (Ingredient): The ingredient to add.
        """
        self.ingredients[ingredient.name] = ingredient

    def simulate(self, ingredient_name):
        """
        Simulates the effects of an ingredient on health metrics.

        Args:
            ingredient_name (str): The name of the ingredient.

        Returns:
            dict: The updated health metrics.
        """
        if ingredient_name in self.ingredients:
            ingredient = self.ingredients[ingredient_name]
            updated_health_metrics = ingredient.apply_effects(self.health_metrics)
            return updated_health_metrics
        else:
            raise ValueError(f"Ingredient '{ingredient_name}' not found.")

    def print_health_metrics(self, health_metrics):
        """
        Prints the health metrics.

        Args:
            health_metrics (dict): A dictionary of health metrics.
        """
        for health_metric in health_metrics.values():
            print(health_metric)


def main():
    simulator = RelivoSimulator()

    # Create ingredients
    collagen = Ingredient("Collagen")
    collagen.add_effect("energy_levels", 10)
    collagen.add_effect("gut_health", 20)

    magnesium = Ingredient("Magnesium")
    magnesium.add_effect("energy_levels", 15)
    magnesium.add_effect("immunity", 5)

    probiotics = Ingredient("Probiotics")
    probiotics.add_effect("gut_health", 30)
    probiotics.add_effect("immunity", 10)

    # Add ingredients to simulator
    simulator.add_ingredient(collagen)
    simulator.add_ingredient(magnesium)
    simulator.add_ingredient(probiotics)

    # Print initial health metrics
    print("Initial Health Metrics:")
    simulator.print_health_metrics(simulator.health_metrics)

    # Simulate effects of ingredients
    print("\nSimulating effects of Collagen:")
    updated_health_metrics = simulator.simulate("Collagen")
    simulator.print_health_metrics(updated_health_metrics)

    print("\nSimulating effects of Magnesium:")
    updated_health_metrics = simulator.simulate("Magnesium")
    simulator.print_health_metrics(updated_health_metrics)

    print("\nSimulating effects of Probiotics:")
    updated_health_metrics = simulator.simulate("Probiotics")
    simulator.print_health_metrics(updated_health_metrics)


if __name__ == "__main__":
    main()
```
