"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Generate a sample privacy policy template for a mobile app, incorporating key points from the STELLAR TECHNOLOGY LIMITED policy, including definitions of personal information, sensitive information, and data retention periods.
Generated: DETERMINISTIC_3d50c6ba85256755
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Privacy Policy Template Generator

class PrivacyPolicy:
    def __init__(self, company_name):
        """
        Initialize the PrivacyPolicy class.

        Args:
            company_name (str): The name of the company.
        """
        self.company_name = company_name

    def generate_policy(self):
        """
        Generate a sample privacy policy template.

        Returns:
            str: The generated privacy policy template.
        """
        policy = f"# {self.company_name} Privacy Policy\n\n"

        policy += "## Introduction\n\n"
        policy += f"{self.company_name} ('we', 'us', or 'our') is committed to protecting the privacy of our users. This Privacy Policy explains how we collect, use, and disclose personal information through our mobile app.\n\n"

        policy += "## Definitions\n\n"
        policy += "### Personal Information\n\n"
        policy += "For the purposes of this Privacy Policy, 'personal information' means any information that can be used to identify you, either on its own or in combination with other information. This may include:\n"
        policy += "- Your name\n"
        policy += "- Email address\n"
        policy += "- Phone number\n"
        policy += "- Device information (e.g., device type, operating system, and unique device identifiers)\n\n"

        policy += "### Sensitive Information\n\n"
        policy += "For the purposes of this Privacy Policy, 'sensitive information' means any information that is sensitive in nature, such as:\n"
        policy += "- Financial information\n"
        policy += "- Health information\n"
        policy += "- Biometric information\n\n"

        policy += "## Data Collection and Use\n\n"
        policy += f"We collect personal information through our mobile app, including when you:\n"
        policy += "- Create an account\n"
        policy += "- Use our services\n"
        policy += "- Interact with us through the app\n\n"

        policy += "## Data Retention\n\n"
        policy += f"We retain personal information for as long as necessary to provide our services to you. The specific retention periods are as follows:\n"
        policy += "- User accounts: 2 years after account deletion\n"
        policy += "- Transactional data: 5 years after the transaction date\n"
        policy += "- Device information: 1 year after last app usage\n\n"

        policy += "## Data Disclosure\n\n"
        policy += f"We may disclose personal information to:\n"
        policy += "- Our affiliates and subsidiaries\n"
        policy += "- Service providers (e.g., cloud storage, analytics tools)\n"
        policy += "- Law enforcement agencies (in response to a valid request)\n\n"

        policy += "## User Rights\n\n"
        policy += f"You have the following rights regarding your personal information:\n"
        policy += "- Right to access\n"
        policy += "- Right to rectify\n"
        policy += "- Right to erase\n"
        policy += "- Right to restrict processing\n\n"

        policy += "## Security\n\n"
        policy += f"We take reasonable steps to protect your personal information from unauthorized access, disclosure, alteration, or destruction.\n\n"

        policy += "## Changes to this Policy\n\n"
        policy += f"We may update this Privacy Policy from time to time. We will notify you of any changes by updating this page.\n\n"

        policy += "## Contact Us\n\n"
        policy += f"If you have any questions or concerns about this Privacy Policy, please contact us at [{self.company_name} Support](mailto:support@stellartech.com).\n\n"

        return policy


def main():
    company_name = "STELLAR TECHNOLOGY LIMITED"
    policy_generator = PrivacyPolicy(company_name)
    policy = policy_generator.generate_policy()

    try:
        with open("privacy_policy.md", "w") as f:
            f.write(policy)
        print("Privacy policy template generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
