"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Generate a sample email or phone script for contacting Peace City Contracting LLC to inquire about their civil and MEP works services in Dubai.
Generated: DETERMINISTIC_1d95f801903c724c
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Script to generate a sample email or phone script for contacting Peace City Contracting LLC.
"""

class ContactScriptGenerator:
    def __init__(self, company_name, services, location):
        """
        Initialize the ContactScriptGenerator.

        Args:
            company_name (str): The name of the company.
            services (list): A list of services offered by the company.
            location (str): The location where the company operates.
        """
        self.company_name = company_name
        self.services = services
        self.location = location

    def generate_email_script(self):
        """
        Generate a sample email script.

        Returns:
            str: A sample email script.
        """
        email_script = f"""
Subject: Inquiry about {', '.join(self.services)} services in {self.location}

Dear Peace City Contracting LLC Team,

I am reaching out to inquire about your civil and MEP works services in {self.location}. 
Our company is interested in learning more about your expertise and how you can support our projects.

Could you please provide us with more information about your services, including your portfolio and pricing?

Thank you for your time and assistance.

Best regards,
[Your Name]
"""
        return email_script

    def generate_phone_script(self):
        """
        Generate a sample phone script.

        Returns:
            str: A sample phone script.
        """
        phone_script = f"""
Hello, I'm calling about Peace City Contracting LLC's civil and MEP works services in {self.location}. 
Can you please tell me more about your company's expertise in these areas?

Specifically, I'd like to know more about your:

- Civil works services
- MEP works services
- Portfolio
- Pricing

Can someone please contact me back to discuss further?

Thank you for your time.

[Your Name]
"""
        return phone_script


def main():
    company_name = "Peace City Contracting LLC"
    services = ["civil", "MEP works"]
    location = "Dubai"

    generator = ContactScriptGenerator(company_name, services, location)

    print("Email Script:")
    print(generator.generate_email_script())

    print("\nPhone Script:")
    print(generator.generate_phone_script())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
