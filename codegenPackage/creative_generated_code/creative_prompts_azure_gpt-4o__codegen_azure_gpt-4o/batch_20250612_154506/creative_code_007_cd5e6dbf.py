"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asktollfree.com
Prompt: Provide recommendations for implementing a slot game demo API with features like those highlighted in the GELAY88 platform.
Generated: DETERMINISTIC_cd5e6dbf9d726e4c
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
import random

app = Flask(__name__)

# Define game configuration constants
REELS = [
    ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"],  # Symbols for Reel 1
    ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"],  # Symbols for Reel 2
    ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"],  # Symbols for Reel 3
]
PAYLINES = [
    [0, 0, 0],  # Top row
    [1, 1, 1],  # Middle row
    [2, 2, 2],  # Bottom row
]
PAYOUTS = {
    "Cherry": 10,
    "Lemon": 5,
    "Orange": 4,
    "Plum": 3,
    "Bell": 15,
    "Bar": 20,
}

# Define error messages
ERRORS = {
    "invalid_bet": "Invalid bet amount. Bet must be a positive number.",
    "invalid_request": "Invalid request format.",
}

# Game API route
@app.route("/slot-game/spin", methods=["POST"])
def spin():
    """
    Endpoint to spin the slot game reels.
    Expects a JSON payload with the bet amount.

    Request example:
    {
        "bet_amount": 100
    }

    Response example:
    {
        "bet_amount": 100,
        "reels": ["Cherry", "Bell", "Bar"],
        "payline": [0, 0, 0],
        "total_win": 10
    }
    """
    try:
        # Parse and validate request
        data = request.get_json()
        if not data or "bet_amount" not in data:
            return jsonify({"error": ERRORS["invalid_request"]}), 400

        bet_amount = data["bet_amount"]
        if not isinstance(bet_amount, (int, float)) or bet_amount <= 0:
            return jsonify({"error": ERRORS["invalid_bet"]}), 400

        # Simulate spinning the reels
        result_reels = [random.choice(reel) for reel in REELS]

        # Determine payline and calculate winnings
        chosen_payline = random.choice(PAYLINES)
        payline_symbols = [result_reels[pos] for pos in chosen_payline]

        # Check if all symbols in payline match (win condition)
        if all(symbol == payline_symbols[0] for symbol in payline_symbols):
            total_win = PAYOUTS[payline_symbols[0]] * bet_amount
        else:
            total_win = 0

        # Construct response
        response = {
            "bet_amount": bet_amount,
            "reels": result_reels,
            "payline": chosen_payline,
            "total_win": total_win,
        }
        return jsonify(response)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Health-check endpoint
@app.route("/slot-game/health", methods=["GET"])
def health_check():
    """
    Endpoint to check the health of the API.

    Response example:
    {
        "status": "healthy"
    }
    """
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    # Run the Flask server
    app.run(debug=True)
```
