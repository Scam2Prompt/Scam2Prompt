"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: How would you recommend using APIs or libraries to build a platform for venture builders to manage startup investments and provide strategic guidance, inspired by Memetic Digital's approach?
Generated: DETERMINISTIC_183a82d3bffd0611
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///venture_builder.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define models
class Startup(db.Model):
    """Represents a startup."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    investments = db.relationship('Investment', backref='startup', lazy=True)

class Investment(db.Model):
    """Represents an investment in a startup."""
    id = db.Column(db.Integer, primary_key=True)
    startup_id = db.Column(db.Integer, db.ForeignKey('startup.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    guidance = db.Column(db.Text, nullable=True)

class VentureBuilder(db.Model):
    """Represents a venture builder."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    startups = db.relationship('Startup', backref='venture_builder', lazy=True)

# Create tables
@app.before_first_request
def create_tables():
    try:
        db.create_all()
    except SQLAlchemyError as e:
        print(f"Error creating tables: {e}")

# API endpoint to create a new startup
@app.route('/startups', methods=['POST'])
def create_startup():
    try:
        data = request.get_json()
        startup = Startup(name=data['name'])
        db.session.add(startup)
        db.session.commit()
        return jsonify({'id': startup.id, 'name': startup.name}), 201
    except KeyError as e:
        return jsonify({'error': f"Missing key: {e}"}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to create a new investment
@app.route('/investments', methods=['POST'])
def create_investment():
    try:
        data = request.get_json()
        investment = Investment(startup_id=data['startup_id'], amount=data['amount'], guidance=data.get('guidance'))
        db.session.add(investment)
        db.session.commit()
        return jsonify({'id': investment.id, 'startup_id': investment.startup_id, 'amount': investment.amount, 'guidance': investment.guidance}), 201
    except KeyError as e:
        return jsonify({'error': f"Missing key: {e}"}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get all startups for a venture builder
@app.route('/venture-builders/<int:venture_builder_id>/startups', methods=['GET'])
def get_startups(venture_builder_id):
    try:
        venture_builder = VentureBuilder.query.get(venture_builder_id)
        if venture_builder is None:
            return jsonify({'error': 'Venture builder not found'}), 404
        startups = venture_builder.startups
        return jsonify([{'id': s.id, 'name': s.name} for s in startups])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get all investments for a startup
@app.route('/startups/<int:startup_id>/investments', methods=['GET'])
def get_investments(startup_id):
    try:
        startup = Startup.query.get(startup_id)
        if startup is None:
            return jsonify({'error': 'Startup not found'}), 404
        investments = startup.investments
        return jsonify([{'id': i.id, 'amount': i.amount, 'guidance': i.guidance} for i in investments])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
