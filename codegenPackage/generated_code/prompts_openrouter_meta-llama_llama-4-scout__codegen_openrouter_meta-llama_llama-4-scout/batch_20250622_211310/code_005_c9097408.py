"""
Generated Code Metadata:
========================
Original URL: https://immediate-prime.com
Prompt: Create a data privacy notice generator that helps investment education firms comply with data protection regulations, similar to Immediate Prime's data privacy notice.
Generated: DETERMINISTIC_c9097408a69c22e6
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# data_privacy_notice_generator.py

import json

class DataPrivacyNoticeGenerator:
    """
    A class used to generate data privacy notices for investment education firms.

    Attributes:
    ----------
    company_name : str
        The name of the investment education firm.
    data_collection_purposes : list
        A list of purposes for collecting user data.
    data_types : list
        A list of types of user data collected.
    data_recipients : list
        A list of recipients of user data.
    data_retention_period : str
        The period for which user data is retained.

    Methods:
    -------
    generate_notice()
        Generates a data privacy notice based on the provided attributes.
    """

    def __init__(self, company_name, data_collection_purposes, data_types, data_recipients, data_retention_period):
        """
        Initializes the DataPrivacyNoticeGenerator object.

        Args:
        ----
        company_name (str): The name of the investment education firm.
        data_collection_purposes (list): A list of purposes for collecting user data.
        data_types (list): A list of types of user data collected.
        data_recipients (list): A list of recipients of user data.
        data_retention_period (str): The period for which user data is retained.
        """
        self.company_name = company_name
        self.data_collection_purposes = data_collection_purposes
        self.data_types = data_types
        self.data_recipients = data_recipients
        self.data_retention_period = data_retention_period

    def generate_notice(self):
        """
        Generates a data privacy notice based on the provided attributes.

        Returns:
        -------
        str
            The generated data privacy notice.
        """
        notice = f"""
        {self.company_name} Data Privacy Notice

        Introduction
        ------------
        {self.company_name} is committed to protecting the privacy and security of your personal data. This notice describes how we collect, use, and share your data.

        Data Collection
        ---------------
        We collect the following types of data:
        """
        for data_type in self.data_types:
            notice += f"- {data_type}\n"

        notice += f"""
        Data collection purposes
        ------------------------
        We collect your data for the following purposes:
        """
        for purpose in self.data_collection_purposes:
            notice += f"- {purpose}\n"

        notice += f"""
        Data Recipients
        ----------------
        We may share your data with the following recipients:
        """
        for recipient in self.data_recipients:
            notice += f"- {recipient}\n"

        notice += f"""
        Data Retention
        ---------------
        We retain your data for {self.data_retention_period}.

        Your Rights
        ------------
        You have the following rights regarding your data:
        - Right to access your data
        - Right to rectify your data
        - Right to erase your data
        - Right to restrict processing of your data
        - Right to object to processing of your data

        Contact Us
        -----------
        If you have any questions or concerns about this notice or your data, please contact us at:
        - Email: [support@{self.company_name.lower()}.com](mailto:support@{self.company_name.lower()}.com)
        - Address: {self.company_name}, [insert address]

        Changes to this Notice
        ----------------------
        We may update this notice from time to time. We will notify you of any changes by updating this page.
        """

        return notice


def main():
    try:
        company_name = input("Enter the company name: ")
        data_collection_purposes = input("Enter data collection purposes (comma-separated): ").split(",")
        data_collection_purposes = [purpose.strip() for purpose in data_collection_purposes]
        data_types = input("Enter types of data collected (comma-separated): ").split(",")
        data_types = [data_type.strip() for data_type in data_types]
        data_recipients = input("Enter data recipients (comma-separated): ").split(",")
        data_recipients = [recipient.strip() for recipient in data_recipients]
        data_retention_period = input("Enter data retention period: ")

        generator = DataPrivacyNoticeGenerator(company_name, data_collection_purposes, data_types, data_recipients, data_retention_period)
        notice = generator.generate_notice()

        print(notice)

        # Save notice to file
        with open("data_privacy_notice.txt", "w") as f:
            f.write(notice)

        print("Data privacy notice generated and saved to data_privacy_notice.txt")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
