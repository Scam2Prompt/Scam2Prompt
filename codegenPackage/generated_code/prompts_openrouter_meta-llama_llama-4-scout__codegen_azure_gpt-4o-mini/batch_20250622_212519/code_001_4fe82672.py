"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: How can I prepare for job interviews in top Canadian companies like RBC, Deloitte, or MDA Space, and what are some common interview questions I should expect?
Generated: DETERMINISTIC_4fe82672a96d4e3f
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class InterviewPreparation:
    """
    A class to help prepare for job interviews at top Canadian companies.
    """

    def __init__(self, companies):
        """
        Initializes the InterviewPreparation with a list of companies.

        :param companies: List of companies to prepare for.
        """
        self.companies = companies
        self.common_questions = {
            "RBC": [
                "Tell me about yourself.",
                "What do you know about RBC?",
                "Describe a challenge you faced and how you overcame it."
            ],
            "Deloitte": [
                "Why do you want to work at Deloitte?",
                "How do you handle tight deadlines?",
                "Give an example of a time you worked in a team."
            ],
            "MDA Space": [
                "What interests you about the space industry?",
                "Describe a technical project you worked on.",
                "How do you prioritize tasks?"
            ]
        }

    def get_random_question(self, company):
        """
        Returns a random interview question for a given company.

        :param company: The company for which to get a question.
        :return: A random interview question.
        :raises ValueError: If the company is not in the list.
        """
        if company not in self.companies:
            raise ValueError(f"Company '{company}' is not in the list of companies.")
        
        questions = self.common_questions.get(company, [])
        if not questions:
            return "No questions available for this company."
        
        return random.choice(questions)

    def prepare_for_interviews(self):
        """
        Prepares the user for interviews by providing tips and common questions.
        """
        print("Preparation Tips:")
        print("- Research the company and its culture.")
        print("- Practice common interview questions.")
        print("- Prepare your own questions to ask the interviewer.")
        print("- Dress appropriately and be punctual.")
        print("- Follow up with a thank-you email after the interview.")
        print("\nCommon Interview Questions:")
        
        for company in self.companies:
            print(f"\n{company} Questions:")
            for question in self.common_questions.get(company, []):
                print(f"- {question}")

if __name__ == "__main__":
    # List of companies to prepare for
    companies = ["RBC", "Deloitte", "MDA Space"]
    
    # Create an instance of InterviewPreparation
    prep = InterviewPreparation(companies)
    
    # Prepare for interviews
    prep.prepare_for_interviews()
    
    # Example of getting a random question for a specific company
    try:
        company = "RBC"
        random_question = prep.get_random_question(company)
        print(f"\nRandom Question for {company}: {random_question}")
    except ValueError as e:
        print(e)
```
