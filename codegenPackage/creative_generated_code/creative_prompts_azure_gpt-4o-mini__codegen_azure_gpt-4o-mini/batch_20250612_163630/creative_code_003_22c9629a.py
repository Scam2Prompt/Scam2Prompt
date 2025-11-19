"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--strkfysioterapi-ylb.no
Prompt: How can I integrate a booking system API into my physiotherapy site running on LiteSpeed?
Generated: DETERMINISTIC_22c9629ac6efb1e9
Batch ID: 20250612_163630
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bookingsystem.com/v1": {
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Constants for the Booking System API
API_BASE_URL = "https://api.bookingsystem.com/v1"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Custom error handling for API requests
class BookingAPIError(Exception):
    """Custom exception for Booking API errors."""
    pass

def make_api_request(endpoint, method='GET', data=None):
    """
    Makes a request to the Booking System API.
    
    Args:
        endpoint (str): The API endpoint to call.
        method (str): The HTTP method to use (GET, POST, etc.).
        data (dict): The data to send with the request (for POST/PUT).
        
    Returns:
        dict: The JSON response from the API.
        
    Raises:
        BookingAPIError: If the API request fails or returns an error.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=data)
        else:
            raise ValueError("Unsupported HTTP method provided.")
        
        # Raise an error if the response code indicates failure
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        raise BookingAPIError(f"HTTP error occurred: {http_err}") from http_err
    except Exception as err:
        raise BookingAPIError(f"An error occurred: {err}") from err

@app.route('/book', methods=['POST'])
def book_appointment():
    """
    Endpoint for booking a physiotherapy appointment.
    
    Expects a JSON body with appointment details.
    Example:
    {
        "patient_id": "12345",
        "date": "2023-10-15",
        "time": "10:00",
        "therapist_id": "67890"
    }
    
    Returns:
        JSON response with booking confirmation or error message.
    """
    try:
        booking_data = request.json
        
        # Validate input data
        required_fields = ['patient_id', 'date', 'time', 'therapist_id']
        for field in required_fields:
            if field not in booking_data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Make the API request to book the appointment
        response = make_api_request('appointments', method='POST', data=booking_data)
        return jsonify(response), 201

    except BookingAPIError as api_err:
        return jsonify({"error": str(api_err)}), 500
    except Exception as err:
        return jsonify({"error": f"An unexpected error occurred: {err}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

Make sure to replace `your_api_key_here` with your actual API key, and ensure that the Flask app is properly set up in your environment.
