"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kocaeli.com
Prompt: Provide a solution using Flask or Django to build a backend for a website similar to Kocaeli.COM, with endpoints for retrieving data about "Devlet Daireleri" and "Spor Kulüpleri."
Generated: DETERMINISTIC_4bf3ab63185efeb6
Batch ID: 20250612_152240
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kocaeli.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the DevletDaireleri model
class DevletDaireleri(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

# Define the SporKulüpleri model
class SporKulüpleri(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sport_type = db.Column(db.String(50), nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all Devlet Daireleri
@app.route('/devletdaireleri', methods=['GET'])
def get_devlet_daireleri():
    try:
        devlet_daireleri = DevletDaireleri.query.all()
        result = [{"id": d.id, "name": d.name, "address": d.address} for d in devlet_daireleri]
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all Spor Kulüpleri
@app.route('/sporkulüpleri', methods=['GET'])
def get_spor_kuluberi():
    try:
        spor_kulüpleri = SporKulüpleri.query.all()
        result = [{"id": s.id, "name": s.name, "sport_type": s.sport_type} for s in spor_kulüpleri]
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
