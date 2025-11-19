"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Create an API endpoint that allows users to claim their "Bonus New Member 100%" after registering on a slot gaming site.
Generated: DETERMINISTIC_56d615c623198b63
Batch ID: 20250612_155235
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
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a database URI appropriate for your setup
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model to represent registered users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    bonus_claimed = db.Column(db.Boolean, default=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/claim_bonus', methods=['POST'])
def claim_bonus():
    """API endpoint to claim the 'Bonus New Member 100%'."""
    try:
        # Retrieve JSON data from the request
        data = request.get_json()

        # Validate incoming data
        if not data or 'username' not in data:
            raise BadRequest('Missing username')

        username = data['username']

        # Fetch the user from the database
        user = User.query.filter_by(username=username).first()
        
        if user is None:
            raise NotFound('User not found')

        # Check if the bonus has already been claimed
        if user.bonus_claimed:
            return jsonify({'message': 'Bonus already claimed'}), 400

        # Mark the bonus as claimed
        user.bonus_claimed = True
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Bonus claimed successfully!'}), 200

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        # Log the exception (here just printing; in production, use proper logging)
        print(f"Internal Server Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
