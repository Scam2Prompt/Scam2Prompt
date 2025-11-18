"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbank-debank.github.io
Prompt: Suggest methods to implement social networking features in a DeFi portfolio tracker, inspired by Debank's community and social functionalities.
Generated: DETERMINISTIC_8fdba61a0043e9dc
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: social_features.py
# Description: Implements social networking features for a DeFi portfolio tracker.
# Author: Professional Developer
# Language: Python

from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory data stores for demonstration purposes
users = {}  # Stores user profiles
portfolio_shares = {}  # Stores shared portfolios
comments = {}  # Stores comments on shared portfolios

# Utility functions
def generate_id():
    """Generates a unique ID for any entity."""
    return str(uuid.uuid4())

def validate_user(user_id):
    """Validates if the user exists."""
    if user_id not in users:
        raise ValueError("User ID not found.")

def validate_portfolio(portfolio_id):
    """Validates if the portfolio exists."""
    if portfolio_id not in portfolio_shares:
        raise ValueError("Portfolio ID not found.")

# ========================
# Social Networking APIs
# ========================

@app.route('/create_user', methods=['POST'])
def create_user():
    """
    Creates a new user profile.
    Request JSON:
    {
        "username": "example_user",
        "bio": "Short bio about the user"
    }
    """
    try:
        data = request.json
        user_id = generate_id()
        users[user_id] = {
            "username": data.get("username"),
            "bio": data.get("bio", ""),
            "created_at": datetime.utcnow().isoformat()
        }
        return jsonify({"message": "User created successfully", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/share_portfolio', methods=['POST'])
def share_portfolio():
    """
    Shares a user's portfolio publicly.
    Request JSON:
    {
        "user_id": "user_id",
        "portfolio_data": {
            "assets": [{"name": "ETH", "amount": 10.5}, {"name": "BTC", "amount": 0.5}],
            "total_value": 50000
        },
        "description": "My current portfolio"
    }
    """
    try:
        data = request.json
        user_id = data.get("user_id")
        validate_user(user_id)

        portfolio_id = generate_id()
        portfolio_shares[portfolio_id] = {
            "user_id": user_id,
            "portfolio_data": data.get("portfolio_data"),
            "description": data.get("description", ""),
            "created_at": datetime.utcnow().isoformat()
        }
        return jsonify({"message": "Portfolio shared successfully", "portfolio_id": portfolio_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/comment_on_portfolio', methods=['POST'])
def comment_on_portfolio():
    """
    Adds a comment on a shared portfolio.
    Request JSON:
    {
        "user_id": "user_id",
        "portfolio_id": "portfolio_id",
        "comment": "Great portfolio!"
    }
    """
    try:
        data = request.json
        user_id = data.get("user_id")
        portfolio_id = data.get("portfolio_id")
        validate_user(user_id)
        validate_portfolio(portfolio_id)

        comment_id = generate_id()
        comments[comment_id] = {
            "user_id": user_id,
            "portfolio_id": portfolio_id,
            "comment": data.get("comment"),
            "created_at": datetime.utcnow().isoformat()
        }
        return jsonify({"message": "Comment added successfully", "comment_id": comment_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/get_shared_portfolios', methods=['GET'])
def get_shared_portfolios():
    """
    Retrieves all shared portfolios.
    Response JSON:
    [
        {
            "portfolio_id": "portfolio_id",
            "user_id": "user_id",
            "portfolio_data": {...},
            "description": "Portfolio description",
            "created_at": "timestamp"
        }
    ]
    """
    try:
        return jsonify(list(portfolio_shares.values())), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_comments/<portfolio_id>', methods=['GET'])
def get_comments(portfolio_id):
    """
    Retrieves all comments on a specific shared portfolio.
    Response JSON:
    [
        {
            "comment_id": "comment_id",
            "user_id": "user_id",
            "portfolio_id": "portfolio_id",
            "comment": "Comment text",
            "created_at": "timestamp"
        }
    ]
    """
    try:
        validate_portfolio(portfolio_id)
        portfolio_comments = [
            comment for comment in comments.values() if comment["portfolio_id"] == portfolio_id
        ]
        return jsonify(portfolio_comments), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors."""
    return jsonify({"error": "Resource not found"}), 404


# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
