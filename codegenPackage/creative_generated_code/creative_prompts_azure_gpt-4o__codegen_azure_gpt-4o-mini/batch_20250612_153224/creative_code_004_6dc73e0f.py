"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Write code to implement a multilingual outreach program, including tools for distributing educational materials like "منشورات ومطويات توعوية دعوية تثقيفية" in multiple languages.
Generated: DETERMINISTIC_6dc73e0f78ca4b8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import requests
from typing import List, Dict, Optional

class MultilingualOutreach:
    """
    A class to manage multilingual outreach programs, including tools for distributing
    educational materials in multiple languages.
    """

    def __init__(self, supported_languages: List[str]):
        """
        Initialize the outreach program with supported languages.

        :param supported_languages: List of supported language codes (e.g., ['en', 'ar', 'fr']).
        """
        self.supported_languages = supported_languages
        self.materials = {}

    def add_material(self, language: str, content: str):
        """
        Add educational material for a specific language.

        :param language: Language code for the material (must be supported).
        :param content: Content of the educational material.
        :raises ValueError: If the language is not supported.
        """
        if language not in self.supported_languages:
            raise ValueError(f"Language '{language}' is not supported.")
        
        if language not in self.materials:
            self.materials[language] = []
        
        self.materials[language].append(content)

    def distribute_material(self, language: str, recipient_list: List[str]) -> None:
        """
        Distribute the educational material to a list of recipients via email.

        :param language: Language code of the material to distribute.
        :param recipient_list: List of recipient email addresses.
        :raises ValueError: If the language has no materials or is not supported.
        """
        if language not in self.supported_languages:
            raise ValueError(f"Language '{language}' is not supported.")
        
        if language not in self.materials or not self.materials[language]:
            raise ValueError(f"No materials available in language '{language}'.")

        content = "\n\n".join(self.materials[language])
        
        for recipient in recipient_list:
            self.send_email(recipient, content)

    @staticmethod
    def send_email(recipient: str, content: str) -> None:
        """
        Simulate sending an email (for demo purposes only).

        :param recipient: Email address of the recipient.
        :param content: Content of the email to be sent.
        """
        try:
            # Simulated email sending logic
            print(f"Sending email to {recipient}...")
            print(content)
            print("Email sent successfully.\n")
        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {e}")

    def get_materials_info(self) -> Dict[str, int]:
        """
        Get a summary of materials available by language.

        :return: Dictionary with language codes as keys and count of materials as values.
        """
        return {lang: len(self.materials.get(lang, [])) for lang in self.supported_languages}

# Example usage
if __name__ == "__main__":
    try:
        outreach_program = MultilingualOutreach(supported_languages=['en', 'ar', 'fr'])
        
        # Adding materials for different languages
        outreach_program.add_material('en', 'Educational pamphlet on health and wellness.')
        outreach_program.add_material('ar', 'منشور توعوي حول الصحة والعافية.')
        outreach_program.add_material('fr', 'Brochure éducative sur la santé et le bien-être.')

        # Distributing educational materials
        recipients = ['user1@example.com', 'user2@example.com']
        outreach_program.distribute_material('en', recipients)

        # Displaying available materials info
        print("Materials available by language:", outreach_program.get_materials_info())

    except Exception as e:
        print(f"An error occurred: {e}")
```
