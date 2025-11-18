"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Develop a REST API for managing sports betting data, including real-time updates and user bets, similar to the sportsbook functionality on VZ99.
Generated: DETERMINISTIC_d590abcd47962106
Batch ID: 20250612_154506
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
from flask_socketio import SocketIO, emit
import datetime

# Initialize Flask app and extensions
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_betting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

# ------------------------------------ Database Models ------------------------------------

class User(db.Model):
    """Model representing a user."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    balance = db.Column(db.Float, default=0.0)

class Match(db.Model):
    """Model representing a sports match."""
    id = db.Column(db.Integer, primary_key=True)
    team1 = db.Column(db.String(50), nullable=False)
    team2 = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='upcoming')  # upcoming, live, completed

class Bet(db.Model):
    """Model representing a bet placed by a user."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    team = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Create database tables
db.create_all()

# ------------------------------------ REST API Routes ------------------------------------

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.json
    try:
        username = data['username']
        balance = data.get('balance', 0.0)
        user = User(username=username, balance=balance)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!', 'user': {'id': user.id, 'username': user.username, 'balance': user.balance}}), 201
    except KeyError:
        return jsonify({'error': 'Invalid data provided.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/matches', methods=['POST'])
def create_match():
    """Create a new match."""
    data = request.json
    try:
        team1 = data['team1']
        team2 = data['team2']
        start_time = datetime.datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
        match = Match(team1=team1, team2=team2, start_time=start_time)
        db.session.add(match)
        db.session.commit()
        return jsonify({'message': 'Match created successfully!', 'match': {'id': match.id, 'team1': match.team1, 'team2': match.team2, 'start_time': match.start_time}}), 201
    except KeyError:
        return jsonify({'error': 'Invalid data provided.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/bets', methods=['POST'])
def place_bet():
    """Place a bet on a match."""
    data = request.json
    try:
        user_id = data['user_id']
        match_id = data['match_id']
        amount = data['amount']
        team = data['team']

        user = User.query.get(user_id)
        match = Match.query.get(match_id)

        if user is None:
            return jsonify({'error': 'User not found.'}), 404
        if match is None:
            return jsonify({'error': 'Match not found.'}), 404
        if user.balance < amount:
            return jsonify({'error': 'Insufficient balance.'}), 400

        bet = Bet(user_id=user_id, match_id=match_id, amount=amount, team=team)
        user.balance -= amount
        db.session.add(bet)
        db.session.commit()

        # Notify via WebSocket
        socketio.emit('bet_placed', {'user_id': user.id, 'match_id': match.id, 'team': team, 'amount': amount}, broadcast=True)

        return jsonify({'message': 'Bet placed successfully!', 'bet': {'id': bet.id, 'user_id': bet.user_id, 'match_id': bet.match_id, 'team': bet.team, 'amount': bet.amount}}), 201
    except KeyError:
        return jsonify({'error': 'Invalid data provided.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/matches/<int:match_id>', methods=['PATCH'])
def update_match_status(match_id):
    """Update the status of a match."""
    data = request.json
    try:
        status = data['status']
        match = Match.query.get(match_id)

        if match is None:
            return jsonify({'error': 'Match not found.'}), 404

        match.status = status
        db.session.commit()

        # Notify via WebSocket
        socketio.emit('match_updated', {'match_id': match.id, 'status': match.status}, broadcast=True)

        return jsonify({'message': 'Match status updated successfully!', 'match': {'id': match.id, 'team1': match.team1, 'team2': match.team2, 'status': match.status}}), 200
    except KeyError:
        return jsonify({'error': 'Invalid data provided.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ------------------------------------ WebSocket Event ------------------------------------

@socketio.on('connect')
def handle_connect():
    """Handle new WebSocket connections."""
    emit('message', {'message': 'Connected to sports betting API WebSocket!'})

# ------------------------------------ Error Handlers ------------------------------------

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({'error': 'An internal server error occurred.'}), 500

# ------------------------------------ Run the Application ------------------------------------

if __name__ == '__main__':
    socketio.run(app, debug=True)
```
