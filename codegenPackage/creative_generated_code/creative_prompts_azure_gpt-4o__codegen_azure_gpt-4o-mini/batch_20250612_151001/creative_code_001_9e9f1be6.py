"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://card.xumicloud.top
Prompt: Recommend libraries or APIs that can be used to implement a web-based navigation system with features like private links and category selection, as seen on "须弥の导航页."
Generated: DETERMINISTIC_9e9f1be65759dc50
Batch ID: 20250612_151001
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
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///navigation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)  # Enable CORS for all routes

# Define the Link model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    private = db.Column(db.Boolean, default=False)

    def __init__(self, title, url, category, private=False):
        self.title = title
        self.url = url
        self.category = category
        self.private = private

# Define the Link schema
class LinkSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Link

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# GET endpoint to retrieve links with optional category filter
@app.route('/links', methods=['GET'])
def get_links():
    try:
        category = request.args.get('category')
        if category:
            links = Link.query.filter_by(category=category).all()
        else:
            links = Link.query.all()
        
        link_schema = LinkSchema(many=True)
        return jsonify(link_schema.dump(links)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST endpoint to add a new link
@app.route('/links', methods=['POST'])
def add_link():
    try:
        title = request.json['title']
        url = request.json['url']
        category = request.json['category']
        private = request.json.get('private', False)

        new_link = Link(title=title, url=url, category=category, private=private)
        db.session.add(new_link)
        db.session.commit()

        return jsonify({"message": "Link added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

**Requirements:**
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- Flask-CORS

Ensure to install these libraries using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow Flask-CORS
```
