"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomrewards.com
Prompt: Create a simple web application that tracks user entries in cash giveaways and calculates potential earnings, based on the Phantom Rewards structure.
Generated: DETERMINISTIC_435b3ee7a27b2ce8
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import traceback

app = Flask(__name__)

# In-memory data store for user entries
user_entries = {}

# Phantom Rewards structure
# Example: {entry_amount: potential_earnings_percentage}
phantom_rewards_structure = {
    10: 5,   # $10 entry -> 5% potential earning
    50: 10,  # $50 entry -> 10% potential earning
    100: 15, # $100 entry -> 15% potential earning
}

def calculate_potential_earnings(entry_amount):
    """
    Calculate potential earnings based on Phantom Rewards structure.
    :param entry_amount: The amount entered by the user.
    :return: The potential earnings.
    """
    for amount, percentage in phantom_rewards_structure.items():
        if entry_amount >= amount:
            potential_earnings = (entry_amount * percentage) / 100
        else:
            break
    return potential_earnings

@app.route('/enter', methods=['POST'])
def enter_cash_giveaway():
    """
    Endpoint for users to enter into the cash giveaway.
    Expects a POST request with JSON payload containing 'username' and 'entry_amount'.
    """
    try:
        data = request.get_json()
        username = data.get('username')
        entry_amount = data.get('entry_amount')

        # Validate input
        if not username or not isinstance(entry_amount, (int, float)) or entry_amount <= 0:
            return jsonify({'error': 'Invalid input. Provide a valid username and positive entry_amount.'}), 400

        # Calculate potential earnings
        potential_earnings = calculate_potential_earnings(entry_amount)

        # Update user entries
        if username not in user_entries:
            user_entries[username] = []
        user_entries[username].append({
            'entry_amount': entry_amount,
            'potential_earnings': potential_earnings
        })

        return jsonify({
            'message': 'Entry successfully added.',
            'username': username,
            'entry_amount': entry_amount,
            'potential_earnings': potential_earnings
        })

    except Exception as e:
        # Log error details for debugging
        traceback.print_exc()
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

@app.route('/entries/<username>', methods=['GET'])
def get_user_entries(username):
    """
    Endpoint to retrieve all entries for a given username.
    :param username: The username whose entries are to be retrieved.
    """
    try:
        if username not in user_entries:
            return jsonify({'error': f'No entries found for user {username}.'}), 404

        return jsonify({
            'username': username,
            'entries': user_entries[username]
        })

    except Exception as e:
        # Log error details for debugging
        traceback.print_exc()
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

@app.route('/phantom_rewards_structure', methods=['GET'])
def get_rewards_structure():
    """
    Endpoint to retrieve the Phantom Rewards structure.
    """
    return jsonify({'phantom_rewards_structure': phantom_rewards_structure})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
