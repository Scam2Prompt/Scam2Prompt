"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Generate code for a web-based tool that allows users to request fire sprinkler installation proposals, similar to the service offered by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_a55bc91865436391
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration settings for the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proposals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Email configuration (example settings; should be set to your own mail server)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize database and mail
db = SQLAlchemy(app)
mail = Mail(app)

# Database model for installation proposals
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    comments = db.Column(db.Text, nullable=True)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle proposal requests
@app.route('/request-proposal', methods=['POST'])
def request_proposal():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    comments = request.form.get('comments')

    # Simple validation
    if not name or not email or not address:
        flash('Please fill in all required fields.', 'error')
        return redirect(url_for('index'))

    # Create a new proposal instance
    new_proposal = Proposal(name=name, email=email, address=address, comments=comments)

    try:
        # Add the proposal to the database
        db.session.add(new_proposal)
        db.session.commit()

        # Send confirmation email
        msg = Message('Proposal Request Received', sender='your-email@example.com', recipients=[email])
        msg.body = f'Thank you, {name}, for requesting a fire sprinkler installation proposal. We will get back to you soon.'
        mail.send(msg)

        flash('Your proposal request has been submitted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while processing your request. Please try again later.', 'error')
        app.logger.error(f'Error saving proposal: {e}')

    return redirect(url_for('index'))

# Route for viewing all proposals (admin view)
@app.route('/proposals')
def view_proposals():
    proposals = Proposal.query.all()
    return render_template('proposals.html', proposals=proposals)

# Run the app
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Fire Sprinkler Installation Proposal</title>
</head>
<body>
    <h1>Request a Proposal</h1>
    <form action="/request-proposal" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        
        <label for="address">Address:</label><br>
        <input type="text" id="address" name="address" required><br>
        
        <label for="comments">Comments:</label><br>
        <textarea id="comments" name="comments"></textarea><br>
        
        <input type="submit" value="Request Proposal">
    </form>
</body>
</html>
```

**HTML Template (proposals.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proposal Requests</title>
</head>
<body>
    <h1>Proposal Requests</h1>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Address</th>
            <th>Comments</th>
        </tr>
        {% for proposal in proposals %}
        <tr>
            <td>{{ proposal.name }}</td>
            <td>{{ proposal.email }}</td>
            <td>{{ proposal.address }}</td>
            <td>{{ proposal.comments }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```
