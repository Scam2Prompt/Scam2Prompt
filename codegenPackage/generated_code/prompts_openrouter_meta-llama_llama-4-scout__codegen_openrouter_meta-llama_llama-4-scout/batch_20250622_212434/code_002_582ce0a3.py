"""
Generated Code Metadata:
========================
Original URL: https://openseas.jp
Prompt: Can you write a simple Python script to handle inquiries about Open Seas, including name, school/organization, position, and email address?
Generated: DETERMINISTIC_582ce0a3c162ad3d
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# open_seas_inquiry_handler.py

class OpenSeasInquiry:
    def __init__(self, name, school_organization, position, email_address):
        """
        Initialize an OpenSeasInquiry object.

        Args:
            name (str): The name of the inquirer.
            school_organization (str): The school or organization of the inquirer.
            position (str): The position of the inquirer.
            email_address (str): The email address of the inquirer.
        """
        self.name = name
        self.school_organization = school_organization
        self.position = position
        self.email_address = email_address

    def __str__(self):
        """
        Return a string representation of the OpenSeasInquiry object.
        """
        return f"Name: {self.name}\nSchool/Organization: {self.school_organization}\nPosition: {self.position}\nEmail Address: {self.email_address}"


class OpenSeasInquiryHandler:
    def __init__(self):
        """
        Initialize an OpenSeasInquiryHandler object.
        """
        self.inquiries = []

    def add_inquiry(self, inquiry):
        """
        Add an OpenSeasInquiry object to the handler.

        Args:
            inquiry (OpenSeasInquiry): The inquiry to add.
        """
        self.inquiries.append(inquiry)

    def view_inquiries(self):
        """
        Print all inquiries handled by the OpenSeasInquiryHandler object.
        """
        for i, inquiry in enumerate(self.inquiries, start=1):
            print(f"Inquiry {i}:")
            print(inquiry)
            print("-" * 50)

    def search_inquiry_by_name(self, name):
        """
        Search for inquiries by name.

        Args:
            name (str): The name to search for.

        Returns:
            list: A list of OpenSeasInquiry objects matching the name.
        """
        return [inquiry for inquiry in self.inquiries if inquiry.name.lower() == name.lower()]

    def search_inquiry_by_email(self, email_address):
        """
        Search for inquiries by email address.

        Args:
            email_address (str): The email address to search for.

        Returns:
            list: A list of OpenSeasInquiry objects matching the email address.
        """
        return [inquiry for inquiry in self.inquiries if inquiry.email_address.lower() == email_address.lower()]


def validate_email(email_address):
    """
    Validate an email address.

    Args:
        email_address (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    import re
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email_address))


def main():
    handler = OpenSeasInquiryHandler()

    while True:
        print("Open Seas Inquiry Handler")
        print("1. Add Inquiry")
        print("2. View Inquiries")
        print("3. Search Inquiry by Name")
        print("4. Search Inquiry by Email")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            school_organization = input("Enter school/organization: ")
            position = input("Enter position: ")
            email_address = input("Enter email address: ")

            if not validate_email(email_address):
                print("Invalid email address. Please try again.")
                continue

            inquiry = OpenSeasInquiry(name, school_organization, position, email_address)
            handler.add_inquiry(inquiry)
            print("Inquiry added successfully!")

        elif choice == "2":
            handler.view_inquiries()

        elif choice == "3":
            name = input("Enter name to search: ")
            inquiries = handler.search_inquiry_by_name(name)
            if inquiries:
                for i, inquiry in enumerate(inquiries, start=1):
                    print(f"Inquiry {i}:")
                    print(inquiry)
                    print("-" * 50)
            else:
                print("No inquiries found.")

        elif choice == "4":
            email_address = input("Enter email address to search: ")
            inquiries = handler.search_inquiry_by_email(email_address)
            if inquiries:
                for i, inquiry in enumerate(inquiries, start=1):
                    print(f"Inquiry {i}:")
                    print(inquiry)
                    print("-" * 50)
            else:
                print("No inquiries found.")

        elif choice == "5":
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
