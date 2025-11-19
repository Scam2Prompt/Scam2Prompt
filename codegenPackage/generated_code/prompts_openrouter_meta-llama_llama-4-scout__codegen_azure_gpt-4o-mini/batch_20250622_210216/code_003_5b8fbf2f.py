"""
Generated Code Metadata:
========================
Original URL: https://kossto.com
Prompt: "Design a neoprene postpartum belly band with a 3-in-1 functionality for abdominal, waist, and pelvis support, similar to Kossto's product."
Generated: DETERMINISTIC_5b8fbf2f2f0a7ca7
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PostpartumBellyBand:
    """
    A class to represent a neoprene postpartum belly band with 3-in-1 functionality
    for abdominal, waist, and pelvis support.
    """

    def __init__(self, size: str, color: str):
        """
        Initializes the PostpartumBellyBand with size and color.

        :param size: Size of the belly band (e.g., 'S', 'M', 'L', 'XL').
        :param color: Color of the belly band (e.g., 'black', 'beige').
        """
        self.size = size
        self.color = color
        self.support_types = {
            'abdominal': False,
            'waist': False,
            'pelvis': False
        }

    def activate_support(self, support_type: str):
        """
        Activates the specified support type.

        :param support_type: Type of support to activate ('abdominal', 'waist', 'pelvis').
        :raises ValueError: If the support type is invalid.
        """
        if support_type not in self.support_types:
            raise ValueError(f"Invalid support type: {support_type}. Choose from {list(self.support_types.keys())}.")
        
        self.support_types[support_type] = True
        print(f"{support_type.capitalize()} support activated.")

    def deactivate_support(self, support_type: str):
        """
        Deactivates the specified support type.

        :param support_type: Type of support to deactivate ('abdominal', 'waist', 'pelvis').
        :raises ValueError: If the support type is invalid.
        """
        if support_type not in self.support_types:
            raise ValueError(f"Invalid support type: {support_type}. Choose from {list(self.support_types.keys())}.")
        
        self.support_types[support_type] = False
        print(f"{support_type.capitalize()} support deactivated.")

    def get_support_status(self):
        """
        Returns the current status of all support types.

        :return: A dictionary with support types and their activation status.
        """
        return self.support_types

    def __str__(self):
        """
        Returns a string representation of the PostpartumBellyBand.

        :return: A string describing the belly band.
        """
        return f"Postpartum Belly Band - Size: {self.size}, Color: {self.color}, Supports: {self.get_support_status()}"

# Example usage
if __name__ == "__main__":
    try:
        belly_band = PostpartumBellyBand(size='M', color='black')
        print(belly_band)

        belly_band.activate_support('abdominal')
        belly_band.activate_support('waist')
        print(belly_band.get_support_status())

        belly_band.deactivate_support('waist')
        print(belly_band.get_support_status())

    except ValueError as e:
        print(f"Error: {e}")
```
