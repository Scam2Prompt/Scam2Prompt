"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitzino.vip
Prompt: Design a rewards program API that tracks user XP and ranks in a gaming platform, inspired by the features of Bitzino's leaderboard system.
Generated: DETERMINISTIC_3750316de08b6df3
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# In-memory storage for users' XP and ranks
# In production, this should be replaced by a proper database
users_data = defaultdict(lambda: {"xp": 0, "rank": None})

# Constants for rank thresholds
RANK_THRESHOLDS = {
    "Bronze": 0,
    "Silver": 1000,
    "Gold": 5000,
    "Platinum": 10000
}


def calculate_rank(xp):
    """
    Calculate the rank of a user based on their XP.
    :param xp: Integer XP value
    :return: String rank name
    """
    for rank, threshold in sorted(RANK_THRESHOLDS.items(), key=lambda x: x[1], reverse=True):
        if xp >= threshold:
            return rank
    return "Bronze"  # Default rank


@app.route("/user/<username>/status", methods=["GET"])
def get_user_status(username):
    """
    Get the current XP and rank of a user.
    :param username: String username
    :return: JSON response with user XP and rank
    """
    if username not in users_data:
        return jsonify({"error": "User not found"}), 404

    user_info = users_data[username]
    return jsonify({"username": username, "xp": user_info["xp"], "rank": user_info["rank"]})


@app.route("/user/<username>/update_xp", methods=["POST"])
def update_user_xp(username):
    """
    Update the XP of a user.
    :param username: String username
    :return: JSON response with updated user XP and rank
    """
    data = request.get_json()

    if not data or "xp" not in data:
        return jsonify({"error": "Invalid request body"}), 400

    try:
        xp_to_add = int(data["xp"])
        if xp_to_add < 0:
            raise ValueError("XP value cannot be negative.")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    # Update or create user data
    users_data[username]["xp"] += xp_to_add
    users_data[username]["rank"] = calculate_rank(users_data[username]["xp"])

    user_info = users_data[username]
    return jsonify({"username": username, "xp": user_info["xp"], "rank": user_info["rank"]})


@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    """
    Get the leaderboard sorted by XP in descending order.
    :return: JSON response with sorted leaderboard
    """
    leaderboard = sorted(
        [{"username": username, "xp": data["xp"], "rank": data["rank"]}
         for username, data in users_data.items()],
        key=lambda x: x["xp"],
        reverse=True
    )
    return jsonify({"leaderboard": leaderboard})


@app.errorhandler(404)
def handle_404(error):
    """Custom 404 error handler."""
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def handle_500(error):
    """Custom 500 error handler."""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
