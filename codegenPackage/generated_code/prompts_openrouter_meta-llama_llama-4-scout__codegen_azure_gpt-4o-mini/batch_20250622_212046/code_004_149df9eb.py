"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: "Develop an API for monitoring and controlling a water filtration system, incorporating features such as real-time water quality monitoring and automated filter replacement alerts."
Generated: DETERMINISTIC_149df9eb743214ea
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///water_filtration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for water quality readings
class WaterQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    pH = db.Column(db.Float, nullable=False)
    turbidity = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)

# Database model for filter replacement alerts
class FilterAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alert_time = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.String(200), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get the latest water quality data
@app.route('/api/water_quality', methods=['GET'])
def get_water_quality():
    try:
        latest_reading = WaterQuality.query.order_by(WaterQuality.timestamp.desc()).first()
        if latest_reading:
            return jsonify({
                'pH': latest_reading.pH,
                'turbidity': latest_reading.turbidity,
                'temperature': latest_reading.temperature,
                'timestamp': latest_reading.timestamp
            }), 200
        else:
            return jsonify({'message': 'No water quality data available.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to simulate adding a new water quality reading
@app.route('/api/water_quality', methods=['POST'])
def add_water_quality():
    try:
        data = request.json
        new_reading = WaterQuality(
            pH=data['pH'],
            turbidity=data['turbidity'],
            temperature=data['temperature']
        )
        db.session.add(new_reading)
        db.session.commit()
        return jsonify({'message': 'Water quality data added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to check for filter replacement alerts
@app.route('/api/filter_alerts', methods=['GET'])
def get_filter_alerts():
    try:
        alerts = FilterAlert.query.all()
        return jsonify([{'id': alert.id, 'alert_time': alert.alert_time, 'message': alert.message} for alert in alerts]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to simulate filter replacement alert generation
def generate_filter_alert():
    if random.random() < 0.1:  # 10% chance to generate an alert
        new_alert = FilterAlert(message="Time to replace the filter!")
        db.session.add(new_alert)
        db.session.commit()

# Background task to generate alerts periodically
@app.before_request
def check_for_alerts():
    generate_filter_alert()

if __name__ == '__main__':
    app.run(debug=True)
```
