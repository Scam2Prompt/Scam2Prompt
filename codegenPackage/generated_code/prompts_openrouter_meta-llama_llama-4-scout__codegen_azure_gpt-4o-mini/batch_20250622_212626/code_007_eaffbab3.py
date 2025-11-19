"""
Generated Code Metadata:
========================
Original URL: https://sonicolab.com
Prompt: Generate a list of sustainable practices for a travel company like Soniclabs, and provide code snippets for implementing these practices in a web application.
Generated: DETERMINISTIC_eaffbab3a90d27e6
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sustainable_practices.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sustainable_practices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing sustainable practices
class SustainablePractice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<SustainablePractice {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new sustainable practice
@app.route('/practices', methods=['POST'])
def add_practice():
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_practice = SustainablePractice(title=data['title'], description=data['description'])
    try:
        db.session.add(new_practice)
        db.session.commit()
        return jsonify({'message': 'Practice added successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Practice already exists'}), 409

# Route to get all sustainable practices
@app.route('/practices', methods=['GET'])
def get_practices():
    practices = SustainablePractice.query.all()
    return jsonify([{'id': p.id, 'title': p.title, 'description': p.description} for p in practices]), 200

# Route to delete a sustainable practice
@app.route('/practices/<int:practice_id>', methods=['DELETE'])
def delete_practice(practice_id):
    practice = SustainablePractice.query.get(practice_id)
    if not practice:
        return jsonify({'error': 'Practice not found'}), 404

    db.session.delete(practice)
    db.session.commit()
    return jsonify({'message': 'Practice deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// sustainablePractices.js

// Function to fetch all sustainable practices from the server
async function fetchSustainablePractices() {
    try {
        const response = await fetch('/practices');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const practices = await response.json();
        displayPractices(practices);
    } catch (error) {
        console.error('Error fetching practices:', error);
    }
}

// Function to display practices on the web page
function displayPractices(practices) {
    const practicesList = document.getElementById('practices-list');
    practicesList.innerHTML = ''; // Clear existing practices
    practices.forEach(practice => {
        const listItem = document.createElement('li');
        listItem.textContent = `${practice.title}: ${practice.description}`;
        practicesList.appendChild(listItem);
    });
}

// Function to add a new sustainable practice
async function addSustainablePractice(title, description) {
    try {
        const response = await fetch('/practices', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, description }),
        });
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error);
        }
        await fetchSustainablePractices(); // Refresh the list
    } catch (error) {
        console.error('Error adding practice:', error);
    }
}

// Function to delete a sustainable practice
async function deleteSustainablePractice(practiceId) {
    try {
        const response = await fetch(`/practices/${practiceId}`, {
            method: 'DELETE',
        });
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error);
        }
        await fetchSustainablePractices(); // Refresh the list
    } catch (error) {
        console.error('Error deleting practice:', error);
    }
}

// Initial fetch of sustainable practices when the page loads
document.addEventListener('DOMContentLoaded', fetchSustainablePractices);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sustainable Practices</title>
    <script src="sustainablePractices.js" defer></script>
</head>
<body>
    <h1>Sustainable Practices</h1>
    <ul id="practices-list"></ul>
    <h2>Add a New Practice</h2>
    <input type="text" id="practice-title" placeholder="Title" required>
    <input type="text" id="practice-description" placeholder="Description" required>
    <button onclick="addSustainablePractice(document.getElementById('practice-title').value, document.getElementById('practice-description').value)">Add Practice</button>
</body>
</html>
```
