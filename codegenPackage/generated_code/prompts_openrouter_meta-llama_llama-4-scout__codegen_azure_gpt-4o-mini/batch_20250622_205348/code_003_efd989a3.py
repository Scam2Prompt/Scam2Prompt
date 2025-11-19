"""
Generated Code Metadata:
========================
Original URL: https://doodles.team
Prompt: Design a basic privacy policy template for a creative agency.
Generated: DETERMINISTIC_efd989a3472b6edd
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PrivacyPolicy:
    """
    A class to represent a basic privacy policy for a creative agency.
    """

    def __init__(self, agency_name, contact_email):
        """
        Initializes the PrivacyPolicy with the agency name and contact email.

        :param agency_name: Name of the creative agency
        :param contact_email: Contact email for privacy inquiries
        """
        self.agency_name = agency_name
        self.contact_email = contact_email
        self.policy_sections = []

    def add_section(self, title, content):
        """
        Adds a section to the privacy policy.

        :param title: Title of the section
        :param content: Content of the section
        """
        if not title or not content:
            raise ValueError("Title and content cannot be empty.")
        self.policy_sections.append({'title': title, 'content': content})

    def generate_policy(self):
        """
        Generates the complete privacy policy as a formatted string.

        :return: Formatted privacy policy
        """
        policy = f"Privacy Policy for {self.agency_name}\n"
        policy += f"Contact: {self.contact_email}\n\n"
        for section in self.policy_sections:
            policy += f"{section['title']}\n"
            policy += f"{section['content']}\n\n"
        return policy.strip()

    def save_policy_to_file(self, filename):
        """
        Saves the generated privacy policy to a text file.

        :param filename: Name of the file to save the policy
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_policy())
            print(f"Privacy policy saved to {filename}")
        except IOError as e:
            print(f"Error saving policy to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of PrivacyPolicy
    agency_policy = PrivacyPolicy("Creative Agency Inc.", "contact@creativeagency.com")

    # Add sections to the privacy policy
    agency_policy.add_section("Introduction", "This privacy policy outlines how we handle your personal information.")
    agency_policy.add_section("Information Collection", "We collect information that you provide to us directly.")
    agency_policy.add_section("Use of Information", "We use your information to provide and improve our services.")
    agency_policy.add_section("Data Security", "We take reasonable measures to protect your information.")
    agency_policy.add_section("Contact Us", "For any questions, please contact us at " + agency_policy.contact_email)

    # Generate and save the privacy policy to a file
    agency_policy.save_policy_to_file("privacy_policy.txt")
```
