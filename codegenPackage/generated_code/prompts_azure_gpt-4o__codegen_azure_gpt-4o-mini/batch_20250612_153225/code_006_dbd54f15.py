"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Create a web application to handle customer inquiries and support requests for automotive parts, incorporating features like FAQs and warranty conditions, as described in the "پشتیبانی پرسش‌های پر تکرار" section of the website.
Generated: DETERMINISTIC_dbd54f1564bbf7a5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the SupportRequest model
class SupportRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    inquiry = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<SupportRequest {self.id} - {self.customer_name}>'

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to submit a support request
@app.route('/submit_request', methods=['POST'])
def submit_request():
    try:
        data = request.get_json()
        new_request = SupportRequest(
            customer_name=data['customer_name'],
            email=data['email'],
            inquiry=data['inquiry']
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'Support request submitted successfully!'}), 201
    except Exception as e:
        logging.error(f'Error submitting request: {e}')
        return jsonify({'error': 'Failed to submit request.'}), 500

# Route to get FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = [
        {"question": "What is the warranty period?", "answer": "The warranty period is 1 year from the date of purchase."},
        {"question": "How can I return a part?", "answer": "You can return a part within 30 days of purchase with a receipt."},
        # Add more FAQs as needed
    ]
    return jsonify(faqs), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Support</title>
</head>
<body>
    <h1>Customer Support for Automotive Parts</h1>
    <form id="supportRequestForm">
        <input type="text" id="customer_name" placeholder="Your Name" required>
        <input type="email" id="email" placeholder="Your Email" required>
        <textarea id="inquiry" placeholder="Your Inquiry" required></textarea>
        <button type="submit">Submit Request</button>
    </form>
    <div id="responseMessage"></div>

    <script>
        document.getElementById('supportRequestForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const data = {
                customer_name: document.getElementById('customer_name').value,
                email: document.getElementById('email').value,
                inquiry: document.getElementById('inquiry').value
            };

            fetch('/submit_request', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('responseMessage').innerText = data.message || data.error;
            })
            .catch(error => {
                document.getElementById('responseMessage').innerText = 'An error occurred.';
            });
        });
    </script>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- The database is set to SQLite for simplicity; you can change it to any other database as needed.
- The HTML template is included for the front-end interface.
