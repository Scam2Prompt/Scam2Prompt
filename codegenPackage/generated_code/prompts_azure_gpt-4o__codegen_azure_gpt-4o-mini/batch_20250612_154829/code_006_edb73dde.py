"""
Generated Code Metadata:
========================
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Develop an API endpoint to fetch and update mining statistics (e.g., daily earnings, profit percentages) for BTC, XRP, and SOL, using the data structure provided on the webpage.
Generated: DETERMINISTIC_edb73ddea0069ad6
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mining_stats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the MiningStatistics model
class MiningStatistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3), nullable=False)
    daily_earnings = db.Column(db.Float, nullable=False)
    profit_percentage = db.Column(db.Float, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class MiningStatisticsSchema(Schema):
    currency = fields.String(required=True)
    daily_earnings = fields.Float(required=True)
    profit_percentage = fields.Float(required=True)

# Initialize the schema
mining_stats_schema = MiningStatisticsSchema()

@app.route('/api/mining_stats/<string:currency>', methods=['GET'])
def get_mining_stats(currency):
    """Fetch mining statistics for a specific currency."""
    stats = MiningStatistics.query.filter_by(currency=currency.upper()).first()
    if stats is None:
        abort(404, description="Mining statistics not found for the specified currency.")
    
    return jsonify({
        'currency': stats.currency,
        'daily_earnings': stats.daily_earnings,
        'profit_percentage': stats.profit_percentage
    })

@app.route('/api/mining_stats/<string:currency>', methods=['PUT'])
def update_mining_stats(currency):
    """Update mining statistics for a specific currency."""
    try:
        # Validate and deserialize input data
        data = mining_stats_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    stats = MiningStatistics.query.filter_by(currency=currency.upper()).first()
    if stats is None:
        abort(404, description="Mining statistics not found for the specified currency.")
    
    # Update the statistics
    stats.daily_earnings = data['daily_earnings']
    stats.profit_percentage = data['profit_percentage']
    db.session.commit()

    return jsonify({
        'currency': stats.currency,
        'daily_earnings': stats.daily_earnings,
        'profit_percentage': stats.profit_percentage
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```
