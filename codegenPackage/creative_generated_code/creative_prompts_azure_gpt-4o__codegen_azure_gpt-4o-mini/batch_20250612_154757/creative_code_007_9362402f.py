"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorswap.shop
Prompt: Create a dashboard for monitoring trade success metrics and user engagement on an NFT trading platform, inspired by Grailswap's statistics and user base.
Generated: DETERMINISTIC_9362402f9c9deb24
Batch ID: 20250612_154757
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_trading.db'  # Example with SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Define the Trade model
class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    trade_value = db.Column(db.Float, nullable=False)
    success = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Trade {self.id}>'

# Define the UserEngagement model
class UserEngagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    engagement_time = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<UserEngagement {self.id}>'

# Schema for validating input data
class TradeSchema(Schema):
    user_id = fields.Str(required=True)
    trade_value = fields.Float(required=True)
    success = fields.Bool()

class UserEngagementSchema(Schema):
    user_id = fields.Str(required=True)
    engagement_time = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to log a new trade
@app.route('/trades', methods=['POST'])
def log_trade():
    json_data = request.get_json()
    try:
        # Validate input data
        trade_schema = TradeSchema()
        data = trade_schema.load(json_data)
        
        new_trade = Trade(**data)
        db.session.add(new_trade)
        db.session.commit()

        logging.info(f'Trade logged: {new_trade}')
        return jsonify({'message': 'Trade logged successfully!'}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f'Error logging trade: {e}')
        return jsonify({'error': 'Could not log trade'}), 500

# Route to log user engagement
@app.route('/engagement', methods=['POST'])
def log_engagement():
    json_data = request.get_json()
    try:
        # Validate input data
        engagement_schema = UserEngagementSchema()
        data = engagement_schema.load(json_data)

        new_engagement = UserEngagement(**data)
        db.session.add(new_engagement)
        db.session.commit()

        logging.info(f'User engagement logged: {new_engagement}')
        return jsonify({'message': 'Engagement logged successfully!'}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f'Error logging engagement: {e}')
        return jsonify({'error': 'Could not log engagement'}), 500

# Route to get trade success metrics
@app.route('/metrics/trades', methods=['GET'])
def get_trade_metrics():
    try:
        total_trades = Trade.query.count()
        successful_trades = Trade.query.filter_by(success=True).count()
        success_rate = (successful_trades / total_trades * 100) if total_trades > 0 else 0
        
        metrics = {
            'total_trades': total_trades,
            'successful_trades': successful_trades,
            'success_rate': success_rate,
        }

        return jsonify(metrics), 200
    except Exception as e:
        logging.error(f'Error fetching trade metrics: {e}')
        return jsonify({'error': 'Could not fetch metrics'}), 500

# Route to get user engagement metrics
@app.route('/metrics/engagement', methods=['GET'])
def get_engagement_metrics():
    try:
        total_engagements = UserEngagement.query.count()
        average_engagement_time = db.session.query(db.func.avg(UserEngagement.engagement_time)).scalar() or 0
        
        metrics = {
            'total_engagements': total_engagements,
            'average_engagement_time': average_engagement_time,
        }

        return jsonify(metrics), 200
    except Exception as e:
        logging.error(f'Error fetching engagement metrics: {e}')
        return jsonify({'error': 'Could not fetch metrics'}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
