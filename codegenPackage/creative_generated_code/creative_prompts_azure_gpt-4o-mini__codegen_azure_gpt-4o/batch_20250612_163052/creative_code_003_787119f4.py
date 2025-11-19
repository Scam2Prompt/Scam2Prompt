"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Describe how Immediate Peak facilitates the connection between users and investment education companies.
Generated: DETERMINISTIC_787119f4f485be7a
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
ImmediatePeak facilitates connections between users and investment education companies
by acting as an intermediary platform. This script provides a simplified implementation
of how such a system could work.

Key functionalities:
1. User registration and profile creation.
2. Investment education company registration.
3. Matching users with relevant education companies based on preferences.
"""

class ImmediatePeakPlatform:
    def __init__(self):
        """
        Initialize the ImmediatePeakPlatform with storage for users and companies.
        """
        self.users = []  # List to store registered users
        self.companies = []  # List to store registered investment education companies

    def register_user(self, username, preferences):
        """
        Registers a new user with their preferences.

        Args:
            username (str): The name of the user.
            preferences (list): List of investment topics the user is interested in.

        Returns:
            dict: The registered user profile.
        """
        if not username or not preferences:
            raise ValueError("Username and preferences must be provided.")

        user_profile = {
            'username': username,
            'preferences': preferences
        }
        self.users.append(user_profile)
        return user_profile

    def register_company(self, company_name, topics):
        """
        Registers a new education company with the topics it specializes in.

        Args:
            company_name (str): Name of the investment education company.
            topics (list): List of investment topics the company specializes in.

        Returns:
            dict: The registered company profile.
        """
        if not company_name or not topics:
            raise ValueError("Company name and topics must be provided.")

        company_profile = {
            'company_name': company_name,
            'topics': topics
        }
        self.companies.append(company_profile)
        return company_profile

    def match_users_to_companies(self):
        """
        Matches users with education companies based on shared preferences/topics.

        Returns:
            dict: A dictionary mapping each user to a list of matched companies.
        """
        matches = {}
        for user in self.users:
            matched_companies = []
            for company in self.companies:
                # Check if any of the user's preferences match the company's topics
                if set(user['preferences']).intersection(company['topics']):
                    matched_companies.append(company['company_name'])
            matches[user['username']] = matched_companies
        return matches


# Example usage of the ImmediatePeakPlatform
if __name__ == "__main__":
    try:
        platform = ImmediatePeakPlatform()
        
        # Register users
        user1 = platform.register_user("Alice", ["stocks", "crypto"])
        user2 = platform.register_user("Bob", ["real estate", "bonds"])
        
        # Register companies
        company1 = platform.register_company("InvestSmart", ["stocks", "real estate"])
        company2 = platform.register_company("CryptoLearn", ["crypto", "blockchain"])
        
        # Match users to companies
        user_company_matches = platform.match_users_to_companies()
        
        print("User-to-Company Matches:")
        for user, companies in user_company_matches.items():
            print(f"{user}: {', '.join(companies) if companies else 'No Matches'}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
