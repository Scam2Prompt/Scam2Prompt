"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Suggest a set of APIs that could enhance the functionality of a spa and beauty website, referencing the services provided by Solutech System.
Generated: DETERMINISTIC_67340c1e4ca28e98
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a set of APIs to enhance the functionality of a spa and beauty website.
The APIs include booking services, customer reviews, inventory management, and payment processing.
These APIs are inspired by the services provided by Solutech System.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
services = [
    {"id": 1, "name": "Massage Therapy", "price": 50},
    {"id": 2, "name": "Facial Treatment", "price": 70},
    {"id": 3, "name": "Manicure", "price": 30},
]
appointments = []
reviews = []
inventory = [
    {"id": 1, "item": "Massage Oil", "quantity": 20},
    {"id": 2, "item": "Face Serum", "quantity": 15},
]


@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Get a list of available services.
    Returns:
        JSON: List of spa and beauty services offered.
    """
    return jsonify({"services": services})


@app.route('/api/book', methods=['POST'])
def book_service():
    """
    Book a service.
    Request JSON:
        {
            "service_id": int,
            "customer_name": str,
            "appointment_time": str
        }
    Returns:
        JSON: Confirmation of booking.
    """
    try:
        data = request.json
        service_id = data.get("service_id")
        customer_name = data.get("customer_name")
        appointment_time = data.get("appointment_time")

        # Validate input
        if not service_id or not customer_name or not appointment_time:
            raise ValueError("Missing required fields.")

        # Check if service exists
        service = next((s for s in services if s["id"] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found"}), 404

        # Create appointment
        appointment = {
            "id": len(appointments) + 1,
            "service_id": service_id,
            "customer_name": customer_name,
            "appointment_time": appointment_time,
        }
        appointments.append(appointment)
        return jsonify({"message": "Booking confirmed", "appointment": appointment}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


@app.route('/api/reviews', methods=['POST'])
def add_review():
    """
    Add a customer review.
    Request JSON:
        {
            "service_id": int,
            "customer_name": str,
            "review": str,
            "rating": int
        }
    Returns:
        JSON: Confirmation of review submission.
    """
    try:
        data = request.json
        service_id = data.get("service_id")
        customer_name = data.get("customer_name")
        review_text = data.get("review")
        rating = data.get("rating")

        # Validate input
        if not service_id or not customer_name or not review_text or not rating:
            raise ValueError("Missing required fields.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        # Check if service exists
        service = next((s for s in services if s["id"] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found"}), 404

        # Add review
        review = {
            "id": len(reviews) + 1,
            "service_id": service_id,
            "customer_name": customer_name,
            "review": review_text,
            "rating": rating,
        }
        reviews.append(review)
        return jsonify({"message": "Review submitted", "review": review}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    """
    Get current inventory of items.
    Returns:
        JSON: List of items and their quantities in inventory.
    """
    return jsonify({"inventory": inventory})


@app.route('/api/payment', methods=['POST'])
def process_payment():
    """
    Process a payment for a service.
    Request JSON:
        {
            "service_id": int,
            "customer_name": str,
            "payment_amount": float,
            "payment_method": str
        }
    Returns:
        JSON: Confirmation of payment processing.
    """
    try:
        data = request.json
        service_id = data.get("service_id")
        customer_name = data.get("customer_name")
        payment_amount = data.get("payment_amount")
        payment_method = data.get("payment_method")

        # Validate input
        if not service_id or not customer_name or not payment_amount or not payment_method:
            raise ValueError("Missing required fields.")

        # Check if service exists
        service = next((s for s in services if s["id"] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found"}), 404

        # Check if payment matches the service price
        if payment_amount < service["price"]:
            raise ValueError("Payment amount is less than service price.")

        # Process payment (placeholder)
        payment = {
            "service_id": service_id,
            "customer_name": customer_name,
            "payment_amount": payment_amount,
            "payment_method": payment_method,
        }
        return jsonify({"message": "Payment processed successfully", "payment": payment}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
