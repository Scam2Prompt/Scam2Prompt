"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockguild.pages.dev
Prompt: Recommend APIs or libraries for building a blockchain-based leaderboard system similar to Guild Pins on Guild.xyz, including support for multiple categories.
Generated: DETERMINISTIC_9f6773c3d9b468fd
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE_URL = 'sqlite:///leaderboard.db'  # Change to your preferred database
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    scores = relationship("Score", back_populates="user")

# Define Score model
class Score(Base):
    __tablename__ = 'scores'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category = Column(String, nullable=False)
    points = Column(Integer, nullable=False)

    user = relationship("User", back_populates="scores")

# Create the database tables
Base.metadata.create_all(engine)

# Define schema for request validation
class UserSchema(Schema):
    username = fields.Str(required=True)

class ScoreSchema(Schema):
    user_id = fields.Int(required=True)
    category = fields.Str(required=True)
    points = fields.Int(required=True)

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Validate incoming request data
        user_schema = UserSchema()
        user_data = user_schema.load(request.json)
        
        with Session() as session:
            new_user = User(username=user_data['username'])
            session.add(new_user)
            session.commit()
        
        return jsonify({"message": "User created successfully!"}), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to submit a score
@app.route('/scores', methods=['POST'])
def submit_score():
    try:
        # Validate incoming request data
        score_schema = ScoreSchema()
        score_data = score_schema.load(request.json)
        
        with Session() as session:
            new_score = Score(user_id=score_data['user_id'], category=score_data['category'], points=score_data['points'])
            session.add(new_score)
            session.commit()
        
        return jsonify({"message": "Score submitted successfully!"}), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    category = request.args.get('category')
    
    try:
        with Session() as session:
            if category:
                scores = session.query(Score).filter_by(category=category).order_by(Score.points.desc()).all()
            else:
                scores = session.query(Score).order_by(Score.points.desc()).all()

            leaderboard = [{"username": score.user.username, "category": score.category, "points": score.points} for score in scores]
        
        return jsonify(leaderboard), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
