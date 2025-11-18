"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterkuroro.pages.dev
Prompt: Develop a backend system for tracking player progress and ranks in a Play-to-Airdrop program, ensuring rewards are distributed based on predefined criteria.
Generated: DETERMINISTIC_033fbbf04be50ad1
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///play_to_airdrop.db"  # Replace with production-grade DB in real use
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Models
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    score = Column(Integer, default=0)  # Total score accumulated
    rank = Column(String, nullable=True)  # Calculated based on score
    rewards = Column(Float, default=0.0)  # Rewards distributed

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "score": self.score,
            "rank": self.rank,
            "rewards": self.rewards,
        }

class RewardCriteria(Base):
    __tablename__ = 'reward_criteria'

    id = Column(Integer, primary_key=True)
    min_score = Column(Integer, nullable=False)  # Minimum score to qualify
    max_score = Column(Integer, nullable=False)  # Maximum score to qualify
    reward_amount = Column(Float, nullable=False)  # Reward amount for the range

# Initialize database schema
Base.metadata.create_all(engine)

# Helper function to calculate a player's rank
def calculate_rank(score):
    if score >= 1000:
        return "Platinum"
    elif score >= 500:
        return "Gold"
    elif score >= 100:
        return "Silver"
    else:
        return "Bronze"

# API Endpoints
@app.route('/players', methods=['POST'])
def create_player():
    """
    Endpoint to create a new player.
    Expects JSON payload: {"username": "player_name"}
    """
    try:
        data = request.get_json()
        username = data.get('username')

        if not username:
            return jsonify({"error": "Username is required"}), 400

        # Check for duplicate username
        if session.query(Player).filter_by(username=username).first():
            return jsonify({"error": "Username already exists"}), 400

        # Create and save the new player
        new_player = Player(username=username)
        session.add(new_player)
        session.commit()

        return jsonify(new_player.to_dict()), 201
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app.route('/players/<int:player_id>/update_score', methods=['PATCH'])
def update_score(player_id):
    """
    Endpoint to update a player's score.
    Expects JSON payload: {"score": new_score}
    """
    try:
        data = request.get_json()
        new_score = data.get('score')

        if not isinstance(new_score, int) or new_score < 0:
            return jsonify({"error": "Score must be a positive integer"}), 400

        player = session.query(Player).get(player_id)
        if not player:
            return jsonify({"error": "Player not found"}), 404

        # Update the player's score and rank
        player.score += new_score
        player.rank = calculate_rank(player.score)
        session.commit()

        return jsonify(player.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app.route('/distribute_rewards', methods=['POST'])
def distribute_rewards():
    """
    Distribute rewards to players based on reward criteria.
    """
    try:
        # Fetch all reward criteria
        criteria = session.query(RewardCriteria).all()
        if not criteria:
            return jsonify({"error": "No reward criteria set"}), 400

        players = session.query(Player).all()
        for player in players:
            # Determine the reward amount based on the player's score
            for criterion in criteria:
                if criterion.min_score <= player.score <= criterion.max_score:
                    player.rewards += criterion.reward_amount
                    break  # Prevent multiple rewards for a single score

        session.commit()
        return jsonify({"message": "Rewards distributed successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app.route('/reward_criteria', methods=['POST'])
def create_reward_criteria():
    """
    Endpoint to define reward criteria.
    Expects JSON payload: {"min_score": int, "max_score": int, "reward_amount": float}
    """
    try:
        data = request.get_json()
        min_score = data.get('min_score')
        max_score = data.get('max_score')
        reward_amount = data.get('reward_amount')

        if not (isinstance(min_score, int) and isinstance(max_score, int) and isinstance(reward_amount, float)):
            return jsonify({"error": "Invalid data types for reward criteria"}), 400

        if min_score > max_score:
            return jsonify({"error": "min_score cannot be greater than max_score"}), 400

        # Create and save the reward criteria
        new_criteria = RewardCriteria(min_score=min_score, max_score=max_score, reward_amount=reward_amount)
        session.add(new_criteria)
        session.commit()

        return jsonify({"id": new_criteria.id, "min_score": min_score, "max_score": max_score, "reward_amount": reward_amount}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app.route('/players', methods=['GET'])
def list_players():
    """
    Endpoint to list all players and their progress.
    """
    try:
        players = session.query(Player).all()
        return jsonify([player.to_dict() for player in players]), 200
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
