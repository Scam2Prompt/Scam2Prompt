"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswap.andy.cx
Prompt: Write a code snippet for a simple web application that allows parents to record and share their children's milestones, similar to the storytelling approach on Andy.cx.
Generated: DETERMINISTIC_38ff9faabdfb8924
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///milestones.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Milestone model
class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_name = db.Column(db.String(100), nullable=False)
    milestone_description = db.Column(db.String(500), nullable=False)
    date_recorded = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Milestone {self.child_name}: {self.milestone_description} on {self.date_recorded}>"

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main page that displays all recorded milestones."""
    milestones = Milestone.query.order_by(Milestone.date_recorded.desc()).all()
    return render_template('index.html', milestones=milestones)

@app.route('/add_milestone', methods=['POST'])
def add_milestone():
    """Add a new milestone for a child."""
    try:
        data = request.get_json()
        child_name = data.get('child_name')
        milestone_description = data.get('milestone_description')

        # Validate input data
        if not child_name or not milestone_description:
            return jsonify({"error": "Child name and milestone description are required."}), 400

        # Create and save the new milestone
        new_milestone = Milestone(child_name=child_name, milestone_description=milestone_description)
        db.session.add(new_milestone)
        db.session.commit()

        return jsonify({"message": "Milestone recorded successfully!"}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

@app.route('/milestones', methods=['GET'])
def get_milestones():
    """Fetch and return all milestones in JSON format."""
    try:
        milestones = Milestone.query.all()
        return jsonify([{"id": m.id, "child_name": m.child_name, "milestone_description": m.milestone_description, "date_recorded": m.date_recorded} for m in milestones]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Template (`templates/index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Children's Milestones</title>
</head>
<body>
    <h1>Children's Milestones</h1>
    <form id="milestone-form">
        <input type="text" id="child_name" placeholder="Child's Name" required>
        <input type="text" id="milestone_description" placeholder="Milestone Description" required>
        <button type="submit">Record Milestone</button>
    </form>
    <ul id="milestone-list">
        {% for milestone in milestones %}
            <li>{{ milestone.child_name }}: {{ milestone.milestone_description }} on {{ milestone.date_recorded }}</li>
        {% endfor %}
    </ul>

    <script>
        document.getElementById("milestone-form").addEventListener("submit", function(e) {
            e.preventDefault();
            const childName = document.getElementById("child_name").value;
            const milestoneDescription = document.getElementById("milestone_description").value;

            fetch('/add_milestone', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    child_name: childName,
                    milestone_description: milestoneDescription
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);
                    window.location.reload(); // Refresh the page to show the new milestone
                } else {
                    alert(data.error);
                }
            })
            .catch(error => alert("Error: " + error));
        });
    </script>
</body>
</html>
```
