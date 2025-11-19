"""
Generated Code Metadata:
========================
Original URL: https://terminaltunja.com
Prompt: Write a Python program to parse and analyze the manual de funciones and organigrama of the Terminal Tunja, extracting key roles and responsibilities.
Generated: DETERMINISTIC_142d0c07db8a6c46
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import json
from typing import List, Dict

class TerminalTunjaAnalyzer:
    """
    A class to analyze the manual de funciones and organigrama of the Terminal Tunja.
    """

    def __init__(self, text: str):
        """
        Initializes the analyzer with the provided text.

        :param text: The text containing the manual de funciones and organigrama.
        """
        self.text = text
        self.roles = {}

    def parse_roles(self) -> None:
        """
        Parses the text to extract key roles and their responsibilities.
        """
        # Regular expression to find roles and responsibilities
        role_pattern = re.compile(r'(?P<role>[A-Z\s]+):\s*(?P<responsibilities>.+?)(?=\n[A-Z\s]+:|$)', re.DOTALL)
        
        matches = role_pattern.finditer(self.text)
        for match in matches:
            role = match.group('role').strip()
            responsibilities = match.group('responsibilities').strip().split('\n')
            self.roles[role] = [resp.strip() for resp in responsibilities if resp.strip()]

    def get_roles(self) -> Dict[str, List[str]]:
        """
        Returns the extracted roles and their responsibilities.

        :return: A dictionary with roles as keys and a list of responsibilities as values.
        """
        return self.roles

    def save_to_json(self, filename: str) -> None:
        """
        Saves the extracted roles and responsibilities to a JSON file.

        :param filename: The name of the file to save the data.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(self.roles, json_file, ensure_ascii=False, indent=4)
            print(f"Data successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

def main():
    # Sample text input (replace with actual text from the manual de funciones and organigrama)
    sample_text = """
    DIRECTOR: 
    - Manage overall operations
    - Ensure compliance with regulations

    ADMINISTRADOR: 
    - Oversee administrative functions
    - Manage staff and resources

    COORDINADOR DE OPERACIONES: 
    - Coordinate daily operations
    - Liaise with external partners
    """

    # Create an instance of the analyzer
    analyzer = TerminalTunjaAnalyzer(sample_text)

    # Parse the roles from the text
    analyzer.parse_roles()

    # Retrieve and print the roles
    roles = analyzer.get_roles()
    print(json.dumps(roles, ensure_ascii=False, indent=4))

    # Save the roles to a JSON file
    analyzer.save_to_json('terminal_tunja_roles.json')

if __name__ == "__main__":
    main()
```
