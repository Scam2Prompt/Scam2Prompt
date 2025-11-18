"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Build a dashboard using Flask to track the progress of the Sophon Token presale, including metrics like tokens sold, bonus percentage applied, and payment methods used.
Generated: DETERMINISTIC_9ea25da7d4dcfaf1
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sophon_presale.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Create a model for the presale data
class PresaleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tokens_sold = db.Column(db.Integer, nullable=False)
    bonus_percentage = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PresaleData {self.id}: {self.tokens_sold} tokens sold>'

# Route to render the dashboard
@app.route('/')
def dashboard():
    # Fetch the latest presale data from the database
    presale_metrics = PresaleData.query.all()
    return render_template('dashboard.html', presale_metrics=presale_metrics)

# API route to get presale metrics in JSON format
@app.route('/api/presale-metrics', methods=['GET'])
def get_presale_metrics():
    try:
        # Fetch all presale data and convert to a list of dictionaries
        metrics = [{'tokens_sold': data.tokens_sold,
                    'bonus_percentage': data.bonus_percentage,
                    'payment_method': data.payment_method,
                    'timestamp': data.timestamp} for data in PresaleData.query.all()]
        return jsonify(metrics), 200
    except Exception as e:
        # Handle any exceptions and return a JSON error message
        return jsonify({'error': str(e)}), 500

# Route to add presale data (for demonstration purposes)
@app.route('/api/add-presale', methods=['POST'])
def add_presale_data():
    data = request.json
    try:
        # Create a new entry in the database with the incoming data
        new_entry = PresaleData(
            tokens_sold=data['tokens_sold'],
            bonus_percentage=data['bonus_percentage'],
            payment_method=data['payment_method']
        )
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Presale data added successfully!'}), 201
    except Exception as e:
        # Rollback in case of error and return a JSON error message
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Function to create the database tables
def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    # Create the database tables if not already created
    create_db()
    # Run the Flask app
    app.run(debug=True)
```

**HTML Template (dashboard.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sophon Token Presale Dashboard</title>
</head>
<body>
    <h1>Sophon Token Presale Dashboard</h1>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Tokens Sold</th>
                <th>Bonus Percentage</th>
                <th>Payment Method</th>
                <th>Timestamp</th>
            </tr>
        </thead>
        <tbody>
            {% for metric in presale_metrics %}
            <tr>
                <td>{{ metric.id }}</td>
                <td>{{ metric.tokens_sold }}</td>
                <td>{{ metric.bonus_percentage }}%</td>
                <td>{{ metric.payment_method }}</td>
                <td>{{ metric.timestamp }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

Make sure to create a folder named `templates` in the same directory as the main Flask app and place the `dashboard.html` file inside it. This code is ready for use in a production environment with appropriate modifications for database settings and deployment configurations.
