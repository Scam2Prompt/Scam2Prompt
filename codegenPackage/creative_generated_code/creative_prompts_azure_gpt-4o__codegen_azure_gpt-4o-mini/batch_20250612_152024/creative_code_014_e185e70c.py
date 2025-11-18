"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Generate code to build a student community platform for sharing IELTS and PTE preparation tips, inspired by the student community mentioned on RNW International's website.
Generated: DETERMINISTIC_e185e70cd956572f
Batch ID: 20250612_152024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`.": {
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
# student_community.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the preparation tips
class PreparationTip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    tip = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Tip {self.id}: {self.tip}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the home page with the list of preparation tips."""
    tips = PreparationTip.query.all()
    return render_template('index.html', tips=tips)

@app.route('/tips', methods=['POST'])
def add_tip():
    """Add a new preparation tip to the database."""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        tip = data.get('tip')

        # Validate input
        if not user_id or not tip:
            return jsonify({"error": "User ID and tip are required."}), 400

        new_tip = PreparationTip(user_id=user_id, tip=tip)
        db.session.add(new_tip)
        db.session.commit()
        
        return jsonify({"message": "Tip added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tips/<int:tip_id>', methods=['DELETE'])
def delete_tip(tip_id):
    """Delete a preparation tip from the database."""
    try:
        tip = PreparationTip.query.get_or_404(tip_id)
        db.session.delete(tip)
        db.session.commit()
        
        return jsonify({"message": "Tip deleted successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the application in debug mode during development
    app.run(debug=os.environ.get('FLASK_DEBUG', default=True))
```

### HTML Template (index.html)
```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Community - IELTS & PTE Tips</title>
</head>
<body>
    <h1>Preparation Tips for IELTS & PTE</h1>
    <ul>
        {% for tip in tips %}
            <li>{{ tip.tip }} (Submitted on: {{ tip.created_at }})</li>
        {% endfor %}
    </ul>
    <h2>Submit a new tip</h2>
    <form id="tip-form">
        <input type="hidden" name="user_id" value="1" /> <!-- Example user ID -->
        <textarea name="tip" required placeholder="Share your preparation tip..."></textarea>
        <button type="submit">Submit</button>
    </form>

    <script>
        document.getElementById('tip-form').addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const data = {
                user_id: formData.get('user_id'),
                tip: formData.get('tip')
            };
            fetch('/tips', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                location.reload(); // Reload the page to see the new tip
            })
            .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>
```

### Requirements
To run this application, make sure to install Flask and Flask-SQLAlchemy:
```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
Run the application using:
```bash
python student_community.py
```
Access the platform in your web browser at `http://127.0.0.1:5000/`.
