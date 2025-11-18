"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Generate code to implement a "Notify Me" feature for out-of-stock items in an e-commerce store, specifically for jewelry products with customizable options like plating and font styles.
Generated: DETERMINISTIC_6cec966c59ddb05d
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from email.mime.text import MIMEText
import smtplib

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notify_me.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the JewelryProduct model
class JewelryProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    plating_option = db.Column(db.String(50), nullable=False)
    font_style = db.Column(db.String(50), nullable=False)
    in_stock = db.Column(db.Boolean, default=True)

# Define the NotifyRequest model
class NotifyRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('jewelry_product.id'), nullable=False)
    requested_date = db.Column(db.DateTime, default=db.func.current_timestamp())

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Helper function to send email notifications
def send_email(to_email, product_name):
    try:
        from_email = 'yourstore@example.com'
        subject = f'Restock Notification: {product_name}'
        body = f'Hello,\n\nThe product "{product_name}" is back in stock. Visit our store to purchase it now!\n\nThank you.'
        
        # Create email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        # Connect to SMTP server and send email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(from_email, 'your-email-password')  # Replace with your credentials
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email notification: {e}")

# Route to handle Notify Me requests
@app.route('/notify-me', methods=['POST'])
def notify_me():
    data = request.json
    try:
        # Validate input data
        email = data.get('email')
        product_id = data.get('product_id')
        if not email or not product_id:
            return jsonify({'error': 'Invalid request data'}), 400

        # Check if product exists and is out of stock
        product = JewelryProduct.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        if product.in_stock:
            return jsonify({'error': 'Product is in stock, no notification needed'}), 400

        # Create a NotifyRequest record
        notify_request = NotifyRequest(email=email, product_id=product_id)
        db.session.add(notify_request)
        db.session.commit()
        return jsonify({'message': 'Notification request submitted successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Duplicate notification request'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# Route to mark a product as back in stock and notify users
@app.route('/mark-in-stock/<int:product_id>', methods=['PUT'])
def mark_in_stock(product_id):
    try:
        # Fetch the product
        product = JewelryProduct.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404

        # Update product status
        product.in_stock = True
        db.session.commit()

        # Notify users who requested notifications
        notify_requests = NotifyRequest.query.filter_by(product_id=product_id).all()
        for request in notify_requests:
            send_email(to_email=request.email, product_name=product.name)

        # Delete notification requests after sending emails
        NotifyRequest.query.filter_by(product_id=product_id).delete()
        db.session.commit()

        return jsonify({'message': 'Product marked as in stock and notifications sent'}), 200
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
