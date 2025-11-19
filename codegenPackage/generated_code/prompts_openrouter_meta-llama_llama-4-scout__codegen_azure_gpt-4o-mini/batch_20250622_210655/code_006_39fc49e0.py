"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Write a Python program to generate custom sewing patterns based on user input for garment type, fabric type, and measurements."
Generated: DETERMINISTIC_39fc49e0d4435d53
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class SewingPatternGenerator:
    def __init__(self):
        """Initialize the SewingPatternGenerator with default values."""
        self.patterns = {
            "shirt": {"fabric": ["cotton", "linen", "polyester"], "measurements": ["chest", "waist", "length"]},
            "pants": {"fabric": ["denim", "cotton", "wool"], "measurements": ["waist", "hip", "inseam"]},
            "dress": {"fabric": ["silk", "cotton", "satin"], "measurements": ["bust", "waist", "hip", "length"]}
        }

    def get_user_input(self):
        """Get garment type, fabric type, and measurements from the user."""
        garment_type = input("Enter garment type (shirt, pants, dress): ").strip().lower()
        if garment_type not in self.patterns:
            raise ValueError("Invalid garment type. Please choose from: shirt, pants, dress.")

        fabric_type = input(f"Enter fabric type for {garment_type} ({', '.join(self.patterns[garment_type]['fabric'])}): ").strip().lower()
        if fabric_type not in self.patterns[garment_type]['fabric']:
            raise ValueError(f"Invalid fabric type. Please choose from: {', '.join(self.patterns[garment_type]['fabric'])}.")

        measurements = {}
        for measurement in self.patterns[garment_type]['measurements']:
            value = input(f"Enter your {measurement} measurement: ")
            try:
                measurements[measurement] = float(value)
            except ValueError:
                raise ValueError(f"Invalid measurement for {measurement}. Please enter a numeric value.")

        return garment_type, fabric_type, measurements

    def generate_pattern(self, garment_type, fabric_type, measurements):
        """Generate a sewing pattern based on user input."""
        pattern = {
            "garment_type": garment_type,
            "fabric_type": fabric_type,
            "measurements": measurements,
            "pattern_details": f"{garment_type.capitalize()} pattern created with {fabric_type} fabric."
        }
        return pattern

    def save_pattern(self, pattern):
        """Save the generated pattern to a JSON file."""
        filename = f"{pattern['garment_type']}_pattern.json"
        try:
            with open(filename, 'w') as file:
                json.dump(pattern, file, indent=4)
            print(f"Pattern saved successfully as {filename}.")
        except IOError as e:
            print(f"Error saving pattern: {e}")

    def run(self):
        """Run the sewing pattern generator."""
        try:
            garment_type, fabric_type, measurements = self.get_user_input()
            pattern = self.generate_pattern(garment_type, fabric_type, measurements)
            self.save_pattern(pattern)
        except ValueError as e:
            print(f"Input error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    generator = SewingPatternGenerator()
    generator.run()
```
