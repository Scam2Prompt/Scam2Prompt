"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-gifts.blogspot.com
Prompt: Generate a code snippet for a gift recommendation API that suggests personalized gifts based on user preferences.
Generated: DETERMINISTIC_6722d6275565dea6
Batch ID: 20250612_160600
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database (using SQLite for simplicity; can be changed to any preferred DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gifts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing gift information
class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    keywords = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Gift {self.name}>'

# Initialize the database and create sample data
@app.before_first_request
def create_tables():
    db.create_all()
    if not Gift.query.first():
        sample_gifts = [
            Gift(name='Wireless Headphones', category='Electronics', keywords='music, tech, gift'),
            Gift(name='Cooking Class Voucher', category='Experiences', keywords='cooking, food, class'),
            Gift(name='Personalized Mug', category='Home', keywords='kitchen, home, personalized'),
        ]
        db.session.bulk_save_objects(sample_gifts)
        db.session.commit()

# Endpoint to get gift recommendations
@app.route('/recommend', methods=['POST'])
def recommend_gifts():
    try:
        # Get user preferences from the request
        user_preferences = request.json.get('preferences', [])
        if not user_preferences:
            return jsonify({'error': 'No preferences provided'}), 400

        # Find gifts that match user preferences
        recommendations = Gift.query.filter(Gift.keywords.ilike('%' + '% OR %'.join(user_preferences) + '%')).all()

        # Format the recommendations into a list of dicts
        gift_list = [{'id': gift.id, 'name': gift.name, 'category': gift.category} for gift in recommendations]

        # Return the recommendations as a JSON response
        return jsonify({'recommendations': gift_list}), 200

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': 'Database error', 'message': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
