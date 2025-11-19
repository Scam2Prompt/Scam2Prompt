"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Generate a code snippet for a web application that allows students to track their progress in preparing for admission exams, focusing on features like topic feedback and study resources.
Generated: DETERMINISTIC_bbd84797d0ed4a76
Batch ID: 20250612_162203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web framework and data handling
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure key

# Initialize the database
db = SQLAlchemy(app)

# Define the Topic model
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.String(200), nullable=True)
    resource_link = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Topic {self.name}>'

# Route for home page
@app.route('/')
def index():
    topics = Topic.query.all()  # Fetch all topics from the database
    return render_template('index.html', topics=topics)

# Route to add a new topic
@app.route('/add', methods=['POST'])
def add_topic():
    try:
        topic_name = request.form['name']
        feedback = request.form['feedback']
        resource_link = request.form['resource_link']

        # Validate input
        if not topic_name:
            flash('Topic name is required!', 'danger')
            return redirect(url_for('index'))

        # Create a new topic instance
        new_topic = Topic(name=topic_name, feedback=feedback, resource_link=resource_link)

        # Add to the database
        db.session.add(new_topic)
        db.session.commit()
        flash('Topic added successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        flash(f'Error adding topic: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Route to update topic feedback
@app.route('/update/<int:topic_id>', methods=['POST'])
def update_topic(topic_id):
    try:
        topic = Topic.query.get_or_404(topic_id)  # Fetch topic by ID
        topic.feedback = request.form['feedback']  # Update feedback
        topic.resource_link = request.form['resource_link']  # Update resource link

        db.session.commit()  # Commit the updated topic to the database
        flash('Topic updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        flash(f'Error updating topic: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Route to delete a topic
@app.route('/delete/<int:topic_id>')
def delete_topic(topic_id):
    try:
        topic = Topic.query.get_or_404(topic_id)  # Fetch topic by ID
        db.session.delete(topic)  # Delete the topic
        db.session.commit()  # Commit the deletion
        flash('Topic deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        flash(f'Error deleting topic: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

**HTML Template (index.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Study Tracker</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Study Tracker</h1>

        <!-- Flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}

        <!-- Form to add a new topic -->
        <form action="/add" method="POST">
            <div class="form-group">
                <label for="name">Topic Name:</label>
                <input type="text" class="form-control" name="name" required>
            </div>
            <div class="form-group">
                <label for="feedback">Feedback:</label>
                <textarea class="form-control" name="feedback"></textarea>
            </div>
            <div class="form-group">
                <label for="resource_link">Resource Link:</label>
                <input type="url" class="form-control" name="resource_link">
            </div>
            <button type="submit" class="btn btn-primary">Add Topic</button>
        </form>

        <!-- Displaying topics -->
        <h2 class="mt-5">Your Topics</h2>
        <ul class="list-group">
            {% for topic in topics %}
                <li class="list-group-item">
                    <h5>{{ topic.name }}</h5>
                    <p>Feedback: {{ topic.feedback }}</p>
                    <p>Resource: <a href="{{ topic.resource_link }}">{{ topic.resource_link }}</a></p>
                    <form action="/update/{{ topic.id }}" method="POST" class="mt-2">
                        <input type="text" name="feedback" placeholder="Update Feedback" class="form-control">
                        <input type="url" name="resource_link" placeholder="Update Resource Link" class="form-control mt-2">
                        <button type="submit" class="btn btn-warning mt-2">Update</button>
                    </form>
                    <a href="/delete/{{ topic.id }}" class="btn btn-danger mt-2">Delete</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```
