"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://textcounsellingonline.com.au
Prompt: How can I create a user-friendly interface for a text counselling service that accommodates individuals who prefer writing over speaking, similar to the model used by Text Counselling Online?
Generated: DETERMINISTIC_d7c38ae358a4e6b0
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css": {
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
# Import necessary libraries for the web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counselling_service.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# Database model for storing user messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.id} from {self.username}>'

# Route for the homepage
@app.route('/')
def index():
    # Fetch all messages from the database
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

# Route for submitting a message
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get username and message content from the form
        username = request.form['username']
        content = request.form['content']
        
        # Basic validation
        if not username or not content:
            flash('Username and message cannot be empty.', 'error')
            return redirect(url_for('index'))

        # Create a new message instance
        new_message = Message(username=username, content=content)
        
        # Add the message to the database
        db.session.add(new_message)
        db.session.commit()
        
        # Flash success message
        flash('Your message has been sent!', 'success')
        return redirect(url_for('index'))
    
    except Exception as e:
        # Handle any errors that occur during message submission
        db.session.rollback()  # Rollback the session on error
        flash('An error occurred while submitting your message. Please try again.', 'error')
        return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Counselling Service</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Text Counselling Service</h1>
        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}

        <!-- Messages display area -->
        <div class="messages">
            <h3>Messages:</h3>
            <ul class="list-group">
                {% for message in messages %}
                    <li class="list-group-item">
                        <strong>{{ message.username }}</strong>: {{ message.content }}
                        <small class="text-muted">- {{ message.created_at.strftime('%Y-%m-%d %H:%M:%S') }}</small>
                    </li>
                {% endfor %}
            </ul>
        </div>

        <!-- Message submission form -->
        <h3>Send a Message:</h3>
        <form action="{{ url_for('submit') }}" method="POST">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" class="form-control" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="content">Message:</label>
                <textarea class="form-control" id="content" name="content" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Send</button>
        </form>
    </div>
</body>
</html>
```

To use this code:
1. Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
2. Create a folder named `templates` in the same directory as your Python file and place the HTML code in a file named `index.html` inside this folder.
3. Run the Python script to start the web application.
