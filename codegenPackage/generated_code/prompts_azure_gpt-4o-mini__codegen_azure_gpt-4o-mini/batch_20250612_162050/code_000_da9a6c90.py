"""
Generated Code Metadata:
========================
Original URL: https://agnedoveikaite.lt
Prompt: Generate a code snippet for a web application that integrates emotional intelligence training modules, inspired by Agne Doveikaite's approach to personal development.
Generated: DETERMINISTIC_da9a6c9010f38d64
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotional_intelligence.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the TrainingModule model
class TrainingModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<TrainingModule {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display all training modules
@app.route('/')
def index():
    try:
        modules = TrainingModule.query.all()
        return render_template('index.html', modules=modules)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new training module
@app.route('/add_module', methods=['POST'])
def add_module():
    try:
        data = request.get_json()
        new_module = TrainingModule(title=data['title'], description=data['description'])
        db.session.add(new_module)
        db.session.commit()
        return jsonify({"message": "Module added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get a specific training module
@app.route('/module/<int:module_id>', methods=['GET'])
def get_module(module_id):
    try:
        module = TrainingModule.query.get_or_404(module_id)
        return jsonify({
            "id": module.id,
            "title": module.title,
            "description": module.description,
            "created_at": module.created_at
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emotional Intelligence Training Modules</title>
</head>
<body>
    <h1>Emotional Intelligence Training Modules</h1>
    <ul>
        {% for module in modules %}
            <li>{{ module.title }}: {{ module.description }}</li>
        {% endfor %}
    </ul>
    <form id="moduleForm">
        <input type="text" id="title" placeholder="Module Title" required>
        <textarea id="description" placeholder="Module Description" required></textarea>
        <button type="submit">Add Module</button>
    </form>
    <script>
        document.getElementById('moduleForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const title = document.getElementById('title').value;
            const description = document.getElementById('description').value;

            fetch('/add_module', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, description })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                location.reload(); // Reload the page to see the new module
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
```
