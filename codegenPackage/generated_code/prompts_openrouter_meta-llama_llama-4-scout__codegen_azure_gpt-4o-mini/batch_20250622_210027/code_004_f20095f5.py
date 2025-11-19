"""
Generated Code Metadata:
========================
Original URL: https://protocol-concrete.pages.dev
Prompt: "Design a basic API for managing waitlists and priority access for on-chain financial applications, inspired by Concrete's waitlist feature."
Generated: DETERMINISTIC_f20095f5a4605c58
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waitlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Waitlist
class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    priority = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Waitlist {self.email}>'

# Schema for validating input data
class WaitlistSchema(Schema):
    email = fields.Email(required=True)
    priority = fields.Integer(missing=0)

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to add a user to the waitlist
@app.route('/waitlist', methods=['POST'])
def add_to_waitlist():
    schema = WaitlistSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
        new_entry = Waitlist(email=data['email'], priority=data['priority'])
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({"message": "Added to waitlist", "email": new_entry.email}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Email already in waitlist"}), 409
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

# API endpoint to get the waitlist
@app.route('/waitlist', methods=['GET'])
def get_waitlist():
    try:
        waitlist_entries = Waitlist.query.all()
        result = [{"email": entry.email, "priority": entry.priority} for entry in waitlist_entries]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

# API endpoint to remove a user from the waitlist
@app.route('/waitlist/<int:id>', methods=['DELETE'])
def remove_from_waitlist(id):
    try:
        entry = Waitlist.query.get_or_404(id)
        db.session.delete(entry)
        db.session.commit()
        return jsonify({"message": "Removed from waitlist", "email": entry.email}), 200
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
