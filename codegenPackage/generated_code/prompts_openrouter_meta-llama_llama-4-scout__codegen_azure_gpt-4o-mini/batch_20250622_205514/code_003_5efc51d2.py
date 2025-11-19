"""
Generated Code Metadata:
========================
Original URL: https://cecd33.fr
Prompt: "Provide a list of industry-specific standards and certifications, such as ISO 9001 and EN 9100, that a mechanical engineering company like CECD 33 would need to comply with, along with a brief description of each."
Generated: DETERMINISTIC_5efc51d27e6e2d11
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Certification:
    """
    A class to represent a certification with its name and description.
    """

    def __init__(self, name: str, description: str):
        """
        Initializes a new Certification instance.

        :param name: The name of the certification.
        :param description: A brief description of the certification.
        """
        self.name = name
        self.description = description

    def to_dict(self):
        """
        Converts the Certification instance to a dictionary.

        :return: A dictionary representation of the certification.
        """
        return {
            "name": self.name,
            "description": self.description
        }


class CertificationList:
    """
    A class to manage a list of certifications.
    """

    def __init__(self):
        """
        Initializes a new CertificationList instance.
        """
        self.certifications = []

    def add_certification(self, certification: Certification):
        """
        Adds a certification to the list.

        :param certification: An instance of Certification to add.
        """
        self.certifications.append(certification)

    def to_json(self):
        """
        Converts the list of certifications to a JSON string.

        :return: A JSON string representation of the certifications.
        """
        return json.dumps([cert.to_dict() for cert in self.certifications], indent=4)


def main():
    """
    Main function to create a list of industry-specific standards and certifications.
    """
    try:
        cert_list = CertificationList()

        # Adding certifications
        cert_list.add_certification(Certification("ISO 9001", "Quality management systems - Requirements."))
        cert_list.add_certification(Certification("EN 9100", "Quality management systems - Requirements for aviation, space, and defense organizations."))
        cert_list.add_certification(Certification("ISO 14001", "Environmental management systems - Requirements with guidance for use."))
        cert_list.add_certification(Certification("AS9100", "Quality management system for aerospace organizations."))
        cert_list.add_certification(Certification("ISO 45001", "Occupational health and safety management systems - Requirements with guidance for use."))

        # Output the certifications in JSON format
        print(cert_list.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
