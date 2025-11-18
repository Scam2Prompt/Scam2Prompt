"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mocaverse-b29.pages.dev
Prompt: Recommend best practices for designing an NFT quest system similar to Mocaverse, incorporating features like rankings and gamified experiences.
Generated: DETERMINISTIC_e3fab974c6b3cf6a
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_quests.db'
db = SQLAlchemy(app)

# Database Model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    ranking = db.Column(db.Integer, default=0)

# Database Model for Quests
class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    reward = db.Column(db.String(50), nullable=False)

# Schema for User
class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    ranking = fields.Int()

# Schema for Quest
class QuestSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    reward = fields.Str(required=True)

# Initialize database (run this once to create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        user_schema = UserSchema()
        user = user_schema.load(user_data)
        new_user = User(**user)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to create a new quest
@app.route('/quests', methods=['POST'])
def create_quest():
    try:
        quest_data = request.get_json()
        quest_schema = QuestSchema()
        quest = quest_schema.load(quest_data)
        new_quest = Quest(**quest)
        db.session.add(new_quest)
        db.session.commit()
        return quest_schema.jsonify(new_quest), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all quests
@app.route('/quests', methods=['GET'])
def get_quests():
    try:
        quests = Quest.query.all()
        quest_schema = QuestSchema(many=True)
        return quest_schema.jsonify(quests), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get user rankings
@app.route('/rankings', methods=['GET'])
def get_rankings():
    try:
        users = User.query.order_by(User.ranking.desc()).all()
        user_schema = UserSchema(many=True)
        return user_schema.jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
```
