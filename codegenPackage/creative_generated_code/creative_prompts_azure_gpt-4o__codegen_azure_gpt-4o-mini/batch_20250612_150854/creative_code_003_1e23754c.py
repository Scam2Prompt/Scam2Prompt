"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategpt.nl
Prompt: Create a Python script to simulate the process of connecting users to investment education companies after registration, as outlined on Immediate GPT.
Generated: DETERMINISTIC_1e23754c7c3402b1
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from typing import List, Dict

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """Class to represent a user in the investment education platform."""
    
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

class InvestmentEducationCompany:
    """Class to represent an investment education company."""
    
    def __init__(self, name: str, specialties: List[str]):
        self.name = name
        self.specialties = specialties

class RegistrationSystem:
    """Class to manage user registration and company connections."""
    
    def __init__(self):
        self.users: List[User] = []
        self.companies: List[InvestmentEducationCompany] = []

    def register_user(self, username: str, email: str) -> User:
        """Register a new user and return the User object."""
        if not username or not email:
            logging.error("Username and email must not be empty.")
            raise ValueError("Username and email must not be empty.")
        user = User(username, email)
        self.users.append(user)
        logging.info(f"User registered: {username}, {email}")
        return user

    def add_company(self, name: str, specialties: List[str]) -> InvestmentEducationCompany:
        """Add a new investment education company."""
        if not name or not specialties:
            logging.error("Company name and specialties must not be empty.")
            raise ValueError("Company name and specialties must not be empty.")
        company = InvestmentEducationCompany(name, specialties)
        self.companies.append(company)
        logging.info(f"Company added: {name} with specialties {specialties}")
        return company

    def connect_user_to_company(self, user: User) -> Dict[str, str]:
        """Connect a user to a random investment education company."""
        if not self.companies:
            logging.warning("No companies available to connect.")
            raise RuntimeError("No companies available to connect.")
        
        company = random.choice(self.companies)
        connection_info = {
            'user': user.username,
            'company': company.name,
            'specialties': company.specialties
        }
        logging.info(f"Connected user '{user.username}' to company '{company.name}'")
        return connection_info

def main():
    """Main function to simulate the registration and connection process."""
    registration_system = RegistrationSystem()
    
    # Adding some investment education companies
    registration_system.add_company("InvestSmart", ["Stocks", "Bonds", "Mutual Funds"])
    registration_system.add_company("WealthBuilders", ["Real Estate", "Retirement Planning"])
    
    # Registering a user
    try:
        user = registration_system.register_user("john_doe", "john@example.com")
        
        # Connecting registered user to a company
        connection_info = registration_system.connect_user_to_company(user)
        print(f"User {connection_info['user']} has been connected to {connection_info['company']} specializing in {', '.join(connection_info['specialties'])}.")
    
    except (ValueError, RuntimeError) as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
