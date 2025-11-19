"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaimin.pages.dev
Prompt: How do I create a system that allows users to claim $GMRX rewards after earning ELO from their Twitter activity?
Generated: DETERMINISTIC_842bab5210889b42
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import tweepy
from flask import Flask, request, jsonify
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Flask application setup
app = Flask(__name__)

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///rewards.db")  # Use ENV variables for production DB
Base = declarative_base()

# Twitter API setup
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    twitter_handle = Column(String, unique=True, nullable=False)
    elo = Column(Float, default=0.0)  # ELO score earned via Twitter activity
    gmrx_rewards = Column(Float, default=0.0)  # $GMRX rewards balance
    last_claimed = Column(DateTime, default=None)

# Initialize the database
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Helper function to calculate ELO score
def calculate_elo_score(twitter_handle):
    """
    Calculate ELO score based on recent Twitter activity.
    This is a placeholder logic that checks the number of tweets made by a user in the last week.
    Replace this logic with an actual ELO scoring algorithm.
    """
    try:
        tweets = twitter_api.user_timeline(screen_name=twitter_handle, count=100)
        elo_score = sum(1 for tweet in tweets if (datetime.now() - tweet.created_at).days < 7)
        return elo_score
    except tweepy.TweepError as e:
        print(f"Error fetching tweets for {twitter_handle}: {e}")
        return None

# Endpoint to claim rewards
@app.route('/claim_rewards', methods=['POST'])
def claim_rewards():
    """
    POST endpoint to claim $GMRX rewards for the user.
    Expects JSON payload with 'twitter_handle'.
    """
    data = request.json
    if 'twitter_handle' not in data:
        return jsonify({"error": "Missing 'twitter_handle' in request"}), 400
    
    twitter_handle = data['twitter_handle']
    
    try:
        # Fetch or create user
        user = session.query(User).filter_by(twitter_handle=twitter_handle).first()
        if not user:
            user = User(twitter_handle=twitter_handle)
            session.add(user)
            session.commit()
        
        # Calculate ELO score
        elo_score = calculate_elo_score(twitter_handle)
        if elo_score is None:
            return jsonify({"error": f"Unable to calculate ELO score for {twitter_handle}"}), 500
        
        # Update user ELO and $GMRX rewards
        user.elo += elo_score
        user.gmrx_rewards += elo_score * 0.1  # Example conversion rate: 0.1 $GMRX per ELO
        user.last_claimed = datetime.now()
        session.commit()
        
        return jsonify({
            "message": "Rewards claimed successfully!",
            "twitter_handle": twitter_handle,
            "elo": user.elo,
            "gmrx_rewards": user.gmrx_rewards
        }), 200
    
    except Exception as e:
        print(f"Error processing claim for {twitter_handle}: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
