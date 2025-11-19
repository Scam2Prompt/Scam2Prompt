"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Write code to simulate the blending process of color masterbatches, including black and white masterbatches, using the specifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_2434a6983366d1b4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ColorMasterbatch:
    """
    A class to represent a color masterbatch for blending.
    """

    def __init__(self, name, color, concentration):
        """
        Initializes a ColorMasterbatch instance.

        :param name: str - The name of the masterbatch.
        :param color: tuple - The RGB color value as a tuple (R, G, B).
        :param concentration: float - The concentration of the masterbatch (0 to 1).
        """
        self.name = name
        self.color = color
        self.concentration = concentration

    def blend(self, other, ratio):
        """
        Blends this masterbatch with another masterbatch.

        :param other: ColorMasterbatch - The other masterbatch to blend with.
        :param ratio: float - The ratio of this masterbatch in the blend (0 to 1).
        :return: tuple - The resulting blended color as an RGB tuple.
        """
        if not (0 <= ratio <= 1):
            raise ValueError("Ratio must be between 0 and 1.")

        # Calculate the blended color
        r = int((self.color[0] * self.concentration * ratio) + 
                 (other.color[0] * other.concentration * (1 - ratio)))
        g = int((self.color[1] * self.concentration * ratio) + 
                 (other.color[1] * other.concentration * (1 - ratio)))
        b = int((self.color[2] * self.concentration * ratio) + 
                 (other.color[2] * other.concentration * (1 - ratio)))

        return (r, g, b)


def simulate_blending(masterbatches, ratios):
    """
    Simulates the blending of multiple color masterbatches.

    :param masterbatches: list - A list of ColorMasterbatch instances.
    :param ratios: list - A list of ratios corresponding to each masterbatch.
    :return: tuple - The resulting blended color as an RGB tuple.
    """
    if len(masterbatches) != len(ratios):
        raise ValueError("The number of masterbatches must match the number of ratios.")

    blended_color = (0, 0, 0)
    total_concentration = 0

    for masterbatch, ratio in zip(masterbatches, ratios):
        blended_color = (
            blended_color[0] + masterbatch.blend(blended_color, ratio)[0],
            blended_color[1] + masterbatch.blend(blended_color, ratio)[1],
            blended_color[2] + masterbatch.blend(blended_color, ratio)[2]
        )
        total_concentration += masterbatch.concentration * ratio

    # Normalize the blended color by the total concentration
    if total_concentration > 0:
        blended_color = (
            int(blended_color[0] / total_concentration),
            int(blended_color[1] / total_concentration),
            int(blended_color[2] / total_concentration)
        )
    else:
        raise ValueError("Total concentration must be greater than zero.")

    return blended_color


# Example usage
if __name__ == "__main__":
    try:
        # Define masterbatches
        black_masterbatch = ColorMasterbatch("Black", (0, 0, 0), 1.0)
        white_masterbatch = ColorMasterbatch("White", (255, 255, 255), 1.0)
        red_masterbatch = ColorMasterbatch("Red", (255, 0, 0), 0.5)

        # Simulate blending
        masterbatches = [black_masterbatch, white_masterbatch, red_masterbatch]
        ratios = [0.5, 0.3, 0.2]  # Ratios for blending

        blended_color = simulate_blending(masterbatches, ratios)
        print(f"Blended Color (RGB): {blended_color}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
