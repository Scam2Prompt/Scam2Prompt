"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Create a web application to handle customer inquiries and support requests for automotive parts, incorporating features like FAQs and warranty conditions, as described in the "پشتیبانی پرسش‌های پر تکرار" section of the website.
Generated: DETERMINISTIC_dbd54f1564bbf7a5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for Support Requests
class SupportRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    inquiry = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<SupportRequest {self.customer_name}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle inquiries
@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    try:
        # Get data from the request
        customer_name = request.form['customer_name']
        email = request.form['email']
        inquiry = request.form['inquiry']
        
        # Create a new support request
        new_request = SupportRequest(customer_name=customer_name, email=email, inquiry=inquiry)
        db.session.add(new_request)
        db.session.commit()

        # Log the submission
        logging.info(f"New inquiry submitted by {customer_name}")

        return jsonify({'success': True, 'message': 'Inquiry submitted successfully!'}), 200

    except Exception as e:
        logging.error(f"Error submitting inquiry: {e}")
        return jsonify({'success': False, 'message': 'An error occurred while submitting your inquiry.'}), 500

# Route for FAQs
@app.route('/faqs')
def faqs():
    # Static list of FAQs
    faqs_list = [
        {"question": "What is your warranty policy?", "answer": "All parts come with a 1-year warranty."},
        {"question": "How can I track my order?", "answer": "You can track your order using the tracking number provided in your confirmation email."},
        {"question": "What is your return policy?", "answer": "Returns are accepted within 30 days of purchase with a receipt."},
    ]
    return render_template('faqs.html', faqs=faqs_list)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Support</title>
</head>
<body>
    <h1>Customer Support Inquiry</h1>
    <form id="inquiryForm">
        <input type="text" name="customer_name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="inquiry" placeholder="Your Inquiry" required></textarea>
        <button type="submit">Submit Inquiry</button>
    </form>
    <div id="response"></div>

    <script>
    document.getElementById('inquiryForm').onsubmit = async function(e) {
        e.preventDefault(); // Stop the form from submitting the normal way
        try {
            const formData = new FormData(this);
            const response = await fetch('/submit_inquiry', {
                method: 'POST',
                body: formData,
            });
            const result = await response.json();
            document.getElementById('response').innerText = result.message;
        } catch (error) {
            document.getElementById('response').innerText = 'An error occurred. Please try again.';
        }
    };
    </script>
</body>
</html>
```

```html
<!-- templates/faqs.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQs</title>
</head>
<body>
    <h1>Frequently Asked Questions</h1>
    <ul>
        {% for faq in faqs %}
            <li>
                <strong>{{ faq.question }}</strong>
                <p>{{ faq.answer }}</p>
            </li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Please try again later.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

### Requirements
To run this application, make sure to install the necessary packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Database Initialization
Make sure to initialize the database before running the app:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

Now you can start the application by running:
```bash
python app.py
```
