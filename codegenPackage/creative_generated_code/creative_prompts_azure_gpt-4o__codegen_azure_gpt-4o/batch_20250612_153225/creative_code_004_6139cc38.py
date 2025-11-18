"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Suggest tools or libraries to implement a scientific validation system for DBT therapy outcomes, such as reducing self-harm and suicidal ideation, based on the claims made on the Mente Sana Psicología site.
Generated: DETERMINISTIC_6139cc38e29a0354
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example Python implementation using Flask (a web framework), SQLAlchemy (an ORM for database interaction), and Pandas (for scientific data analysis):

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbt_validation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a database model for storing DBT therapy outcomes
class Outcome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    pre_therapy_score = db.Column(db.Float, nullable=False)  # e.g., self-harm scale before therapy
    post_therapy_score = db.Column(db.Float, nullable=False) # e.g., self-harm scale after therapy
    suicidal_ideation_pre = db.Column(db.Float, nullable=False)  # e.g., suicidal ideation score before therapy
    suicidal_ideation_post = db.Column(db.Float, nullable=False) # e.g., suicidal ideation score after therapy

# Create the database (only required once)
with app.app_context():
    db.create_all()

# Endpoint to add DBT therapy outcome data
@app.route('/add_outcome', methods=['POST'])
def add_outcome():
    try:
        # Parse incoming JSON data
        data = request.json
        patient_id = data['patient_id']
        pre_therapy_score = data['pre_therapy_score']
        post_therapy_score = data['post_therapy_score']
        suicidal_ideation_pre = data['suicidal_ideation_pre']
        suicidal_ideation_post = data['suicidal_ideation_post']

        # Validate data
        if not all([patient_id, pre_therapy_score, post_therapy_score, suicidal_ideation_pre, suicidal_ideation_post]):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create and save the Outcome record
        outcome = Outcome(
            patient_id=patient_id,
            pre_therapy_score=pre_therapy_score,
            post_therapy_score=post_therapy_score,
            suicidal_ideation_pre=suicidal_ideation_pre,
            suicidal_ideation_post=suicidal_ideation_post
        )
        db.session.add(outcome)
        db.session.commit()

        return jsonify({'message': 'Outcome added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to analyze outcomes (scientific validation)
@app.route('/validate_outcomes', methods=['GET'])
def validate_outcomes():
    try:
        # Fetch all outcomes from the database
        outcomes = Outcome.query.all()
        
        # Convert outcomes to a Pandas DataFrame for analysis
        data = [{
            'patient_id': outcome.patient_id,
            'pre_therapy_score': outcome.pre_therapy_score,
            'post_therapy_score': outcome.post_therapy_score,
            'suicidal_ideation_pre': outcome.suicidal_ideation_pre,
            'suicidal_ideation_post': outcome.suicidal_ideation_post
        } for outcome in outcomes]
        df = pd.DataFrame(data)

        # Perform scientific validation
        pre_self_harm_mean = df['pre_therapy_score'].mean()
        post_self_harm_mean = df['post_therapy_score'].mean()
        pre_suicidal_mean = df['suicidal_ideation_pre'].mean()
        post_suicidal_mean = df['suicidal_ideation_post'].mean()

        # Calculate percentage change in scores
        self_harm_reduction = ((pre_self_harm_mean - post_self_harm_mean) / pre_self_harm_mean) * 100
        suicidal_reduction = ((pre_suicidal_mean - post_suicidal_mean) / pre_suicidal_mean) * 100

        # Return analysis results
        return jsonify({
            'self_harm_reduction_percentage': self_harm_reduction,
            'suicidal_ideation_reduction_percentage': suicidal_reduction
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    # Use debug mode during development
    app.run(debug=True)
```

### Notes:
- This code provides endpoints for adding outcome data and validating therapy outcomes.
- The `/add_outcome` endpoint accepts JSON data to store therapy results for individual patients.
- The `/validate_outcomes` endpoint performs analysis using Pandas to calculate mean scores and percentage reductions.
- Proper error handling is included to ensure reliability.
- To use this code in production, additional security considerations, such as input sanitization and authentication, should be implemented.
