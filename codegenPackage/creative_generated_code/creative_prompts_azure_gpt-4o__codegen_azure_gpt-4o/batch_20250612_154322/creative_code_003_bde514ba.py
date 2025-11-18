"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Create a program that compares Apple M1 and M2 chipsets for MacBooks and iPads, using the use cases and recommendations outlined in EcoSwap's blog post.
Generated: DETERMINISTIC_bde514ba0ccbdd4d
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to compare Apple M1 and M2 chipsets for MacBooks and iPads.
The program uses data from EcoSwap's blog post to provide use cases and recommendations
for users deciding between the two chipsets.

Requirements:
- Comparison based on performance, energy efficiency, and price-to-value ratio.
- Different recommendations for MacBooks and iPads.
"""

# Import necessary modules
import json


class ChipsetComparison:
    """
    Class to compare M1 and M2 chipsets and provide use case recommendations.
    """

    def __init__(self):
        # Initialize comparison data (mock data from EcoSwap's blog post)
        self.data = {
            "macbook": {
                "M1": {
                    "performance_score": 8,
                    "energy_efficiency_score": 9,
                    "price_to_value_score": 9
                },
                "M2": {
                    "performance_score": 10,
                    "energy_efficiency_score": 8,
                    "price_to_value_score": 8
                }
            },
            "ipad": {
                "M1": {
                    "performance_score": 7,
                    "energy_efficiency_score": 9,
                    "price_to_value_score": 9
                },
                "M2": {
                    "performance_score": 9,
                    "energy_efficiency_score": 8,
                    "price_to_value_score": 7
                }
            }
        }

    def compare_chipsets(self, device_type):
        """
        Compare M1 and M2 chipsets based on the device type (macbook or ipad).
        
        Args:
            device_type (str): The type of device, either 'macbook' or 'ipad'.
        
        Returns:
            dict: Comparison results and recommendations.
        """
        if device_type not in self.data:
            raise ValueError("Invalid device type. Please choose 'macbook' or 'ipad'.")

        m1 = self.data[device_type]["M1"]
        m2 = self.data[device_type]["M2"]

        # Calculate total scores for each chipset
        m1_total_score = sum(m1.values())
        m2_total_score = sum(m2.values())

        # Generate recommendations based on total scores
        if m1_total_score > m2_total_score:
            recommendation = f"For {device_type}, M1 is recommended due to its overall better scores."
        else:
            recommendation = f"For {device_type}, M2 is recommended due to its higher performance."

        return {
            "device_type": device_type,
            "M1": m1,
            "M2": m2,
            "recommendation": recommendation
        }

    def export_to_json(self, comparison_result, filename="comparison_result.json"):
        """
        Export comparison results to a JSON file.
        
        Args:
            comparison_result (dict): The comparison results to save.
            filename (str): Name of the output JSON file.
        """
        try:
            with open(filename, "w") as file:
                json.dump(comparison_result, file, indent=4)
            print(f"Comparison results successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving results to file: {e}")


# Main function
def main():
    """
    Main entry point for the program.
    """
    try:
        # Create an instance of ChipsetComparison
        comparator = ChipsetComparison()

        # Prompt user for device type
        device_type = input("Enter device type ('macbook' or 'ipad'): ").strip().lower()

        # Perform comparison
        results = comparator.compare_chipsets(device_type)

        # Display results
        print("\nComparison Results:")
        print(json.dumps(results, indent=4))

        # Export results to a JSON file
        comparator.export_to_json(results)

    except ValueError as ve:
        # Handle invalid device type input
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
```
