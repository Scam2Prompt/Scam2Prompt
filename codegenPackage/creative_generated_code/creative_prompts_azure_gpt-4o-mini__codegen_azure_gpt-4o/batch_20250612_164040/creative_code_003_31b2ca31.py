"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: How can I create a web application that allows users to view and book properties like those listed on the Moms PG site, including amenities and pricing details?
Generated: DETERMINISTIC_31b2ca31b9167a07
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-structured implementation for your request using Python and Flask for backend development. This code provides a simple property listing and booking system.

### `app.py` (Backend with Flask)

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory database for properties and bookings
properties = [
    {
        "id": str(uuid.uuid4()),
        "name": "Luxury Apartment",
        "location": "Downtown",
        "price_per_night": 120,
        "amenities": ["WiFi", "Air Conditioning", "Parking"],
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Cozy Studio",
        "location": "Suburb",
        "price_per_night": 80,
        "amenities": ["WiFi", "Kitchen", "Heating"],
    },
]

bookings = []

@app.route('/properties', methods=['GET'])
def get_properties():
    """
    Fetch the list of all properties.
    Returns:
      JSON response containing property details.
    """
    return jsonify({"properties": properties}), 200

@app.route('/properties/<property_id>', methods=['GET'])
def get_property_details(property_id):
    """
    Fetch details of a specific property by ID.
    Args:
      property_id (str): ID of the property.
    Returns:
      JSON response with property details or error message.
    """
    property = next((p for p in properties if p["id"] == property_id), None)
    if property:
        return jsonify({"property": property}), 200
    return jsonify({"error": "Property not found"}), 404

@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Book a property.
    Request Body:
      {
        "property_id": "string",
        "customer_name": "string",
        "check_in_date": "YYYY-MM-DD",
        "check_out_date": "YYYY-MM-DD"
      }
    Returns:
      JSON response with booking confirmation or error message.
    """
    data = request.get_json()
    property_id = data.get("property_id")
    customer_name = data.get("customer_name")
    check_in_date = data.get("check_in_date")
    check_out_date = data.get("check_out_date")

    # Validate input
    if not property_id or not customer_name or not check_in_date or not check_out_date:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if property exists
    property = next((p for p in properties if p["id"] == property_id), None)
    if not property:
        return jsonify({"error": "Property not found"}), 404

    # Create booking
    booking = {
        "id": str(uuid.uuid4()),
        "property_id": property_id,
        "customer_name": customer_name,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
    }
    bookings.append(booking)
    return jsonify({"message": "Booking successful", "booking": booking}), 201

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Fetch all bookings.
    Returns:
      JSON response containing booking details.
    """
    return jsonify({"bookings": bookings}), 200

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Route not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### `requirements.txt`

```text
Flask==2.2.5
uuid
```

### Notes:
1. Save the code in a file named `app.py`.
2. Create a virtual environment, install Flask (`pip install Flask`), and run the app (`python app.py`).
3. This backend handles property listings, property details, and property bookings.
4. Test endpoints using Postman or any API testing tool:
   - `GET /properties` to get all properties.
   - `GET /properties/<property_id>` for property details.
   - `POST /bookings` to create a booking (provide JSON body with property_id, customer_name, check_in_date, check_out_date).
   - `GET /bookings` to view all bookings.
