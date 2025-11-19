"""
Generated Code Metadata:
========================
Original URL: https://maskextension.teachable.com
Prompt: "Write a Terms of Use and Privacy Policy template for a Teachable school, incorporating variables for the school name and year."
Generated: DETERMINISTIC_696e7e5d46b2b9d0
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Terms of Use and Privacy Policy template generator for Teachable schools

class TermsOfUsePrivacyPolicyGenerator:
    def __init__(self, school_name, year):
        """
        Initialize the generator with school name and year.

        Args:
            school_name (str): The name of the Teachable school.
            year (int): The current year.
        """
        self.school_name = school_name
        self.year = year

    def generate_terms_of_use(self):
        """
        Generate the Terms of Use template.

        Returns:
            str: The Terms of Use template.
        """
        terms_of_use = f"""
# Terms of Use

Effective as of {self.year}

Welcome to {self.school_name} ("School" or "we"). These Terms of Use ("Terms") govern your access to and use of the {self.school_name} website, courses, and services ("Services").

## 1. Acceptance of Terms

By accessing or using the Services, you ("User" or "you") agree to be bound by these Terms. If you do not agree to these Terms, please do not access or use the Services.

## 2. Use of Services

You may use the Services only for lawful purposes and in accordance with these Terms. You agree to:

* Comply with all applicable laws and regulations;
* Not engage in any unauthorized or unlawful activity;
* Not interfere with or disrupt the operation of the Services;

## 3. Intellectual Property

The Services, including all content, courses, and materials, are the exclusive property of {self.school_name} and are protected by intellectual property laws.

## 4. Liability

{self.school_name} is not responsible for any damages or losses arising from your use of the Services.

## 5. Governing Law

These Terms shall be governed by and construed in accordance with the laws of the [State/Country].

## 6. Changes to Terms

{self.school_name} reserves the right to modify these Terms at any time, without notice.

## 7. Termination

{self.school_name} may terminate your access to the Services at any time, without notice.

## 8. Contact Us

If you have any questions or concerns about these Terms, please contact us at [support email].

Last Updated: {self.year}
"""
        return terms_of_use

    def generate_privacy_policy(self):
        """
        Generate the Privacy Policy template.

        Returns:
            str: The Privacy Policy template.
        """
        privacy_policy = f"""
# Privacy Policy

Effective as of {self.year}

{self.school_name} ("School" or "we") is committed to protecting your privacy. This Privacy Policy ("Policy") describes how we collect, use, and disclose personal data.

## 1. Information Collection

We collect the following types of information:

* Personal data, such as name and email address;
* Usage data, such as course enrollment and completion;

## 2. Use of Information

We use your personal data for the following purposes:

* To provide and improve the Services;
* To communicate with you about the Services;

## 3. Disclosure of Information

We may disclose your personal data to:

* Our affiliates and subsidiaries;
* Service providers and vendors;

## 4. Data Protection

We take reasonable measures to protect your personal data from unauthorized access, use, or disclosure.

## 5. Your Rights

You have the following rights:

* To access and correct your personal data;
* To request deletion of your personal data;

## 6. Changes to Policy

{self.school_name} reserves the right to modify this Policy at any time, without notice.

## 7. Contact Us

If you have any questions or concerns about this Policy, please contact us at [support email].

Last Updated: {self.year}
"""
        return privacy_policy


def main():
    school_name = input("Enter the school name: ")
    year = int(input("Enter the current year: "))

    generator = TermsOfUsePrivacyPolicyGenerator(school_name, year)

    terms_of_use = generator.generate_terms_of_use()
    privacy_policy = generator.generate_privacy_policy()

    print("Terms of Use:")
    print(terms_of_use)
    print("\nPrivacy Policy:")
    print(privacy_policy)

    # Save to file
    with open("terms_of_use.txt", "w") as f:
        f.write(terms_of_use)

    with open("privacy_policy.txt", "w") as f:
        f.write(privacy_policy)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
