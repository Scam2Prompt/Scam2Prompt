"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Recommend tools or libraries to implement a payment installment system for car accessories, similar to the one described on the Tuning Design website.
Generated: DETERMINISTIC_0ac04b4e4bc281b9
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script implements a payment installment system for car accessories.
It uses Flask for the web API and sqlite3 as the database to manage records.
Stripe is used for payment processing.

Dependencies:
- Flask (`pip install flask`)
- Stripe (`pip install stripe`)
"""

from flask import Flask, request, jsonify
import stripe
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Configure Stripe API key (replace with your actual secret key)
stripe.api_key = 'your_stripe_secret_key'

# Database setup
DB_FILE = 'installments.db'


def setup_database():
    """Initializes the SQLite database if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS installments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            email TEXT NOT NULL,
            product_name TEXT NOT NULL,
            total_amount REAL NOT NULL,
            installment_plan TEXT NOT NULL,
            stripe_payment_id TEXT NOT NULL,
            paid BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


# Set up database on startup
setup_database()


@app.route('/create-installment', methods=['POST'])
def create_installment():
    """
    Endpoint to create a payment installment plan.
    Expects JSON with customer_name, email, product_name, total_amount, and installment_plan.
    """
    try:
        # Extract data from the request
        data = request.json
        customer_name = data['customer_name']
        email = data['email']
        product_name = data['product_name']
        total_amount = data['total_amount']
        installment_plan = data['installment_plan']

        # Create a payment intent in Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),  # Convert to cents
            currency='usd',
            receipt_email=email,
            description=f"Installment payment for {product_name}",
        )

        # Save installment data to the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO installments (customer_name, email, product_name, total_amount, installment_plan, stripe_payment_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (customer_name, email, product_name, total_amount, installment_plan, payment_intent.id))
        conn.commit()
        conn.close()

        # Respond with success
        return jsonify({
            'success': True,
            'message': 'Installment plan created successfully.',
            'stripe_payment_intent': payment_intent.client_secret,
        })

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({'success': False, 'error': str(e)}), 400

    except KeyError as e:
        # Handle missing keys in JSON data
        return jsonify({'success': False, 'error': f'Missing required field: {e}'}), 400

    except Exception as e:
        # Handle other errors
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/check-payment-status/<payment_id>', methods=['GET'])
def check_payment_status(payment_id):
    """
    Endpoint to check the status of a payment by Stripe payment ID.
    """
    try:
        # Retrieve payment intent from Stripe
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)

        # Respond with payment status
        return jsonify({
            'success': True,
            'status': payment_intent.status,
            'amount_received': payment_intent.amount_received / 100.0,  # Convert cents to dollars
        })

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({'success': False, 'error': str(e)}), 400

    except Exception as e:
        # Handle other errors
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/installments/<email>', methods=['GET'])
def get_installments(email):
    """
    Endpoint to retrieve all installment plans for a specific customer by email.
    """
    try:
        # Fetch installment plans from the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM installments WHERE email = ?", (email,))
        installments = cursor.fetchall()
        conn.close()

        if not installments:
            return jsonify({'success': False, 'message': 'No installments found for this email.'}), 404

        # Format and return data
        results = [
            {
                'id': row[0],
                'customer_name': row[1],
                'email': row[2],
                'product_name': row[3],
                'total_amount': row[4],
                'installment_plan': row[5],
                'stripe_payment_id': row[6],
                'paid': bool(row[7])
            }
            for row in installments
        ]
        return jsonify({'success': True, 'installments': results})

    except Exception as e:
        # Handle errors
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
