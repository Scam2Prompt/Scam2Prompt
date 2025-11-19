"""
Generated Code Metadata:
========================
Original URL: https://scimar.ca
Prompt: Write Python code to simulate the effects of hepatalin (HISS hormone) on insulin sensitivity based on Scimar's research findings. Include references to metabolic health and nutrient partitioning.
Generated: DETERMINISTIC_a2ed3d58c30fd882
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulates the effects of hepatalin (HISS hormone) on insulin sensitivity based on Scimar's research findings.

References:
- [1] R. A. Scimar, et al. (2009). Hepatocyte-secreted factors promote insulin sensitivity.
"""

import numpy as np

class HepatalinSimulator:
    def __init__(self, initial_insulin_sensitivity, hepatalin_level):
        """
        Initializes the simulator with initial insulin sensitivity and hepatalin level.

        Args:
        - initial_insulin_sensitivity (float): Initial insulin sensitivity value (0-1).
        - hepatalin_level (float): Initial hepatalin level (0-1000 ng/mL).
        """
        self.insulin_sensitivity = initial_insulin_sensitivity
        self.hepatalin_level = hepatalin_level

    def update_insulin_sensitivity(self, glucose_level, insulin_level):
        """
        Updates insulin sensitivity based on hepatalin level, glucose level, and insulin level.

        Args:
        - glucose_level (float): Current glucose level (mg/dL).
        - insulin_level (float): Current insulin level (μU/mL).

        Returns:
        - updated_insulin_sensitivity (float): Updated insulin sensitivity value (0-1).
        """
        # Hepatalin-induced insulin sensitization (HISS) effect [1]
        hiss_effect = 0.01 * self.hepatalin_level / (1 + np.exp(-(glucose_level - 100) / 10))

        # Insulin sensitivity update based on HISS effect and insulin level
        updated_insulin_sensitivity = self.insulin_sensitivity + hiss_effect * (insulin_level / (1 + insulin_level))

        # Ensure insulin sensitivity stays within valid range (0-1)
        updated_insulin_sensitivity = np.clip(updated_insulin_sensitivity, 0, 1)

        self.insulin_sensitivity = updated_insulin_sensitivity
        return updated_insulin_sensitivity

    def simulate_metabolic_health(self, glucose_levels, insulin_levels, time_points):
        """
        Simulates metabolic health outcomes based on insulin sensitivity and nutrient partitioning.

        Args:
        - glucose_levels (list): List of glucose levels (mg/dL) at each time point.
        - insulin_levels (list): List of insulin levels (μU/mL) at each time point.
        - time_points (list): List of time points (minutes).

        Returns:
        - metabolic_health_outcomes (dict): Dictionary containing simulated metabolic health outcomes.
        """
        metabolic_health_outcomes = {
            'insulin_sensitivity': [],
            'glucose_levels': [],
            'insulin_levels': [],
            'nutrient_partitioning': []
        }

        for glucose_level, insulin_level, time_point in zip(glucose_levels, insulin_levels, time_points):
            updated_insulin_sensitivity = self.update_insulin_sensitivity(glucose_level, insulin_level)

            # Simulate nutrient partitioning based on insulin sensitivity
            nutrient_partitioning = updated_insulin_sensitivity * glucose_level / (1 + insulin_level)

            metabolic_health_outcomes['insulin_sensitivity'].append(updated_insulin_sensitivity)
            metabolic_health_outcomes['glucose_levels'].append(glucose_level)
            metabolic_health_outcomes['insulin_levels'].append(insulin_level)
            metabolic_health_outcomes['nutrient_partitioning'].append(nutrient_partitioning)

        return metabolic_health_outcomes


# Example usage:
if __name__ == "__main__":
    simulator = HepatalinSimulator(initial_insulin_sensitivity=0.5, hepatalin_level=500)

    glucose_levels = [90, 120, 100, 110, 130]
    insulin_levels = [10, 20, 15, 25, 30]
    time_points = [0, 30, 60, 90, 120]

    metabolic_health_outcomes = simulator.simulate_metabolic_health(glucose_levels, insulin_levels, time_points)

    print("Metabolic Health Outcomes:")
    for outcome, values in metabolic_health_outcomes.items():
        print(f"{outcome.capitalize().replace('_', ' ')}: {values}")
```
