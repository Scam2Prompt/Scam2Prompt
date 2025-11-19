"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Design a RESTful API for a chiller van rental company in Dubai, including endpoints for booking, tracking, and managing deliveries with temperature monitoring.
Generated: DETERMINISTIC_1cfea8a800101791
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for simplicity
bookings = {}
deliveries = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Endpoint: Book a chiller van
@app.route('/api/book', methods=['POST'])
def book_van():
    try:
        data = request.json
        if not data or 'customer_name' not in data or 'pickup_location' not in data or 'dropoff_location' not in data or 'date' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        booking_id = generate_id()
        bookings[booking_id] = {
            "customer_name": data['customer_name'],
            "pickup_location": data['pickup_location'],
            "dropoff_location": data['dropoff_location'],
            "date": data['date'],
            "status": "Booked"
        }
        return jsonify({"message": "Booking successful", "booking_id": booking_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Track a delivery
@app.route('/api/track/<delivery_id>', methods=['GET'])
def track_delivery(delivery_id):
    try:
        delivery = deliveries.get(delivery_id)
        if not delivery:
            return jsonify({"error": "Delivery not found"}), 404
        
        return jsonify({"delivery_id": delivery_id, "status": delivery['status'], "temperature": delivery['temperature']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Manage deliveries (update status and temperature)
@app.route('/api/delivery/<delivery_id>', methods=['PUT'])
def update_delivery(delivery_id):
    try:
        data = request.json
        if not data or 'status' not in data or 'temperature' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        delivery = deliveries.get(delivery_id)
        if not delivery:
            return jsonify({"error": "Delivery not found"}), 404
        
        delivery['status'] = data['status']
        delivery['temperature'] = data['temperature']
        return jsonify({"message": "Delivery updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Create a delivery (for testing purposes)
@app.route('/api/delivery', methods=['POST'])
def create_delivery():
    try:
        data = request.json
        if not data or 'booking_id' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        booking = bookings.get(data['booking_id'])
        if not booking:
            return jsonify({"error": "Booking not found"}), 404
        
        delivery_id = generate_id()
        deliveries[delivery_id] = {
            "booking_id": data['booking_id'],
            "status": "In Transit",
            "temperature": "Unknown"
        }
        return jsonify({"message": "Delivery created successfully", "delivery_id": delivery_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
