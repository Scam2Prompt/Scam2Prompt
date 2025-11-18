"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argnt.xyz
Prompt: Develop a backend system for managing lottery app data, including fields like "邀请码" and "开奖信息," as described on the webpage.
Generated: DETERMINISTIC_7a27ce97c4cf02ce
Batch ID: 20250612_152410
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Lottery data model
class LotteryData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invite_code = db.Column(db.String(50), nullable=False, unique=True)
    draw_info = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<LotteryData {self.invite_code}>'

# Schema for validating input data
class LotteryDataSchema(Schema):
    invite_code = fields.Str(required=True)
    draw_info = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create lottery data
@app.route('/lottery', methods=['POST'])
def create_lottery_data():
    schema = LotteryDataSchema()
    try:
        # Validate input data
        validated_data = schema.load(request.json)
        new_lottery = LotteryData(**validated_data)
        db.session.add(new_lottery)
        db.session.commit()
        return jsonify(schema.dump(new_lottery)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Invite code must be unique."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all lottery data
@app.route('/lottery', methods=['GET'])
def get_lottery_data():
    lottery_data = LotteryData.query.all()
    schema = LotteryDataSchema(many=True)
    return jsonify(schema.dump(lottery_data)), 200

# Endpoint to retrieve a specific lottery data by ID
@app.route('/lottery/<int:id>', methods=['GET'])
def get_lottery_data_by_id(id):
    lottery_data = LotteryData.query.get(id)
    if not lottery_data:
        return jsonify({"error": "Lottery data not found."}), 404
    schema = LotteryDataSchema()
    return jsonify(schema.dump(lottery_data)), 200

# Endpoint to update lottery data
@app.route('/lottery/<int:id>', methods=['PUT'])
def update_lottery_data(id):
    lottery_data = LotteryData.query.get(id)
    if not lottery_data:
        return jsonify({"error": "Lottery data not found."}), 404

    schema = LotteryDataSchema()
    try:
        validated_data = schema.load(request.json)
        for key, value in validated_data.items():
            setattr(lottery_data, key, value)
        db.session.commit()
        return jsonify(schema.dump(lottery_data)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete lottery data
@app.route('/lottery/<int:id>', methods=['DELETE'])
def delete_lottery_data(id):
    lottery_data = LotteryData.query.get(id)
    if not lottery_data:
        return jsonify({"error": "Lottery data not found."}), 404

    db.session.delete(lottery_data)
    db.session.commit()
    return jsonify({"message": "Lottery data deleted."}), 204

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
