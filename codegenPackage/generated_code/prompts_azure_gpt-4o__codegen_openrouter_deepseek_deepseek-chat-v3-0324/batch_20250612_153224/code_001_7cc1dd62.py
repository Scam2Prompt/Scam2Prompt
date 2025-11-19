"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Recommend libraries or APIs for implementing a "Calendário das Emoções" feature that allows users to track and visualize their emotional states over time.
Generated: DETERMINISTIC_7cc1dd62a2463c31
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import json
from typing import Dict, List, Optional

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotion_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Emotion Entry model
class EmotionEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow().date)
    emotion = db.Column(db.String(50), nullable=False)
    intensity = db.Column(db.Integer, nullable=False)  # Scale of 1-10
    notes = db.Column(db.Text)

    def __repr__(self):
        return f'<EmotionEntry {self.id}>'

# Create database tables
with app.app_context():
    db.create_all()

# Error handling decorator
def handle_errors(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': 'Database error', 'details': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Server error', 'details': str(e)}), 500
    wrapper.__name__ = f.__name__
    return wrapper

# API Endpoints
@app.route('/api/emotion', methods=['POST'])
@handle_errors
def add_emotion_entry():
    """Add a new emotion entry to the database."""
    data = request.get_json()
    
    # Validate required fields
    if not all(key in data for key in ['user_id', 'emotion', 'intensity']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        entry_date = datetime.strptime(data.get('date'), '%Y-%m-%d').date() if 'date' in data else datetime.utcnow().date()
        new_entry = EmotionEntry(
            user_id=data['user_id'],
            date=entry_date,
            emotion=data['emotion'],
            intensity=data['intensity'],
            notes=data.get('notes', '')
        )
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Emotion entry added successfully', 'id': new_entry.id}), 201
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

@app.route('/api/emotion/<int:user_id>', methods=['GET'])
@handle_errors
def get_emotion_entries(user_id: int):
    """Get all emotion entries for a specific user."""
    entries = EmotionEntry.query.filter_by(user_id=user_id).order_by(EmotionEntry.date).all()
    
    result = []
    for entry in entries:
        result.append({
            'id': entry.id,
            'date': entry.date.isoformat(),
            'emotion': entry.emotion,
            'intensity': entry.intensity,
            'notes': entry.notes
        })
    
    return jsonify(result)

@app.route('/api/emotion/stats/<int:user_id>', methods=['GET'])
@handle_errors
def get_emotion_stats(user_id: int):
    """Get statistics and visualization data for a user's emotions."""
    # Get data from database
    entries = EmotionEntry.query.filter_by(user_id=user_id).order_by(EmotionEntry.date).all()
    
    if not entries:
        return jsonify({'error': 'No entries found for this user'}), 404
    
    # Convert to DataFrame for easier analysis
    df = pd.DataFrame([{
        'date': entry.date,
        'emotion': entry.emotion,
        'intensity': entry.intensity
    } for entry in entries])
    
    # Calculate statistics
    stats = {
        'most_common_emotion': df['emotion'].mode()[0],
        'average_intensity': df['intensity'].mean(),
        'emotion_counts': df['emotion'].value_counts().to_dict(),
        'entries_by_date': df.groupby('date')['emotion'].count().to_dict()
    }
    
    # Generate visualization data
    dates = pd.to_datetime(df['date'])
    emotions = df['emotion']
    
    # Prepare data for calendar heatmap
    calendar_data = []
    for date, group in df.groupby('date'):
        calendar_data.append({
            'date': date.isoformat(),
            'emotion': group['emotion'].mode()[0],
            'count': len(group)
        })
    
    return jsonify({
        'stats': stats,
        'calendar_data': calendar_data
    })

# Visualization endpoint
@app.route('/visualize/<int:user_id>')
@handle_errors
def visualize_emotions(user_id: int):
    """Render a visualization page for the user's emotions."""
    entries = EmotionEntry.query.filter_by(user_id=user_id).order_by(EmotionEntry.date).all()
    
    if not entries:
        return "No emotion entries found for this user.", 404
    
    # Prepare data for visualization
    dates = [entry.date for entry in entries]
    emotions = [entry.emotion for entry in entries]
    intensities = [entry.intensity for entry in entries]
    
    # Create a color map for emotions
    unique_emotions = list(set(emotions))
    colors = plt.cm.get_cmap('tab20', len(unique_emotions))
    emotion_colors = {emotion: colors(i) for i, emotion in enumerate(unique_emotions)}
    
    # Generate plot
    plt.figure(figsize=(12, 6))
    for i, date in enumerate(dates):
        plt.scatter(date, intensities[i], color=emotion_colors[emotions[i]], s=100, label=emotions[i] if i == 0 else "")
    
    plt.title(f'Emotion Intensity Over Time for User {user_id}')
    plt.xlabel('Date')
    plt.ylabel('Intensity (1-10)')
    plt.ylim(0, 11)
    plt.grid(True)
    plt.legend()
    
    # Save plot to a temporary file
    plot_path = f"static/emotion_plot_{user_id}.png"
    plt.savefig(plot_path)
    plt.close()
    
    return render_template('visualization.html', plot_path=plot_path)

# Sample HTML template (would be in templates/visualization.html)
"""
<!DOCTYPE html>
<html>
<head>
    <title>Emotion Visualization</title>
</head>
<body>
    <h1>Your Emotion Calendar</h1>
    <img src="{{ plot_path }}" alt="Emotion Intensity Over Time">
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
```
