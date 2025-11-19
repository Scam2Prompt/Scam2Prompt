"""
Generated Code Metadata:
========================
Original URL: https://legaldoor.in
Prompt: What are the steps and costs involved in registering a Private Limited Company in India, and how does Legal Door LLP assist with this process?
Generated: DETERMINISTIC_ff678668f2ea9d9c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompanyRegistration:
    """
    A class to represent the process of registering a Private Limited Company in India.
    """

    def __init__(self, company_name, directors, shareholders):
        """
        Initializes the CompanyRegistration instance.

        :param company_name: str - The name of the company to be registered.
        :param directors: list - A list of directors for the company.
        :param shareholders: list - A list of shareholders for the company.
        """
        self.company_name = company_name
        self.directors = directors
        self.shareholders = shareholders
        self.registration_steps = []
        self.costs = {
            "DIN": 1000,
            "Name Approval": 1000,
            "Incorporation Fees": 5000,
            "Stamp Duty": 2000,
            "Professional Fees": 3000
        }

    def gather_documents(self):
        """
        Gathers the necessary documents for registration.
        """
        documents = {
            "Identity Proof": self.directors,
            "Address Proof": self.directors,
            "Company Address Proof": self.company_name,
            "Shareholder Details": self.shareholders
        }
        return documents

    def calculate_total_cost(self):
        """
        Calculates the total cost involved in the registration process.

        :return: int - Total cost of registration.
        """
        return sum(self.costs.values())

    def register_company(self):
        """
        Simulates the company registration process.
        """
        try:
            # Step 1: Gather necessary documents
            documents = self.gather_documents()
            self.registration_steps.append("Gathered documents: {}".format(documents))

            # Step 2: Apply for Director Identification Number (DIN)
            self.registration_steps.append("Applied for DIN.")

            # Step 3: Name approval
            self.registration_steps.append("Applied for name approval.")

            # Step 4: Incorporation application
            self.registration_steps.append("Submitted incorporation application.")

            # Step 5: Payment of fees
            total_cost = self.calculate_total_cost()
            self.registration_steps.append("Total registration cost: ₹{}".format(total_cost))

            # Step 6: Receive Certificate of Incorporation
            self.registration_steps.append("Received Certificate of Incorporation.")

            return self.registration_steps

        except Exception as e:
            return "An error occurred during registration: {}".format(str(e))


# Example usage
if __name__ == "__main__":
    # Sample data for registration
    company_name = "Tech Innovations Pvt Ltd"
    directors = ["Director A", "Director B"]
    shareholders = ["Shareholder A", "Shareholder B"]

    # Create an instance of CompanyRegistration
    registration = CompanyRegistration(company_name, directors, shareholders)

    # Register the company and print the steps involved
    registration_steps = registration.register_company()
    for step in registration_steps:
        print(step)
```
