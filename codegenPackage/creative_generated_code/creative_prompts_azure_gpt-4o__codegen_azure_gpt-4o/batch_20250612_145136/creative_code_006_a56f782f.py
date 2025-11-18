"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bharatnews18.com
Prompt: Write code to design a smartphone comparison tool that highlights features such as "Dual camera," "Clean UI," and "Android 12," as described for the Nothing Phone (1) on BharatNews18.
Generated: DETERMINISTIC_a56f782f7ab92dd2
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Smartphone:
    """
    A class to represent a smartphone and its features.
    """
    def __init__(self, name, features):
        """
        Initialize the Smartphone object.

        :param name: str - Name of the smartphone
        :param features: list - List of features for the smartphone
        """
        self.name = name
        self.features = features

    def compare_features(self, other_smartphone):
        """
        Compare features with another smartphone.

        :param other_smartphone: Smartphone - Another smartphone object to compare with
        :return: dict - A dictionary highlighting differences in features
        """
        common_features = set(self.features).intersection(set(other_smartphone.features))
        unique_to_self = set(self.features) - common_features
        unique_to_other = set(other_smartphone.features) - common_features

        return {
            "common_features": list(common_features),
            "unique_to_self": list(unique_to_self),
            "unique_to_other": list(unique_to_other)
        }

    def display_features(self):
        """
        Display the features of the smartphone in a readable format.

        :return: str - Formatted string representation of the features
        """
        return f"{self.name} Features:\n- " + "\n- ".join(self.features)


def main():
    """
    Main function to demonstrate the smartphone comparison tool.
    """
    try:
        # Create Smartphone objects
        nothing_phone_1 = Smartphone(
            "Nothing Phone (1)",
            ["Dual camera", "Clean UI", "Android 12"]
        )

        example_phone = Smartphone(
            "Example Phone X",
            ["Triple camera", "Heavy UI", "Android 11"]
        )

        # Display features of each smartphone
        print(nothing_phone_1.display_features())
        print(example_phone.display_features())

        # Compare features of the two smartphones
        comparison_result = nothing_phone_1.compare_features(example_phone)

        # Display comparison results
        print("\nFeature Comparison:")
        print("Common Features:", ", ".join(comparison_result["common_features"]))
        print(f"Features unique to {nothing_phone_1.name}:",
              ", ".join(comparison_result["unique_to_self"]))
        print(f"Features unique to {example_phone.name}:",
              ", ".join(comparison_result["unique_to_other"]))
    
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
