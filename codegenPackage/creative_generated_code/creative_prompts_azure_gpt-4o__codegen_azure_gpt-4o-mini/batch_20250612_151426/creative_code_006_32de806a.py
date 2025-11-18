"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myneel.com
Prompt: Create a Python script that incorporates gamification elements, such as leaderboards and challenges, to encourage users to stay on track with their weight loss goals, as described on myneel.com.
Generated: DETERMINISTIC_32de806af13aba2e
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

class User:
    """Represents a user in the weight loss challenge."""
    
    def __init__(self, username):
        self.username = username
        self.weight_loss_goals = []
        self.current_weight = None
        self.weight_records = []
        self.score = 0
    
    def set_current_weight(self, weight):
        """Set the current weight of the user."""
        self.current_weight = weight
        self.weight_records.append(weight)
    
    def add_weight_loss_goal(self, goal):
        """Add a weight loss goal for the user."""
        self.weight_loss_goals.append(goal)
    
    def record_weight_loss(self, weight_loss):
        """Record weight loss and update score."""
        if weight_loss > 0:
            self.score += weight_loss * 10  # Example scoring system: 10 points per kg lost

class Challenge:
    """Represents a weight loss challenge."""
    
    def __init__(self, name):
        self.name = name
        self.participants = {}
    
    def add_participant(self, user):
        """Add a user to the challenge."""
        self.participants[user.username] = user
    
    def calculate_leaderboard(self):
        """Calculate and return the leaderboard sorted by score."""
        leaderboard = sorted(self.participants.values(), key=lambda u: u.score, reverse=True)
        return [(user.username, user.score) for user in leaderboard]

class WeightLossApp:
    """Main application to manage weight loss challenges and users."""
    
    def __init__(self):
        self.challenges = {}
    
    def create_challenge(self, name):
        """Create a new weight loss challenge."""
        if name in self.challenges:
            raise ValueError("Challenge with this name already exists.")
        self.challenges[name] = Challenge(name)
    
    def add_user_to_challenge(self, challenge_name, username):
        """Add a user to a specific challenge."""
        if challenge_name not in self.challenges:
            raise ValueError("Challenge not found.")
        user = User(username)
        self.challenges[challenge_name].add_participant(user)
    
    def save_data(self, filename):
        """Save the application data to a JSON file."""
        data = {name: [{'username': user.username, 'score': user.score} for user in challenge.participants.values()]
                for name, challenge in self.challenges.items()}
        with open(filename, 'w') as f:
            json.dump(data, f)
    
    def load_data(self, filename):
        """Load application data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            for challenge_name, users in data.items():
                self.create_challenge(challenge_name)
                for user_data in users:
                    user = User(user_data['username'])
                    user.score = user_data['score']
                    self.challenges[challenge_name].add_participant(user)
        except FileNotFoundError:
            print("File not found, starting with an empty application.")
        except json.JSONDecodeError:
            print("Error reading the JSON file.")

# Example usage:
if __name__ == "__main__":
    app = WeightLossApp()
    
    # Load existing data
    app.load_data('weight_loss_data.json')
    
    # Create a new challenge
    app.create_challenge("Summer Slimdown")
    
    # Add users
    app.add_user_to_challenge("Summer Slimdown", "Alice")
    app.add_user_to_challenge("Summer Slimdown", "Bob")

    # Update user weights and scores
    user_alice = app.challenges["Summer Slimdown"].participants["Alice"]
    user_alice.set_current_weight(70)
    user_alice.record_weight_loss(2)  # Alice lost 2 kg
    
    user_bob = app.challenges["Summer Slimdown"].participants["Bob"]
    user_bob.set_current_weight(85)
    user_bob.record_weight_loss(3)  # Bob lost 3 kg
    
    # Print leaderboard
    leaderboard = app.challenges["Summer Slimdown"].calculate_leaderboard()
    print("Leaderboard:", leaderboard)
    
    # Save data
    app.save_data('weight_loss_data.json')
```
