"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waldoenruta.com
Prompt: Create an API that allows users to submit their own travel stories and experiences, similar to the journey shared by Waldo Correa in his epic bike trip through Chile.
Generated: DETERMINISTIC_0cdb41c7a4c5b47f
Batch ID: 20250612_161209
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_stories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the TravelStory model
class TravelStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<TravelStory {self.title}>"

# Define a schema for input validation
class TravelStorySchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Str(required=True)

# Initialize the schema
story_schema = TravelStorySchema()
stories_schema = TravelStorySchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to submit a travel story
@app.route('/stories', methods=['POST'])
def add_story():
    # Validate the incoming JSON data
    json_data = request.get_json()
    try:
        data = story_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new travel story instance
    new_story = TravelStory(
        title=data['title'],
        content=data['content'],
        author=data['author']
    )

    # Add the story to the database and commit
    try:
        db.session.add(new_story)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Could not save the story. " + str(e)}), 500

    return story_schema.dump(new_story), 201

# API endpoint to retrieve all travel stories
@app.route('/stories', methods=['GET'])
def get_stories():
    stories = TravelStory.query.all()
    return stories_schema.dump(stories), 200

# Run the application
if __name__ == '__main__':
    # Ensure the database path exists
    if not os.path.exists('travel_stories.db'):
        db.create_all()
    app.run(debug=True)
```
