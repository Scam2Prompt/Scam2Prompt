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
# faq_generator.py
"""
A script to generate a list of frequently asked questions (FAQs) related to Tomi's NBN plans.
Includes information on contract terms, pricing, and hardware.
"""

def generate_faqs():
    """
    Generates and returns a list of FAQs about Tomi's NBN plans.
    
    Returns:
        list: A list of dictionaries, each containing a question and answer.
    """
    faqs = [
        {
            "question": "What NBN plans does Tomi offer?",
            "answer": "Tomi offers a range of NBN plans including Basic (12/1 Mbps), Standard (25/5 Mbps), Fast (50/20 Mbps), and Superfast (100/20 Mbps) speeds. Each plan comes with unlimited data."
        },
        {
            "question": "Are there any contracts for Tomi's NBN plans?",
            "answer": "Tomi offers both no-contract (month-to-month) and 12/24-month contract options. Contract plans may include discounts or waived setup fees."
        },
        {
            "question": "What is the pricing for Tomi's NBN plans?",
            "answer": "Pricing starts at $49/month for Basic, $59/month for Standard, $69/month for Fast, and $89/month for Superfast. Prices may vary based on contract length and promotions."
        },
        {
            "question": "Is there a setup fee for Tomi's NBN service?",
            "answer": "Setup fees may apply depending on the plan and contract length. Some promotions waive the setup fee for contract plans."
        },
        {
            "question": "What hardware is provided with Tomi's NBN service?",
            "answer": "Tomi provides a free modem-router with all NBN plans. For Fibre to the Premises (FTTP) connections, an NBN connection box will also be installed."
        },
        {
            "question": "Can I use my own modem with Tomi's NBN service?",
            "answer": "Yes, you can use your own modem if it is NBN-compatible. However, Tomi recommends using their provided modem for optimal performance and support."
        },
        {
            "question": "How long does it take to activate Tomi's NBN service?",
            "answer": "Activation typically takes 2-10 business days, depending on your location and NBN connection type. Some areas may experience longer wait times."
        },
        {
            "question": "Is there a speed guarantee for Tomi's NBN plans?",
            "answer": "Tomi offers a speed guarantee during peak hours (7-11 PM) for selected plans. If speeds consistently fall below the guaranteed minimum, you may be eligible for a plan change or credit."
        },
        {
            "question": "What happens if I move house with Tomi's NBN service?",
            "answer": "You can transfer your Tomi NBN service to your new address if NBN is available there. A relocation fee may apply, and installation may be required at the new premises."
        },
        {
            "question": "How do I cancel my Tomi NBN service?",
            "answer": "For no-contract plans, you can cancel anytime by giving 30 days notice. For contract plans, early termination fees may apply unless you're moving to an area without NBN coverage."
        }
    ]
    
    return faqs

def display_faqs(faqs):
    """
    Displays the FAQs in a user-friendly format.
    
    Args:
        faqs (list): A list of FAQs to display.
    """
    print("Frequently Asked Questions (FAQs) - Tomi's NBN Plans\n")
    print("--------------------------------------------------\n")
    
    for i, faq in enumerate(faqs, 1):
        print(f"{i}. {faq['question']}")
        print(f"   {faq['answer']}\n")

def main():
    """
    Main function to generate and display FAQs.
    """
    try:
        faqs = generate_faqs()
        display_faqs(faqs)
    except Exception as e:
        print(f"An error occurred while generating FAQs: {e}")

if __name__ == "__main__":
    main()
```
