"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mary.finance
Prompt: What features of MARY AI make it accessible for non-professionals to create functional prototypes?
Generated: DETERMINISTIC_9ac1554eed1cb088
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MaryAI:
    """
    A class to represent the MARY AI platform for creating functional prototypes.
    """

    def __init__(self):
        """
        Initialize the MARY AI platform with necessary components.
        """
        self.features = {
            'User-Friendly Interface': 'Intuitive design for easy navigation.',
            'Pre-built Templates': 'Ready-to-use templates for quick prototypes.',
            'Drag-and-Drop Functionality': 'Easily add components without coding.',
            'Collaborative Tools': 'Work with teams in real-time.',
            'Integration Capabilities': 'Connects with various APIs and services.',
            'Extensive Documentation': 'Comprehensive guides and tutorials for users.'
        }

    def get_features(self):
        """
        Retrieve the list of features available in MARY AI.

        Returns:
            dict: A dictionary containing the features of MARY AI.
        """
        return self.features

    def is_accessible(self):
        """
        Check if MARY AI is accessible for non-professionals.

        Returns:
            bool: True if accessible, False otherwise.
        """
        # Accessibility criteria for non-professionals
        accessibility_criteria = [
            'User-Friendly Interface',
            'Pre-built Templates',
            'Drag-and-Drop Functionality',
            'Extensive Documentation'
        ]
        
        # Check if all criteria are present
        return all(feature in self.features for feature in accessibility_criteria)

    def display_features(self):
        """
        Display the features of MARY AI in a user-friendly format.
        """
        try:
            features = self.get_features()
            print("MARY AI Features:")
            for feature, description in features.items():
                print(f"- {feature}: {description}")
        except Exception as e:
            print(f"An error occurred while displaying features: {e}")

# Example usage
if __name__ == "__main__":
    mary_ai = MaryAI()
    mary_ai.display_features()
    if mary_ai.is_accessible():
        print("MARY AI is accessible for non-professionals.")
    else:
        print("MARY AI is not fully accessible for non-professionals.")
```
