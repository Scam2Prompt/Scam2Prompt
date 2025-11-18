"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Recommend tools or libraries to implement unlimited course offerings (both free and paid) with InfinitiAI's platform capabilities.
Generated: DETERMINISTIC_67209939a57f7757
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to implement unlimited course offerings (free and paid) 
using InfinitiAI's platform capabilities. The implementation uses Flask for the web 
API and Stripe for payment processing. Both free and paid courses are supported.
"""

from flask import Flask, request, jsonify
import stripe

# Flask application setup
app = Flask(__name__)

# Stripe API key setup (replace with your actual secret key)
stripe.api_key = "your_stripe_secret_key"

# Mock database for storing course information
courses_db = {
    "1": {"id": "1", "title": "Free Course Example", "price": 0},
    "2": {"id": "2", "title": "Paid Course Example", "price": 20.0},
}

@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Endpoint to get all available courses.
    Returns:
        JSON response with available courses.
    """
    return jsonify({"courses": list(courses_db.values())}), 200

@app.route('/courses/<course_id>', methods=['GET'])
def get_course(course_id):
    """
    Endpoint to get details of a specific course.
    Args:
        course_id (str): The ID of the course.
    Returns:
        JSON response with course details or error message.
    """
    course = courses_db.get(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify(course), 200

@app.route('/enroll/<course_id>', methods=['POST'])
def enroll_course(course_id):
    """
    Endpoint to enroll in a course.
    Free courses are enrolled directly, while paid courses require payment.
    Args:
        course_id (str): The ID of the course.
    Returns:
        JSON response indicating enrollment status or payment instructions.
    """
    course = courses_db.get(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    if course["price"] == 0:
        # Enroll directly for free courses
        return jsonify({"message": "Successfully enrolled in the course!"}), 200

    try:
        # Create a Stripe payment intent for paid courses
        payment_intent = stripe.PaymentIntent.create(
            amount=int(course["price"] * 100),  # convert price to cents
            currency="usd",
            payment_method_types=["card"],
        )
        return jsonify({
            "message": "Payment required to enroll in course",
            "client_secret": payment_intent.client_secret
        }), 200
    except stripe.error.StripeError as e:
        # Stripe error handling
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    """
    Entry point for the application. Run the Flask server.
    Note:
        Ensure debugging is disabled in production by setting debug=False.
    """
    app.run(debug=True)
```
