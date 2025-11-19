"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Generate documentation for a Código-generated smart contract, including a list of exposed methods, input parameters, and account structure for a Solana-based virtual machine.
Generated: DETERMINISTIC_5ae68634288be9f6
Batch ID: 20250622_211342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Smart Contract Documentation Generator for Solana-based Virtual Machine
=======================================================================

This script generates documentation for a given smart contract written for the Solana blockchain.
It extracts and lists:
1. Exposed methods
2. Input parameters for each method
3. Account structure used by the contract

Usage:
- Ensure the smart contract code is available in the specified file path.
- Run this script to generate a markdown file containing the documentation.

Dependencies:
- Python 3.7+
- `solana-py` library (for parsing Solana-specific structures)

Output:
- A markdown file named `smart_contract_documentation.md` containing the generated documentation.
"""

import os
import re
import json
from typing import List, Dict, Any

# Constants
INPUT_CONTRACT_FILE = "smart_contract.rs"  # Path to the smart contract file
OUTPUT_DOC_FILE = "smart_contract_documentation.md"  # Output documentation file


def parse_smart_contract(file_path: str) -> Dict[str, Any]:
    """
    Parses the smart contract file to extract exposed methods, input parameters, and account structure.

    Args:
        file_path (str): Path to the smart contract file.

    Returns:
        Dict[str, Any]: A dictionary containing the parsed methods, parameters, and account structure.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Smart contract file not found: {file_path}")

    with open(file_path, "r") as file:
        contract_code = file.read()

    # Regex patterns to extract methods and account structures
    method_pattern = r"pub fn (\w+)\((.*?)\)"
    account_pattern = r"#[\[\]a-zA-Z0-9_]*AccountInfo.*?pub struct (\w+).*?\{(.*?)\}"

    # Extract methods
    methods = []
    for match in re.finditer(method_pattern, contract_code, re.DOTALL):
        method_name = match.group(1)
        params = match.group(2).strip()
        param_list = [param.strip() for param in params.split(",") if param.strip()]
        methods.append({"name": method_name, "parameters": param_list})

    # Extract account structures
    accounts = []
    for match in re.finditer(account_pattern, contract_code, re.DOTALL):
        account_name = match.group(1)
        account_fields = match.group(2).strip()
        fields = [field.strip() for field in account_fields.split("\n") if field.strip()]
        accounts.append({"name": account_name, "fields": fields})

    return {"methods": methods, "accounts": accounts}


def generate_documentation(parsed_data: Dict[str, Any], output_file: str) -> None:
    """
    Generates a markdown file containing the documentation for the smart contract.

    Args:
        parsed_data (Dict[str, Any]): Parsed data containing methods and account structures.
        output_file (str): Path to the output markdown file.
    """
    with open(output_file, "w") as file:
        file.write("# Smart Contract Documentation\n\n")
        file.write("## Exposed Methods\n")
        for method in parsed_data["methods"]:
            file.write(f"### {method['name']}\n")
            file.write("#### Parameters:\n")
            if method["parameters"]:
                for param in method["parameters"]:
                    file.write(f"- `{param}`\n")
            else:
                file.write("- None\n")
            file.write("\n")

        file.write("## Account Structures\n")
        for account in parsed_data["accounts"]:
            file.write(f"### {account['name']}\n")
            file.write("#### Fields:\n")
            if account["fields"]:
                for field in account["fields"]:
                    file.write(f"- `{field}`\n")
            else:
                file.write("- None\n")
            file.write("\n")


def main():
    """
    Main function to parse the smart contract and generate documentation.
    """
    try:
        # Parse the smart contract
        parsed_data = parse_smart_contract(INPUT_CONTRACT_FILE)

        # Generate documentation
        generate_documentation(parsed_data, OUTPUT_DOC_FILE)

        print(f"Documentation successfully generated: {OUTPUT_DOC_FILE}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
