"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandboxii121.pages.dev
Prompt: Create an API endpoint for processing ticket purchases that includes features like order summary and fee calculation, inspired by the checkout details from the Moongate AI Crypto Summit.
Generated: DETERMINISTIC_9d0423ce8ade792d
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Define a constant for ticket price and fees
TICKET_PRICE = 100.00  # Base price in USD
PROCESSING_FEE_PERCENTAGE = 5  # Processing fee as a percentage
CRYPTO_DISCOUNT_PERCENTAGE = 10  # Discount for crypto payments

@app.route('/api/purchase-ticket', methods=['POST'])
def purchase_ticket():
    """
    API Endpoint to handle ticket purchases.
    Request payload should include:
    - "quantity" (int): Number of tickets to purchase
    - "payment_method" (str): Payment method (e.g., "credit_card", "crypto")
    Returns:
    - JSON response with order summary, including ticket cost, fees, total amount, and discount (if applicable).
    """
    try:
        # Parse and validate request data
        data = request.get_json()
        if not data:
            raise BadRequest("Invalid or missing JSON payload")
        
        # Validate required fields
        quantity = data.get('quantity')
        payment_method = data.get('payment_method')

        if not isinstance(quantity, int) or quantity <= 0:
            raise BadRequest("Invalid 'quantity'. Must be a positive integer.")
        
        if payment_method not in ['credit_card', 'crypto']:
            raise BadRequest("Invalid 'payment_method'. Must be 'credit_card' or 'crypto'.")

        # Calculate ticket cost
        ticket_cost = TICKET_PRICE * quantity

        # Calculate processing fees
        processing_fee = (PROCESSING_FEE_PERCENTAGE / 100) * ticket_cost

        # Calculate discount
        discount = 0.0
        if payment_method == 'crypto':
            discount = (CRYPTO_DISCOUNT_PERCENTAGE / 100) * ticket_cost

        # Calculate total cost
        total_cost = ticket_cost + processing_fee - discount

        # Build order summary
        order_summary = {
            'quantity': quantity,
            'ticket_cost': round(ticket_cost, 2),
            'processing_fee': round(processing_fee, 2),
            'discount': round(discount, 2),
            'total_cost': round(total_cost, 2),
            'payment_method': payment_method
        }

        return jsonify({'status': 'success', 'order_summary': order_summary}), 200

    except BadRequest as e:
        # Handle validation errors
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({'status': 'error', 'message': 'An unexpected error occurred.'}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
