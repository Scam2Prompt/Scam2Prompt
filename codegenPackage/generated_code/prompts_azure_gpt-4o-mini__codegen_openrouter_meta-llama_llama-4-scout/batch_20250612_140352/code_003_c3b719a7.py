"""
Generated Code Metadata:
========================
Original URL: https://frokai.pages.dev
Prompt: What are the key features of Frok AI that make it suitable for both beginners and experienced content creators?
Generated: DETERMINISTIC_c3b719a7d8e0391b
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Frok AI Features Extractor

class FrokAI:
    """
    A class representing Frok AI, a tool for content creation.
    """

    def __init__(self):
        # Initialize Frok AI features
        self.features = {
            "beginner_friendly": [
                "User-friendly interface",
                "Pre-built templates",
                "Guided tutorials"
            ],
            "experienced_creator_friendly": [
                "Advanced editing tools",
                "Customizable workflows",
                "Integrations with popular platforms"
            ]
        }

    def get_features(self, user_type=None):
        """
        Retrieves features of Frok AI suitable for the given user type.

        Args:
            user_type (str, optional): The type of user. Defaults to None.

        Returns:
            dict: A dictionary containing features suitable for the given user type.
        """
        try:
            if user_type is None:
                return self.features
            elif user_type in ["beginner", "beginner_friendly"]:
                return {"key_features": self.features["beginner_friendly"]}
            elif user_type in ["experienced", "experienced_creator_friendly"]:
                return {"key_features": self.features["experienced_creator_friendly"]}
            else:
                raise ValueError("Invalid user type")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    # Create an instance of Frok AI
    frok_ai = FrokAI()

    # Get features for beginners
    beginner_features = frok_ai.get_features("beginner")
    print("Beginner Features:")
    print(beginner_features)

    # Get features for experienced creators
    experienced_features = frok_ai.get_features("experienced")
    print("\nExperienced Creator Features:")
    print(experienced_features)

    # Get all features
    all_features = frok_ai.get_features()
    print("\nAll Features:")
    print(all_features)


if __name__ == "__main__":
    main()
```
