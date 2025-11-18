"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myneel.com
Prompt: Suggest tools or libraries for building a real-time progress tracking system for a weight loss app, as described on Neel's webpage.
Generated: DETERMINISTIC_88e296d0188ff397
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_marshmallow import Marshmallow
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weight_loss_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Initialize SocketIO for real-time communication
socketio = SocketIO(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    target_weight = db.Column(db.Float, nullable=False)

    def __init__(self, name, weight, target_weight):
        self.name = name
        self.weight = weight
        self.target_weight = target_weight

# Create a schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new user
@app.route('/user', methods=['POST'])
def add_user():
    try:
        name = request.json['name']
        weight = request.json['weight']
        target_weight = request.json['target_weight']

        new_user = User(name=name, weight=weight, target_weight=target_weight)
        db.session.add(new_user)
        db.session.commit()
        
        # Emit a message to all connected clients
        socketio.emit('user_added', {'name': name, 'weight': weight})
        
        return UserSchema().jsonify(new_user), 201
    except Exception as e:
        logging.error(f"Error adding user: {e}")
        return {"message": "Error adding user"}, 500

# Endpoint to update user weight
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_weight(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            return {"message": "User not found"}, 404

        user.weight = request.json['weight']
        db.session.commit()

        # Emit an update message
        socketio.emit('weight_updated', {'id': user.id, 'weight': user.weight})

        return UserSchema().jsonify(user), 200
    except Exception as e:
        logging.error(f"Error updating weight for user {user_id}: {e}")
        return {"message": "Error updating weight"}, 500

# Run the app
if __name__ == '__main__':
    socketio.run(app, debug=True)
```
