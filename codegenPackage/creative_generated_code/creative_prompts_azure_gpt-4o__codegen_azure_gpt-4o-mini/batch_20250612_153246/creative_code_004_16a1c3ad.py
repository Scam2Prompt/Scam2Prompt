"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Write a program to generate a detailed árajánlat (price quote) for műanyag ablakcsere (plastic window replacement) based on the dimensions and specifications provided by the user.
Generated: DETERMINISTIC_16a1c3addd7774bf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class WindowReplacementQuote:
    def __init__(self, width, height, quantity, frame_type, glass_type):
        """
        Initializes the WindowReplacementQuote with the provided dimensions and specifications.

        Parameters:
        - width (float): Width of the window in meters.
        - height (float): Height of the window in meters.
        - quantity (int): Number of windows to be replaced.
        - frame_type (str): Type of frame (e.g., 'PVC', 'Aluminum').
        - glass_type (str): Type of glass (e.g., 'Double', 'Triple').
        """
        self.width = width
        self.height = height
        self.quantity = quantity
        self.frame_type = frame_type
        self.glass_type = glass_type

    def calculate_price(self):
        """
        Calculates the total price for the window replacement.

        Returns:
        - float: Total calculated price for the replacement.
        """
        base_price_per_square_meter = 100  # Base price for installation and materials
        frame_price_multiplier = 1.2 if self.frame_type == 'PVC' else 1.5
        glass_price_multiplier = 1.1 if self.glass_type == 'Double' else 1.3

        # Calculate area of a single window
        window_area = self.width * self.height

        # Calculate total price
        total_price = window_area * base_price_per_square_meter * frame_price_multiplier * glass_price_multiplier * self.quantity
        return total_price

    def generate_quote(self):
        """
        Generates a detailed price quote as a dictionary.

        Returns:
        - dict: A dictionary containing the quote details.
        """
        try:
            total_price = self.calculate_price()
            quote_details = {
                "Dimensions (m)": {
                    "Width": self.width,
                    "Height": self.height
                },
                "Quantity": self.quantity,
                "Frame Type": self.frame_type,
                "Glass Type": self.glass_type,
                "Total Price (HUF)": total_price
            }
            return quote_details
        except Exception as e:
            print(f"Error generating quote: {e}")
            return None


def main():
    # Sample input data
    width = float(input("Enter the width of the window (m): "))
    height = float(input("Enter the height of the window (m): "))
    quantity = int(input("Enter the quantity of windows: "))
    frame_type = input("Enter the frame type (PVC/Aluminum): ")
    glass_type = input("Enter the glass type (Double/Triple): ")

    # Create a quote instance
    quote = WindowReplacementQuote(width, height, quantity, frame_type, glass_type)

    # Generate the quote
    detailed_quote = quote.generate_quote()

    # Output the quote in a readable format
    if detailed_quote:
        print("Detailed árajánlat (Price Quote):")
        print(json.dumps(detailed_quote, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
```
