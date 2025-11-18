"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testopolistomarta.pages.dev
Prompt: Develop a REST API endpoint for "Notcoin" that allows users to claim rewards, check their activity, and view their referral bonuses.
Generated: DETERMINISTIC_c47d5dc65b7e2c94
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notcoin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    rewards = db.Column(db.Float, default=0.0)
    activity_log = db.Column(db.Text, default='')
    referral_bonus = db.Column(db.Float, default=0.0)

# Schema for validating incoming requests
class UserSchema(Schema):
    username = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Claim rewards endpoint
@app.route('/api/claim_rewards', methods=['POST'])
def claim_rewards():
    try:
        data = request.json
        user_schema = UserSchema()
        validated_data = user_schema.load(data)

        user = User.query.filter_by(username=validated_data['username']).first()
        if not user:
            abort(404, description="User not found")

        # Logic to claim rewards (arbitrary logic for demonstration)
        user.rewards += 10.0
        db.session.commit()
        
        return jsonify({"message": "Rewards claimed successfully", "total_rewards": user.rewards}), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Check activity endpoint
@app.route('/api/check_activity', methods=['GET'])
def check_activity():
    username = request.args.get('username')
    if not username:
        abort(400, description="Username is required")

    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404, description="User not found")

    return jsonify({"activity_log": user.activity_log}), 200

# View referral bonuses endpoint
@app.route('/api/referral_bonuses', methods=['GET'])
def referral_bonuses():
    username = request.args.get('username')
    if not username:
        abort(400, description="Username is required")

    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404, description="User not found")

    return jsonify({"referral_bonus": user.referral_bonus}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
