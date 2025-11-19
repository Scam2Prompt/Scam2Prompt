"""
Generated Code Metadata:
========================
Original URL: https://airsol.vercel.app
Prompt: Design a simple plane object using object-oriented programming in Python, including attributes like "length", "wing_span", and "engines", and provide a humorous description of the plane using the object's attributes.
Generated: DETERMINISTIC_c4ca193878ee1f1f
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Plane:
    """
    A class representing a simple plane object.

    Attributes:
        length (float): The length of the plane in meters.
        wing_span (float): The wing span of the plane in meters.
        engines (int): The number of engines in the plane.
    """

    def __init__(self, length: float, wing_span: float, engines: int):
        """
        Initializes a Plane object.

        Args:
            length (float): The length of the plane in meters.
            wing_span (float): The wing span of the plane in meters.
            engines (int): The number of engines in the plane.

        Raises:
            ValueError: If length, wing_span, or engines are not positive.
        """
        if length <= 0 or wing_span <= 0 or engines <= 0:
            raise ValueError("Length, wing span, and engines must be positive.")

        self.length = length
        self.wing_span = wing_span
        self.engines = engines

    def __str__(self):
        return f"Plane - Length: {self.length}m, Wing Span: {self.wing_span}m, Engines: {self.engines}"

    def get_humorous_description(self) -> str:
        """
        Generates a humorous description of the plane.

        Returns:
            str: A humorous description of the plane.
        """
        engine_str = "monster" if self.engines > 2 else "baby"
        size_str = "giant" if self.length > 50 else "tiny"
        return f"This {size_str} plane has a wing span that's almost as wide as its ego, powered by a {engine_str} of an engine."


def main():
    try:
        plane = Plane(60, 40, 4)
        print(plane)
        print(plane.get_humorous_description())

        # Test error handling
        Plane(0, 40, 4)  # Should raise ValueError
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
