"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Create a script to compare the UV állóság (UV resistance) of different műanyag ablak (plastic window) profiles, such as Aluplast 70 Prémium and Rehau Euro Design 86.
Generated: DETERMINISTIC_2c3bc906835550f9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class WindowProfile:
    """
    A class to represent a plastic window profile and its UV resistance.
    """

    def __init__(self, name, uv_resistance):
        """
        Initializes a new WindowProfile instance.

        :param name: str - The name of the window profile.
        :param uv_resistance: float - The UV resistance value of the profile.
        """
        self.name = name
        self.uv_resistance = uv_resistance

    def __repr__(self):
        return f"{self.name}: {self.uv_resistance} UV resistance"

def compare_uv_resistance(profiles):
    """
    Compares the UV resistance of different window profiles.

    :param profiles: list - A list of WindowProfile instances.
    :return: str - A summary of the comparison.
    """
    if not profiles:
        raise ValueError("The profiles list cannot be empty.")

    # Sort profiles by UV resistance in descending order
    sorted_profiles = sorted(profiles, key=lambda p: p.uv_resistance, reverse=True)

    # Create a summary of the comparison
    comparison_summary = "UV Resistance Comparison:\n"
    for profile in sorted_profiles:
        comparison_summary += f"{profile}\n"

    return comparison_summary

def main():
    """
    Main function to execute the UV resistance comparison.
    """
    try:
        # Define the window profiles with their UV resistance values
        profiles = [
            WindowProfile("Aluplast 70 Prémium", 8.5),
            WindowProfile("Rehau Euro Design 86", 9.0),
            WindowProfile("Veka Softline 82", 8.0),
            WindowProfile("Schüco LivIng", 9.5)
        ]

        # Compare the UV resistance of the profiles
        result = compare_uv_resistance(profiles)
        print(result)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
