"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: Generate code for a contact form with multiple versions (e.g., Contact v.1, Contact v.2) as described on the Recuperación JC website.
Generated: DETERMINISTIC_44ab8d1791dce131
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Contact Form Code**
```python
# contact_form.py

from abc import ABC, abstractmethod
from typing import Dict

class ContactForm(ABC):
    """Base class for contact forms"""

    def __init__(self, name: str, email: str, message: str):
        self.name = name
        self.email = email
        self.message = message

    @abstractmethod
    def validate(self) -> bool:
        """Validate form data"""
        pass

    @abstractmethod
    def send(self) -> bool:
        """Send form data"""
        pass


class ContactFormV1(ContactForm):
    """Contact form version 1"""

    def validate(self) -> bool:
        """Validate form data for version 1"""
        if not self.name or not self.email or not self.message:
            return False
        return True

    def send(self) -> bool:
        """Send form data for version 1"""
        try:
            # Simulate sending form data (e.g., via email or API)
            print(f"Sending form data for {self.name}...")
            return True
        except Exception as e:
            print(f"Error sending form data: {str(e)}")
            return False


class ContactFormV2(ContactForm):
    """Contact form version 2"""

    def __init__(self, name: str, email: str, message: str, phone: str):
        super().__init__(name, email, message)
        self.phone = phone

    def validate(self) -> bool:
        """Validate form data for version 2"""
        if not self.name or not self.email or not self.message or not self.phone:
            return False
        return True

    def send(self) -> bool:
        """Send form data for version 2"""
        try:
            # Simulate sending form data (e.g., via email or API)
            print(f"Sending form data for {self.name}...")
            return True
        except Exception as e:
            print(f"Error sending form data: {str(e)}")
            return False


def create_contact_form(version: str, data: Dict[str, str]) -> ContactForm:
    """Create a contact form instance based on version"""
    if version == "v1":
        return ContactFormV1(data["name"], data["email"], data["message"])
    elif version == "v2":
        return ContactFormV2(data["name"], data["email"], data["message"], data["phone"])
    else:
        raise ValueError("Invalid version")


def main():
    # Example usage
    data_v1 = {"name": "John Doe", "email": "john@example.com", "message": "Hello!"}
    data_v2 = {"name": "Jane Doe", "email": "jane@example.com", "message": "Hello!", "phone": "123-456-7890"}

    form_v1 = create_contact_form("v1", data_v1)
    form_v2 = create_contact_form("v2", data_v2)

    if form_v1.validate():
        form_v1.send()
    else:
        print("Invalid form data")

    if form_v2.validate():
        form_v2.send()
    else:
        print("Invalid form data")


if __name__ == "__main__":
    main()
```
