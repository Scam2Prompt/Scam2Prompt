"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld2.pages.dev
Prompt: Can you provide an example of how to create a dual incentivization model for a socialfi platform like Everyworld, focusing on user engagement and environmental conservation?
Generated: DETERMINISTIC_7c9d882ef0e843e1
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SocialFiPlatform:
    """
    A SocialFi Platform that incentivizes users for engagement and environmental conservation.
    """
    def __init__(self):
        # Initialize user data and system logs
        self.users = {}  # Dictionary to store user information and activity
        self.environmental_fund = 0  # Fund for environmental initiatives

    def register_user(self, username):
        """
        Register a new user in the platform.
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        
        self.users[username] = {
            'engagement_points': 0,
            'eco_points': 0,
            'last_activity': None
        }
        print(f"User '{username}' registered successfully.")
    
    def log_engagement(self, username):
        """
        Log an engagement activity for a user (e.g., posting, commenting).
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")

        # Award engagement points
        self.users[username]['engagement_points'] += 10  # Example point system
        self.users[username]['last_activity'] = datetime.datetime.now()
        print(f"Engagement logged for user '{username}'. Points awarded: 10")

    def log_environmental_action(self, username, action_description):
        """
        Log an environmental conservation action (e.g., tree planting, recycling).
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        
        # Award eco points for environmental actions
        self.users[username]['eco_points'] += 20  # Example point system
        self.environmental_fund += 5  # Add funds for environmental initiatives
        print(f"Environmental action logged for user '{username}'. Points awarded: 20")
        print(f"Description: {action_description}")
    
    def user_summary(self, username):
        """
        Display user summary including points and last activity.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        
        user_data = self.users[username]
        summary = {
            'Engagement Points': user_data['engagement_points'],
            'Eco Points': user_data['eco_points'],
            'Last Activity': user_data['last_activity']
        }
        return summary
    
    def platform_summary(self):
        """
        Display a summary of the platform's environmental fund and user base stats.
        """
        total_engagement_points = sum(user['engagement_points'] for user in self.users.values())
        total_eco_points = sum(user['eco_points'] for user in self.users.values())
        
        summary = {
            'Total Engagement Points': total_engagement_points,
            'Total Eco Points': total_eco_points,
            'Environmental Fund': self.environmental_fund,
            'Registered Users': len(self.users)
        }
        return summary


# Example usage of the platform
if __name__ == "__main__":
    try:
        # Initialize the SocialFi platform
        platform = SocialFiPlatform()

        # Register users
        platform.register_user("Alice")
        platform.register_user("Bob")

        # Log activities
        platform.log_engagement("Alice")
        platform.log_environmental_action("Alice", "Planted a tree in the city park.")
        platform.log_engagement("Bob")
        platform.log_environmental_action("Bob", "Recycled 5kg of plastic waste.")

        # Display user summaries
        print("User Summary for Alice:")
        print(platform.user_summary("Alice"))

        print("\nUser Summary for Bob:")
        print(platform.user_summary("Bob"))

        # Display platform summary
        print("\nPlatform Summary:")
        print(platform.platform_summary())
        
    except Exception as e:
        print(f"Error: {e}")
```
