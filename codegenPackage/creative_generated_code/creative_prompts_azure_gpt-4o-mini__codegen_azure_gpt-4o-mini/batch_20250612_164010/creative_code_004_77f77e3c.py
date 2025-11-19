"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://howtosuecslplasma.org
Prompt: Provide a code snippet for a web application that allows users to share their experiences with CSL Plasma and connect for potential class action lawsuits.
Generated: DETERMINISTIC_77f77e3cdf019b28
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the web application
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experiences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Experience model for storing user experiences
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    experience_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Experience {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to render the main page
@app.route('/')
def index():
    # Fetch all experiences to display them
    experiences = Experience.query.all()
    return render_template('index.html', experiences=experiences)

# Route to submit a new experience
@app.route('/submit', methods=['POST'])
def submit_experience():
    try:
        # Get data from the form
        username = request.form['username']
        experience_text = request.form['experience_text']

        # Validate input
        if not username or not experience_text:
            return jsonify({'error': 'Username and experience text are required!'}), 400
        
        # Create a new experience entry
        new_experience = Experience(username=username, experience_text=experience_text)
        db.session.add(new_experience)
        db.session.commit()

        return jsonify({'message': 'Experience submitted successfully!'}), 201
    except Exception as e:
        # Handle any errors that occur during submission
        return jsonify({'error': str(e)}), 500

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
    <title>CSL Plasma Experiences</title>
</head>
<body>
    <h1>Share Your Experience with CSL Plasma</h1>
    <form action="/submit" method="POST">
        <label for="username">Your Name:</label>
        <input type="text" id="username" name="username" required>
        <label for="experience_text">Your Experience:</label>
        <textarea id="experience_text" name="experience_text" required></textarea>
        <button type="submit">Submit</button>
    </form>
    <h2>Shared Experiences</h2>
    <ul>
        {% for experience in experiences %}
            <li><strong>{{ experience.username }}</strong>: {{ experience.experience_text }} ({{ experience.created_at }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
- Save the HTML template in a folder named `templates` in the same directory as your Python script.
- This example uses SQLite as a database; adjust the database URI for production use.
