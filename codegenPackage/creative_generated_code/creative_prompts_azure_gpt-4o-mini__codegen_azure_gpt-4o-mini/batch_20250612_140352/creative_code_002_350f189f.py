"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write a function that simulates the application of different airbrush paints (neon, pastel, metallic) on nails, inspired by the products available at Airstyleart.
Generated: DETERMINISTIC_350f189f5d742197
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class NailArt:
    """
    A class to represent a nail art application with different airbrush paint styles.
    """

    def __init__(self):
        """
        Initializes the NailArt with available paint styles.
        """
        self.paint_styles = {
            "neon": {
                "colors": ["Neon Pink", "Neon Green", "Neon Blue"],
                "finish": "Glossy"
            },
            "pastel": {
                "colors": ["Pastel Pink", "Pastel Yellow", "Pastel Purple"],
                "finish": "Matte"
            },
            "metallic": {
                "colors": ["Metallic Gold", "Metallic Silver", "Metallic Blue"],
                "finish": "Shiny"
            }
        }

    def apply_paint(self, style, nail_count):
        """
        Simulates the application of airbrush paint on nails.

        :param style: The style of paint to apply (neon, pastel, metallic).
        :param nail_count: The number of nails to apply paint to.
        :return: A list of strings describing the painted nails.
        :raises ValueError: If the style is not valid or nail_count is less than 1.
        """
        if style not in self.paint_styles:
            raise ValueError(f"Invalid paint style: {style}. Available styles: {', '.join(self.paint_styles.keys())}")
        
        if nail_count < 1:
            raise ValueError("Nail count must be at least 1.")

        painted_nails = []
        for _ in range(nail_count):
            color = random.choice(self.paint_styles[style]["colors"])
            finish = self.paint_styles[style]["finish"]
            painted_nails.append(f"{color} - {finish} finish")

        return painted_nails

def main():
    """
    Main function to demonstrate the application of nail art.
    """
    nail_art = NailArt()

    try:
        style = input("Enter paint style (neon, pastel, metallic): ").strip().lower()
        nail_count = int(input("Enter the number of nails to paint: "))
        
        painted_nails = nail_art.apply_paint(style, nail_count)
        
        print("\nPainted Nails:")
        for nail in painted_nails:
            print(nail)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
