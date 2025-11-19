"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.khadamy.com
Prompt: Generate a code snippet for a web application that allows users to book mobile car polishing services in Riyadh.
Generated: DETERMINISTIC_b6db105f66b8fe8f
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data - In a production environment, use a database
available_slots = [
    {"id": 1, "date": "2023-10-15", "time": "10:00 AM", "available": True},
    {"id": 2, "date": "2023-10-15", "time": "02:00 PM", "available": True},
    {"id": 3, "date": "2023-10-16", "time": "11:00 AM", "available": True}
]

bookings = []


@app.route('/slots', methods=['GET'])
def get_available_slots():
    """
    Endpoint to fetch available slots for mobile car polishing services.
    Returns a list of slots that are still available.
    """
    return jsonify([slot for slot in available_slots if slot["available"]])


@app.route('/book', methods=['POST'])
def book_slot():
    """
    Endpoint to book a slot for mobile car polishing services.
    Expects JSON data with `slot_id` and `customer_name`.
    Returns a confirmation or error message based on availability.
    """
    try:
        # Parse JSON data from the request
        data = request.json
        slot_id = data.get('slot_id')
        customer_name = data.get('customer_name')

        # Validate input
        if not slot_id or not customer_name:
            return jsonify({"error": "Missing required fields: slot_id, customer_name"}), 400

        # Find the slot by ID
        slot = next((s for s in available_slots if s["id"] == slot_id), None)

        if not slot:
            return jsonify({"error": "Slot not found"}), 404

        if not slot["available"]:
            return jsonify({"error": "Slot is already booked"}), 400

        # Mark the slot as booked
        slot["available"] = False
        bookings.append({"slot_id": slot_id, "customer_name": customer_name})

        return jsonify({"message": "Slot booked successfully", "slot": slot}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to fetch all bookings.
    Returns a list of all booked slots along with customer names.
    """
    return jsonify(bookings)


if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=True)
```
