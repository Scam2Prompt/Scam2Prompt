"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: Suggest tools or frameworks suitable for building an app like GiftGo that specializes in analyzing user data to recommend gifts.
Generated: DETERMINISTIC_9397993b9c8d8472
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'giftgo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    interests = db.Column(db.String(500))
    budget = db.Column(db.Float)
    past_purchases = db.Column(db.String(1000))

    def __init__(self, name, age, interests, budget, past_purchases):
        self.name = name
        self.age = age
        self.interests = interests
        self.budget = budget
        self.past_purchases = past_purchases

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'interests', 'budget', 'past_purchases')

# Initialize schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Define Gift model
class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    price = db.Column(db.Float)
    popularity = db.Column(db.Integer)
    tags = db.Column(db.String(500))

    def __init__(self, name, category, price, popularity, tags):
        self.name = name
        self.category = category
        self.price = price
        self.popularity = popularity
        self.tags = tags

# Gift Schema
class GiftSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'category', 'price', 'popularity', 'tags')

# Initialize schema
gift_schema = GiftSchema()
gifts_schema = GiftSchema(many=True)

# Recommendation Engine
class GiftRecommender:
    def __init__(self):
        self.model = NearestNeighbors(n_neighbors=5, algorithm='auto')
        self.gifts_df = None
        self.features = None

    def prepare_data(self, gifts):
        """Prepare gift data for recommendation engine"""
        self.gifts_df = pd.DataFrame([{
            'id': gift.id,
            'category': gift.category,
            'price': gift.price,
            'popularity': gift.popularity,
            'tags': gift.tags
        } for gift in gifts])

        # One-hot encode categories and tags
        categories = pd.get_dummies(self.gifts_df['category'])
        tags = self.gifts_df['tags'].str.get_dummies(sep=',')
        
        # Combine features
        self.features = pd.concat([
            categories,
            tags,
            self.gifts_df[['price', 'popularity']]
        ], axis=1)

        # Fit the model
        self.model.fit(self.features)

    def recommend(self, user_interests, user_budget, n_recommendations=5):
        """Generate gift recommendations based on user data"""
        if self.gifts_df is None:
            raise ValueError("Recommendation engine not initialized with gift data")

        # Create user profile vector
        user_tags = pd.Series(user_interests.split(',')).str.get_dummies().sum()
        user_vector = pd.concat([
            pd.Series([1 if col in user_interests else 0 for col in self.features.columns 
                      if col.startswith('category_')], index=[col for col in self.features.columns 
                      if col.startswith('category_')]),
            user_tags.reindex(self.features.columns, fill_value=0),
            pd.Series([user_budget, 0], index=['price', 'popularity'])
        ])

        # Find nearest neighbors
        distances, indices = self.model.kneighbors([user_vector])
        
        # Filter by budget and get top recommendations
        recommended_gifts = []
        for idx in indices[0]:
            gift = self.gifts_df.iloc[idx]
            if gift['price'] <= user_budget * 1.2:  # Allow 20% over budget
                recommended_gifts.append(gift)
                if len(recommended_gifts) >= n_recommendations:
                    break

        return recommended_gifts

# Initialize recommender
recommender = GiftRecommender()

# API Endpoints
@app.route('/api/users', methods=['POST'])
def add_user():
    """Add a new user to the database"""
    try:
        name = request.json['name']
        age = request.json['age']
        interests = request.json['interests']
        budget = request.json['budget']
        past_purchases = request.json.get('past_purchases', '')

        new_user = User(name, age, interests, budget, past_purchases)
        db.session.add(new_user)
        db.session.commit()

        return user_schema.jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/gifts', methods=['POST'])
def add_gift():
    """Add a new gift to the database"""
    try:
        name = request.json['name']
        category = request.json['category']
        price = request.json['price']
        popularity = request.json['popularity']
        tags = request.json['tags']

        new_gift = Gift(name, category, price, popularity, tags)
        db.session.add(new_gift)
        db.session.commit()

        # Update recommender with new gift data
        gifts = Gift.query.all()
        recommender.prepare_data(gifts)

        return gift_schema.jsonify(new_gift), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/recommend/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    """Get gift recommendations for a user"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        recommendations = recommender.recommend(user.interests, user.budget)
        return jsonify([gift.to_dict() for gift in recommendations]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Helper method to convert DataFrame row to dict
pd.DataFrame.to_dict = lambda self: {col: self[col] for col in self.index}

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
