"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-web.pages.dev
Prompt: Generate code for creating a digital pass system that tracks user profiles, rewards, and career opportunities, inspired by Metacade's platform functionality.
Generated: DETERMINISTIC_24b059259edaf866
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# digital_pass_system.py

import json
from typing import List, Dict, Optional

class UserProfile:
    """Class representing a user's profile in the digital pass system."""
    
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.rewards: List[str] = []
        self.career_opportunities: List[str] = []

    def add_reward(self, reward: str):
        """Add a reward to the user's profile."""
        if reward not in self.rewards:
            self.rewards.append(reward)
            print(f"Reward '{reward}' added to {self.username}'s profile.")
        else:
            print(f"Reward '{reward}' already exists in {self.username}'s profile.")

    def add_career_opportunity(self, opportunity: str):
        """Add a career opportunity to the user's profile."""
        if opportunity not in self.career_opportunities:
            self.career_opportunities.append(opportunity)
            print(f"Career opportunity '{opportunity}' added to {self.username}'s profile.")
        else:
            print(f"Career opportunity '{opportunity}' already exists in {self.username}'s profile.")

    def to_dict(self) -> Dict:
        """Convert the user profile to a dictionary."""
        return {
            "username": self.username,
            "email": self.email,
            "rewards": self.rewards,
            "career_opportunities": self.career_opportunities
        }

class DigitalPassSystem:
    """Class managing the digital pass system."""
    
    def __init__(self):
        self.user_profiles: Dict[str, UserProfile] = {}

    def create_user_profile(self, username: str, email: str) -> UserProfile:
        """Create a new user profile."""
        if username in self.user_profiles:
            raise ValueError(f"Username '{username}' already exists.")
        user_profile = UserProfile(username, email)
        self.user_profiles[username] = user_profile
        print(f"User profile for '{username}' created successfully.")
        return user_profile

    def get_user_profile(self, username: str) -> Optional[UserProfile]:
        """Retrieve a user profile by username."""
        return self.user_profiles.get(username)

    def save_profiles_to_file(self, filename: str):
        """Save all user profiles to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({username: profile.to_dict() for username, profile in self.user_profiles.items()}, file)
                print(f"User profiles saved to '{filename}'.")
        except IOError as e:
            print(f"Error saving profiles to file: {e}")

    def load_profiles_from_file(self, filename: str):
        """Load user profiles from a JSON file."""
        try:
            with open(filename, 'r') as file:
                profiles_data = json.load(file)
                for username, data in profiles_data.items():
                    user_profile = UserProfile(data['username'], data['email'])
                    user_profile.rewards = data.get('rewards', [])
                    user_profile.career_opportunities = data.get('career_opportunities', [])
                    self.user_profiles[username] = user_profile
                print(f"User profiles loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the file.")
        except IOError as e:
            print(f"Error loading profiles from file: {e}")

# Example Usage
if __name__ == "__main__":
    pass_system = DigitalPassSystem()
    
    # Create user profiles
    try:
        user1 = pass_system.create_user_profile("john_doe", "john@example.com")
        user1.add_reward("10% Discount")
        user1.add_career_opportunity("Junior Developer Position")
        
        user2 = pass_system.create_user_profile("jane_doe", "jane@example.com")
        user2.add_reward("Free Month Subscription")
        
    except ValueError as e:
        print(e)
    
    # Save to file
    pass_system.save_profiles_to_file("user_profiles.json")
    
    # Load from file
    pass_system.load_profiles_from_file("user_profiles.json")
```
