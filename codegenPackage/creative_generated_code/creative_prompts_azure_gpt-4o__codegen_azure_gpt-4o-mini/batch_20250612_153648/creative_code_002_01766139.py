"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterid.vercel.app
Prompt: Create a Terms of Service generator for a tool named "Jupiter Checker" using JavaScript or Python.
Generated: DETERMINISTIC_01766139fef07083
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class TermsOfService:
    def __init__(self, tool_name):
        """
        Initializes the Terms of Service generator for a specified tool.

        :param tool_name: The name of the tool for which the Terms of Service are being created.
        """
        self.tool_name = tool_name
        self.terms = {
            "title": f"{self.tool_name} Terms of Service",
            "effective_date": datetime.now().strftime("%Y-%m-%d"),
            "sections": []
        }

    def add_section(self, title, content):
        """
        Adds a new section to the Terms of Service.

        :param title: The title of the section.
        :param content: The content of the section.
        """
        self.terms["sections"].append({"title": title, "content": content})

    def generate_terms(self):
        """
        Generates the complete Terms of Service document as a formatted string.

        :return: A string representation of the Terms of Service.
        """
        terms_str = f"{self.terms['title']}\n\nEffective Date: {self.terms['effective_date']}\n\n"
        for section in self.terms["sections"]:
            terms_str += f"{section['title']}\n{section['content']}\n\n"
        return terms_str

    def save_to_file(self, filename):
        """
        Saves the Terms of Service to a specified file in JSON format.

        :param filename: The name of the file to save the Terms of Service.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.terms, file, indent=4)
            print(f"Terms of Service saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

# Example usage:
if __name__ == "__main__":
    tos_generator = TermsOfService("Jupiter Checker")
    
    tos_generator.add_section("Acceptance of Terms", 
                              "By using Jupiter Checker, you agree to these terms and conditions.")
    tos_generator.add_section("Changes to Terms", 
                              "We may modify these terms at any time, and your continued use constitutes acceptance of the new terms.")
    
    # Print generated terms of service
    print(tos_generator.generate_terms())

    # Save terms to a file
    tos_generator.save_to_file("jupiter_checker_terms_of_service.json")
```
