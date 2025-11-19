"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velemeny.moriczdental.hu
Prompt: Develop a REST API endpoint that allows patients to submit their dental treatment evaluations, capturing details like "doctor's helpfulness" and "pain level during treatment," as seen on the Móricz Dental feedback platform.
Generated: DETERMINISTIC_185bfe0f60ddd7df
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_helpfulness = db.Column(db.Integer, nullable=False)
    pain_level = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id}: Helpfulness={self.doctor_helpfulness}, Pain Level={self.pain_level}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit dental treatment evaluations.
    Expected JSON payload:
    {
        "doctor_helpfulness": int,
        "pain_level": int
    }
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate the incoming data
        if 'doctor_helpfulness' not in data or 'pain_level' not in data:
            return jsonify({"error": "Missing parameters"}), 400
        
        doctor_helpfulness = data['doctor_helpfulness']
        pain_level = data['pain_level']

        # Ensure values are within expected ranges
        if not (1 <= doctor_helpfulness <= 5):
            return jsonify({"error": "Doctor's helpfulness must be between 1 and 5"}), 400
        if not (1 <= pain_level <= 10):
            return jsonify({"error": "Pain level must be between 1 and 10"}), 400

        # Create a new Feedback instance
        new_feedback = Feedback(doctor_helpfulness=doctor_helpfulness, pain_level=pain_level)

        # Add to the session and commit to the database
        db.session.add(new_feedback)
        db.session.commit()

        return jsonify({"message": "Feedback submitted successfully", "feedback_id": new_feedback.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
