"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dissolar.co
Prompt: What features can I expect from the DISSOLAR website once it's completed?
Generated: DETERMINISTIC_2cc3acc35626e0d8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DISSOLARWebsite:
    """
    A class representing the DISSOLAR website features.
    """

    def __init__(self):
        """
        Initializes the DISSOLAR website with default features.
        """
        self.features = [
            "User-friendly interface",
            "Solar product catalog",
            "Online shopping cart",
            "Secure payment gateway",
            "Customer account management",
            "Installation service booking",
            "Live chat support",
            "Blog and resource center",
            "Newsletter subscription",
            "Social media integration",
            "Feedback and review system"
        ]

    def get_features(self):
        """
        Returns the list of features available on the DISSOLAR website.

        Returns:
            list: A list containing the features of the DISSOLAR website.
        """
        return self.features

    def add_feature(self, feature):
        """
        Adds a new feature to the DISSOLAR website.

        Args:
            feature (str): The feature to be added.

        Raises:
            ValueError: If the feature is empty or already exists.
        """
        if not feature:
            raise ValueError("Feature cannot be empty.")
        if feature in self.features:
            raise ValueError("Feature already exists.")
        self.features.append(feature)

    def remove_feature(self, feature):
        """
        Removes an existing feature from the DISSOLAR website.

        Args:
            feature (str): The feature to be removed.

        Raises:
            ValueError: If the feature does not exist.
        """
        if feature not in self.features:
            raise ValueError("Feature does not exist.")
        self.features.remove(feature)

    def display_features(self):
        """
        Displays the current features of the DISSOLAR website in a readable format.
        """
        print("DISSOLAR Website Features:")
        for feature in self.features:
            print(f"- {feature}")


if __name__ == "__main__":
    try:
        # Create an instance of the DISSOLARWebsite class
        dissolar_website = DISSOLARWebsite()
        
        # Display the initial features
        dissolar_website.display_features()
        
        # Adding a new feature
        dissolar_website.add_feature("Energy consumption calculator")
        
        # Display updated features
        dissolar_website.display_features()
        
        # Attempting to add a duplicate feature
        dissolar_website.add_feature("Online shopping cart")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
