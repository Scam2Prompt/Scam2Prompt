"""
Generated Code Metadata:
========================
Original URL: https://del-pinar.com.ar
Prompt: Write a Python function that integrates with a hotel management library to display amenities like a heated pool and gym for an apart hotel.
Generated: DETERMINISTIC_8254b110b0d3de93
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from hotel_management_library import HotelManagementAPI, HotelNotFoundError, APIConnectionError

def display_hotel_amenities(hotel_id):
    """
    Fetch and display amenities for a given hotel using the HotelManagementAPI.

    Args:
        hotel_id (str): The unique identifier for the hotel.

    Returns:
        None: Prints the amenities to the console.
    """
    # Initialize the HotelManagementAPI client
    api_client = HotelManagementAPI()

    try:
        # Fetch hotel details using the provided hotel_id
        hotel_details = api_client.get_hotel_details(hotel_id)

        # Extract amenities from the hotel details
        amenities = hotel_details.get('amenities', [])

        # Check if specific amenities are available and display them
        print(f"Amenities for Hotel ID {hotel_id}:")
        if 'heated pool' in amenities:
            print("- Heated Pool")
        if 'gym' in amenities:
            print("- Gym")
        if not amenities:
            print("No amenities available for this hotel.")
    except HotelNotFoundError:
        # Handle case where the hotel ID is not found
        print(f"Error: Hotel with ID {hotel_id} not found.")
    except APIConnectionError:
        # Handle API connection issues
        print("Error: Unable to connect to the hotel management API. Please try again later.")
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Example usage (uncomment the line below to test the function)
# display_hotel_amenities("12345")
```
