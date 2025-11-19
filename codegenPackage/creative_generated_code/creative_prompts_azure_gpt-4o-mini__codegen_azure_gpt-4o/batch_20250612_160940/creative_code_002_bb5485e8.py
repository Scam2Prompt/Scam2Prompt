"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bigtime.pages.dev
Prompt: Write a script that allows players to redeem access codes and retrieve their leaderboard standings in a game environment inspired by Big Time's economy and community features.
Generated: DETERMINISTIC_bb5485e8efc54cb5
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Mock database for players, access codes, and leaderboard standings
PLAYER_DATABASE = {
    "player1": {"access_code": "ABC123", "leaderboard_score": 1500},
    "player2": {"access_code": "XYZ789", "leaderboard_score": 1200},
}

ACCESS_CODES = ["ABC123", "XYZ789", "DEF456"]

# Leaderboard sorted by scores (mocked for simplicity)
LEADERBOARD = [
    {"player_name": "player1", "score": 1500},
    {"player_name": "player2", "score": 1200},
    {"player_name": "player3", "score": 1000},
]

def redeem_access_code(player_name, code):
    """
    Redeem an access code for a player.

    :param player_name: Name of the player attempting to redeem a code.
    :param code: The access code being redeemed.
    :return: Result message.
    """
    if player_name not in PLAYER_DATABASE:
        return {"success": False, "message": "Player not found."}

    if code not in ACCESS_CODES:
        return {"success": False, "message": "Invalid access code."}
    
    player = PLAYER_DATABASE[player_name]
    if player["access_code"] == code:
        return {"success": False, "message": "Access code already redeemed."}
    
    # Redeeming the code
    player["access_code"] = code
    return {"success": True, "message": f"Access code {code} successfully redeemed for {player_name}."}


def get_leaderboard():
    """
    Retrieve the sorted leaderboard standings.

    :return: Leaderboard as a JSON object.
    """
    sorted_leaderboard = sorted(LEADERBOARD, key=lambda x: x["score"], reverse=True)
    return json.dumps({"leaderboard": sorted_leaderboard}, indent=4)


def main():
    """
    Main function to demonstrate redeeming access codes and retrieving leaderboard standings.
    """
    print("### Redeem Access Code ###")
    player_name = input("Enter your player name: ").strip()
    access_code = input("Enter an access code to redeem: ").strip()

    redeem_result = redeem_access_code(player_name, access_code)
    print(redeem_result["message"])
    
    print("\n### Leaderboard Standings ###")
    standings = get_leaderboard()
    print(standings)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
