"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftbuy.site
Prompt: Suggest an API for tracking user engagement metrics (e.g., playtime, clicks) for games like "Skibidi Toilet Wars" and "Tank War Two Player" on a gaming platform.
Generated: DETERMINISTIC_f28221051334b9c9
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engagement_metrics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the EngagementMetric model
class EngagementMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    playtime = db.Column(db.Integer, nullable=False)  # in seconds
    clicks = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<EngagementMetric {self.game_title}, User {self.user_id}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/engagement', methods=['POST'])
def track_engagement():
    """
    API endpoint to track user engagement metrics for games.
    Expects JSON data with game_title, user_id, playtime, and clicks.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        game_title = data.get('game_title')
        user_id = data.get('user_id')
        playtime = data.get('playtime')
        clicks = data.get('clicks')

        # Validate incoming data
        if not all([game_title, user_id, isinstance(playtime, int), isinstance(clicks, int)]):
            return jsonify({"error": "Invalid data provided"}), 400

        # Create a new EngagementMetric instance
        metric = EngagementMetric(game_title=game_title, user_id=user_id, playtime=playtime, clicks=clicks)
        db.session.add(metric)
        db.session.commit()

        logging.info(f"Engagement recorded: {metric}")

        return jsonify({"message": "Engagement metric tracked successfully"}), 201

    except Exception as e:
        logging.error(f"Error tracking engagement: {e}")
        return jsonify({"error": "An error occurred while tracking engagement metrics"}), 500

@app.route('/api/engagement/<user_id>', methods=['GET'])
def get_user_engagement(user_id):
    """
    API endpoint to retrieve engagement metrics for a specific user.
    """
    try:
        metrics = EngagementMetric.query.filter_by(user_id=user_id).all()
        if not metrics:
            return jsonify({"error": "No engagement metrics found for this user"}), 404

        return jsonify([{
            "game_title": metric.game_title,
            "playtime": metric.playtime,
            "clicks": metric.clicks,
            "timestamp": metric.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for metric in metrics]), 200

    except Exception as e:
        logging.error(f"Error retrieving engagement metrics for user {user_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving engagement metrics"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
