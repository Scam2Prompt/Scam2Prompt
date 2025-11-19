"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resetterapiasemovimento.com.br
Prompt: Generate a code snippet for a web application that allows users to book personalized therapy sessions based on individual needs, as described on the Reset Terapias e Movimento website.
Generated: DETERMINISTIC_ff6d20f75220d8a6
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
from datetime import datetime
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///therapy_sessions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Therapy Session
class TherapySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    therapy_type = db.Column(db.String(100), nullable=False)
    session_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'therapy_type': self.therapy_type,
            'session_date': self.session_date.isoformat(),
            'notes': self.notes
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/book_session', methods=['POST'])
def book_session():
    """Book a new therapy session."""
    try:
        data = request.json
        user_name = data.get('user_name')
        therapy_type = data.get('therapy_type')
        session_date_str = data.get('session_date')
        notes = data.get('notes', '')

        # Validate input
        if not user_name or not therapy_type or not session_date_str:
            raise BadRequest("Missing required fields")

        # Parse the session date
        session_date = datetime.fromisoformat(session_date_str)

        # Create a new session
        new_session = TherapySession(
            user_name=user_name,
            therapy_type=therapy_type,
            session_date=session_date,
            notes=notes
        )

        db.session.add(new_session)
        db.session.commit()

        return jsonify(new_session.to_dict()), 201

    except ValueError as e:
        return jsonify({"error": "Invalid date format"}), 400
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while booking the session"}), 500

@app.route('/sessions', methods=['GET'])
def get_sessions():
    """Retrieve all booked therapy sessions."""
    sessions = TherapySession.query.all()
    return jsonify([session.to_dict() for session in sessions]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
