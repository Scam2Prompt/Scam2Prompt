"""
Generated Code Metadata:
========================
Original URL: https://argnt.xyz
Prompt: Develop a backend system for managing lottery app data, including fields like "邀请码" and "开奖信息," as described on the webpage.
Generated: DETERMINISTIC_7a27ce97c4cf02ce
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Lottery model
class Lottery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invite_code = db.Column(db.String(50), unique=True, nullable=False)  # "邀请码"
    draw_info = db.Column(db.String(200), nullable=False)  # "开奖信息"

    def __repr__(self):
        return f'<Lottery {self.invite_code}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new lottery entry
@app.route('/lottery', methods=['POST'])
def create_lottery():
    data = request.get_json()
    
    # Validate input data
    if not data or '邀请码' not in data or '开奖信息' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_lottery = Lottery(invite_code=data['邀请码'], draw_info=data['开奖信息'])
    
    try:
        db.session.add(new_lottery)
        db.session.commit()
        return jsonify({'message': 'Lottery entry created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Invite code already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get all lottery entries
@app.route('/lottery', methods=['GET'])
def get_lotteries():
    lotteries = Lottery.query.all()
    return jsonify([{'邀请码': lottery.invite_code, '开奖信息': lottery.draw_info} for lottery in lotteries]), 200

# Route to get a specific lottery entry by invite code
@app.route('/lottery/<string:invite_code>', methods=['GET'])
def get_lottery(invite_code):
    lottery = Lottery.query.filter_by(invite_code=invite_code).first()
    
    if lottery is None:
        return jsonify({'error': 'Lottery entry not found'}), 404
    
    return jsonify({'邀请码': lottery.invite_code, '开奖信息': lottery.draw_info}), 200

# Route to update a lottery entry
@app.route('/lottery/<string:invite_code>', methods=['PUT'])
def update_lottery(invite_code):
    data = request.get_json()
    lottery = Lottery.query.filter_by(invite_code=invite_code).first()
    
    if lottery is None:
        return jsonify({'error': 'Lottery entry not found'}), 404

    if '开奖信息' in data:
        lottery.draw_info = data['开奖信息']
    
    db.session.commit()
    return jsonify({'message': 'Lottery entry updated successfully'}), 200

# Route to delete a lottery entry
@app.route('/lottery/<string:invite_code>', methods=['DELETE'])
def delete_lottery(invite_code):
    lottery = Lottery.query.filter_by(invite_code=invite_code).first()
    
    if lottery is None:
        return jsonify({'error': 'Lottery entry not found'}), 404

    db.session.delete(lottery)
    db.session.commit()
    return jsonify({'message': 'Lottery entry deleted successfully'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
