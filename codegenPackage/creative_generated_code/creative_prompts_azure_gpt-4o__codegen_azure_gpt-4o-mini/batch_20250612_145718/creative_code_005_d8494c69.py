"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: Design a game API for managing Squad Kombat characters, skins, and time-limited events, referencing the Q3 2024 launch details from the Hamster Kombat roadmap.
Generated: DETERMINISTIC_d8494c69de523ae1
Batch ID: 20250612_145718
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///squad_kombat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Character(db.Model):
    """Model representing a character in the game."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    skin_id = db.Column(db.Integer, db.ForeignKey('skin.id'), nullable=True)

    def __repr__(self):
        return f"<Character {self.name}>"

class Skin(db.Model):
    """Model representing a skin for characters."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Skin {self.name}>"

class Event(db.Model):
    """Model representing a time-limited event."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Event {self.title}>"

# Schemas for data validation
class CharacterSchema(Schema):
    """Schema for character input validation."""
    name = fields.Str(required=True)
    skin_id = fields.Int()

class SkinSchema(Schema):
    """Schema for skin input validation."""
    name = fields.Str(required=True)
    description = fields.Str()

class EventSchema(Schema):
    """Schema for event input validation."""
    title = fields.Str(required=True)
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Character routes
@app.route('/characters', methods=['POST'])
def add_character():
    """Add a new character."""
    try:
        data = request.get_json()
        CharacterSchema().load(data)  # Validate input
        new_character = Character(name=data['name'], skin_id=data.get('skin_id'))
        db.session.add(new_character)
        db.session.commit()
        return jsonify({"message": "Character created", "character": data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/characters', methods=['GET'])
def get_characters():
    """Get all characters."""
    characters = Character.query.all()
    return jsonify([{'id': char.id, 'name': char.name, 'skin_id': char.skin_id} for char in characters]), 200

# Skin routes
@app.route('/skins', methods=['POST'])
def add_skin():
    """Add a new skin."""
    try:
        data = request.get_json()
        SkinSchema().load(data)  # Validate input
        new_skin = Skin(name=data['name'], description=data.get('description'))
        db.session.add(new_skin)
        db.session.commit()
        return jsonify({"message": "Skin created", "skin": data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/skins', methods=['GET'])
def get_skins():
    """Get all skins."""
    skins = Skin.query.all()
    return jsonify([{'id': skin.id, 'name': skin.name, 'description': skin.description} for skin in skins]), 200

# Event routes
@app.route('/events', methods=['POST'])
def add_event():
    """Add a new time-limited event."""
    try:
        data = request.get_json()
        EventSchema().load(data)  # Validate input
        new_event = Event(
            title=data['title'],
            start_time=datetime.fromisoformat(data['start_time']),
            end_time=datetime.fromisoformat(data['end_time'])
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({"message": "Event created", "event": data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/events', methods=['GET'])
def get_events():
    """Get all time-limited events."""
    events = Event.query.all()
    return jsonify([{'id': event.id, 'title': event.title, 'start_time': event.start_time.isoformat(), 'end_time': event.end_time.isoformat()} for event in events]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
