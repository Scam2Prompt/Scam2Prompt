"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Provide code to build a feature that allows users to save a list of desired properties and email it to themselves, similar to the "Envía tu lista de deseos" functionality on the Félix Trujillo Falla website.
Generated: DETERMINISTIC_426490c0d3e7dc02
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/save_property', methods=['POST'])
def save_property():
    """
    Endpoint to save a property to the database.
    Expects JSON data with 'name' and 'location'.
    """
    data = request.json
    if not data or 'name' not in data or 'location' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_property = Property(name=data['name'], location=data['location'])
    try:
        db.session.add(new_property)
        db.session.commit()
        return jsonify({"message": "Property saved successfully!"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/send_properties', methods=['POST'])
def send_properties():
    """
    Endpoint to send a list of properties to the user's email.
    Expects JSON data with 'email'.
    """
    data = request.json
    if not data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        properties = Property.query.all()
        property_list = "\n".join([f"{p.name} - {p.location}" for p in properties])
        
        # Create email content
        msg = MIMEMultipart()
        msg['From'] = 'your_email@example.com'
        msg['To'] = data['email']
        msg['Subject'] = 'Your Desired Properties'
        msg.attach(MIMEText(property_list, 'plain'))

        # Send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')  # Use environment variables in production
            server.sendmail(msg['From'], msg['To'], msg.as_string())

        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
