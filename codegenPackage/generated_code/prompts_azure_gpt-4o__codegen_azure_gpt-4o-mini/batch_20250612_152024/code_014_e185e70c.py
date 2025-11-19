"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Generate code to build a student community platform for sharing IELTS and PTE preparation tips, inspired by the student community mentioned on RNW International's website.
Generated: DETERMINISTIC_e185e70cd956572f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_community.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the StudentTip model
class StudentTip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    tip = db.Column(db.Text, nullable=False)

# Define the schema for validation
class StudentTipSchema(Schema):
    username = fields.Str(required=True)
    tip = fields.Str(required=True)

# Initialize the schema
tip_schema = StudentTipSchema()
tips_schema = StudentTipSchema(many=True)

# Route to create a new tip
@app.route('/tips', methods=['POST'])
def create_tip():
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = tip_schema.load(data)

        # Create a new StudentTip instance
        new_tip = StudentTip(username=validated_data['username'], tip=validated_data['tip'])
        db.session.add(new_tip)
        db.session.commit()

        return jsonify(tip_schema.dump(new_tip)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all tips
@app.route('/tips', methods=['GET'])
def get_tips():
    try:
        tips = StudentTip.query.all()
        return jsonify(tips_schema.dump(tips)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific tip by ID
@app.route('/tips/<int:tip_id>', methods=['GET'])
def get_tip(tip_id):
    try:
        tip = StudentTip.query.get_or_404(tip_id)
        return jsonify(tip_schema.dump(tip)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a tip
@app.route('/tips/<int:tip_id>', methods=['DELETE'])
def delete_tip(tip_id):
    try:
        tip = StudentTip.query.get_or_404(tip_id)
        db.session.delete(tip)
        db.session.commit()
        return jsonify({"message": "Tip deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

### Environment Variables
Set the `DATABASE_URL` environment variable to configure the database connection string. If not set, it defaults to a SQLite database named `students.db`.
