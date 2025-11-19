"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Illustrate how to implement a feature in a mobile app that showcases CreatexPro's creative gift ideas and allows users to order customized items directly.
Generated: DETERMINISTIC_e935c508b30385f1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///createxpro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the GiftIdea model
class GiftIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price

# Create a schema for serializing GiftIdea objects
class GiftIdeaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GiftIdea

# Initialize the schema
gift_idea_schema = GiftIdeaSchema()
gift_ideas_schema = GiftIdeaSchema(many=True)

# Error handling decorator
def handle_error(e):
    response = {
        "status": "error",
        "message": str(e),
    }
    return jsonify(response), 400

# Route to create a new gift idea
@app.route('/gift-ideas', methods=['POST'])
def add_gift_idea():
    try:
        title = request.json.get('title')
        description = request.json.get('description')
        price = request.json.get('price')

        # Validate input
        if not title or not description or price is None:
            return handle_error("All fields are required.")

        # Create a new gift idea
        new_gift_idea = GiftIdea(title, description, price)
        db.session.add(new_gift_idea)
        db.session.commit()

        return gift_idea_schema.jsonify(new_gift_idea), 201
    except Exception as e:
        return handle_error(e)

# Route to retrieve all gift ideas
@app.route('/gift-ideas', methods=['GET'])
def get_gift_ideas():
    try:
        all_gift_ideas = GiftIdea.query.all()
        return gift_ideas_schema.jsonify(all_gift_ideas), 200
    except Exception as e:
        return handle_error(e)

# Route to order a customized item
@app.route('/order', methods=['POST'])
def order_customized_item():
    try:
        gift_idea_id = request.json.get('gift_idea_id')
        custom_message = request.json.get('custom_message')

        # Validate input
        if gift_idea_id is None or not custom_message:
            return handle_error("Gift idea ID and custom message are required.")

        # Placeholder for order processing logic
        # In a real application, you would implement the order logic here

        return jsonify({"status": "success", "message": "Order placed successfully!"}), 201
    except Exception as e:
        return handle_error(e)

# Run the app
if __name__ == '__main__':
    with app.app_context():
        # Create the database tables
        db.create_all()
    app.run(debug=True)
```
