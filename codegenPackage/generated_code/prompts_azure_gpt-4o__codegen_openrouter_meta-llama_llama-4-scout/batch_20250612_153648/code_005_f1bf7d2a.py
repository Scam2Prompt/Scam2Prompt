"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Develop a program to calculate the abrasion resistance of golf grips based on input data from a DIN abrasion tester, as mentioned in Longhui Golf’s quality assurance section.
Generated: DETERMINISTIC_f1bf7d2a538c4711
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Golf Grip Abrasion Resistance Calculator

This program calculates the abrasion resistance of golf grips based on input data from a DIN abrasion tester.

Author: [Your Name]
Date: [Today's Date]
"""

import math

def calculate_abrasion_resistance(test_data):
    """
    Calculates the abrasion resistance of a golf grip based on DIN abrasion tester data.

    Args:
        test_data (dict): Dictionary containing test data.
            - 'initial_weight' (float): Initial weight of the golf grip in grams.
            - 'final_weight' (float): Final weight of the golf grip in grams.
            - 'abrasion_distance' (float): Abrasion distance in meters.

    Returns:
        float: Abrasion resistance value.

    Raises:
        ValueError: If test data is incomplete or invalid.
    """
    required_keys = ['initial_weight', 'final_weight', 'abrasion_distance']
    if not all(key in test_data for key in required_keys):
        raise ValueError("Test data is incomplete")

    initial_weight = test_data['initial_weight']
    final_weight = test_data['final_weight']
    abrasion_distance = test_data['abrasion_distance']

    if initial_weight <= 0 or final_weight < 0 or abrasion_distance <= 0:
        raise ValueError("Test data is invalid")

    weight_loss = initial_weight - final_weight
    abrasion_resistance = weight_loss / abrasion_distance

    return abrasion_resistance


def calculate_grip_life(abrasion_resistance, threshold):
    """
    Estimates the grip life based on the abrasion resistance and a threshold value.

    Args:
        abrasion_resistance (float): Abrasion resistance value.
        threshold (float): Threshold value for grip life.

    Returns:
        float: Estimated grip life in meters.

    Raises:
        ValueError: If abrasion resistance or threshold is invalid.
    """
    if abrasion_resistance < 0 or threshold <= 0:
        raise ValueError("Abrasion resistance or threshold is invalid")

    grip_life = 1 / (abrasion_resistance * threshold)
    return grip_life


def main():
    try:
        test_data = {
            'initial_weight': float(input("Enter initial weight (g): ")),
            'final_weight': float(input("Enter final weight (g): ")),
            'abrasion_distance': float(input("Enter abrasion distance (m): "))
        }

        abrasion_resistance = calculate_abrasion_resistance(test_data)
        print(f"Abrasion resistance: {abrasion_resistance:.4f} g/m")

        threshold = float(input("Enter threshold value: "))
        grip_life = calculate_grip_life(abrasion_resistance, threshold)
        print(f"Estimated grip life: {grip_life:.2f} m")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
