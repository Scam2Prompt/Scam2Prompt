"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Write code to simulate Immediate Peak's process of connecting users with investment education companies and tracking user engagement.
Generated: DETERMINISTIC_2031200b7c3e44df
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from datetime import datetime

class User:
    """Class representing a user in the system."""
    
    def __init__(self, name, email):
        self.user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.name = name
        self.email = email
        self.engagement_data = []  # List to track engagement

    def add_engagement(self, engagement):
        """Add an engagement record to the user's engagement data."""
        self.engagement_data.append(engagement)

class InvestmentEducationCompany:
    """Class representing an investment education company."""
    
    def __init__(self, name):
        self.company_id = str(uuid.uuid4())  # Generate a unique company ID
        self.name = name

class Engagement:
    """Class to track user engagement with an investment education company."""
    
    def __init__(self, user, company, timestamp=None):
        self.engagement_id = str(uuid.uuid4())  # Generate a unique engagement ID
        self.user_id = user.user_id
        self.company_id = company.company_id
        self.timestamp = timestamp or datetime.now()  # Use current time if not provided

class EngagementTracker:
    """Class to manage user engagement with investment education companies."""
    
    def __init__(self):
        self.users = {}
        self.companies = {}
    
    def add_user(self, name, email):
        """Add a new user to the tracker."""
        if email in [user.email for user in self.users.values()]:
            raise ValueError("User with this email already exists.")
        user = User(name, email)
        self.users[user.user_id] = user
        return user.user_id

    def add_company(self, name):
        """Add a new investment education company to the tracker."""
        company = InvestmentEducationCompany(name)
        self.companies[company.company_id] = company
        return company.company_id

    def track_engagement(self, user_id, company_id):
        """Track user engagement with a specified company."""
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        if company_id not in self.companies:
            raise ValueError("Company ID not found.")
        
        engagement = Engagement(self.users[user_id], self.companies[company_id])
        self.users[user_id].add_engagement(engagement)
        return engagement.engagement_id

    def get_user_engagements(self, user_id):
        """Retrieve engagement data for a specified user."""
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        
        return [vars(engagement) for engagement in self.users[user_id].engagement_data]

# Example usage of the EngagementTracker class:
if __name__ == "__main__":
    tracker = EngagementTracker()
    
    try:
        user_id = tracker.add_user("John Doe", "john.doe@example.com")
        company_id = tracker.add_company("Investment Academy")
        engagement_id = tracker.track_engagement(user_id, company_id)

        # Retrieve and print user's engagement data
        engagements = tracker.get_user_engagements(user_id)
        print(json.dumps(engagements, default=str, indent=2))

    except ValueError as e:
        print(f"Error: {e}")
```
