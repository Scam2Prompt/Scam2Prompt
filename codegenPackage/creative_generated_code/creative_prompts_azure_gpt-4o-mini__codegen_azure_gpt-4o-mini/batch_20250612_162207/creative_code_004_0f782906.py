"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petn.org
Prompt: Construct a REST API endpoint that allows users to submit comments to the Presbytery of East Tennessee, as referenced on their contact page.
Generated: DETERMINISTIC_0f7829068860bace
Batch ID: 20250612_162207
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Define the schema for validating comments
class CommentSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    message = fields.String(required=True)

# Initialize the schema
comment_schema = CommentSchema()

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

@app.errorhandler(Exception)
def handle_general_exception(error):
    return jsonify({"error": "An unexpected error occurred."}), 500

# Define the endpoint for submitting comments
@app.route('/api/comments', methods=['POST'])
def submit_comment():
    try:
        # Validate and deserialize the input data
        data = request.get_json()
        validated_data = comment_schema.load(data)

        # Create a new Comment instance
        comment = Comment(
            name=validated_data['name'],
            email=validated_data['email'],
            message=validated_data['message']
        )

        # Add the comment to the session and commit to the database
        db.session.add(comment)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Comment submitted successfully."}), 201

    except ValidationError as err:
        return handle_validation_error(err)
    except Exception as e:
        return handle_general_exception(e)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```
