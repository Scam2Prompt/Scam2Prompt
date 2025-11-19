"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hostalcasadelmar.es
Prompt: Create a RESTful API for a hotel management system that allows users to reserve rooms and view amenities, taking cues from the unique offerings of Hostal Casa del Mar.
Generated: DETERMINISTIC_5110de76dc199d07
Batch ID: 20250612_162051
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
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Room model
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(50), nullable=False)
    amenities = db.Column(db.String(250), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    is_reserved = db.Column(db.Boolean, default=False)

# Define the schema for serializing Room data
class RoomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Room

# Initialize the database and create the tables
with app.app_context():
    db.create_all()

# Create a route to view available rooms and their amenities
@app.route('/rooms', methods=['GET'])
def get_rooms():
    """Retrieve a list of all available rooms with their amenities."""
    try:
        rooms = Room.query.filter_by(is_reserved=False).all()
        room_schema = RoomSchema(many=True)
        return jsonify(room_schema.dump(rooms)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Create a route to reserve a room
@app.route('/reserve', methods=['POST'])
def reserve_room():
    """Reserve a room by providing the room ID."""
    room_id = request.json.get('room_id')
    if not room_id:
        return jsonify({"error": "Room ID is required."}), 400

    try:
        room = Room.query.get(room_id)
        if not room:
            return jsonify({"error": "Room not found."}), 404
        if room.is_reserved:
            return jsonify({"error": "Room is already reserved."}), 409

        room.is_reserved = True
        db.session.commit()
        return jsonify({"message": "Room reserved successfully."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Create a route to view amenities of a specific room
@app.route('/rooms/<int:room_id>/amenities', methods=['GET'])
def get_room_amenities(room_id):
    """Retrieve the amenities of a specific room by ID."""
    try:
        room = Room.query.get(room_id)
        if not room:
            return jsonify({"error": "Room not found."}), 404
        return jsonify({"amenities": room.amenities}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask for the web framework and SQLAlchemy for database interaction.
- It provides basic endpoints for retrieving available rooms, reserving a room, and obtaining amenities for a specific room.
- Proper error handling is included for various scenarios such as missing room IDs, unavailable rooms, etc.
- The SQLite database is used for simplicity. In a production scenario, a more robust database should be considered.
- Make sure to install the required packages: `Flask`, `Flask-SQLAlchemy`, `Flask-Marshmallow`, and `marshmallow-sqlalchemy`.
