"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raffle-front-beige.vercel.app
Prompt: Create an API endpoint for retrieving active raffles and past raffles, including support for SOL and USDC tokens.
Generated: DETERMINISTIC_c9cd7a5a15b767df
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Mock data: a list of raffles
raffles = [
    {
        "id": 1,
        "name": "Raffle 1",
        "status": "active",
        "token": "SOL",
        "end_date": None
    },
    {
        "id": 2,
        "name": "Raffle 2",
        "status": "past",
        "token": "USDC",
        "end_date": "2023-08-15"
    },
    {
        "id": 3,
        "name": "Raffle 3",
        "status": "active",
        "token": "USDC",
        "end_date": None
    },
    {
        "id": 4,
        "name": "Raffle 4",
        "status": "past",
        "token": "SOL",
        "end_date": "2023-06-30"
    }
]

@app.route("/api/raffles", methods=["GET"])
def get_raffles():
    """
    API endpoint to retrieve active and past raffles.
    Filters can be applied using query parameters for token type.
    """
    try:
        # Retrieve query parameters for filtering by token type (SOL or USDC)
        token_filter = request.args.get("token", None)

        # Separate active and past raffles
        active_raffles = [
            raffle for raffle in raffles if raffle["status"] == "active"
        ]
        past_raffles = [
            raffle for raffle in raffles if raffle["status"] == "past"
        ]

        # Filter by token type if a filter is specified
        if token_filter:
            active_raffles = [
                raffle for raffle in active_raffles if raffle["token"] == token_filter
            ]
            past_raffles = [
                raffle for raffle in past_raffles if raffle["token"] == token_filter
            ]

        # Build the response
        response = {
            "active_raffles": active_raffles,
            "past_raffles": past_raffles,
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
