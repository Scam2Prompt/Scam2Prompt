"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thaizslots.site
Prompt: Provide an example of how to integrate a VIP group sharing feature into a gaming application, inspired by the content on thaizslots.site.
Generated: DETERMINISTIC_90d3b418ed00db3f
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for VIP Group
class VIPGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    members = db.relationship('User', backref='vip_group', lazy=True)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    vip_group_id = db.Column(db.Integer, db.ForeignKey('vIP_group.id'), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/create_vip_group', methods=['POST'])
def create_vip_group():
    """Create a new VIP group."""
    data = request.json
    group_name = data.get('name')

    if not group_name:
        return jsonify({"error": "Group name is required."}), 400

    new_group = VIPGroup(name=group_name)
    db.session.add(new_group)
    try:
        db.session.commit()
        return jsonify({"message": "VIP group created successfully.", "group_id": new_group.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Group name must be unique."}), 400

@app.route('/add_member', methods=['POST'])
def add_member():
    """Add a user to an existing VIP group."""
    data = request.json
    username = data.get('username')
    group_id = data.get('group_id')

    if not username or not group_id:
        return jsonify({"error": "Username and group ID are required."}), 400

    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"error": "User does not exist."}), 404

    group = VIPGroup.query.get(group_id)
    if group is None:
        return jsonify({"error": "VIP group does not exist."}), 404

    user.vip_group = group
    db.session.commit()
    return jsonify({"message": f"User {username} added to group {group.name}."}), 200

@app.route('/get_vip_group/<int:group_id>', methods=['GET'])
def get_vip_group(group_id):
    """Retrieve details of a VIP group, including its members."""
    group = VIPGroup.query.get(group_id)

    if group is None:
        return jsonify({"error": "VIP group does not exist."}), 404

    members = [user.username for user in group.members]
    return jsonify({"group_id": group.id, "group_name": group.name, "members": members}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a simple Flask application for managing a VIP group sharing feature in a gaming application. It includes endpoints for creating a VIP group, adding members, and retrieving group details. Error handling is implemented for various edge cases, and the database is set up using SQLAlchemy with SQLite as the backend.
