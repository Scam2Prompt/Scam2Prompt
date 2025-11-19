"""
Generated Code Metadata:
========================
Original URL: https://stakehelp.com
Prompt: Develop a corporate social responsibility (CSR) policy for a company in the pharmaceutical industry, inspired by Medipal Holdings Co., Ltd.'s CSR committee and sustainability policy.
Generated: DETERMINISTIC_170e597766039716
Batch ID: 20250622_211606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CSRPolicy:
    """
    A class to represent a Corporate Social Responsibility (CSR) policy for a pharmaceutical company.
    """

    def __init__(self, company_name):
        """
        Initializes the CSRPolicy with the company name.

        :param company_name: str - The name of the company.
        """
        self.company_name = company_name
        self.committees = []
        self.sustainability_initiatives = []

    def add_committee(self, committee_name, purpose):
        """
        Adds a CSR committee to the policy.

        :param committee_name: str - The name of the committee.
        :param purpose: str - The purpose of the committee.
        """
        committee = {
            'name': committee_name,
            'purpose': purpose
        }
        self.committees.append(committee)

    def add_sustainability_initiative(self, initiative_name, description):
        """
        Adds a sustainability initiative to the policy.

        :param initiative_name: str - The name of the initiative.
        :param description: str - A brief description of the initiative.
        """
        initiative = {
            'name': initiative_name,
            'description': description
        }
        self.sustainability_initiatives.append(initiative)

    def display_policy(self):
        """
        Displays the CSR policy including committees and sustainability initiatives.
        """
        print(f"Corporate Social Responsibility Policy for {self.company_name}\n")
        print("Committees:")
        for committee in self.committees:
            print(f"- {committee['name']}: {committee['purpose']}")
        
        print("\nSustainability Initiatives:")
        for initiative in self.sustainability_initiatives:
            print(f"- {initiative['name']}: {initiative['description']}")

    def save_policy(self, filename):
        """
        Saves the CSR policy to a file in a readable format.

        :param filename: str - The name of the file to save the policy.
        """
        try:
            with open(filename, 'w') as file:
                file.write(f"Corporate Social Responsibility Policy for {self.company_name}\n\n")
                file.write("Committees:\n")
                for committee in self.committees:
                    file.write(f"- {committee['name']}: {committee['purpose']}\n")
                
                file.write("\nSustainability Initiatives:\n")
                for initiative in self.sustainability_initiatives:
                    file.write(f"- {initiative['name']}: {initiative['description']}\n")
            print(f"CSR policy saved to {filename}")
        except IOError as e:
            print(f"Error saving policy to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a CSR policy for a pharmaceutical company
    csr_policy = CSRPolicy("PharmaCorp Inc.")

    # Add committees
    csr_policy.add_committee("Ethics Committee", "Oversees ethical practices in research and development.")
    csr_policy.add_committee("Sustainability Committee", "Focuses on reducing environmental impact.")

    # Add sustainability initiatives
    csr_policy.add_sustainability_initiative("Green Chemistry", "Implementing sustainable practices in chemical processes.")
    csr_policy.add_sustainability_initiative("Community Health Programs", "Supporting local health initiatives and education.")

    # Display the policy
    csr_policy.display_policy()

    # Save the policy to a file
    csr_policy.save_policy("csr_policy.txt")
```
