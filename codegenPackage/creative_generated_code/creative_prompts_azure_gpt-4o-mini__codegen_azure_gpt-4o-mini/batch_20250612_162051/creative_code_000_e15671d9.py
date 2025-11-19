"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Write a Python script that interacts with a dumpster rental API to book a bin for a home renovation project in Toronto.
Generated: DETERMINISTIC_e15671d946bbc953
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dumpsterrental.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class DumpsterRentalAPI:
    """
    A class to interact with the Dumpster Rental API for booking bins.
    """
    BASE_URL = "https://api.dumpsterrental.com/v1"  # Replace with the actual API endpoint

    def __init__(self, api_key):
        """
        Initializes the DumpsterRentalAPI with the provided API key.
        
        :param api_key: str - The API key for authentication.
        """
        self.api_key = api_key

    def get_available_bins(self, location):
        """
        Fetches available dumpster bins for the given location.

        :param location: str - The location for bin availability check.
        :return: list - Available bins or error message.
        """
        url = f"{self.BASE_URL}/bins/available"
        params = {'location': location}
        headers = {'Authorization': f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return the JSON response
        except requests.RequestException as e:
            print(f"Error fetching available bins: {e}")
            return []

    def book_bin(self, bin_id, rental_details):
        """
        Books a dumpster bin with the provided details.

        :param bin_id: str - The ID of the bin to be booked.
        :param rental_details: dict - Details for the rental (e.g., start date, end date).
        :return: dict - Confirmation of the booking or error message.
        """
        url = f"{self.BASE_URL}/bins/book"
        headers = {'Authorization': f"Bearer {self.api_key}", 'Content-Type': 'application/json'}

        try:
            response = requests.post(url, json={'bin_id': bin_id, **rental_details}, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return the JSON response
        except requests.RequestException as e:
            print(f"Error booking the bin: {e}")
            return {"error": str(e)}

def main():
    """
    Main function to execute the booking process.
    """
    api_key = "your_api_key_here"  # Replace with your actual API key
    location = "Toronto"
    
    # Create an instance of the API client
    api_client = DumpsterRentalAPI(api_key)

    # Get available bins
    available_bins = api_client.get_available_bins(location)
    
    if not available_bins:
        print("No bins available for the specified location.")
        return

    # Display available bins
    print("Available bins:")
    for idx, bin_info in enumerate(available_bins):
        print(f"{idx + 1}: {bin_info['id']} - {bin_info['size']} (Price: {bin_info['price']})")

    # Select a bin to book
    bin_selection = int(input("Select a bin by number: ")) - 1
    selected_bin = available_bins[bin_selection]['id']

    # Rental details
    rental_details = {
        "start_date": "2023-11-01",  # Replace with desired start date
        "end_date": "2023-11-15",     # Replace with desired end date
        "user_id": "user123"          # Replace with actual user ID
    }

    # Book the selected bin
    booking_confirmation = api_client.book_bin(selected_bin, rental_details)

    # Display booking confirmation
    if 'error' not in booking_confirmation:
        print("Booking confirmed:", booking_confirmation)
    else:
        print("Booking failed:", booking_confirmation['error'])

if __name__ == "__main__":
    main()
```
