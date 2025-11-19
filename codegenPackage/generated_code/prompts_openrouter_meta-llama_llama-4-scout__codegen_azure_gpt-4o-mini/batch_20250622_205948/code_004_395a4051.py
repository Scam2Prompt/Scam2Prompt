"""
Generated Code Metadata:
========================
Original URL: https://wpcontrol.be
Prompt: "Design a REST API for WPControl to manage WordPress themes and patterns remotely."
Generated: DETERMINISTIC_395a405187a9cb7b
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wpcontrol.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Theme model
class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    version = db.Column(db.String(20), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'version': self.version,
            'is_active': self.is_active
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Create a new theme
@app.route('/themes', methods=['POST'])
def create_theme():
    data = request.get_json()
    if not data or 'name' not in data or 'version' not in data:
        abort(400)

    new_theme = Theme(name=data['name'], version=data['version'])
    db.session.add(new_theme)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400)

    return jsonify(new_theme.to_dict()), 201

# Get all themes
@app.route('/themes', methods=['GET'])
def get_themes():
    themes = Theme.query.all()
    return jsonify([theme.to_dict() for theme in themes]), 200

# Get a specific theme by ID
@app.route('/themes/<int:theme_id>', methods=['GET'])
def get_theme(theme_id):
    theme = Theme.query.get_or_404(theme_id)
    return jsonify(theme.to_dict()), 200

# Update a theme
@app.route('/themes/<int:theme_id>', methods=['PUT'])
def update_theme(theme_id):
    theme = Theme.query.get_or_404(theme_id)
    data = request.get_json()

    if 'name' in data:
        theme.name = data['name']
    if 'version' in data:
        theme.version = data['version']
    if 'is_active' in data:
        theme.is_active = data['is_active']

    db.session.commit()
    return jsonify(theme.to_dict()), 200

# Delete a theme
@app.route('/themes/<int:theme_id>', methods=['DELETE'])
def delete_theme(theme_id):
    theme = Theme.query.get_or_404(theme_id)
    db.session.delete(theme)
    db.session.commit()
    return jsonify({'message': 'Theme deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
