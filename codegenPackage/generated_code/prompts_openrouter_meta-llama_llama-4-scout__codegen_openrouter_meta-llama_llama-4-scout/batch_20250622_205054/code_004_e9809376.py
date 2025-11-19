"""
Generated Code Metadata:
========================
Original URL: https://tomi.com.au
Prompt: Generate a list of frequently asked questions (FAQs) related to Tomi's nbn plans, including information on contract terms, pricing, and hardware.
Generated: DETERMINISTIC_e9809376a1d7f74d
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent an FAQ
class FAQ:
    def __init__(self, question, answer):
        """
        Initialize an FAQ object.

        Args:
            question (str): The question being asked.
            answer (str): The answer to the question.
        """
        self.question = question
        self.answer = answer

# Define a class to represent Tomi's nbn plans
class TomiNBNPlans:
    def __init__(self):
        """
        Initialize a TomiNBNPlans object with a list of FAQs.
        """
        self.faqs = []

    def add_faq(self, question, answer):
        """
        Add an FAQ to the list.

        Args:
            question (str): The question being asked.
            answer (str): The answer to the question.
        """
        self.faqs.append(FAQ(question, answer))

    def get_faqs(self):
        """
        Get the list of FAQs.

        Returns:
            list: A list of FAQ objects.
        """
        return self.faqs

# Define a function to generate FAQs related to Tomi's nbn plans
def generate_faqs():
    """
    Generate a list of FAQs related to Tomi's nbn plans.

    Returns:
        list: A list of FAQ objects.
    """
    tomi_plans = TomiNBNPlans()

    # Contract terms FAQs
    tomi_plans.add_faq(
        "What is the contract term for Tomi's nbn plans?",
        "The contract term for Tomi's nbn plans is 24 months."
    )
    tomi_plans.add_faq(
        "Can I exit my contract early?",
        "Yes, you can exit your contract early, but an early termination fee may apply."
    )

    # Pricing FAQs
    tomi_plans.add_faq(
        "How much do Tomi's nbn plans cost?",
        "Prices start at $49.99 per month for our Starter plan."
    )
    tomi_plans.add_faq(
        "Are there any additional fees?",
        "Yes, a $9.99 per month modem rental fee applies if you don't have your own modem."
    )

    # Hardware FAQs
    tomi_plans.add_faq(
        "What type of modem do I need for Tomi's nbn plans?",
        "You will need a modem that is compatible with the nbn network."
    )
    tomi_plans.add_faq(
        "Can I use my own hardware?",
        "Yes, you can use your own hardware, but it must be compatible with the nbn network."
    )

    return tomi_plans.get_faqs()

# Define a function to print the FAQs
def print_faqs(faqs):
    """
    Print the FAQs.

    Args:
        faqs (list): A list of FAQ objects.
    """
    for i, faq in enumerate(faqs, start=1):
        print(f"**Q{i}: {faq.question}**")
        print(f"A{i}: {faq.answer}\n")

# Main function
def main():
    try:
        faqs = generate_faqs()
        print_faqs(faqs)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
