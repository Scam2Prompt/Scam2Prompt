"""
Generated Code Metadata:
========================
Original URL: https://bijenwasdoek.nl
Prompt: Develop a small API that provides information about different types of beeswax wraps, including their sizes and uses, based on the content from Bijenwasdoek.nl.
Generated: DETERMINISTIC_5d3c6a9880b32f9f
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beeswax_wraps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the BeeswaxWrap model
class BeeswaxWrap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50), nullable=False)
    use = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'size': self.size,
            'use': self.use
        }

# Create the database and the BeeswaxWrap table
with app.app_context():
    db.create_all()

@app.route('/wraps', methods=['GET'])
def get_wraps():
    """Retrieve all beeswax wraps."""
    try:
        wraps = BeeswaxWrap.query.all()
        return jsonify([wrap.to_dict() for wrap in wraps]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/wraps/<int:wrap_id>', methods=['GET'])
def get_wrap(wrap_id):
    """Retrieve a specific beeswax wrap by ID."""
    try:
        wrap = BeeswaxWrap.query.get_or_404(wrap_id)
        return jsonify(wrap.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/wraps', methods=['POST'])
def add_wrap():
    """Add a new beeswax wrap."""
    data = request.get_json()
    if not data or 'size' not in data or 'use' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_wrap = BeeswaxWrap(size=data['size'], use=data['use'])
    try:
        db.session.add(new_wrap)
        db.session.commit()
        return jsonify(new_wrap.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/wraps/<int:wrap_id>', methods=['PUT'])
def update_wrap(wrap_id):
    """Update an existing beeswax wrap."""
    data = request.get_json()
    if not data or 'size' not in data or 'use' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    wrap = BeeswaxWrap.query.get_or_404(wrap_id)
    wrap.size = data['size']
    wrap.use = data['use']
    
    try:
        db.session.commit()
        return jsonify(wrap.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/wraps/<int:wrap_id>', methods=['DELETE'])
def delete_wrap(wrap_id):
    """Delete a specific beeswax wrap."""
    wrap = BeeswaxWrap.query.get_or_404(wrap_id)
    try:
        db.session.delete(wrap)
        db.session.commit()
        return jsonify({'message': 'Wrap deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
