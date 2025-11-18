"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Create a REST API for managing sports betting transactions, including placing bets, updating odds, and tracking payouts, inspired by BaxBet's sports betting section.
Generated: DETERMINISTIC_82a506ae0618c911
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for transactions and odds
bets = {}
odds = {}
payouts = {}

# Helper functions
def calculate_payout(bet_amount, odd):
    return round(bet_amount * odd, 2)

# Routes
@app.route('/bets', methods=['POST'])
def place_bet():
    """
    Endpoint to place a bet.
    Request Body:
    {
        "user_id": "<string>",
        "sport": "<string>",
        "team": "<string>",
        "bet_amount": <float>
    }
    """
    try:
        data = request.json
        user_id = data['user_id']
        sport = data['sport']
        team = data['team']
        bet_amount = data['bet_amount']

        if sport not in odds or team not in odds[sport]:
            return jsonify({"error": "Odds for the specified team or sport are not available."}), 404

        odd = odds[sport][team]
        payout = calculate_payout(bet_amount, odd)

        bet_id = str(uuid.uuid4())
        bets[bet_id] = {
            "user_id": user_id,
            "sport": sport,
            "team": team,
            "bet_amount": bet_amount,
            "odd": odd,
            "potential_payout": payout,
            "status": "placed"
        }

        return jsonify({"bet_id": bet_id, "details": bets[bet_id]}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/odds', methods=['PUT'])
def update_odds():
    """
    Endpoint to update odds.
    Request Body:
    {
        "sport": "<string>",
        "team": "<string>",
        "odd": <float>
    }
    """
    try:
        data = request.json
        sport = data['sport']
        team = data['team']
        odd = data['odd']

        if odd <= 0:
            return jsonify({"error": "Odds must be greater than 0."}), 400

        if sport not in odds:
            odds[sport] = {}

        odds[sport][team] = odd

        return jsonify({"message": "Odds updated successfully.", "odds": odds}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/payouts/<bet_id>', methods=['GET'])
def get_payout(bet_id):
    """
    Endpoint to retrieve payout details for a bet.
    """
    try:
        bet = bets.get(bet_id)

        if not bet:
            return jsonify({"error": "Bet not found."}), 404

        if bet_id in payouts:
            return jsonify({"bet_id": bet_id, "payout": payouts[bet_id]}), 200

        return jsonify({"message": "Bet is still active or awaiting finalization.", "bet": bet}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/finalize-bet/<bet_id>', methods=['POST'])
def finalize_bet(bet_id):
    """
    Endpoint to finalize a bet and calculate payout.
    Request Body:
    {
        "result": "<win/loss>"
    }
    """
    try:
        bet = bets.get(bet_id)

        if not bet:
            return jsonify({"error": "Bet not found."}), 404

        data = request.json
        result = data['result']

        if result not in ['win', 'loss']:
            return jsonify({"error": "Invalid result. Must be 'win' or 'loss'."}), 400

        if result == 'win':
            payouts[bet_id] = bet['potential_payout']
            bet['status'] = 'completed'
        else:
            payouts[bet_id] = 0
            bet['status'] = 'completed'

        return jsonify({"message": "Bet finalized.", "bet": bet, "payout": payouts[bet_id]}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
