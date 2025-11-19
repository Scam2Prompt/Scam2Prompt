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

def parse_manual_de_funciones(file_path: str) -> List[Dict[str, str]]:
    """
    Parses the manual de funciones file to extract key roles and responsibilities.

    Args:
        file_path (str): Path to the manual de funciones file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing roles and responsibilities.
    """
    roles_responsibilities = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Regex pattern to extract roles and responsibilities
        pattern = r"Role:\s*(.*?)\s*Responsibility:\s*(.*?)\s*(?=Role:|$)"
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            role, responsibility = match
            roles_responsibilities.append({
                "Role": role.strip(),
                "Responsibility": responsibility.strip()
            })

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred while parsing the manual: {e}")

    return roles_responsibilities


def parse_organigrama(file_path: str) -> Dict[str, List[str]]:
    """
    Parses the organigrama file to extract the organizational structure.

    Args:
        file_path (str): Path to the organigrama file.

    Returns:
        Dict[str, List[str]]: A dictionary representing the organizational structure.
    """
    organizational_structure = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Regex pattern to extract departments and their members
        pattern = r"Department:\s*(.*?)\s*Members:\s*(.*?)\s*(?=Department:|$)"
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            department, members = match
            organizational_structure[department.strip()] = [
                member.strip() for member in members.split(',')
            ]

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred while parsing the organigrama: {e}")

    return organizational_structure


def save_to_json(data: Dict, output_file: str) -> None:
    """
    Saves the extracted data to a JSON file.

    Args:
        data (Dict): Data to be saved.
        output_file (str): Path to the output JSON file.

    Returns:
        None
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while saving to JSON: {e}")


def main():
    """
    Main function to parse and analyze the manual de funciones and organigrama.
    """
    # File paths (update these paths as needed)
    manual_de_funciones_path = "manual_de_funciones.txt"
    organigrama_path = "organigrama.txt"
    output_file = "terminal_tunja_analysis.json"

    # Parse files
    roles_responsibilities = parse_manual_de_funciones(manual_de_funciones_path)
    organizational_structure = parse_organigrama(organigrama_path)

    # Combine results
    analysis_result = {
        "Roles and Responsibilities": roles_responsibilities,
        "Organizational Structure": organizational_structure
    }

    # Save results to JSON
    save_to_json(analysis_result, output_file)


if __name__ == "__main__":
    main()
```
