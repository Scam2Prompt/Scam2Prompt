"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cefor.org.br
Prompt: Create an API endpoint that allows users to submit volunteer applications for CEFOR's Casa Abrigo and Projeto Vida services.
Generated: DETERMINISTIC_ef4c5196ba0d9690
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration (Replace with your actual configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cefor_volunteer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the VolunteerApplication model
class VolunteerApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    casa_abrigo = db.Column(db.Boolean, default=False)  # Volunteering for Casa Abrigo
    projeto_vida = db.Column(db.Boolean, default=False)  # Volunteering for Projeto Vida
    message = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "casa_abrigo": self.casa_abrigo,
            "projeto_vida": self.projeto_vida,
            "message": self.message,
        }

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to submit volunteer application
@app.route('/apply', methods=['POST'])
def apply_volunteer():
    try:
        # Parse JSON data from the request
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request payload"}), 400

        # Validate required fields
        name = data.get("name")
        email = data.get("email")
        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        # Create a new VolunteerApplication instance
        application = VolunteerApplication(
            name=name,
            email=email,
            phone=data.get("phone"),
            casa_abrigo=data.get("casa_abrigo", False),
            projeto_vida=data.get("projeto_vida", False),
            message=data.get("message"),
        )

        # Save to the database
        db.session.add(application)
        db.session.commit()

        # Respond with success and the application ID
        return jsonify({"message": "Application submitted successfully", "application_id": application.id}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
