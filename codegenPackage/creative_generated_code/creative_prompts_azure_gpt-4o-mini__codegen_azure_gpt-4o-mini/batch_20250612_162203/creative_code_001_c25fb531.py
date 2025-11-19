"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Recommend an API for managing financial reports and client interactions for a cooperative like Cooprometa.
Generated: DETERMINISTIC_c25fb53113827a5e
Batch ID: 20250612_162203
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cooprometa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for financial reports
class FinancialReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<FinancialReport {self.title}>'

# Define a model for clients
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f'<Client {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/reports', methods=['POST'])
def create_report():
    """Create a new financial report."""
    data = request.json
    new_report = FinancialReport(
        title=data['title'],
        amount=data['amount'],
        date=data['date']
    )
    try:
        db.session.add(new_report)
        db.session.commit()
        return jsonify({'message': 'Report created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/reports', methods=['GET'])
def get_reports():
    """Retrieve all financial reports."""
    reports = FinancialReport.query.all()
    return jsonify([{'id': report.id, 'title': report.title, 'amount': report.amount, 'date': report.date.isoformat()} for report in reports]), 200

@app.route('/clients', methods=['POST'])
def create_client():
    """Create a new client."""
    data = request.json
    new_client = Client(
        name=data['name'],
        email=data['email']
    )
    try:
        db.session.add(new_client)
        db.session.commit()
        return jsonify({'message': 'Client created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/clients', methods=['GET'])
def get_clients():
    """Retrieve all clients."""
    clients = Client.query.all()
    return jsonify([{'id': client.id, 'name': client.name, 'email': client.email} for client in clients]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
