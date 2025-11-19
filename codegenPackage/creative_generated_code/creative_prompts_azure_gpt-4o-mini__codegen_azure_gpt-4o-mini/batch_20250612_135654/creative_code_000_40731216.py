"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatime.pro
Prompt: Generate code for a web application that implements a self-development program similar to the METATIME concept, focusing on body and consciousness integration.
Generated: DETERMINISTIC_407312168737d4a0
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///self_development_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name}>"

# Define the Program model
class Program(db.Model):
    __tablename__ = 'programs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='programs')

    def __repr__(self):
        return f"<Program {self.title}>"

# Route for creating a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    try:
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!", "user_id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route for creating a new program
@app.route('/programs', methods=['POST'])
def create_program():
    data = request.json
    try:
        new_program = Program(title=data['title'], description=data.get('description'), user_id=data['user_id'])
        db.session.add(new_program)
        db.session.commit()
        return jsonify({"message": "Program created successfully!", "program_id": new_program.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route for retrieving all programs for a specific user
@app.route('/users/<int:user_id>/programs', methods=['GET'])
def get_user_programs(user_id):
    try:
        user = User.query.get_or_404(user_id)
        programs = [{'id': p.id, 'title': p.title, 'description': p.description} for p in user.programs]
        return jsonify(programs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
