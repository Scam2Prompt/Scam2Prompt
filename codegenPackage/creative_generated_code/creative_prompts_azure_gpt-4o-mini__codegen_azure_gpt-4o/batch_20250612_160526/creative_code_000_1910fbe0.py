"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekrollindustrial.com.br
Prompt: Generate a code snippet for a system that optimizes the process of lifting and transporting heavy loads, focusing on ergonomic safety and efficiency as described by Tekroll Industrial.
Generated: DETERMINISTIC_1910fbe0a2d1b2f6
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class LoadOptimizer:
    """
    A system to optimize the process of lifting and transporting heavy loads,
    focusing on ergonomic safety and efficiency.
    """

    def __init__(self, max_weight_capacity, max_distance):
        """
        Initialize the LoadOptimizer instance.

        :param max_weight_capacity: Maximum weight capacity the system can handle (kg).
        :param max_distance: Maximum transport distance the system is designed for (meters).
        """
        self.max_weight_capacity = max_weight_capacity
        self.max_distance = max_distance

    def calculate_optimal_lift_angle(self, load_weight):
        """
        Calculate the optimal lift angle for ergonomic safety.

        :param load_weight: Weight of the load being lifted (kg).
        :return: Optimal angle in degrees.
        """
        if load_weight <= 0 or load_weight > self.max_weight_capacity:
            raise ValueError(f"Load weight must be within 1 and {self.max_weight_capacity} kg.")

        # Use a simplified formula based on ergonomic principles (example: proportional to load weight).
        optimal_angle = max(45 - (load_weight / self.max_weight_capacity) * 20, 15)
        return optimal_angle

    def calculate_transport_efficiency(self, load_weight, distance):
        """
        Calculate transport efficiency based on load weight and distance.

        :param load_weight: Weight of the load being transported (kg).
        :param distance: Distance to transport the load (meters).
        :return: Efficiency score (higher is better).
        """
        if load_weight <= 0 or load_weight > self.max_weight_capacity:
            raise ValueError(f"Load weight must be within 1 and {self.max_weight_capacity} kg.")
        if distance <= 0 or distance > self.max_distance:
            raise ValueError(f"Distance must be within 1 and {self.max_distance} meters.")

        # Efficiency calculation: inversely proportional to weight and distance.
        efficiency_score = (self.max_weight_capacity / load_weight) * (self.max_distance / distance)
        return round(efficiency_score, 2)

    def get_safety_recommendations(self, load_weight):
        """
        Provide safety recommendations based on the load weight.

        :param load_weight: Weight of the load being lifted (kg).
        :return: List of safety recommendations.
        """
        if load_weight <= 0 or load_weight > self.max_weight_capacity:
            raise ValueError(f"Load weight must be within 1 and {self.max_weight_capacity} kg.")

        recommendations = [
            "Use proper lifting techniques to avoid strain.",
            "Wear appropriate protective gear (e.g., gloves, steel-toed boots)."
        ]

        # Add more recommendations for heavier loads.
        if load_weight > self.max_weight_capacity * 0.75:
            recommendations.append("Consider using mechanical assistance (e.g., forklifts, hoists).")
            recommendations.append("Work in teams to distribute the load.")

        return recommendations


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the system with max capacity of 100 kg and max distance of 500 meters.
        optimizer = LoadOptimizer(max_weight_capacity=100, max_distance=500)

        # Sample calculations.
        load_weight = 60  # kg
        distance = 150  # meters

        optimal_lift_angle = optimizer.calculate_optimal_lift_angle(load_weight)
        print(f"Optimal lift angle: {optimal_lift_angle}°")

        efficiency_score = optimizer.calculate_transport_efficiency(load_weight, distance)
        print(f"Transport efficiency score: {efficiency_score}")

        safety_tips = optimizer.get_safety_recommendations(load_weight)
        print("Safety recommendations:")
        for tip in safety_tips:
            print(f"- {tip}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
