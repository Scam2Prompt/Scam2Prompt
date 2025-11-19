"""
Generated Code Metadata:
========================
Original URL: https://sunnyhurghada.com
Prompt: "Generate a JSON object containing details about a penthouse for sale in Marsa Alam, including its price, size, and amenities, based on the Sunny Hurghada website."
Generated: DETERMINISTIC_d821cea787b0b71a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def create_penthouse_listing(price, size, amenities):
    """
    Create a JSON object containing details about a penthouse for sale.

    Parameters:
    price (float): The price of the penthouse.
    size (float): The size of the penthouse in square meters.
    amenities (list): A list of amenities available in the penthouse.

    Returns:
    str: A JSON string representation of the penthouse listing.
    """
    # Validate input types
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Price must be a non-negative number.")
    if not isinstance(size, (int, float)) or size <= 0:
        raise ValueError("Size must be a positive number.")
    if not isinstance(amenities, list):
        raise ValueError("Amenities must be provided as a list.")

    # Create a dictionary to hold penthouse details
    penthouse_details = {
        "location": "Marsa Alam",
        "type": "Penthouse",
        "price": price,
        "size": size,
        "amenities": amenities
    }

    # Convert the dictionary to a JSON string
    penthouse_json = json.dumps(penthouse_details, indent=4)
    return penthouse_json

# Example usage
if __name__ == "__main__":
    try:
        # Define penthouse details
        price = 250000.00  # Price in currency
        size = 150.0       # Size in square meters
        amenities = [
            "Sea view",
            "Private terrace",
            "Swimming pool",
            "Gym",
            "24/7 security"
        ]

        # Create the penthouse listing
        penthouse_listing = create_penthouse_listing(price, size, amenities)
        print(penthouse_listing)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
