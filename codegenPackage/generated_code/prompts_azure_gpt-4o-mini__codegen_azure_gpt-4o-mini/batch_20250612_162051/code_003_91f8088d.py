"""
Generated Code Metadata:
========================
Original URL: https://isbgames.isbeventteam.com
Prompt: Develop a set of FAQs for the ISB Games 2024 that addresses common participant inquiries about registration, event rules, and contact information for the ISB Event Team.
Generated: DETERMINISTIC_91f8088d79a754c8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FAQ:
    """
    A class to represent a set of Frequently Asked Questions (FAQs) for the ISB Games 2024.
    """

    def __init__(self):
        """
        Initializes the FAQ with common questions and their answers.
        """
        self.faqs = {
            "registration": {
                "question": "How do I register for the ISB Games 2024?",
                "answer": "You can register online through our official website. Please ensure you complete all required fields."
            },
            "event_rules": {
                "question": "What are the rules for participating in the events?",
                "answer": "Each event has specific rules outlined on the event page. Please review them carefully before participating."
            },
            "contact_info": {
                "question": "How can I contact the ISB Event Team?",
                "answer": "You can reach the ISB Event Team via email at events@isbgames2024.com or call us at +123456789."
            },
            "age_limit": {
                "question": "Is there an age limit for participants?",
                "answer": "Participants must be at least 12 years old to register for the ISB Games 2024."
            },
            "team_size": {
                "question": "What is the maximum team size for team events?",
                "answer": "The maximum team size for team events is 5 participants."
            }
        }

    def get_faq(self, category):
        """
        Retrieves the FAQ for a specific category.

        Args:
            category (str): The category of the FAQ to retrieve.

        Returns:
            dict: A dictionary containing the question and answer, or an error message if the category is not found.
        """
        try:
            if category in self.faqs:
                return self.faqs[category]
            else:
                raise KeyError(f"FAQ category '{category}' not found.")
        except KeyError as e:
            return {"error": str(e)}

    def list_categories(self):
        """
        Lists all available FAQ categories.

        Returns:
            list: A list of available FAQ categories.
        """
        return list(self.faqs.keys())


# Example usage
if __name__ == "__main__":
    faq_system = FAQ()

    # List all FAQ categories
    print("Available FAQ Categories:")
    print(faq_system.list_categories())

    # Retrieve a specific FAQ
    category = "registration"
    faq = faq_system.get_faq(category)
    print(f"\nFAQ for '{category}':")
    print(f"Q: {faq['question']}\nA: {faq['answer']}")
    
    # Attempt to retrieve a non-existent FAQ
    invalid_category = "non_existent"
    invalid_faq = faq_system.get_faq(invalid_category)
    print(f"\nFAQ for '{invalid_category}':")
    print(invalid_faq)
```
