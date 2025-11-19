"""
Generated Code Metadata:
========================
Original URL: https://www.betterbooking.pk
Prompt: "Generate a list of questions and answers based on Better Booking's Hajj FAQs, focusing on booking procedures and travel tips."
Generated: DETERMINISTIC_ba072278c7840fc5
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

class HajjFAQs:
    def __init__(self):
        # Initialize FAQs data
        self.faqs = {
            "booking_procedures": [
                {
                    "question": "What is the first step in booking a Hajj package?",
                    "answer": "The first step is to visit our website and fill out the registration form with your details."
                },
                {
                    "question": "How do I pay for my Hajj package?",
                    "answer": "We accept various payment methods including credit/debit cards, bank transfers, and cash payments at our office."
                },
                {
                    "question": "Can I customize my Hajj package?",
                    "answer": "Yes, we offer customizable packages to suit your needs. Please contact us for more information."
                }
            ],
            "travel_tips": [
                {
                    "question": "What vaccinations do I need for Hajj?",
                    "answer": "It is recommended to consult your doctor and ensure you have all necessary vaccinations before traveling to Saudi Arabia."
                },
                {
                    "question": "What is the best time to perform Umrah during Hajj?",
                    "answer": "The best time to perform Umrah is during the months of Ramadan and Shawwal."
                },
                {
                    "question": "What should I pack for Hajj?",
                    "answer": "Please refer to our packing guide on our website for a comprehensive list of essentials."
                }
            ]
        }

    def get_faqs(self, category=None):
        try:
            if category:
                return self.faqs.get(category, [])
            else:
                return self.faqs
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def save_faqs_to_json(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(self.faqs, f, indent=4)
            print(f"FAQs saved to {filename} successfully.")
        except Exception as e:
            print(f"Failed to save FAQs to {filename}: {e}")


def main():
    # Create an instance of HajjFAQs
    hajj_faqs = HajjFAQs()

    # Get all FAQs
    all_faqs = hajj_faqs.get_faqs()
    print("All FAQs:")
    print(json.dumps(all_faqs, indent=4))

    # Get booking procedures FAQs
    booking_procedures = hajj_faqs.get_faqs('booking_procedures')
    print("\nBooking Procedures FAQs:")
    print(json.dumps(booking_procedures, indent=4))

    # Save FAQs to JSON file
    hajj_faqs.save_faqs_to_json('hajj_faqs.json')


if __name__ == "__main__":
    main()
```
