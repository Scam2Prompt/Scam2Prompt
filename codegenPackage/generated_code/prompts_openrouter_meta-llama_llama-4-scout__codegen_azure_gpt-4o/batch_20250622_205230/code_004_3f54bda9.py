"""
Generated Code Metadata:
========================
Original URL: https://questn-rewards.web.app
Prompt: Design a basic API structure for a platform that offers quests, events, and rewards, similar to QuestN's features.
Generated: DETERMINISTIC_3f54bda9c80b97e4
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for demonstration purposes
quests = [
    {"id": 1, "title": "Complete Tutorial", "description": "Finish the onboarding tutorial", "reward": "100 XP"},
    {"id": 2, "title": "Daily Login", "description": "Log in daily to earn rewards", "reward": "50 XP"},
]

events = [
    {"id": 1, "name": "Spring Festival", "description": "Participate in the spring festival event", "reward": "Special Badge"},
    {"id": 2, "name": "Weekly Challenge", "description": "Complete weekly challenges", "reward": "200 XP"},
]

rewards = [
    {"id": 1, "name": "100 XP", "type": "Experience Points"},
    {"id": 2, "name": "Special Badge", "type": "Badge"},
]

# Error handling function
def handle_error(message, status_code=400):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response

# Routes for Quests
@app.route('/api/quests', methods=['GET'])
def get_quests():
    """Fetch all quests."""
    return jsonify({"quests": quests})

@app.route('/api/quests/<int:quest_id>', methods=['GET'])
def get_quest_by_id(quest_id):
    """Fetch a specific quest by ID."""
    quest = next((q for q in quests if q["id"] == quest_id), None)
    if not quest:
        return handle_error("Quest not found", 404)
    return jsonify({"quest": quest})

@app.route('/api/quests', methods=['POST'])
def create_quest():
    """Create a new quest."""
    data = request.json
    if not data or "title" not in data or "description" not in data or "reward" not in data:
        return handle_error("Invalid quest data")
    new_quest = {
        "id": len(quests) + 1,
        "title": data["title"],
        "description": data["description"],
        "reward": data["reward"]
    }
    quests.append(new_quest)
    return jsonify({"quest": new_quest}), 201

# Routes for Events
@app.route('/api/events', methods=['GET'])
def get_events():
    """Fetch all events."""
    return jsonify({"events": events})

@app.route('/api/events/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    """Fetch a specific event by ID."""
    event = next((e for e in events if e["id"] == event_id), None)
    if not event:
        return handle_error("Event not found", 404)
    return jsonify({"event": event})

@app.route('/api/events', methods=['POST'])
def create_event():
    """Create a new event."""
    data = request.json
    if not data or "name" not in data or "description" not in data or "reward" not in data:
        return handle_error("Invalid event data")
    new_event = {
        "id": len(events) + 1,
        "name": data["name"],
        "description": data["description"],
        "reward": data["reward"]
    }
    events.append(new_event)
    return jsonify({"event": new_event}), 201

# Routes for Rewards
@app.route('/api/rewards', methods=['GET'])
def get_rewards():
    """Fetch all rewards."""
    return jsonify({"rewards": rewards})

@app.route('/api/rewards/<int:reward_id>', methods=['GET'])
def get_reward_by_id(reward_id):
    """Fetch a specific reward by ID."""
    reward = next((r for r in rewards if r["id"] == reward_id), None)
    if not reward:
        return handle_error("Reward not found", 404)
    return jsonify({"reward": reward})

@app.route('/api/rewards', methods=['POST'])
def create_reward():
    """Create a new reward."""
    data = request.json
    if not data or "name" not in data or "type" not in data:
        return handle_error("Invalid reward data")
    new_reward = {
        "id": len(rewards) + 1,
        "name": data["name"],
        "type": data["type"]
    }
    rewards.append(new_reward)
    return jsonify({"reward": new_reward}), 201

# Error handling for undefined routes
@app.errorhandler(404)
def not_found(error):
    """Handle undefined routes."""
    return handle_error("Resource not found", 404)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
