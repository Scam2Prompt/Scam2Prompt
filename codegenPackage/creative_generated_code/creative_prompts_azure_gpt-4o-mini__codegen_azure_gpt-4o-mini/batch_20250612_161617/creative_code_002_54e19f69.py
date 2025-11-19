"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munakalati.org
Prompt: What are the key features of Muna Kalati's capacity development programs for children's book professionals?
Generated: DETERMINISTIC_54e19f691ac41242
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CapacityDevelopmentProgram:
    """
    Represents a capacity development program for children's book professionals.
    """

    def __init__(self, name, features):
        """
        Initializes a new capacity development program.

        Args:
            name (str): The name of the program.
            features (list): A list of key features of the program.
        """
        self.name = name
        self.features = features

    def display_features(self):
        """
        Displays the key features of the program.
        """
        print(f"Key features of the program '{self.name}':")
        for feature in self.features:
            print(f"- {feature}")

    def add_feature(self, feature):
        """
        Adds a new feature to the program.

        Args:
            feature (str): The feature to add.
        """
        if feature and isinstance(feature, str):
            self.features.append(feature)
        else:
            raise ValueError("Feature must be a non-empty string.")

    def remove_feature(self, feature):
        """
        Removes a feature from the program.

        Args:
            feature (str): The feature to remove.

        Raises:
            ValueError: If the feature is not found in the list.
        """
        try:
            self.features.remove(feature)
        except ValueError:
            raise ValueError(f"Feature '{feature}' not found in the program.")

def main():
    """
    Main function to create and manage capacity development programs.
    """
    try:
        # Example features for Muna Kalati's capacity development program
        muna_kalati_features = [
            "Workshops on writing children's literature",
            "Training on illustration techniques",
            "Networking opportunities for authors and illustrators",
            "Mentorship programs with established professionals",
            "Access to publishing resources and guidelines"
        ]

        # Create an instance of the capacity development program
        muna_program = CapacityDevelopmentProgram("Muna Kalati Program", muna_kalati_features)

        # Display the features of the program
        muna_program.display_features()

        # Adding a new feature
        muna_program.add_feature("Online courses on digital storytelling")

        # Display updated features
        muna_program.display_features()

        # Removing a feature
        muna_program.remove_feature("Networking opportunities for authors and illustrators")

        # Display final features
        muna_program.display_features()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
