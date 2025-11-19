"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwan.om
Prompt: What libraries or APIs can I use to create a list management feature for an e-commerce platform, inspired by Alwan's functionality?
Generated: DETERMINISTIC_322622bf4669dc52
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for demonstration, can be changed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lists.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the List model
class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<List {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new list
@app.route('/lists', methods=['POST'])
def create_list():
    """Create a new list for a user."""
    data = request.json
    new_list = List(user_id=data['user_id'], name=data['name'])
    
    try:
        db.session.add(new_list)
        db.session.commit()
        return jsonify({"message": "List created", "list_id": new_list.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "List creation failed"}), 400

# Route to get lists for a specific user
@app.route('/lists/<int:user_id>', methods=['GET'])
def get_lists(user_id):
    """Get all lists for a specific user."""
    lists = List.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": lst.id, "name": lst.name} for lst in lists]), 200

# Route to delete a list by ID
@app.route('/lists/<int:list_id>', methods=['DELETE'])
def delete_list(list_id):
    """Delete a specific list by ID."""
    list_to_delete = List.query.get_or_404(list_id)
    
    try:
        db.session.delete(list_to_delete)
        db.session.commit()
        return jsonify({"message": "List deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
