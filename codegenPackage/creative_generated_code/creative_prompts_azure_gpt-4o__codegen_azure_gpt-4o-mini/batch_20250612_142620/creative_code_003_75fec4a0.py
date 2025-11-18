"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-virgocx.teachable.com
Prompt: Create a privacy policy template for a Teachable-hosted course website that offers help and tutorials for Metamask users.
Generated: DETERMINISTIC_75fec4a08bc53e17
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrivacyPolicy:
    """
    A class to represent a Privacy Policy for a Teachable-hosted course website.
    The website offers help and tutorials for Metamask users.
    """

    def __init__(self, website_name, contact_email):
        """
        Initializes the Privacy Policy with the website name and contact email.

        Args:
            website_name (str): The name of the website.
            contact_email (str): The contact email for privacy inquiries.
        """
        if not isinstance(website_name, str) or not isinstance(contact_email, str):
            raise ValueError("Website name and contact email must be strings.")
        
        self.website_name = website_name
        self.contact_email = contact_email

    def generate_policy(self):
        """
        Generates the privacy policy template as a string.

        Returns:
            str: A formatted privacy policy.
        """
        policy = f"""
        Privacy Policy for {self.website_name}

        Effective Date: [Insert Date]

        This privacy policy outlines how we collect, use, and protect your information when you visit our website.

        1. Information We Collect
        We may collect personal information from you when you visit our site, register for a course, or engage in other activities. This information may include:
            - Name
            - Email address
            - Payment information (processed securely)
            - Course interaction data

        2. How We Use Your Information
        We use the information collected for the following purposes:
            - To provide and maintain our services
            - To notify you about changes to our site or services
            - To allow you to participate in interactive features of our services when you choose to do so
            - To provide customer support
            - To gather analysis or valuable information so that we can improve our services

        3. Data Security
        We take the security of your personal information seriously. We implement various security measures to maintain the safety of your personal data.

        4. Sharing Your Information
        We do not sell or rent your personal information to third parties. We may share your information in the following circumstances:
            - With service providers who assist us in operating our website or conducting our business
            - To comply with legal obligations

        5. Your Rights
        Depending on your location, you may have the following rights concerning your personal data:
            - The right to access
            - The right to rectification
            - The right to erasure
            - The right to restrict processing
            - The right to data portability

        6. Changes to This Privacy Policy
        We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page.

        7. Contact Us
        If you have any questions about this Privacy Policy, please contact us at {self.contact_email}.

        Thank you for choosing {self.website_name} for your Metamask tutorial needs!
        """
        return policy.strip()

# Example usage
if __name__ == "__main__":
    try:
        privacy_policy = PrivacyPolicy("Metamask Tutorials", "support@metamasktutorials.com")
        print(privacy_policy.generate_policy())
    except ValueError as e:
        print(f"Error: {e}")
```
