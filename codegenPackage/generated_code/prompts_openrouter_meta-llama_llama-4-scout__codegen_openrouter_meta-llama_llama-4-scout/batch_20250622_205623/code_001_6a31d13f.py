"""
Generated Code Metadata:
========================
Original URL: https://pixels-3s4.pages.dev
Prompt: Generate a list of community guidelines for a project like Pixels.
Generated: DETERMINISTIC_6a31d13f43fecc8c
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_guidelines.py

class CommunityGuidelines:
    def __init__(self):
        """
        Initialize community guidelines with default rules.
        """
        self.guidelines = [
            "Be respectful and considerate of others.",
            "No harassment or bullying of any kind.",
            "No spam or self-promotion.",
            "No hate speech or discriminatory language.",
            "No sharing of sensitive or confidential information.",
            "Follow the project's code of conduct."
        ]

    def add_guideline(self, guideline):
        """
        Add a new community guideline.

        Args:
            guideline (str): The new guideline to add.

        Raises:
            ValueError: If the guideline is empty or already exists.
        """
        if not guideline:
            raise ValueError("Guideline cannot be empty.")
        if guideline in self.guidelines:
            raise ValueError("Guideline already exists.")
        self.guidelines.append(guideline)

    def remove_guideline(self, guideline):
        """
        Remove a community guideline.

        Args:
            guideline (str): The guideline to remove.

        Raises:
            ValueError: If the guideline does not exist.
        """
        if guideline not in self.guidelines:
            raise ValueError("Guideline does not exist.")
        self.guidelines.remove(guideline)

    def get_guidelines(self):
        """
        Get the list of community guidelines.

        Returns:
            list: The list of community guidelines.
        """
        return self.guidelines


def main():
    try:
        guidelines = CommunityGuidelines()
        print("Default Community Guidelines:")
        for i, guideline in enumerate(guidelines.get_guidelines()):
            print(f"{i+1}. {guideline}")

        # Add a new guideline
        new_guideline = "Be kind to newcomers."
        guidelines.add_guideline(new_guideline)
        print("\nUpdated Community Guidelines:")
        for i, guideline in enumerate(guidelines.get_guidelines()):
            print(f"{i+1}. {guideline}")

        # Remove a guideline
        guideline_to_remove = "No spam or self-promotion."
        guidelines.remove_guideline(guideline_to_remove)
        print("\nUpdated Community Guidelines after removal:")
        for i, guideline in enumerate(guidelines.get_guidelines()):
            print(f"{i+1}. {guideline}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
