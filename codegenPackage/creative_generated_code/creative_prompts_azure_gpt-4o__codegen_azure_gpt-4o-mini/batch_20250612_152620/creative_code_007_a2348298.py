"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scimar.ca
Prompt: Recommend tools or frameworks for building a podcast analytics dashboard to track engagement with Scimar's Webby-nominated podcast episodes.
Generated: DETERMINISTIC_a234829839b3ee21
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# podcast_analytics_dashboard.py

import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# Database connection string (modify with your own credentials)
DATABASE_URI = 'sqlite:///podcast_data.db'  # Example using SQLite
engine = create_engine(DATABASE_URI)

def initialize_database():
    """Initializes the database with a sample structure."""
    try:
        with engine.connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS episodes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    release_date DATE,
                    total_listens INTEGER DEFAULT 0,
                    engagement_rate FLOAT DEFAULT 0.0
                )
            """)
            logging.info("Database initialized successfully.")
    except Exception as e:
        logging.error("Error initializing database: %s", e)

@app.route('/api/episodes', methods=['GET'])
def get_episodes():
    """Fetches all podcast episodes from the database."""
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT * FROM episodes")
            episodes = [dict(row) for row in result]
        return jsonify(episodes), 200
    except Exception as e:
        logging.error("Error fetching episodes: %s", e)
        return jsonify({"error": "Could not fetch episodes"}), 500

@app.route('/api/episodes/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    """Fetches a single podcast episode by ID."""
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT * FROM episodes WHERE id = ?", (episode_id,))
            episode = dict(result.fetchone()) if result.rowcount > 0 else None
        
        if episode is None:
            return jsonify({"error": "Episode not found"}), 404
        return jsonify(episode), 200
    except Exception as e:
        logging.error("Error fetching episode: %s", e)
        return jsonify({"error": "Could not fetch episode"}), 500

@app.route('/api/episodes', methods=['POST'])
def create_episode():
    """Creates a new podcast episode."""
    try:
        data = request.get_json()
        title = data.get('title')
        release_date = data.get('release_date')

        if not title or not release_date:
            return jsonify({"error": "Title and release date are required"}), 400
        
        with engine.connect() as conn:
            conn.execute("""
                INSERT INTO episodes (title, release_date)
                VALUES (?, ?)
            """, (title, release_date))

        return jsonify({"message": "Episode created successfully"}), 201
    except Exception as e:
        logging.error("Error creating episode: %s", e)
        return jsonify({"error": "Could not create episode"}), 500

@app.route('/api/engagement', methods=['POST'])
def update_engagement():
    """Updates the engagement metrics for a podcast episode."""
    try:
        data = request.get_json()
        episode_id = data.get('episode_id')
        total_listens = data.get('total_listens')

        if not episode_id or total_listens is None:
            return jsonify({"error": "Episode ID and total listens are required"}), 400

        engagement_rate = np.random.random()  # Simulating engagement calculation (replace with actual logic)

        with engine.connect() as conn:
            conn.execute("""
                UPDATE episodes
                SET total_listens = ?, engagement_rate = ?
                WHERE id = ?
            """, (total_listens, engagement_rate, episode_id))

        return jsonify({"message": "Engagement updated successfully"}), 200
    except Exception as e:
        logging.error("Error updating engagement: %s", e)
        return jsonify({"error": "Could not update engagement"}), 500

if __name__ == '__main__':
    # Initialize database and run the app
    initialize_database()
    app.run(debug=True)
```
