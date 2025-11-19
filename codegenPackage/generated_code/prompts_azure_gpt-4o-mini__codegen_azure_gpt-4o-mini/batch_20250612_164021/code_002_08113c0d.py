"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Create a code snippet for a digital illustration project that incorporates elements of color theory, as taught in the painting courses at Ânima.
Generated: DETERMINISTIC_08113c0d965175f2
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

def create_color_wheel(num_colors=12):
    """
    Create a color wheel using the HSL color model.

    Parameters:
    num_colors (int): The number of colors to generate in the wheel.

    Returns:
    list: A list of colors in hex format.
    """
    # Generate hues evenly spaced around the color wheel
    hues = np.linspace(0, 1, num_colors, endpoint=False)
    colors = [hsl_to_hex(hue, 0.5, 0.5) for hue in hues]
    return colors

def hsl_to_hex(h, s, l):
    """
    Convert HSL color values to HEX format.

    Parameters:
    h (float): Hue value (0-1).
    s (float): Saturation value (0-1).
    l (float): Lightness value (0-1).

    Returns:
    str: Color in hex format.
    """
    try:
        if not (0 <= h <= 1) or not (0 <= s <= 1) or not (0 <= l <= 1):
            raise ValueError("H, S, and L values must be between 0 and 1.")

        # Convert HSL to RGB
        if s == 0:
            r = g = b = l  # Achromatic (grey)
        else:
            def hue_to_rgb(p, q, t):
                if t < 0:
                    t += 1
                if t > 1:
                    t -= 1
                if t < 1/6:
                    return p + (q - p) * 6 * t
                if t < 1/2:
                    return q
                if t < 2/3:
                    return p + (q - p) * (2/3 - t) * 6
                return p

            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = hue_to_rgb(p, q, h + 1/3)
            g = hue_to_rgb(p, q, h)
            b = hue_to_rgb(p, q, h - 1/3)

        # Convert RGB to HEX
        return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
    except Exception as e:
        print(f"Error in hsl_to_hex: {e}")
        return "#000000"  # Return black on error

def display_color_wheel(colors):
    """
    Display the color wheel using matplotlib.

    Parameters:
    colors (list): List of colors in hex format.
    """
    try:
        num_colors = len(colors)
        plt.figure(figsize=(8, 8))
        for i, color in enumerate(colors):
            plt.fill_between([i, i + 1], 0, 1, color=color)
        plt.xlim(0, num_colors)
        plt.axis('off')  # Hide axes
        plt.title("Color Wheel")
        plt.show()
    except Exception as e:
        print(f"Error in display_color_wheel: {e}")

if __name__ == "__main__":
    # Create and display a color wheel with 12 colors
    color_wheel = create_color_wheel(12)
    display_color_wheel(color_wheel)
```
