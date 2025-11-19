"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://del-pinar.com.ar
Prompt: Write a Python function that integrates with a hotel management library to display amenities like a heated pool and gym for an apart hotel.
Generated: DETERMINISTIC_8254b110b0d3de93
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for hotel management integration
from hotel_management_library import HotelManagementAPI, HotelAmenitiesError

def get_apart_hotel_amenities(hotel_id):
    """
    Fetch and display amenities for a given apart hotel.

    Args:
        hotel_id (str): The unique identifier for the apart hotel.

    Returns:
        list: A list of amenities available at the apart hotel.

    Raises:
        ValueError: If the hotel_id is invalid.
        HotelAmenitiesError: If there is an issue retrieving amenities.
    """
    # Validate input
    if not isinstance(hotel_id, str) or not hotel_id.strip():
        raise ValueError("Invalid hotel_id. It must be a non-empty string.")

    try:
        # Initialize the API client
        api_client = HotelManagementAPI()

        # Fetch amenities using the API
        amenities = api_client.get_amenities(hotel_id)

        # Filter amenities specific to the apart hotel
        apart_hotel_amenities = [amenity for amenity in amenities if amenity in ["Heated Pool", "Gym"]]

        # Display the amenities
        print("Amenities for Apart Hotel:")
        for amenity in apart_hotel_amenities:
            print(f"- {amenity}")

        return apart_hotel_amenities

    except HotelAmenitiesError as e:
        # Handle API-specific errors
        print(f"Failed to retrieve amenities for hotel ID {hotel_id}: {e}")
        raise
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        raise

# Example usage:
# Replace 'hotel123' with a valid hotel ID
# amenities = get_apart_hotel_amenities('hotel123')
```
