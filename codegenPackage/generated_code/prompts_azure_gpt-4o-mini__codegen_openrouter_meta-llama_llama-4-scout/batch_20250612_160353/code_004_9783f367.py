"""
Generated Code Metadata:
========================
Original URL: https://contentxlabs.dev
Prompt: Create a sample contract template for licensing content to AI partners, based on the practices outlined by ContentXLabs.
Generated: DETERMINISTIC_9783f3670a0cee15
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# content_license_contract.py

from datetime import date
from typing import List

class ContentLicenseContract:
    """
    A sample contract template for licensing content to AI partners.

    Attributes:
        licensor (str): The content owner/licensor.
        licensee (str): The AI partner/licensee.
        content_description (str): A brief description of the licensed content.
        territory (str): The geographic territory where the content can be used.
        term_start (date): The start date of the license term.
        term_end (date): The end date of the license term.
        permitted_uses (List[str]): A list of permitted uses for the licensed content.
    """

    def __init__(self, 
                 licensor: str, 
                 licensee: str, 
                 content_description: str, 
                 territory: str, 
                 term_start: date, 
                 term_end: date, 
                 permitted_uses: List[str]):
        """
        Initializes a ContentLicenseContract instance.

        Args:
            licensor (str): The content owner/licensor.
            licensee (str): The AI partner/licensee.
            content_description (str): A brief description of the licensed content.
            territory (str): The geographic territory where the content can be used.
            term_start (date): The start date of the license term.
            term_end (date): The end date of the license term.
            permitted_uses (List[str]): A list of permitted uses for the licensed content.

        Raises:
            ValueError: If term_start is after term_end.
        """
        if term_start > term_end:
            raise ValueError("Term start date cannot be after term end date")

        self.licensor = licensor
        self.licensee = licensee
        self.content_description = content_description
        self.territory = territory
        self.term_start = term_start
        self.term_end = term_end
        self.permitted_uses = permitted_uses

    def __str__(self):
        """
        Returns a string representation of the contract.

        Returns:
            str: A formatted string containing the contract details.
        """
        contract_str = f"CONTENT LICENSE CONTRACT\n\n"
        contract_str += f"Licensor: {self.licensor}\n"
        contract_str += f"Licensee: {self.licensee}\n\n"
        contract_str += f"Content Description: {self.content_description}\n\n"
        contract_str += f"Territory: {self.territory}\n\n"
        contract_str += f"Term: {self.term_start} - {self.term_end}\n\n"
        contract_str += "Permitted Uses:\n"
        for use in self.permitted_uses:
            contract_str += f"- {use}\n"

        return contract_str

    def to_dict(self):
        """
        Returns a dictionary representation of the contract.

        Returns:
            dict: A dictionary containing the contract details.
        """
        return {
            "licensor": self.licensor,
            "licensee": self.licensee,
            "content_description": self.content_description,
            "territory": self.territory,
            "term_start": self.term_start.isoformat(),
            "term_end": self.term_end.isoformat(),
            "permitted_uses": self.permitted_uses
        }


def main():
    try:
        # Example usage
        licensor = "ContentXLabs"
        licensee = "AI Partner Inc."
        content_description = "Sample content for AI model training"
        territory = "Worldwide"
        term_start = date(2024, 1, 1)
        term_end = date(2024, 12, 31)
        permitted_uses = ["Training AI models", "Content analysis"]

        contract = ContentLicenseContract(
            licensor, 
            licensee, 
            content_description, 
            territory, 
            term_start, 
            term_end, 
            permitted_uses
        )

        print(contract)
        print("\nContract as dictionary:")
        print(contract.to_dict())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
