"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimedsonic.pages.dev
Prompt: Write code to implement a "Coinflip" feature for guild-based blockchain applications, inspired by the Guildhall platform.
Generated: DETERMINISTIC_53f3aecf2a8a3a1a
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate a simple database of guilds and their balances
guilds = {
    "guild1": {"balance": 100},
    "guild2": {"balance": 200},
}

@app.route('/coinflip', methods=['POST'])
def coinflip():
    """
    Coinflip API Endpoint
    Allows a guild to flip a coin and bet a specified amount.
    If the guild wins, their balance is increased by the bet amount.
    If the guild loses, their balance is decreased by the bet amount.
    """
    try:
        # Parse input data
        data = request.get_json()
        guild_id = data.get("guild_id")
        bet_amount = data.get("bet_amount")
        
        # Input validation
        if guild_id not in guilds:
            return jsonify({"error": "Invalid guild ID"}), 400
        
        if not isinstance(bet_amount, (int, float)) or bet_amount <= 0:
            return jsonify({"error": "Invalid bet amount. Must be a positive number."}), 400
        
        if guilds[guild_id]["balance"] < bet_amount:
            return jsonify({"error": "Insufficient balance for this bet"}), 400
        
        # Perform the coinflip
        outcome = random.choice(["heads", "tails"])
        user_choice = data.get("choice", "").lower()
        
        if user_choice not in ["heads", "tails"]:
            return jsonify({"error": "Invalid choice. Must be 'heads' or 'tails'"}), 400
        
        # Determine result and adjust balance
        if outcome == user_choice:
            guilds[guild_id]["balance"] += bet_amount
            result = "win"
        else:
            guilds[guild_id]["balance"] -= bet_amount
            result = "lose"
        
        # Return response
        return jsonify({
            "guild_id": guild_id,
            "outcome": outcome,
            "result": result,
            "new_balance": guilds[guild_id]["balance"]
        })

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@app.route('/guilds/<guild_id>', methods=['GET'])
def get_guild_balance(guild_id):
    """
    Endpoint to retrieve a guild's balance.
    """
    try:
        if guild_id not in guilds:
            return jsonify({"error": "Invalid guild ID"}), 400
        
        return jsonify({
            "guild_id": guild_id,
            "balance": guilds[guild_id]["balance"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
