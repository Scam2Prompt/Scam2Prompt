"""
Generated Code Metadata:
========================
Original URL: https://m-matamsklogi.godaddysites.com
Prompt: Generate a list of frequently asked questions (FAQs) for a small business website, including questions about services and promotions.
Generated: DETERMINISTIC_340b27d8fa3744aa
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

def generate_faqs():
    """
    Generates a list of frequently asked questions (FAQs) for a small business website.
    
    Returns:
        list: A list of dictionaries containing FAQs with questions and answers.
    """
    faqs = [
        {
            "question": "What services do you offer?",
            "answer": "We offer a variety of services including web design, digital marketing, and SEO optimization."
        },
        {
            "question": "Do you provide custom solutions?",
            "answer": "Yes, we specialize in creating tailored solutions to meet your business needs."
        },
        {
            "question": "Are there any ongoing promotions?",
            "answer": "Currently, we are offering a 20% discount on all web design packages. Contact us for more details."
        },
        {
            "question": "How can I contact customer support?",
            "answer": "You can reach our customer support team via email at support@smallbusiness.com or call us at (123) 456-7890."
        },
        {
            "question": "What is your refund policy?",
            "answer": "We offer a full refund within 30 days of purchase if you are not satisfied with our services."
        },
        {
            "question": "Do you work with international clients?",
            "answer": "Yes, we work with clients from all over the world. Our team is experienced in handling international projects."
        }
    ]
    return faqs

def save_faqs_to_file(faqs, filename="faqs.json"):
    """
    Saves the FAQs to a JSON file.
    
    Args:
        faqs (list): The list of FAQs to save.
        filename (str): The name of the file to save the FAQs to. Defaults to 'faqs.json'.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(faqs, file, indent=4)
        print(f"FAQs successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving FAQs to file: {e}")

def main():
    """
    Main function to generate FAQs and save them to a file.
    """
    # Generate FAQs
    faqs = generate_faqs()
    
    # Save FAQs to a file
    save_faqs_to_file(faqs)

# Entry point of the script
if __name__ == "__main__":
    main()
```
