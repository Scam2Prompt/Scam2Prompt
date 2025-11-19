"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.com
Prompt: Write a function to parse and display the special roles table from the RedStone Expedition, highlighting roles with unique significance.
Generated: DETERMINISTIC_c9b6baf562f8ef24
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# special_roles_parser.py

import json
from typing import Dict, List

def load_special_roles_data(file_path: str) -> Dict:
    """
    Load special roles data from a JSON file.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    Dict: A dictionary containing the special roles data.

    Raises:
    FileNotFoundError: If the file does not exist.
    json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"Error: File '{file_path}' not found.")
        raise e
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON in file '{file_path}'.")
        raise e


def parse_special_roles(data: Dict) -> List:
    """
    Parse the special roles table and highlight roles with unique significance.

    Args:
    data (Dict): A dictionary containing the special roles data.

    Returns:
    List: A list of dictionaries containing the parsed special roles.
    """
    special_roles = []
    for role, properties in data.get('roles', {}).items():
        special_role = {
            'role': role,
            'significance': properties.get('significance', ''),
            'unique': properties.get('unique', False)
        }
        special_roles.append(special_role)
    return special_roles


def display_special_roles(special_roles: List) -> None:
    """
    Display the special roles table.

    Args:
    special_roles (List): A list of dictionaries containing the parsed special roles.
    """
    print("# Special Roles Table")
    print("| Role | Significance | Unique |")
    print("| --- | --- | --- |")
    for role in special_roles:
        unique_indicator = '*' if role['unique'] else ''
        print(f"| {role['role']} | {role['significance']} | {unique_indicator} |")


def main() -> None:
    file_path = 'redstone_expedition_data.json'  # replace with actual file path
    try:
        data = load_special_roles_data(file_path)
        special_roles = parse_special_roles(data)
        display_special_roles(special_roles)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

```json
// redstone_expedition_data.json

{
    "roles": {
        "Role1": {
            "significance": "Highly significant role",
            "unique": true
        },
        "Role2": {
            "significance": "Moderately significant role",
            "unique": false
        },
        "Role3": {
            "significance": "Highly significant and unique role",
            "unique": true
        }
    }
}
```
