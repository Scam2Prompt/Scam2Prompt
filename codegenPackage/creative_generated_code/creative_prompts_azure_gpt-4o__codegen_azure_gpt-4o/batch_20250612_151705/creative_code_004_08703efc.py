"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lyvely-claim.pages.dev
Prompt: Write a script to schedule and host video calls with integrated payment processing, similar to Lyvely's video call functionality.
Generated: DETERMINISTIC_08703efc0303d9fd
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import uuid
from flask import Flask, request, jsonify
import stripe

# Initialize Flask app
app = Flask(__name__)

# Stripe API keys (replace with your own keys)
STRIPE_PUBLIC_KEY = "your-public-key"
STRIPE_SECRET_KEY = "your-secret-key"
stripe.api_key = STRIPE_SECRET_KEY

# In-memory database for storing video call sessions
video_calls = {}

# Helper function to generate unique IDs for video calls
def generate_unique_id():
    return str(uuid.uuid4())

@app.route('/schedule', methods=['POST'])
def schedule_video_call():
    """
    Endpoint to schedule a video call. 
    Expects JSON payload with 'date_time', 'duration', and 'price'.
    """
    try:
        data = request.json
        date_time = data.get('date_time')  # Expected in ISO format (e.g., '2023-01-01T15:00:00')
        duration = data.get('duration')  # Duration in minutes
        price = data.get('price')  # Price in cents (e.g., 500 for $5.00)

        # Validate input
        if not date_time or not duration or not price:
            return jsonify({"error": "Missing required fields (date_time, duration, price)."}), 400

        # Parse date_time and validate
        try:
            scheduled_time = datetime.datetime.fromisoformat(date_time)
        except ValueError:
            return jsonify({"error": "Invalid date_time format. Use ISO 8601 format."}), 400

        if scheduled_time < datetime.datetime.now():
            return jsonify({"error": "Cannot schedule a video call in the past."}), 400

        # Generate unique ID for the video call
        video_call_id = generate_unique_id()

        # Save video call details in the in-memory database
        video_calls[video_call_id] = {
            "date_time": scheduled_time,
            "duration": duration,
            "price": price,
            "status": "scheduled"
        }

        return jsonify({"message": "Video call scheduled successfully.", "video_call_id": video_call_id}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a Stripe payment intent for a scheduled video call.
    Expects JSON payload with 'video_call_id'.
    """
    try:
        data = request.json
        video_call_id = data.get('video_call_id')

        # Validate video call ID
        if not video_call_id or video_call_id not in video_calls:
            return jsonify({"error": "Invalid or missing video_call_id."}), 400

        video_call_details = video_calls[video_call_id]

        # Create a payment intent with Stripe
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=video_call_details['price'],  # Amount in cents
                currency='usd',  # Currency
                metadata={"video_call_id": video_call_id}
            )

            return jsonify({"client_secret": payment_intent.client_secret}), 200
        except stripe.error.StripeError as e:
            return jsonify({"error": f"Stripe error: {str(e)}"}), 500
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/start-video-call', methods=['POST'])
def start_video_call():
    """
    Endpoint to start a video call. 
    Expects JSON payload with 'video_call_id'.
    """
    try:
        data = request.json
        video_call_id = data.get('video_call_id')

        # Validate video call ID
        if not video_call_id or video_call_id not in video_calls:
            return jsonify({"error": "Invalid or missing video_call_id."}), 400

        video_call_details = video_calls[video_call_id]

        # Check if the call is already started or completed
        if video_call_details["status"] != "scheduled":
            return jsonify({"error": "Video call is either already started or completed."}), 400

        # Mark the video call as started
        video_call_details["status"] = "in_progress"

        return jsonify({"message": "Video call started successfully.", "video_call_id": video_call_id}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/end-video-call', methods=['POST'])
def end_video_call():
    """
    Endpoint to end a video call. 
    Expects JSON payload with 'video_call_id'.
    """
    try:
        data = request.json
        video_call_id = data.get('video_call_id')

        # Validate video call ID
        if not video_call_id or video_call_id not in video_calls:
            return jsonify({"error": "Invalid or missing video_call_id."}), 400

        video_call_details = video_calls[video_call_id]

        # Check if the call is already completed or not started
        if video_call_details["status"] != "in_progress":
            return jsonify({"error": "Video call is either not started or already completed."}), 400

        # Mark the video call as completed
        video_call_details["status"] = "completed"

        return jsonify({"message": "Video call ended successfully.", "video_call_id": video_call_id}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
```
