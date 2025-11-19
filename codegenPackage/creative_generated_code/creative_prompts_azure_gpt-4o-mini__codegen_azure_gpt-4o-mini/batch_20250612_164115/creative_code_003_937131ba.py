"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Develop a REST API endpoint that allows users to submit their architectural plans for a cabinetry quote, integrating with United Cabinetry's existing systems.
Generated: DETERMINISTIC_937131bab7f4af2b
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest
import os

app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///cabinetry.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing cabinetry plans
class CabinetryPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    plan_file_path = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<CabinetryPlan {self.id} by {self.user_email}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/cabinetry/quote', methods=['POST'])
def submit_cabinetry_plan():
    """
    Endpoint to submit cabinetry plans for a quote.
    Accepts a file upload along with the user's email.
    Returns a confirmation message with the plan ID.
    """

    # Check if the request contains a file and user_email
    if 'file' not in request.files or 'user_email' not in request.form:
        raise BadRequest("Missing file or user_email in request.")

    file = request.files['file']
    user_email = request.form['user_email']

    # Check if the file is valid
    if file.filename == '':
        raise BadRequest("No selected file.")

    # Save the file to a designated directory
    upload_folder = os.getenv('UPLOAD_FOLDER', 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.filename)
    
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": "Failed to save file.", "details": str(e)}), 500

    # Create a new cabinetry plan record
    new_plan = CabinetryPlan(user_email=user_email, plan_file_path=file_path)

    # Add to the session and commit to the database
    try:
        db.session.add(new_plan)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": "Failed to save cabinetry plan.", "details": str(e)}), 500

    # Return a success message with the plan ID
    return jsonify({"message": "Cabinetry plan submitted successfully.", "plan_id": new_plan.id}), 201

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
