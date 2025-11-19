"""
Generated Code Metadata:
========================
Original URL: https://questn-rewards.web.app
Prompt: Design a basic API structure for a platform that offers quests, events, and rewards, similar to QuestN's features.
Generated: DETERMINISTIC_3f54bda9c80b97e4
Batch ID: 20250622_205230
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rewards = db.relationship('Reward', backref='quest', lazy=True)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'), nullable=False)

# Schemas for serialization
class QuestSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    date = fields.Str(required=True)

class RewardSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str(required=True)
    quest_id = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoints

# Get all quests
@app.route('/quests', methods=['GET'])
def get_quests():
    quests = Quest.query.all()
    quest_schema = QuestSchema(many=True)
    return jsonify(quest_schema.dump(quests)), 200

# Create a new quest
@app.route('/quests', methods=['POST'])
def create_quest():
    quest_schema = QuestSchema()
    try:
        quest_data = quest_schema.load(request.json)
        new_quest = Quest(**quest_data)
        db.session.add(new_quest)
        db.session.commit()
        return quest_schema.dump(new_quest), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    event_schema = EventSchema(many=True)
    return jsonify(event_schema.dump(events)), 200

# Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    event_schema = EventSchema()
    try:
        event_data = event_schema.load(request.json)
        new_event = Event(**event_data)
        db.session.add(new_event)
        db.session.commit()
        return event_schema.dump(new_event), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all rewards for a specific quest
@app.route('/quests/<int:quest_id>/rewards', methods=['GET'])
def get_rewards(quest_id):
    rewards = Reward.query.filter_by(quest_id=quest_id).all()
    reward_schema = RewardSchema(many=True)
    return jsonify(reward_schema.dump(rewards)), 200

# Create a new reward for a specific quest
@app.route('/quests/<int:quest_id>/rewards', methods=['POST'])
def create_reward(quest_id):
    reward_schema = RewardSchema()
    try:
        reward_data = reward_schema.load(request.json)
        new_reward = Reward(**reward_data, quest_id=quest_id)
        db.session.add(new_reward)
        db.session.commit()
        return reward_schema.dump(new_reward), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
