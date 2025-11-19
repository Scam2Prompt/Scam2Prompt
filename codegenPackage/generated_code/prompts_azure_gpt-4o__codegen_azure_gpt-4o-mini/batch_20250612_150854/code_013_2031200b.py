"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.io
Prompt: Write code to simulate Immediate Peak's process of connecting users with investment education companies and tracking user engagement.
Generated: DETERMINISTIC_2031200b7c3e44df
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentEducationCompany:
    """Class representing an investment education company."""
    
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.engagement_data = []

    def add_engagement(self, user_id: int, engagement_score: float):
        """Add engagement data for a user."""
        self.engagement_data.append({
            'user_id': user_id,
            'engagement_score': engagement_score
        })
        logging.info(f"Engagement added for user {user_id} with score {engagement_score} at {self.name}.")

class User:
    """Class representing a user in the system."""
    
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

class InvestmentEducationPlatform:
    """Class to manage the investment education platform."""
    
    def __init__(self):
        self.companies: List[InvestmentEducationCompany] = []
        self.users: List[User] = []

    def add_company(self, company: InvestmentEducationCompany):
        """Add a new investment education company to the platform."""
        self.companies.append(company)
        logging.info(f"Company {company.name} added to the platform.")

    def add_user(self, user: User):
        """Add a new user to the platform."""
        self.users.append(user)
        logging.info(f"User {user.name} added to the platform.")

    def connect_user_to_company(self, user_id: int) -> Dict[str, Any]:
        """Connect a user to a random investment education company."""
        if not self.companies:
            logging.error("No companies available to connect to.")
            raise ValueError("No companies available to connect to.")

        user = next((u for u in self.users if u.user_id == user_id), None)
        if user is None:
            logging.error(f"User with ID {user_id} not found.")
            raise ValueError(f"User with ID {user_id} not found.")

        company = random.choice(self.companies)
        engagement_score = random.uniform(0, 100)  # Simulate an engagement score
        company.add_engagement(user_id, engagement_score)

        logging.info(f"User {user.name} connected to company {company.name}.")
        return {
            'user_id': user.user_id,
            'company_id': company.id,
            'company_name': company.name,
            'engagement_score': engagement_score
        }

# Example usage
if __name__ == "__main__":
    platform = InvestmentEducationPlatform()

    # Adding companies
    platform.add_company(InvestmentEducationCompany("InvestSmart", 1))
    platform.add_company(InvestmentEducationCompany("WealthWise", 2))

    # Adding users
    platform.add_user(User(1, "Alice"))
    platform.add_user(User(2, "Bob"))

    # Connecting users to companies and tracking engagement
    try:
        connection_info = platform.connect_user_to_company(1)
        print(connection_info)
    except ValueError as e:
        logging.error(f"Error: {e}")

    try:
        connection_info = platform.connect_user_to_company(3)  # This will raise an error
        print(connection_info)
    except ValueError as e:
        logging.error(f"Error: {e}")
```
