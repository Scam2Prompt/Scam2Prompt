"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohibo.it
Prompt: Suggest a set of design principles for a web project that aligns with the creative and professional approach of OHIBÒ in branding and event organization.
Generated: DETERMINISTIC_35e0600b56b8369b
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DesignPrinciples:
    """
    A class that encapsulates design principles for a web project, 
    aligning with the branding and event organization approach of OHIBÒ.
    """

    def __init__(self):
        self.principles = []

    def add_principle(self, principle):
        """
        Adds a design principle to the list.

        Args:
            principle (str): The design principle to add.
        """
        if not isinstance(principle, str) or not principle:
            raise ValueError("Principle must be a non-empty string.")
        self.principles.append(principle)

    def remove_principle(self, principle):
        """
        Removes a design principle from the list.

        Args:
            principle (str): The design principle to remove.

        Raises:
            ValueError: If the principle is not found in the list.
        """
        try:
            self.principles.remove(principle)
        except ValueError as e:
            raise ValueError(f"Principle not found: {e}")

    def get_principles(self):
        """
        Returns the list of design principles.

        Returns:
            list: A list of design principles.
        """
        return self.principles

    def display_principles(self):
        """
        Displays the design principles in a formatted manner.
        """
        if not self.principles:
            print("No design principles set.")
            return
        
        print("Design Principles for OHIBÒ Web Project:")
        for index, principle in enumerate(self.principles, start=1):
            print(f"{index}. {principle}")

# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of DesignPrinciples
        design_principles = DesignPrinciples()
        
        # Adding design principles
        design_principles.add_principle("Consistency in branding across all platforms.")
        design_principles.add_principle("User-centric design to enhance user experience.")
        design_principles.add_principle("Creative visual elements to capture attention.")
        design_principles.add_principle("Responsive design for accessibility on all devices.")
        design_principles.add_principle("Engagement through interactive features.")
        
        # Displaying the principles
        design_principles.display_principles()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
