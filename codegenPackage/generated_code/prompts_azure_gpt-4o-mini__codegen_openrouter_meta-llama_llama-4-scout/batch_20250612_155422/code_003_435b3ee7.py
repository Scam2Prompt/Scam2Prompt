"""
Generated Code Metadata:
========================
Original URL: https://phantomrewards.com
Prompt: Create a simple web application that tracks user entries in cash giveaways and calculates potential earnings, based on the Phantom Rewards structure.
Generated: DETERMINISTIC_435b3ee7a27b2ce8
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**phantom_rewards_tracker.py**
```python
from flask import Flask, request, jsonify
from typing import Dict

app = Flask(__name__)

# Phantom Rewards structure
PHANTOM_REWARDS_TIERS = {
    1: 0.1,  # 10% reward for 1 entry
    5: 0.2,  # 20% reward for 5 entries
    10: 0.3,  # 30% reward for 10 entries
    20: 0.4,  # 40% reward for 20 entries
    50: 0.5   # 50% reward for 50 entries
}

# In-memory storage for user entries (replace with a database in production)
user_entries: Dict[str, int] = {}

@app.route('/entries', methods=['POST'])
def add_entry():
    """Add a new entry for a user"""
    data = request.json
    if 'user_id' not in data:
        return jsonify({'error': 'User ID is required'}), 400
    
    user_id = data['user_id']
    if user_id in user_entries:
        user_entries[user_id] += 1
    else:
        user_entries[user_id] = 1
    
    return jsonify({'message': 'Entry added successfully'}), 201

@app.route('/entries', methods=['GET'])
def get_entries():
    """Get the total number of entries for a user"""
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    entries = user_entries.get(user_id, 0)
    return jsonify({'entries': entries}), 200

@app.route('/potential_earnings', methods=['GET'])
def calculate_potential_earnings():
    """Calculate potential earnings for a user based on Phantom Rewards structure"""
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    entries = user_entries.get(user_id, 0)
    potential_earnings = 0
    
    # Find the highest tier that the user qualifies for
    for tier, reward in PHANTOM_REWARDS_TIERS.items():
        if entries >= tier:
            potential_earnings = reward
        else:
            break
    
    return jsonify({'potential_earnings': potential_earnings}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**tests/test_phantom_rewards_tracker.py**
```python
import unittest
import json
from phantom_rewards_tracker import app, user_entries, PHANTOM_REWARDS_TIERS

class TestPhantomRewardsTracker(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        user_entries.clear()

    def test_add_entry(self):
        response = self.app.post('/entries', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(user_entries['user1'], 1)

    def test_get_entries(self):
        user_entries['user1'] = 5
        response = self.app.get('/entries', query_string={'user_id': 'user1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['entries'], 5)

    def test_calculate_potential_earnings(self):
        user_entries['user1'] = 10
        response = self.app.get('/potential_earnings', query_string={'user_id': 'user1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['potential_earnings'], 0.3)

    def test_calculate_potential_earnings_tier_not_qualified(self):
        user_entries['user1'] = 4
        response = self.app.get('/potential_earnings', query_string={'user_id': 'user1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['potential_earnings'], 0)

if __name__ == '__main__':
    unittest.main()
```
