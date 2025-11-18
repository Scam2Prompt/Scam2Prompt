"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cokiessnew.pages.dev
Prompt: Develop a script to integrate the Cookie Bakery quests system into a web application, allowing users to earn community points by completing tasks.
Generated: DETERMINISTIC_b4f4a54421da10ec
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users and quests (for the sake of demonstration)
users = {}
quests = {
    1: {'name': 'Bake 10 Cookies', 'points': 50},
    2: {'name': 'Sell 50 Cookies', 'points': 100},
    3: {'name': 'Help a Neighbor Bake Cookies', 'points': 75},
}

@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    Input: JSON payload with 'username'
    Output: Confirmation message
    """
    try:
        data = request.json
        username = data.get('username')

        if not username:
            return jsonify({'error': 'Username is required'}), 400

        if username in users:
            return jsonify({'error': 'Username already exists'}), 400

        # Add the user with an initial score of 0
        users[username] = {'points': 0, 'completed_quests': []}
        return jsonify({'message': f'User {username} registered successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/quests', methods=['GET'])
def list_quests():
    """
    List all available quests.
    Output: JSON list of quests
    """
    try:
        return jsonify({'quests': quests})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/complete_quest', methods=['POST'])
def complete_quest():
    """
    Allow a user to complete a quest and earn points.
    Input: JSON payload with 'username' and 'quest_id'
    Output: Updated user points and completed quests
    """
    try:
        data = request.json
        username = data.get('username')
        quest_id = data.get('quest_id')

        if not username or not quest_id:
            return jsonify({'error': 'Username and quest_id are required'}), 400

        # Check if user exists
        if username not in users:
            return jsonify({'error': 'Invalid username'}), 404

        # Validate quest_id
        if quest_id not in quests:
            return jsonify({'error': 'Invalid quest_id'}), 404

        # Check if the quest has already been completed by the user
        if quest_id in users[username]['completed_quests']:
            return jsonify({'error': 'Quest already completed'}), 400

        # Add quest points to user
        users[username]['points'] += quests[quest_id]['points']
        users[username]['completed_quests'].append(quest_id)

        return jsonify({
            'message': f'Quest {quest_id} completed successfully',
            'user': users[username]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/user_points', methods=['GET'])
def get_user_points():
    """
    Retrieve a user's points and completed quests.
    Input: Query parameter 'username'
    Output: User's points and completed quests
    """
    try:
        username = request.args.get('username')
        
        if not username:
            return jsonify({'error': 'Username is required'}), 400

        # Check if user exists
        if username not in users:
            return jsonify({'error': 'Invalid username'}), 404

        return jsonify({'user': users[username]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
