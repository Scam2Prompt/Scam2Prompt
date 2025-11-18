"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellyjelly.web.app
Prompt: Create a dashboard to display user profile information, including staking details and claimed $Jelly tokens, as described in the "My Profile" section.
Generated: DETERMINISTIC_dfa7965983fc3ead
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data for demonstration purposes
user_profiles = {
    "user1": {
        "username": "user1",
        "staking_details": {
            "staked_amount": 1000,
            "staking_duration": "30 days",
            "rewards": 50
        },
        "claimed_tokens": 200
    },
    "user2": {
        "username": "user2",
        "staking_details": {
            "staked_amount": 500,
            "staking_duration": "15 days",
            "rewards": 20
        },
        "claimed_tokens": 100
    }
}

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('dashboard.html')

@app.route('/profile/<username>')
def user_profile(username):
    """Fetch and return user profile information."""
    try:
        profile = user_profiles.get(username)
        if not profile:
            return jsonify({"error": "User not found"}), 404

        return jsonify(profile), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/update_staking', methods=['POST'])
def update_staking():
    """Update the staking details for a user."""
    try:
        data = request.json
        username = data.get('username')
        staked_amount = data.get('staked_amount')
        
        if username not in user_profiles:
            return jsonify({"error": "User not found"}), 404

        user_profiles[username]['staking_details']['staked_amount'] = staked_amount
        return jsonify({"message": "Staking details updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
</head>
<body>
    <h1>User Dashboard</h1>
    <div id="user-profile"></div>

    <script>
        async function loadUserProfile(username) {
            try {
                const response = await fetch(`/profile/${username}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const profile = await response.json();
                displayProfile(profile);
            } catch (error) {
                console.error('Error fetching user profile:', error);
            }
        }

        function displayProfile(profile) {
            const profileDiv = document.getElementById('user-profile');
            profileDiv.innerHTML = `
                <h2>${profile.username}</h2>
                <p>Staked Amount: ${profile.staking_details.staked_amount}</p>
                <p>Staking Duration: ${profile.staking_details.staking_duration}</p>
                <p>Rewards: ${profile.staking_details.rewards}</p>
                <p>Claimed $Jelly Tokens: ${profile.claimed_tokens}</p>
            `;
        }

        // Load user profile for a specific user
        loadUserProfile('user1'); // Change username as needed
    </script>
</body>
</html>
```
