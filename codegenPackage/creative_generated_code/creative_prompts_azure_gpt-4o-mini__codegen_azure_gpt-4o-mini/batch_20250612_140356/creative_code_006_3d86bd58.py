"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Create a mobile app prototype that allows users to access S666's betting features, including a user-friendly interface for placing bets.
Generated: DETERMINISTIC_3d86bd58ca45ad13
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Bet model
class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    odds = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Bet {self.id} - User {self.user_id} - Amount {self.amount}>'

# Create the database and the Bet table
with app.app_context():
    db.create_all()

# Route to render the betting interface
@app.route('/')
def index():
    return render_template('index.html')

# Route to place a bet
@app.route('/place_bet', methods=['POST'])
def place_bet():
    """Place a bet using user input."""
    try:
        user_id = request.json.get('user_id')
        amount = request.json.get('amount')
        odds = request.json.get('odds')

        # Input validation
        if user_id is None or amount <= 0 or odds <= 0:
            raise BadRequest("Invalid input data.")

        # Create a new bet instance
        new_bet = Bet(user_id=user_id, amount=amount, odds=odds)

        # Add and commit the new bet to the database
        db.session.add(new_bet)
        db.session.commit()

        return jsonify({'message': 'Bet placed successfully!', 'bet_id': new_bet.id}), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while placing the bet.', 'details': str(e)}), 500

# Route to get all bets for a user
@app.route('/user_bets/<int:user_id>', methods=['GET'])
def get_user_bets(user_id):
    """Retrieve all bets placed by a specific user."""
    bets = Bet.query.filter_by(user_id=user_id).all()
    if not bets:
        raise NotFound("No bets found for this user.")

    return jsonify([{'id': bet.id, 'amount': bet.amount, 'odds': bet.odds} for bet in bets]), 200

# Error handling for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Betting App</title>
    <script>
        async function placeBet() {
            const userId = document.getElementById('user_id').value;
            const amount = Number(document.getElementById('amount').value);
            const odds = Number(document.getElementById('odds').value);

            const response = await fetch('/place_bet', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_id: userId, amount: amount, odds: odds })
            });

            const data = await response.json();
            alert(data.message || data.error);
        }
    </script>
</head>
<body>
    <h1>Betting App</h1>
    <h2>Place a Bet</h2>
    <input type="number" id="user_id" placeholder="User ID" required>
    <input type="number" id="amount" placeholder="Bet Amount" required>
    <input type="number" id="odds" placeholder="Odds" required>
    <button onclick="placeBet()">Place Bet</button>
</body>
</html>
```
