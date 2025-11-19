"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Create a sample JSON request for a custom metallic sticker order, including details like material type and design specifications as mentioned on Jttlogos.
Generated: DETERMINISTIC_e5a990af4687b826
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def create_metallic_sticker_order():
    """
    Creates a sample JSON request for a custom metallic sticker order.
    
    Returns:
        str: A JSON-formatted string containing the sticker order details.
    """
    try:
        # Define the order details
        order_details = {
            "order_id": "12345",  # Unique identifier for the order
            "customer": {
                "name": "John Doe",  # Name of the customer
                "email": "johndoe@example.com",  # Email of the customer
                "phone": "+1234567890"  # Contact number of the customer
            },
            "shipping_address": {
                "address_line_1": "123 Main Street",  # First line of the address
                "address_line_2": "Apt 4B",  # Second line (optional)
                "city": "Metropolis",  # City name
                "state": "NY",  # State abbreviation
                "postal_code": "10001",  # ZIP/postal code
                "country": "USA"  # Country name
            },
            "sticker_details": {
                "material_type": "metallic_vinyl",  # Material type of the sticker
                "dimensions": {
                    "width": "5cm",  # Width of the sticker
                    "height": "5cm"  # Height of the sticker
                },
                "design": {
                    "background_color": "#FFD700",  # Hex code for the background color
                    "text": "JTT Logos",  # Text to be printed on the sticker
                    "font": "Arial",  # Font style for the text
                    "text_color": "#000000"  # Hex code for the text color
                }
            },
            "quantity": 100,  # Number of stickers ordered
            "special_requests": [
                "Glossy finish",  # Additional customization request
                "Waterproof material"  # Additional customization request
            ],
            "order_date": "2023-11-01",  # Date of the order
            "estimated_delivery_date": "2023-11-15",  # Estimated delivery date
        }

        # Convert the order details to a JSON-formatted string
        json_request = json.dumps(order_details, indent=4)
        return json_request

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while creating the JSON request: {e}")
        return None

# Generate the JSON request and print it
if __name__ == "__main__":
    metallic_sticker_order = create_metallic_sticker_order()
    if metallic_sticker_order:
        print("Sample JSON Request for Metallic Sticker Order:")
        print(metallic_sticker_order)
```
