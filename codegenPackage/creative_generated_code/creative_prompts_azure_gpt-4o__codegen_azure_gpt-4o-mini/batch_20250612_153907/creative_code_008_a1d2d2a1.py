"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Recommend a library for implementing a category-based filtering system (e.g., "Farming," "Food Industry," "Medical") for profiles on a website.
Generated: DETERMINISTIC_a1d2d2a15252354a
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Profile {self.name}, Category {self.category}>'

# Create the database and the tables
with app.app_context():
    db.create_all()

# Endpoint to create a new profile
@app.route('/profiles', methods=['POST'])
def create_profile():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        new_profile = Profile(name=data['name'], category=data['category'])
        
        # Add the new profile to the session and commit
        db.session.add(new_profile)
        db.session.commit()
        
        return jsonify({'message': 'Profile created successfully!'}), 201
    except Exception as e:
        # Handle any exceptions that occur during profile creation
        return jsonify({'error': str(e)}), 400

# Endpoint to filter profiles by category
@app.route('/profiles', methods=['GET'])
def get_profiles_by_category():
    try:
        # Get the category from the query parameters
        category = request.args.get('category')
        
        if not category:
            return jsonify({'error': 'Category parameter is required!'}), 400
        
        # Query the database for profiles in the specified category
        profiles = Profile.query.filter_by(category=category).all()
        
        # Serialize the profiles to a list of dictionaries
        profile_list = [{'id': profile.id, 'name': profile.name, 'category': profile.category} for profile in profiles]
        
        return jsonify(profile_list), 200
    except Exception as e:
        # Handle any exceptions that occur during profile retrieval
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
