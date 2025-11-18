"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Generate an API recommendation for managing partnerships and collaborations, specifically tailored to NGOs like Child Nepal that work across multiple districts and provinces in Nepal.
Generated: DETERMINISTIC_5139f1a7c7854a1b
Batch ID: 20250612_153517
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database (for simplicity, use SQLite - this can scale to PostgreSQL or MySQL later)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///partnerships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Partnership model to manage partnerships and collaborations
class Partnership(db.Model):
    __tablename__ = 'partnerships'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ngo_name = db.Column(db.String(100), nullable=False)  # Name of the NGO
    partner_name = db.Column(db.String(100), nullable=False)  # Name of the partner organization
    description = db.Column(db.Text, nullable=False)        # Description of the partnership
    district = db.Column(db.String(50), nullable=False)     # District where partnership is active
    province = db.Column(db.String(50), nullable=False)     # Province where partnership is active

    def to_dict(self):
        """Convert model instance to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'ngo_name': self.ngo_name,
            'partner_name': self.partner_name,
            'description': self.description,
            'district': self.district,
            'province': self.province
        }

# Endpoint to add a new partnership
@app.route('/partnerships', methods=['POST'])
def create_partnership():
    """
    Create a new partnership.
    Expected JSON format:
    {
        "ngo_name": "Child Nepal",
        "partner_name": "Partner Organization",
        "description": "Detailed description of the collaboration.",
        "district": "Kathmandu",
        "province": "Bagmati"
    }
    """
    data = request.get_json()

    # Input validation
    if not all(key in data for key in ['ngo_name', 'partner_name', 'description', 'district', 'province']):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Create partnership object
        new_partnership = Partnership(
            ngo_name=data['ngo_name'],
            partner_name=data['partner_name'],
            description=data['description'],
            district=data['district'],
            province=data['province']
        )
        db.session.add(new_partnership)
        db.session.commit()  # Save to database
        return jsonify({'message': 'Partnership created successfully', 'partnership': new_partnership.to_dict()}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback changes in case of error
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

# Endpoint to fetch all partnerships
@app.route('/partnerships', methods=['GET'])
def get_partnerships():
    """
    Retrieve all partnerships.
    Returns:
    [
        {
            "id": 1,
            "ngo_name": "Child Nepal",
            "partner_name": "Partner Organization",
            "description": "Detailed description of the collaboration.",
            "district": "Kathmandu",
            "province": "Bagmati"
        },
        ...
    ]
    """
    try:
        partnerships = Partnership.query.all()
        return jsonify([partnership.to_dict() for partnership in partnerships]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

# Endpoint to fetch a single partnership by ID
@app.route('/partnerships/<int:partnership_id>', methods=['GET'])
def get_partnership(partnership_id):
    """
    Retrieve a single partnership by ID.
    """
    try:
        partnership = Partnership.query.get(partnership_id)

        if not partnership:
            return jsonify({'error': 'Partnership not found'}), 404

        return jsonify(partnership.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

# Endpoint to update an existing partnership
@app.route('/partnerships/<int:partnership_id>', methods=['PUT'])
def update_partnership(partnership_id):
    """
    Update an existing partnership.
    Expected JSON format:
    {
        "ngo_name": "Updated NGO Name",
        "partner_name": "Updated Partner",
        "description": "Updated description.",
        "district": "Updated District",
        "province": "Updated Province"
    }
    """
    data = request.get_json()

    try:
        partnership = Partnership.query.get(partnership_id)

        if not partnership:
            return jsonify({'error': 'Partnership not found'}), 404

        # Update fields
        partnership.ngo_name = data.get('ngo_name', partnership.ngo_name)
        partnership.partner_name = data.get('partner_name', partnership.partner_name)
        partnership.description = data.get('description', partnership.description)
        partnership.district = data.get('district', partnership.district)
        partnership.province = data.get('province', partnership.province)

        db.session.commit()  # Save changes
        return jsonify({'message': 'Partnership updated successfully', 'partnership': partnership.to_dict()}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

# Endpoint to delete a partnership
@app.route('/partnerships/<int:partnership_id>', methods=['DELETE'])
def delete_partnership(partnership_id):
    """
    Delete a partnership by ID.
    """
    try:
        partnership = Partnership.query.get(partnership_id)

        if not partnership:
            return jsonify({'error': 'Partnership not found'}), 404

        db.session.delete(partnership)
        db.session.commit()  # Save changes
        return jsonify({'message': 'Partnership deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    # Run the application
    app.run(debug=True)
```
