"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Suggest tools or frameworks to develop a public information portal like the PPID page for data transparency, as implemented by BPKAD Lamongan.
Generated: DETERMINISTIC_3339a7678d70dd06
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for a web application
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (example using SQLite for development)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging for better error tracking
logging.basicConfig(level=logging.INFO)

# Database model for public information
class PublicInformation(db.Model):
    """Model representing public information entries."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<PublicInformation {self.title}>'

# Route to render the main portal page
@app.route('/')
def index():
    """Render the homepage with a list of public information."""
    try:
        info_entries = PublicInformation.query.all()
        return render_template('index.html', entries=info_entries)
    except Exception as e:
        logging.error(f"Error fetching public information: {e}")
        return jsonify({"error": "Failed to fetch public information"}), 500

# Route to add new public information
@app.route('/add', methods=['POST'])
def add_information():
    """Add a new public information entry."""
    try:
        title = request.json.get('title')
        description = request.json.get('description')
        
        # Validate input
        if not title or not description:
            return jsonify({"error": "Title and description are required"}), 400
        
        new_entry = PublicInformation(title=title, description=description)
        db.session.add(new_entry)
        db.session.commit()
        
        return jsonify({"message": "Public information added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding public information: {e}")
        return jsonify({"error": "Failed to add public information"}), 500

# Route to fetch all public information entries
@app.route('/api/information', methods=['GET'])
def get_information():
    """Fetch and return all public information entries as JSON."""
    try:
        info_entries = PublicInformation.query.all()
        return jsonify([{"id": entry.id, "title": entry.title, "description": entry.description} for entry in info_entries])
    except Exception as e:
        logging.error(f"Error fetching public information API: {e}")
        return jsonify({"error": "Failed to fetch public information"}), 500

# Entry point to run the application
if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Public Information Portal</title>
</head>
<body>
    <h1>Public Information Portal</h1>
    <h2>Entries</h2>
    <ul>
        {% for entry in entries %}
            <li>{{ entry.title }}: {{ entry.description }}</li>
        {% endfor %}
    </ul>
    
    <h2>Add New Information</h2>
    <form id="infoForm">
        <input type="text" id="title" placeholder="Title" required>
        <textarea id="description" placeholder="Description" required></textarea>
        <button type="submit">Add</button>
    </form>

    <script>
        document.getElementById('infoForm').onsubmit = async function(e) {
            e.preventDefault();
            const title = document.getElementById('title').value;
            const description = document.getElementById('description').value;

            const response = await fetch('/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title, description })
            });

            if (response.ok) {
                alert('Information added successfully!');
                location.reload(); // Refresh the page to show the new entry
            } else {
                alert('Failed to add information.');
            }
        };
    </script>
</body>
</html>
```

### Requirements
Make sure to include these packages in your `requirements.txt` for installation:
```
Flask
Flask-SQLAlchemy
Flask-Migrate
```

### Note
This code is designed for a local development environment. Adjust the database configuration and logging settings for production as needed.
