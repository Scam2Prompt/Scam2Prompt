"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Suggest tools or APIs to monitor and report daily progress for passing prop firm challenges, including metrics like drawdown, profit targets, and time remaining.
Generated: DETERMINISTIC_7f7f448151e5a6ae
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Monitoring and Reporting Tool for Prop Firm Challenges

This script uses Flask to create an API for monitoring and reporting daily progress
for passing prop firm challenges. Metrics include drawdown, profit targets, and time remaining.

Dependencies:
- Flask: For creating the API
- SQLAlchemy: For database interactions
- SQLite: Local database for storing challenge data

Make sure to install the required packages before running the script:
    pip install flask sqlalchemy
"""

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE_URL = "sqlite:///prop_firm_challenges.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the database model for the challenges
class Challenge(Base):
    __tablename__ = "challenges"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Friendly name for the challenge
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    profit_target = Column(Float, nullable=False)
    max_drawdown = Column(Float, nullable=False)
    current_profit = Column(Float, default=0.0)
    current_drawdown = Column(Float, default=0.0)

# Create the database table if it doesn't already exist
Base.metadata.create_all(engine)

# Helper function to calculate time remaining
def calculate_time_remaining(end_date):
    today = datetime.date.today()
    delta = end_date - today
    return delta.days if delta.days >= 0 else 0

# API Endpoint: Add a new challenge
@app.route('/challenges', methods=['POST'])
def add_challenge():
    try:
        data = request.json
        challenge = Challenge(
            name=data['name'],
            start_date=datetime.datetime.strptime(data['start_date'], "%Y-%m-%d").date(),
            end_date=datetime.datetime.strptime(data['end_date'], "%Y-%m-%d").date(),
            profit_target=data['profit_target'],
            max_drawdown=data['max_drawdown']
        )
        session.add(challenge)
        session.commit()
        return jsonify({"message": "Challenge added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API Endpoint: Update progress for a challenge
@app.route('/challenges/<int:challenge_id>', methods=['PUT'])
def update_challenge(challenge_id):
    try:
        data = request.json
        challenge = session.query(Challenge).filter_by(id=challenge_id).first()
        if not challenge:
            return jsonify({"error": "Challenge not found"}), 404

        if 'current_profit' in data:
            challenge.current_profit = data['current_profit']
        if 'current_drawdown' in data:
            challenge.current_drawdown = data['current_drawdown']
        session.commit()
        return jsonify({"message": "Challenge updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API Endpoint: Get progress report for a challenge
@app.route('/challenges/<int:challenge_id>/report', methods=['GET'])
def get_challenge_report(challenge_id):
    try:
        challenge = session.query(Challenge).filter_by(id=challenge_id).first()
        if not challenge:
            return jsonify({"error": "Challenge not found"}), 404

        time_remaining = calculate_time_remaining(challenge.end_date)
        report = {
            "name": challenge.name,
            "profit_target": challenge.profit_target,
            "max_drawdown": challenge.max_drawdown,
            "current_profit": challenge.current_profit,
            "current_drawdown": challenge.current_drawdown,
            "time_remaining_days": time_remaining,
            "is_profit_target_met": challenge.current_profit >= challenge.profit_target,
            "is_drawdown_limit_exceeded": challenge.current_drawdown > challenge.max_drawdown
        }
        return jsonify(report), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API Endpoint: List all challenges
@app.route('/challenges', methods=['GET'])
def list_challenges():
    try:
        challenges = session.query(Challenge).all()
        challenge_list = [
            {
                "id": challenge.id,
                "name": challenge.name,
                "start_date": challenge.start_date.strftime("%Y-%m-%d"),
                "end_date": challenge.end_date.strftime("%Y-%m-%d"),
                "profit_target": challenge.profit_target,
                "max_drawdown": challenge.max_drawdown,
                "current_profit": challenge.current_profit,
                "current_drawdown": challenge.current_drawdown
            }
            for challenge in challenges
        ]
        return jsonify(challenge_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
