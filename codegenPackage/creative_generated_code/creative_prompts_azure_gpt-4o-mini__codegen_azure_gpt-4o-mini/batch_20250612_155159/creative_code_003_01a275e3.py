"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neami.shop
Prompt: Develop an API that enables users to submit and review business opportunities, ensuring a secure environment based on mutual trust and friendship.
Generated: DETERMINISTIC_01a275e3e0ed68f6
Batch ID: 20250612_155159
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
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.exceptions import BadRequest, Unauthorized

# Initialize Flask app and configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_opportunities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Model for business opportunities
class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class OpportunitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Opportunity

# Model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        raise BadRequest("Username and password are required")

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if not user:
        raise Unauthorized("Invalid username or password")

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

# Submit a new business opportunity
@app.route('/opportunities', methods=['POST'])
@jwt_required()
def submit_opportunity():
    title = request.json.get('title')
    description = request.json.get('description')

    if not title or not description:
        raise BadRequest("Title and description are required")

    user_id = get_jwt_identity()
    new_opportunity = Opportunity(title=title, description=description, user_id=user_id)
    db.session.add(new_opportunity)
    db.session.commit()

    return OpportunitySchema().jsonify(new_opportunity), 201

# Review all business opportunities
@app.route('/opportunities', methods=['GET'])
def get_opportunities():
    opportunities = Opportunity.query.all()
    return OpportunitySchema(many=True).jsonify(opportunities), 200

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify(error=str(error)), 400

# Error handling for unauthorized access
@app.errorhandler(Unauthorized)
def handle_unauthorized(error):
    return jsonify(error=str(error)), 401

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
