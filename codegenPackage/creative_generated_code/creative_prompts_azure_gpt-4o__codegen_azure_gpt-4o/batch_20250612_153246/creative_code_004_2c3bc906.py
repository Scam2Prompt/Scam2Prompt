"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Create a script to compare the UV állóság (UV resistance) of different műanyag ablak (plastic window) profiles, such as Aluplast 70 Prémium and Rehau Euro Design 86.
Generated: DETERMINISTIC_2c3bc906835550f9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to compare UV resistance of different plastic window profiles.

This script uses a predefined dataset of UV resistance values for different
window profiles and compares them to determine the best profile in terms of
UV stability.

Requirements:
- Python 3.x
"""

# Import necessary libraries
import sys

# Define a class for UV resistance comparison
class UVResistanceComparator:
    def __init__(self, profiles):
        """
        Initialize the comparator with a dictionary of profiles.
        
        Args:
            profiles (dict): A dictionary containing window profiles with their UV resistance values.
        """
        self.profiles = profiles

    def compare_profiles(self):
        """
        Compares UV resistance of all profiles and returns the best one.
        
        Returns:
            tuple: The profile name and UV resistance value of the best profile.
        """
        try:
            # Find the profile with the highest UV resistance value
            best_profile = max(self.profiles.items(), key=lambda x: x[1])
            return best_profile
        except ValueError as e:
            raise Exception("Error during comparison: No profiles found.") from e

    def display_profiles(self):
        """
        Displays all the profiles and their UV resistance values.
        """
        print("Available Profiles and UV Resistance:")
        for profile, uv_resistance in self.profiles.items():
            print(f"{profile}: {uv_resistance} (UV Resistance)")

# Define the dataset of window profiles and their UV resistance values
# UV resistance values are hypothetical and should be replaced with actual measurements
window_profiles = {
    "Aluplast 70 Prémium": 85,
    "Rehau Euro Design 86": 90,
    "Veka Softline 82": 80,
    "Gealan S9000": 88
}

def main():
    """
    Main function to execute the script.
    """
    try:
        # Create an instance of the UVResistanceComparator
        comparator = UVResistanceComparator(window_profiles)

        # Display all profiles
        comparator.display_profiles()

        # Compare and find the best profile
        best_profile, uv_resistance = comparator.compare_profiles()

        # Display the result
        print("\nBest Profile in terms of UV Resistance:")
        print(f"{best_profile}: {uv_resistance} (UV Resistance)")
    except Exception as error:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {error}", file=sys.stderr)

# Entry point of the script
if __name__ == "__main__":
    main()
```
