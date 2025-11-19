"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Generate code for a web-based tool that allows users to request fire sprinkler installation proposals, similar to the service offered by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_a55bc91865436391
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
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sprinkler_proposals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Proposal model
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    details = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Proposal {self.id} - {self.name}>'

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to submit a proposal request
@app.route('/submit', methods=['POST'])
def submit_proposal():
    try:
        # Get data from the request
        data = request.json
        name = data.get('name')
        email = data.get('email')
        address = data.get('address')
        details = data.get('details')

        # Validate input data
        if not name or not email or not address:
            return jsonify({'error': 'Name, email, and address are required.'}), 400

        # Create a new proposal instance
        new_proposal = Proposal(name=name, email=email, address=address, details=details)

        # Add the proposal to the database
        db.session.add(new_proposal)
        db.session.commit()

        logging.info(f'New proposal submitted: {new_proposal}')
        return jsonify({'message': 'Proposal submitted successfully!'}), 201

    except Exception as e:
        logging.error(f'Error submitting proposal: {e}')
        return jsonify({'error': 'An error occurred while submitting the proposal.'}), 500

# Route to get all proposals (for admin use)
@app.route('/proposals', methods=['GET'])
def get_proposals():
    try:
        proposals = Proposal.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'email': p.email, 'address': p.address, 'details': p.details} for p in proposals]), 200
    except Exception as e:
        logging.error(f'Error retrieving proposals: {e}')
        return jsonify({'error': 'An error occurred while retrieving proposals.'}), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fire Sprinkler Proposal Request</title>
</head>
<body>
    <h1>Request a Fire Sprinkler Installation Proposal</h1>
    <form id="proposalForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required>
        <br>
        <label for="details">Details:</label>
        <textarea id="details" name="details"></textarea>
        <br>
        <button type="submit">Submit Proposal</button>
    </form>

    <script>
        document.getElementById('proposalForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            fetch('/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                if (data.message) {
                    this.reset(); // Reset form on success
                }
            })
            .catch(error => {
                alert('An error occurred: ' + error);
            });
        });
    </script>
</body>
</html>
```

### Requirements
To run this application, you will need to install the following Python packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Database Initialization
To initialize the database, run the following commands in the Python shell:
```python
from your_flask_app import db
db.create_all()
```

Replace `your_flask_app` with the name of your Python file (without the `.py` extension).
