"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kid-69m.pages.dev
Prompt: Write code to create a "Yearbook" feature for AKCB, where NFT holders can voluntarily add and update their ownership history and personal details in a gallery format.
Generated: DETERMINISTIC_96cc5b81e37a5d2f
Batch ID: 20250612_150226
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
# Configure the database URI, please update with your actual database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yearbook.db'
db = SQLAlchemy(app)

class User(db.Model):
    """Model to represent a user in the yearbook."""
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    nfts_owned = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f'<User {self.wallet_address}>'

@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint to add a new user to the yearbook."""
    data = request.json
    try:
        new_user = User(
            wallet_address=data['wallet_address'],
            name=data['name'],
            bio=data.get('bio'),
            nfts_owned=data.get('nfts_owned', [])
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User with this wallet address already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/update_user/<wallet_address>', methods=['PUT'])
def update_user(wallet_address):
    """Endpoint to update an existing user's details."""
    user = User.query.filter_by(wallet_address=wallet_address).first()
    if user is None:
        return jsonify({"error": "User not found."}), 404
    
    data = request.json
    user.name = data.get('name', user.name)
    user.bio = data.get('bio', user.bio)
    user.nfts_owned = data.get('nfts_owned', user.nfts_owned)

    db.session.commit()
    return jsonify({"message": "User updated successfully!"}), 200

@app.route('/get_user/<wallet_address>', methods=['GET'])
def get_user(wallet_address):
    """Endpoint to retrieve a user's details by wallet address."""
    user = User.query.filter_by(wallet_address=wallet_address).first()
    if user is None:
        return jsonify({"error": "User not found."}), 404
    
    return jsonify({
        "wallet_address": user.wallet_address,
        "name": user.name,
        "bio": user.bio,
        "nfts_owned": user.nfts_owned
    }), 200

@app.route('/delete_user/<wallet_address>', methods=['DELETE'])
def delete_user(wallet_address):
    """Endpoint to delete a user from the yearbook."""
    user = User.query.filter_by(wallet_address=wallet_address).first()
    if user is None:
        return jsonify({"error": "User not found."}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully!"}), 200

if __name__ == '__main__':
    # Initialize the database (only necessary on first run)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

Make sure to install the required packages before running the code:

```bash
pip install Flask Flask-SQLAlchemy
``` 

This code creates a simple Flask application that allows NFT holders to manage their information in a "Yearbook" feature. Adjust the database URI as necessary for your production environment.
