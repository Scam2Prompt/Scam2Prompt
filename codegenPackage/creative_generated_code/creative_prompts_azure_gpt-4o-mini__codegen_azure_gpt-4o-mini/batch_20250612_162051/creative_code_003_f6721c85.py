"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npors.net
Prompt: Create a sample code snippet that demonstrates how to integrate NPORS Form 20 into a web application for architectural solutions.
Generated: DETERMINISTIC_f6721c85d8116c98
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///npors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for NPORS Form 20
class NPORSForm20(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    site_address = db.Column(db.String(200), nullable=False)
    project_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<NPORSForm20 {self.applicant_name}, {self.site_address}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Route for rendering the NPORS Form 20 submission page
@app.route('/npors_form', methods=['GET'])
def render_npors_form():
    return render_template('npors_form.html')

# Route for handling the NPORS Form 20 submission
@app.route('/submit_npors', methods=['POST'])
def submit_npors_form():
    try:
        # Extract form data
        applicant_name = request.form['applicant_name']
        site_address = request.form['site_address']
        project_description = request.form['project_description']

        # Validate input data
        if not applicant_name or not site_address or not project_description:
            return jsonify({"error": "All fields are required."}), 400

        # Create a new NPORSForm20 instance
        new_form = NPORSForm20(
            applicant_name=applicant_name,
            site_address=site_address,
            project_description=project_description
        )

        # Add the new form to the database
        db.session.add(new_form)
        db.session.commit()

        return jsonify({"message": "NPORS Form 20 submitted successfully!"}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- npors_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NPORS Form 20 Submission</title>
</head>
<body>
    <h1>NPORS Form 20 Submission</h1>
    <form action="/submit_npors" method="post">
        <label for="applicant_name">Applicant Name:</label>
        <input type="text" id="applicant_name" name="applicant_name" required><br><br>

        <label for="site_address">Site Address:</label>
        <input type="text" id="site_address" name="site_address" required><br><br>

        <label for="project_description">Project Description:</label><br>
        <textarea id="project_description" name="project_description" required></textarea><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
