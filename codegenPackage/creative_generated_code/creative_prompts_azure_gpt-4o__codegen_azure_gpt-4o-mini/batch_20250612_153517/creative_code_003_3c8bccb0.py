"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fesit.cl
Prompt: Suggest tools or frameworks for creating a web-based platform to disseminate studies and reports on Chile's tax system, similar to the initiatives by FESIT.
Generated: DETERMINISTIC_3c8bccb0d9b33010
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tax_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for the tax reports
class TaxReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<TaxReport {self.title}>'

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new tax report
@app.route('/reports', methods=['POST'])
def create_report():
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('title', 'content', 'author')):
        return jsonify({'error': 'Missing fields'}), 400
    
    new_report = TaxReport(title=data['title'], content=data['content'], author=data['author'])
    
    try:
        db.session.add(new_report)
        db.session.commit()
        return jsonify({'message': 'Report created successfully', 'report_id': new_report.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Report could not be created'}), 500

# Route to get all reports
@app.route('/reports', methods=['GET'])
def get_reports():
    reports = TaxReport.query.all()
    return jsonify([{'id': report.id, 'title': report.title, 'author': report.author} for report in reports]), 200

# Route to get a specific report by ID
@app.route('/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    report = TaxReport.query.get(report_id)
    if report:
        return jsonify({'id': report.id, 'title': report.title, 'content': report.content, 'author': report.author}), 200
    else:
        return jsonify({'error': 'Report not found'}), 404

# Main execution point
if __name__ == '__main__':
    # Run the app in debug mode for development purposes
    app.run(debug=True)
```
