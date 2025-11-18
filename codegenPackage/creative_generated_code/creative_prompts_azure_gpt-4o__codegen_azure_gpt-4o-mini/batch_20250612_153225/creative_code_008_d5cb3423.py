"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgastepanova.com.ua
Prompt: Develop a web application that allows users to book consultations with a nutritionist, select services like Ayurvedic consultations, and receive follow-up plans, modeled after Olga Stepanova's offerings.
Generated: DETERMINISTIC_d5cb34234b81d98a
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

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for consultations
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    consultation_date = db.Column(db.DateTime, nullable=False)
    follow_up_plan = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Consultation {self.id} - {self.user_name}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to render the booking form
@app.route('/')
def index():
    return render_template('index.html')

# Route to book a consultation
@app.route('/book', methods=['POST'])
def book_consultation():
    data = request.get_json()
    # Validate input
    if 'user_name' not in data or 'service_type' not in data or 'consultation_date' not in data:
        raise BadRequest("Missing required fields: user_name, service_type, or consultation_date")
    
    consultation_date = datetime.fromisoformat(data['consultation_date'])

    # Create and save consultation
    consultation = Consultation(
        user_name=data['user_name'],
        service_type=data['service_type'],
        consultation_date=consultation_date
    )

    db.session.add(consultation)
    db.session.commit()

    return jsonify({"message": "Consultation booked successfully", "id": consultation.id}), 201

# Route to retrieve consultation details
@app.route('/consultation/<int:id>', methods=['GET'])
def get_consultation(id):
    consultation = Consultation.query.get(id)
    if consultation is None:
        raise NotFound("Consultation not found")

    return jsonify({
        "user_name": consultation.user_name,
        "service_type": consultation.service_type,
        "consultation_date": consultation.consultation_date.isoformat(),
        "follow_up_plan": consultation.follow_up_plan
    })

# Route to update follow-up plan
@app.route('/consultation/<int:id>/followup', methods=['PUT'])
def update_followup(id):
    consultation = Consultation.query.get(id)
    if consultation is None:
        raise NotFound("Consultation not found")

    data = request.get_json()
    consultation.follow_up_plan = data.get('follow_up_plan', consultation.follow_up_plan)

    db.session.commit()

    return jsonify({"message": "Follow-up plan updated successfully"})

# Error handling for 404 - Not Found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for 400 - Bad Request
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

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
    <title>Book a Consultation</title>
    <script>
        async function bookConsultation() {
            const userName = document.getElementById('user_name').value;
            const serviceType = document.getElementById('service_type').value;
            const consultationDate = document.getElementById('consultation_date').value;

            const response = await fetch('/book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_name: userName,
                    service_type: serviceType,
                    consultation_date: consultationDate
                })
            });

            const result = await response.json();
            alert(result.message);
        }
    </script>
</head>
<body>
    <h1>Book a Consultation with a Nutritionist</h1>
    <form onsubmit="event.preventDefault(); bookConsultation();">
        <label for="user_name">Your Name:</label>
        <input type="text" id="user_name" required>
        <br>
        <label for="service_type">Service Type:</label>
        <select id="service_type" required>
            <option value="Ayurvedic Consultation">Ayurvedic Consultation</option>
            <option value="Nutritional Counseling">Nutritional Counseling</option>
        </select>
        <br>
        <label for="consultation_date">Consultation Date:</label>
        <input type="datetime-local" id="consultation_date" required>
        <br>
        <button type="submit">Book Consultation</button>
    </form>
</body>
</html>
```
