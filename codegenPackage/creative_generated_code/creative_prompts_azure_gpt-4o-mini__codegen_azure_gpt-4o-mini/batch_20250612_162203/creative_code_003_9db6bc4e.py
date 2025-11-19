"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordoflifenw.com
Prompt: Create a RESTful API design for a church community platform that supports features like member engagement and ministry updates, reflecting the mission of Word of Life Northwest.
Generated: DETERMINISTIC_9db6bc4eb9a44303
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import logging

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///church_community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

# Define the MinistryUpdate model
class MinistryUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# Endpoint to create a new member
@app.route('/members', methods=['POST'])
def create_member():
    data = request.get_json()
    new_member = Member(name=data['name'], email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({"message": "Member created", "id": new_member.id}), 201

# Endpoint to get all members
@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{"id": member.id, "name": member.name, "email": member.email, "active": member.active} for member in members]), 200

# Endpoint to create a new ministry update
@app.route('/updates', methods=['POST'])
def create_update():
    data = request.get_json()
    new_update = MinistryUpdate(title=data['title'], content=data['content'])
    db.session.add(new_update)
    db.session.commit()
    return jsonify({"message": "Update created", "id": new_update.id}), 201

# Endpoint to get all ministry updates
@app.route('/updates', methods=['GET'])
def get_updates():
    updates = MinistryUpdate.query.all()
    return jsonify([{"id": update.id, "title": update.title, "content": update.content, "created_at": update.created_at} for update in updates]), 200

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
