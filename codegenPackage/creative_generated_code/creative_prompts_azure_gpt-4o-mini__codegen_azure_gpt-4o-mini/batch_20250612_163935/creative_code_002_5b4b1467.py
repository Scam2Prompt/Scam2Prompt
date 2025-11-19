"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Create an API endpoint that allows users to search for sports items like "Troféus" and "Medalhas" based on specific sports or activities mentioned in the blog content.
Generated: DETERMINISTIC_5b4b146731684aa3
Batch ID: 20250612_163935
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for sports items
class SportsItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sport = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sport': self.sport
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/sports-items', methods=['GET'])
def search_sports_items():
    """
    API endpoint to search for sports items based on sport type.
    
    Query Parameters:
        sport (str): The type of sport or activity to filter items.
    
    Returns:
        JSON response containing a list of sports items.
    """
    sport = request.args.get('sport', default='', type=str)

    # Input validation
    if not sport:
        return jsonify({'error': 'Sport parameter is required'}), 400

    try:
        # Query the database for sports items that match the sport type
        items = SportsItem.query.filter(SportsItem.sport.ilike(f'%{sport}%')).all()
        return jsonify([item.to_dict() for item in items]), 200
    except SQLAlchemyError as e:
        # Handle database errors and return a 500 error
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
