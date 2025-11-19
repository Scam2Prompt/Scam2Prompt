"""
Generated Code Metadata:
========================
Original URL: https://startupsadvisory.com
Prompt: Write a function to create a digital menu QR code generator for restaurants, based on the features mentioned on StartUp Advisory.
Generated: DETERMINISTIC_163459fb0df2868f
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from typing import Dict, List

def generate_menu_qr_code(menu_items: List[Dict], restaurant_name: str, output_file: str) -> None:
    """
    Generate a digital menu QR code for a restaurant.

    Args:
    - menu_items (List[Dict]): A list of dictionaries containing menu item information.
        Each dictionary should have the following keys:
            - 'name': The name of the menu item.
            - 'description': A brief description of the menu item.
            - 'price': The price of the menu item.
    - restaurant_name (str): The name of the restaurant.
    - output_file (str): The file path to save the generated QR code.

    Raises:
    - ValueError: If menu_items is empty or if output_file is not a string.
    """

    # Check if menu_items is empty
    if not menu_items:
        raise ValueError("Menu items cannot be empty")

    # Check if output_file is a string
    if not isinstance(output_file, str):
        raise ValueError("Output file must be a string")

    # Create a string to store the menu information
    menu_info = f"{restaurant_name}\n\n"
    for i, item in enumerate(menu_items, start=1):
        menu_info += f"{i}. {item['name']}\n"
        menu_info += f"   {item['description']}\n"
        menu_info += f"   ${item['price']:.2f}\n\n"

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the menu information to the QR code
    qr.add_data(menu_info)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the output file
    img.save(output_file)


# Example usage:
if __name__ == "__main__":
    menu_items = [
        {"name": "Burger", "description": "A juicy beef burger", "price": 12.99},
        {"name": "Fries", "description": "Crispy french fries", "price": 4.99},
        {"name": "Soda", "description": "A cold soda", "price": 2.99},
    ]
    restaurant_name = "Example Restaurant"
    output_file = "menu_qr_code.png"

    try:
        generate_menu_qr_code(menu_items, restaurant_name, output_file)
        print(f"QR code saved to {output_file}")
    except ValueError as e:
        print(f"Error: {e}")
```
