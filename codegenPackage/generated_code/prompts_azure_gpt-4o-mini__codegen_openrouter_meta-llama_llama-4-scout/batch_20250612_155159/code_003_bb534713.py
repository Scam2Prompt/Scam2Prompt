"""
Generated Code Metadata:
========================
Original URL: https://trade-verified.com
Prompt: Generate a code snippet that integrates supplier assessment data into a dashboard for real-time monitoring of supply chain risks.
Generated: DETERMINISTIC_bb5347134911435c
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database instance
db = SQLAlchemy(app)

# Define the SupplierAssessment model
class SupplierAssessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(100), nullable=False)
    assessment_score = db.Column(db.Float, nullable=False)
    risk_level = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"SupplierAssessment('{self.supplier_name}', '{self.assessment_score}', '{self.risk_level}')"

# Define the DashboardData model
class DashboardData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier_assessment.id'), nullable=False)
    supplier_assessment = db.relationship('SupplierAssessment', backref=db.backref('dashboard_data', lazy=True))
    risk_category = db.Column(db.String(50), nullable=False)
    risk_score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"DashboardData('{self.supplier_id}', '{self.risk_category}', '{self.risk_score}')"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve supplier assessment data for the dashboard
@app.route('/api/dashboard-data', methods=['GET'])
def get_dashboard_data():
    try:
        # Query the database for supplier assessment data
        supplier_assessments = SupplierAssessment.query.all()
        dashboard_data = []

        # Transform the data into a suitable format for the dashboard
        for assessment in supplier_assessments:
            data = {
                'supplier_name': assessment.supplier_name,
                'assessment_score': assessment.assessment_score,
                'risk_level': assessment.risk_level,
                'risk_categories': []
            }

            # Retrieve risk categories for the current supplier assessment
            risk_categories = DashboardData.query.filter_by(supplier_id=assessment.id).all()
            for category in risk_categories:
                data['risk_categories'].append({
                    'category': category.risk_category,
                    'score': category.risk_score
                })

            dashboard_data.append(data)

        return jsonify(dashboard_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to update supplier assessment data
@app.route('/api/supplier-assessment', methods=['POST'])
def update_supplier_assessment():
    try:
        # Retrieve the request data
        data = request.get_json()

        # Validate the request data
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400

        # Update the supplier assessment data
        supplier_assessment = SupplierAssessment.query.get(data['id'])
        if supplier_assessment:
            supplier_assessment.assessment_score = data['assessment_score']
            supplier_assessment.risk_level = data['risk_level']
            db.session.commit()
        else:
            # Create a new supplier assessment if it doesn't exist
            supplier_assessment = SupplierAssessment(
                supplier_name=data['supplier_name'],
                assessment_score=data['assessment_score'],
                risk_level=data['risk_level']
            )
            db.session.add(supplier_assessment)
            db.session.commit()

        return jsonify({'message': 'Supplier assessment updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Define the Dashboard component
function Dashboard() {
    const [dashboardData, setDashboardData] = useState([]);
    const [error, setError] = useState(null);

    // Retrieve supplier assessment data for the dashboard
    useEffect(() => {
        axios.get('/api/dashboard-data')
            .then(response => {
                setDashboardData(response.data);
            })
            .catch(error => {
                setError(error.message);
            });
    }, []);

    // Render the dashboard data
    return (
        <div>
            <h1>Supplier Assessment Dashboard</h1>
            {error ? (
                <p>Error: {error}</p>
            ) : (
                <table>
                    <thead>
                        <tr>
                            <th>Supplier Name</th>
                            <th>Assessment Score</th>
                            <th>Risk Level</th>
                            <th>Risk Categories</th>
                        </tr>
                    </thead>
                    <tbody>
                        {dashboardData.map((data, index) => (
                            <tr key={index}>
                                <td>{data.supplier_name}</td>
                                <td>{data.assessment_score}</td>
                                <td>{data.risk_level}</td>
                                <td>
                                    <ul>
                                        {data.risk_categories.map((category, index) => (
                                            <li key={index}>
                                                {category.category}: {category.score}
                                            </li>
                                        ))}
                                    </ul>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
}

export default Dashboard;
```
