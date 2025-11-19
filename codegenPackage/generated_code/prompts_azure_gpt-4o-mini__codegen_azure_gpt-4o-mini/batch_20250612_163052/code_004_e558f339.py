"""
Generated Code Metadata:
========================
Original URL: https://immediate-enigma.net
Prompt: Explain how Immediate Migna acts as an intermediary between learners and investment education companies, including the registration process.
Generated: DETERMINISTIC_e558f3397b0e7174
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ImmediateMigna:
    """
    A class to represent Immediate Migna as an intermediary between learners and investment education companies.
    """

    def __init__(self):
        """
        Initializes the Immediate Migna platform with empty lists for learners and companies.
        """
        self.learners = []
        self.companies = []

    def register_learner(self, learner_name, learner_email):
        """
        Registers a new learner in the system.

        Parameters:
        learner_name (str): The name of the learner.
        learner_email (str): The email of the learner.

        Raises:
        ValueError: If the learner email is already registered.
        """
        if any(learner['email'] == learner_email for learner in self.learners):
            raise ValueError("This email is already registered.")
        
        learner = {
            'name': learner_name,
            'email': learner_email
        }
        self.learners.append(learner)
        print(f"Learner {learner_name} registered successfully.")

    def register_company(self, company_name, company_email):
        """
        Registers a new investment education company in the system.

        Parameters:
        company_name (str): The name of the company.
        company_email (str): The email of the company.

        Raises:
        ValueError: If the company email is already registered.
        """
        if any(company['email'] == company_email for company in self.companies):
            raise ValueError("This email is already registered.")
        
        company = {
            'name': company_name,
            'email': company_email
        }
        self.companies.append(company)
        print(f"Company {company_name} registered successfully.")

    def match_learners_to_companies(self):
        """
        Matches learners with investment education companies based on their interests.
        For simplicity, this method currently matches all learners to all companies.
        """
        matches = {}
        for learner in self.learners:
            matches[learner['name']] = [company['name'] for company in self.companies]
        return matches

    def get_registered_learners(self):
        """
        Returns a list of registered learners.

        Returns:
        list: A list of dictionaries containing learner information.
        """
        return self.learners

    def get_registered_companies(self):
        """
        Returns a list of registered investment education companies.

        Returns:
        list: A list of dictionaries containing company information.
        """
        return self.companies


# Example usage
if __name__ == "__main__":
    try:
        platform = ImmediateMigna()
        
        # Register learners
        platform.register_learner("Alice Smith", "alice@example.com")
        platform.register_learner("Bob Johnson", "bob@example.com")
        
        # Register companies
        platform.register_company("InvestSmart", "contact@investsmart.com")
        platform.register_company("WealthAcademy", "info@wealthacademy.com")
        
        # Match learners to companies
        matches = platform.match_learners_to_companies()
        print("Learner to Company Matches:")
        for learner, companies in matches.items():
            print(f"{learner}: {', '.join(companies)}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
