"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Generate a code snippet for a web application that allows users to book a real estate photography session, incorporating features like scheduling and client testimonials.
Generated: DETERMINISTIC_b5cab19b0f2578fe
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photography_sessions.db'
db = SQLAlchemy(app)

# Model for storing client testimonials
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Model for storing photography sessions
class PhotographySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    session_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Route to render the homepage with testimonials
@app.route('/')
def index():
    testimonials = Testimonial.query.all()
    return render_template('index.html', testimonials=testimonials)

# Route to book a photography session
@app.route('/book_session', methods=['POST'])
def book_session():
    data = request.get_json()
    
    # Validate required fields
    if not data or 'client_name' not in data or 'session_date' not in data:
        raise BadRequest('Missing required fields: client_name, session_date.')

    session_date = datetime.strptime(data['session_date'], '%Y-%m-%d %H:%M:%S')
    
    new_session = PhotographySession(client_name=data['client_name'], session_date=session_date)

    db.session.add(new_session)
    db.session.commit()

    return jsonify({'message': 'Session booked successfully!'}), 201

# Route to submit a testimonial
@app.route('/submit_testimonial', methods=['POST'])
def submit_testimonial():
    data = request.get_json()
    
    # Validate required fields
    if not data or 'client_name' not in data or 'message' not in data:
        raise BadRequest('Missing required fields: client_name, message.')

    new_testimonial = Testimonial(client_name=data['client_name'], message=data['message'])

    db.session.add(new_testimonial)
    db.session.commit()

    return jsonify({'message': 'Testimonial submitted successfully!'}), 201

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Photography</title>
</head>
<body>
    <h1>Real Estate Photography Booking</h1>
    
    <h2>Client Testimonials</h2>
    <ul>
        {% for testimonial in testimonials %}
            <li><strong>{{ testimonial.client_name }}:</strong> {{ testimonial.message }}</li>
        {% endfor %}
    </ul>

    <h2>Book a Session</h2>
    <form id="bookingForm">
        <input type="text" id="clientName" placeholder="Your Name" required>
        <input type="datetime-local" id="sessionDate" required>
        <button type="submit">Book Session</button>
    </form>

    <h2>Submit a Testimonial</h2>
    <form id="testimonialForm">
        <input type="text" id="testimonialName" placeholder="Your Name" required>
        <textarea id="testimonialMessage" placeholder="Your Testimonial" required></textarea>
        <button type="submit">Submit Testimonial</button>
    </form>

    <script>
        document.getElementById('bookingForm').onsubmit = async function(e) {
            e.preventDefault();
            const response = await fetch('/book_session', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    client_name: document.getElementById('clientName').value,
                    session_date: new Date(document.getElementById('sessionDate').value).toISOString()
                })
            });
            const result = await response.json();
            alert(result.message);
        };

        document.getElementById('testimonialForm').onsubmit = async function(e) {
            e.preventDefault();
            const response = await fetch('/submit_testimonial', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    client_name: document.getElementById('testimonialName').value,
                    message: document.getElementById('testimonialMessage').value
                })
            });
            const result = await response.json();
            alert(result.message);
        };
    </script>
</body>
</html>
```
