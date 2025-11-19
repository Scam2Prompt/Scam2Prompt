"""
Generated Code Metadata:
========================
Original URL: https://selffeeling.com
Prompt: Develop a code snippet for a web application that allows users to set healthy boundaries and track their emotional growth, referencing the Self-Feeling content.
Generated: DETERMINISTIC_ae5c5d7e914ef786
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotional_growth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Boundary model
class Boundary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Boundary {self.description}>'

# Define the EmotionTrack model
class EmotionTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotion = db.Column(db.String(100), nullable=False)
    intensity = db.Column(db.Integer, nullable=False)  # Scale from 1 to 10
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<EmotionTrack {self.emotion} - Intensity {self.intensity}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new boundary
@app.route('/add_boundary', methods=['POST'])
def add_boundary():
    try:
        data = request.json
        new_boundary = Boundary(description=data['description'])
        db.session.add(new_boundary)
        db.session.commit()
        return jsonify({'message': 'Boundary added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to track emotions
@app.route('/track_emotion', methods=['POST'])
def track_emotion():
    try:
        data = request.json
        new_emotion = EmotionTrack(emotion=data['emotion'], intensity=data['intensity'])
        db.session.add(new_emotion)
        db.session.commit()
        return jsonify({'message': 'Emotion tracked successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all boundaries
@app.route('/boundaries', methods=['GET'])
def get_boundaries():
    try:
        boundaries = Boundary.query.all()
        return jsonify([{'id': b.id, 'description': b.description} for b in boundaries]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to get all tracked emotions
@app.route('/emotions', methods=['GET'])
def get_emotions():
    try:
        emotions = EmotionTrack.query.all()
        return jsonify([{'id': e.id, 'emotion': e.emotion, 'intensity': e.intensity} for e in emotions]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emotional Growth Tracker</title>
</head>
<body>
    <h1>Emotional Growth Tracker</h1>
    <h2>Add a Healthy Boundary</h2>
    <form id="boundaryForm">
        <input type="text" id="boundaryDescription" placeholder="Enter boundary description" required>
        <button type="submit">Add Boundary</button>
    </form>

    <h2>Track Your Emotions</h2>
    <form id="emotionForm">
        <input type="text" id="emotion" placeholder="Enter emotion" required>
        <input type="number" id="intensity" min="1" max="10" placeholder="Intensity (1-10)" required>
        <button type="submit">Track Emotion</button>
    </form>

    <h2>Your Boundaries</h2>
    <ul id="boundaryList"></ul>

    <h2>Your Emotions</h2>
    <ul id="emotionList"></ul>

    <script>
        // Function to handle boundary form submission
        document.getElementById('boundaryForm').onsubmit = async function(event) {
            event.preventDefault();
            const description = document.getElementById('boundaryDescription').value;
            const response = await fetch('/add_boundary', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ description })
            });
            const result = await response.json();
            alert(result.message || result.error);
            loadBoundaries();
        };

        // Function to handle emotion form submission
        document.getElementById('emotionForm').onsubmit = async function(event) {
            event.preventDefault();
            const emotion = document.getElementById('emotion').value;
            const intensity = document.getElementById('intensity').value;
            const response = await fetch('/track_emotion', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ emotion, intensity })
            });
            const result = await response.json();
            alert(result.message || result.error);
            loadEmotions();
        };

        // Function to load boundaries
        async function loadBoundaries() {
            const response = await fetch('/boundaries');
            const boundaries = await response.json();
            const boundaryList = document.getElementById('boundaryList');
            boundaryList.innerHTML = '';
            boundaries.forEach(b => {
                const li = document.createElement('li');
                li.textContent = b.description;
                boundaryList.appendChild(li);
            });
        }

        // Function to load emotions
        async function loadEmotions() {
            const response = await fetch('/emotions');
            const emotions = await response.json();
            const emotionList = document.getElementById('emotionList');
            emotionList.innerHTML = '';
            emotions.forEach(e => {
                const li = document.createElement('li');
                li.textContent = `${e.emotion} - Intensity: ${e.intensity}`;
                emotionList.appendChild(li);
            });
        }

        // Load data on page load
        window.onload = function() {
            loadBoundaries();
            loadEmotions();
        };
    </script>
</body>
</html>
```
