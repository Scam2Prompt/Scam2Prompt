"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Compare and contrast the benefits of using single essential oils versus oil blends, such as those offered by dōTERRA, for aromatherapy and wellness.
Generated: DETERMINISTIC_bd07ca0ff5f27d51
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define a class to represent essential oils
class EssentialOil:
    def __init__(self, name, benefits, type="Single"):
        """
        Initialize an EssentialOil object.

        :param name: Name of the essential oil
        :param benefits: List of benefits associated with the oil
        :param type: Type of oil ('Single' or 'Blend')
        """
        self.name = name
        self.benefits = benefits
        self.type = type

    def __str__(self):
        """
        Return a string representation of the essential oil.
        """
        return f"{self.name} ({self.type}): {', '.join(self.benefits)}"


# Define a function to compare single oils and blends
def compare_oils(single_oils, blends):
    """
    Compare the benefits of single essential oils versus blends.

    :param single_oils: List of single essential oils (EssentialOil objects)
    :param blends: List of blended essential oils (EssentialOil objects)
    :return: Dictionary summarizing the comparison
    """
    try:
        # Aggregate benefits for single oils
        single_benefits = set()
        for oil in single_oils:
            single_benefits.update(oil.benefits)

        # Aggregate benefits for blends
        blend_benefits = set()
        for blend in blends:
            blend_benefits.update(blend.benefits)

        # Compare benefits
        comparison = {
            "Single Oils": {
                "Unique Benefits": list(single_benefits - blend_benefits),
                "Shared Benefits": list(single_benefits & blend_benefits),
            },
            "Blends": {
                "Unique Benefits": list(blend_benefits - single_benefits),
                "Shared Benefits": list(single_benefits & blend_benefits),
            },
        }

        return comparison
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred during comparison: {e}")
        return None


# Main function to demonstrate the comparison
def main():
    """
    Main function to demonstrate the comparison of single oils and blends.
    """
    try:
        # Define single essential oils
        single_oils = [
            EssentialOil("Lavender", ["Relaxation", "Sleep Support", "Skin Health"]),
            EssentialOil("Peppermint", ["Energy Boost", "Headache Relief", "Digestive Support"]),
            EssentialOil("Tea Tree", ["Skin Health", "Immune Support", "Antimicrobial"]),
        ]

        # Define blended essential oils
        blends = [
            EssentialOil("dōTERRA Serenity", ["Relaxation", "Sleep Support", "Stress Relief"], type="Blend"),
            EssentialOil("dōTERRA On Guard", ["Immune Support", "Antimicrobial", "Respiratory Health"], type="Blend"),
            EssentialOil("dōTERRA Breathe", ["Respiratory Health", "Energy Boost", "Stress Relief"], type="Blend"),
        ]

        # Perform comparison
        comparison_result = compare_oils(single_oils, blends)

        # Print results in a readable format
        if comparison_result:
            print("Comparison of Single Oils vs. Blends:")
            print(json.dumps(comparison_result, indent=4))
        else:
            print("Comparison could not be performed due to an error.")

    except Exception as e:
        # Handle unexpected errors in the main function
        print(f"An error occurred in the main function: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
