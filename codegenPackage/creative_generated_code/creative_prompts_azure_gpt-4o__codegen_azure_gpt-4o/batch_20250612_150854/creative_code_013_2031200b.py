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
import uuid
from datetime import datetime

class User:
    """
    Represents a user in the system.
    """
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())  # Unique identifier for the user
        self.name = name
        self.email = email
        self.created_at = datetime.now()
        self.engagement_records = []  # Tracks engagement history

    def record_engagement(self, company_name, engagement_type, timestamp=None):
        """
        Records an engagement activity for the user.
        :param company_name: Name of the investment education company.
        :param engagement_type: Type of engagement (e.g., 'click', 'signup').
        :param timestamp: (Optional) When the engagement happened.
        """
        timestamp = timestamp or datetime.now()
        self.engagement_records.append({
            "company_name": company_name,
            "engagement_type": engagement_type,
            "timestamp": timestamp
        })

    def get_engagement_records(self):
        """
        Returns engagement history for the user.
        """
        return self.engagement_records


class InvestmentEducationCompany:
    """
    Represents an investment education company in the system.
    """
    def __init__(self, name, description):
        self.id = str(uuid.uuid4())  # Unique identifier for the company
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.user_engagements = {}  # Maps user ID to engagement counts

    def track_engagement(self, user_id):
        """
        Tracks user engagement for this company.
        :param user_id: ID of the user engaging with the company.
        """
        if user_id not in self.user_engagements:
            self.user_engagements[user_id] = 0
        self.user_engagements[user_id] += 1

    def get_engagement_summary(self):
        """
        Returns a summary of all user engagements for the company.
        """
        return self.user_engagements


class ImmediatePeak:
    """
    Simulates Immediate Peak's process of connecting users with investment education companies
    and tracking user engagements.
    """
    def __init__(self):
        self.users = {}  # Maps user ID to User objects
        self.companies = {}  # Maps company ID to InvestmentEducationCompany objects

    def register_user(self, name, email):
        """
        Registers a new user.
        :param name: Name of the user.
        :param email: Email of the user.
        :return: User object.
        """
        if email in [user.email for user in self.users.values()]:
            raise ValueError("Email already registered.")  # Ensure unique email addresses

        user = User(name, email)
        self.users[user.id] = user
        return user

    def register_company(self, name, description):
        """
        Registers a new investment education company.
        :param name: Name of the company.
        :param description: Description of the company.
        :return: InvestmentEducationCompany object.
        """
        company = InvestmentEducationCompany(name, description)
        self.companies[company.id] = company
        return company

    def connect_user_to_company(self, user_id, company_id, engagement_type):
        """
        Connects a user to an investment education company and records engagement.
        :param user_id: ID of the user.
        :param company_id: ID of the company.
        :param engagement_type: Type of engagement.
        """
        user = self.users.get(user_id)
        company = self.companies.get(company_id)

        if not user:
            raise ValueError("User not found.")
        if not company:
            raise ValueError("Company not found.")

        # Record user engagement
        user.record_engagement(company.name, engagement_type)
        company.track_engagement(user_id)

    def get_user_engagement_history(self, user_id):
        """
        Retrieves engagement history for a user.
        :param user_id: ID of the user.
        :return: List of engagement records.
        """
        user = self.users.get(user_id)

        if not user:
            raise ValueError("User not found.")

        return user.get_engagement_records()

    def get_company_engagement_summary(self, company_id):
        """
        Retrieves engagement summary for a company.
        :param company_id: ID of the company.
        :return: Dictionary mapping user IDs to engagement counts.
        """
        company = self.companies.get(company_id)

        if not company:
            raise ValueError("Company not found.")

        return company.get_engagement_summary()


# Example Usage:
if __name__ == "__main__":
    try:
        # Initialize Immediate Peak system
        system = ImmediatePeak()

        # Register users
        user1 = system.register_user("Alice", "alice@example.com")
        user2 = system.register_user("Bob", "bob@example.com")

        # Register investment education companies
        company1 = system.register_company("InvestCorp", "Learn investing strategies.")
        company2 = system.register_company("FinanceGuru", "Master financial literacy.")

        # Simulate user engagements
        system.connect_user_to_company(user1.id, company1.id, "click")
        system.connect_user_to_company(user1.id, company2.id, "signup")
        system.connect_user_to_company(user2.id, company1.id, "click")

        # Retrieve engagement history
        print("Alice's Engagement History:", system.get_user_engagement_history(user1.id))
        print("Bob's Engagement History:", system.get_user_engagement_history(user2.id))

        # Retrieve engagement summary for companies
        print("InvestCorp Engagement Summary:", system.get_company_engagement_summary(company1.id))
        print("FinanceGuru Engagement Summary:", system.get_company_engagement_summary(company2.id))

    except Exception as e:
        print("Error:", e)
```
