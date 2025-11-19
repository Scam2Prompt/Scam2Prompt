"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Design a secure payment gateway for processing transactions related to e-book purchases and subscriptions on a platform like Digielearning, considering multiple payment options."
Generated: DETERMINISTIC_6c9b7e0a35fbb96f
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from payment_processor import PaymentProcessor  # Hypothetical external payment processing library

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Configuration for payment gateway
PAYMENT_OPTIONS = ['credit_card', 'paypal', 'stripe']
SECRET_KEY = 'your_secret_key'  # Replace with your actual secret key

class PaymentGateway:
    def __init__(self):
        self.processor = PaymentProcessor(secret_key=SECRET_KEY)

    def process_payment(self, payment_data):
        """
        Process the payment based on the provided payment data.
        
        Args:
            payment_data (dict): A dictionary containing payment information.
        
        Returns:
            dict: A response indicating the success or failure of the payment.
        """
        try:
            # Validate payment option
            if payment_data['payment_option'] not in PAYMENT_OPTIONS:
                raise ValueError("Invalid payment option selected.")

            # Process the payment
            response = self.processor.process(payment_data)
            return response

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
            return {"error": str(ve)}, 400
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {"error": "An unexpected error occurred."}, 500

@app.route('/api/payment', methods=['POST'])
def payment_endpoint():
    """
    Endpoint to handle payment processing for e-book purchases and subscriptions.
    
    Returns:
        JSON response indicating the result of the payment processing.
    """
    try:
        # Parse JSON request
        payment_data = request.get_json()
        if not payment_data:
            raise BadRequest("Request must be JSON.")

        # Create a PaymentGateway instance
        gateway = PaymentGateway()

        # Process the payment
        result = gateway.process_payment(payment_data)
        return jsonify(result)

    except BadRequest as e:
        logging.error(f"BadRequest: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error in payment endpoint: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

### Note:
- The `PaymentProcessor` class is a placeholder for an actual payment processing library that you would need to implement or integrate.
- Ensure to replace `your_secret_key` with a secure key and manage it properly.
- This code assumes the use of Flask for the web framework. Make sure to install Flask and any other dependencies required for your project.
