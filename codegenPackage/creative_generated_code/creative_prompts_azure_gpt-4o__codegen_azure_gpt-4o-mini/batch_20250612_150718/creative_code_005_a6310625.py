"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Suggest tools or APIs to develop an online form submission system for MBA applications, similar to the one described on the SOMTU website.
Generated: DETERMINISTIC_a631062560209d1b
Batch ID: 20250612_150718
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mba_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Application model
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    program = db.Column(db.String(50), nullable=False)
    statement_of_purpose = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Application {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for rendering the application form
@app.route('/apply', methods=['GET'])
def apply_form():
    return render_template('apply.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit_application():
    try:
        # Retrieve form data
        data = request.get_json()

        # Validate input data
        if not all(field in data for field in ['name', 'email', 'program', 'statement_of_purpose']):
            return jsonify({'error': 'Missing fields in the submission'}), 400

        # Create a new application instance
        new_application = Application(
            name=data['name'],
            email=data['email'],
            program=data['program'],
            statement_of_purpose=data['statement_of_purpose']
        )

        # Add to the database and commit
        db.session.add(new_application)
        db.session.commit()

        return jsonify({'message': 'Application submitted successfully!'}), 201

    except Exception as e:
        # Handle unexpected errors
        db.session.rollback()  # Rollback the session in case of an error
        return jsonify({'error': str(e)}), 500

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({'error': e.description}), e.code

# Main execution point
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (apply.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MBA Application Form</title>
</head>
<body>
    <h1>Apply for MBA Program</h1>
    <form id="applicationForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        
        <label for="program">Program:</label>
        <input type="text" id="program" name="program" required>
        <br>
        
        <label for="statement_of_purpose">Statement of Purpose:</label>
        <textarea id="statement_of_purpose" name="statement_of_purpose" required></textarea>
        <br>
        
        <button type="submit">Submit Application</button>
    </form>

    <script>
        document.getElementById('applicationForm').onsubmit = async function(event) {
            event.preventDefault();

            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                program: document.getElementById('program').value,
                statement_of_purpose: document.getElementById('statement_of_purpose').value
            };

            try {
                const response = await fetch('/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                const result = await response.json();
                alert(result.message || result.error);
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
        };
    </script>
</body>
</html>
```
