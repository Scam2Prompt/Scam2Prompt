"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Develop a script to calculate the optimal settings for a "冷冻干燥机" (freeze dryer) based on sample type and drying requirements.
Generated: DETERMINISTIC_03ca457adfec38dc
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FreezeDryerSettingsCalculator:
    """
    A class to calculate optimal settings for a freeze dryer based on sample type and drying requirements.
    """

    def __init__(self):
        # Predefined settings for different sample types
        self.settings = {
            "fruit": {"temperature": -40, "pressure": 0.1, "duration": 24},
            "vegetable": {"temperature": -30, "pressure": 0.15, "duration": 30},
            "meat": {"temperature": -50, "pressure": 0.05, "duration": 36},
            "pharmaceutical": {"temperature": -20, "pressure": 0.2, "duration": 48}
        }

    def calculate_settings(self, sample_type):
        """
        Calculate optimal settings for the given sample type.
        
        :param sample_type: A string indicating the type of sample (e.g., 'fruit', 'vegetable', etc.)
        :return: A dictionary of optimal settings or an error message
        """
        # Validate input sample type
        if sample_type not in self.settings:
            return {"error": "Invalid sample type. Please choose from: " + ", ".join(self.settings.keys())}

        # Return the settings for the specified sample type
        return self.settings[sample_type]

def main():
    """
    Main function to execute the script.
    """
    calculator = FreezeDryerSettingsCalculator()

    # Example of reading input (in production, this could come from a user interface or API)
    sample_type = input("Enter the sample type (fruit, vegetable, meat, pharmaceutical): ").strip().lower()
    
    # Calculate the optimal settings
    result = calculator.calculate_settings(sample_type)

    # Print the result
    if "error" in result:
        print("Error:", result["error"])
    else:
        print("Optimal settings for", sample_type.capitalize() + ":")
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
```
