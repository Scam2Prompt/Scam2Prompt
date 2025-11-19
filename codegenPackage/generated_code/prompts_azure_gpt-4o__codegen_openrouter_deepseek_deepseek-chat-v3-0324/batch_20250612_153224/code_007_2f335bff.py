"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Provide sample code for integrating a customer feedback system into a computer repair service website, inspired by Geeks On Repair’s emphasis on customer satisfaction.
Generated: DETERMINISTIC_2f335bff464fee1d
Batch ID: 20250612_153224
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
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    service_type = db.Column(db.String(100), nullable=False)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.id}>'

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    """Render the home page with feedback form."""
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """Handle feedback submission."""
    try:
        data = request.form
        
        # Validate required fields
        if not all(key in data for key in ['name', 'email', 'rating', 'service_type']):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create new feedback entry
        new_feedback = Feedback(
            customer_name=data['name'],
            email=data['email'],
            rating=int(data['rating']),
            comments=data.get('comments', ''),
            service_type=data['service_type']
        )

        db.session.add(new_feedback)
        db.session.commit()

        return jsonify({'message': 'Feedback submitted successfully!'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Retrieve all feedback entries."""
    try:
        feedback_list = Feedback.query.order_by(Feedback.date_submitted.desc()).all()
        feedback_data = [{
            'id': feedback.id,
            'customer_name': feedback.customer_name,
            'email': feedback.email,
            'rating': feedback.rating,
            'comments': feedback.comments,
            'service_type': feedback.service_type,
            'date_submitted': feedback.date_submitted.strftime('%Y-%m-%d %H:%M:%S')
        } for feedback in feedback_list]

        return jsonify(feedback_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

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
    <title>Geeks On Repair - Feedback</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, select, textarea { width: 100%; padding: 8px; box-sizing: border-box; }
        button { background: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
        button:hover { background: #45a049; }
        .success { color: green; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>Customer Feedback</h1>
    <p>We value your opinion! Please let us know about your experience with our service.</p>
    
    <form id="feedbackForm">
        <div class="form-group">
            <label for="name">Name*</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email*</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="service_type">Service Type*</label>
            <select id="service_type" name="service_type" required>
                <option value="">Select a service</option>
                <option value="Laptop Repair">Laptop Repair</option>
                <option value="Desktop Repair">Desktop Repair</option>
                <option value="Data Recovery">Data Recovery</option>
                <option value="Virus Removal">Virus Removal</option>
                <option value="Other">Other</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="rating">Rating (1-5)*</label>
            <select id="rating" name="rating" required>
                <option value="">Select a rating</option>
                <option value="1">1 - Poor</option>
                <option value="2">2 - Fair</option>
                <option value="3">3 - Good</option>
                <option value="4">4 - Very Good</option>
                <option value="5">5 - Excellent</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="comments">Comments</label>
            <textarea id="comments" name="comments" rows="4"></textarea>
        </div>
        
        <button type="submit">Submit Feedback</button>
    </form>
    
    <div id="message"></div>
    
    <script>
        document.getElementById('feedbackForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const form = e.target;
            const formData = new FormData(form);
            const messageDiv = document.getElementById('message');
            
            try {
                const response = await fetch('/submit_feedback', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    messageDiv.className = 'success';
                    messageDiv.textContent = data.message;
                    form.reset();
                } else {
                    messageDiv.className = 'error';
                    messageDiv.textContent = data.error || 'Error submitting feedback';
                }
            } catch (error) {
                messageDiv.className = 'error';
                messageDiv.textContent = 'Network error. Please try again.';
            }
        });
    </script>
</body>
</html>
```
