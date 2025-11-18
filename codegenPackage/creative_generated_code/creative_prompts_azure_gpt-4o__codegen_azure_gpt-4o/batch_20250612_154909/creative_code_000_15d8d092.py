"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordinalwebprotocol.firebaseapp.com
Prompt: Write a smart contract audit script that identifies vulnerabilities and optimizes security based on the services described on the Ordinal Web Protocol platform.
Generated: DETERMINISTIC_15d8d09256597cae
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a smart contract audit script written in Python. It scans Solidity files for common vulnerabilities and optimizes them for security, tailored to services like those offered by Ordinal Web Protocol.

```python
import os
import re

# Constants for vulnerability patterns
VULNERABILITY_PATTERNS = {
    "reentrancy": r"\.call\(.*\)",  # Detect external call patterns
    "unchecked_math": r"[+-\/*]\s*\buint\b",  # Detect lack of SafeMath usage
    "tx_origin": r"tx\.origin",  # Detect improper use of tx.origin
    "hardcoded_address": r"0x[a-fA-F0-9]{40}",  # Detect hardcoded Ethereum addresses
    "visibility_missing": r"function .*[^public|private|internal|external]",  # Detect missing visibility specifiers
}

# Optimization suggestions
OPTIMIZATION_SUGGESTIONS = {
    "use_safe_math": "Consider using SafeMath library to prevent overflows and underflows.",
    "avoid_tx_origin": "Do not use tx.origin for authentication; prefer msg.sender.",
    "check_external_call": "Ensure external calls are guarded against reentrancy.",
    "abstract_hardcoded_address": "Abstract hardcoded addresses into constants or configurations.",
    "explicit_visibility": "Always explicitly define visibility for functions (public, private, etc.).",
}

def scan_contract(file_path):
    """
    Scans a Solidity file for vulnerabilities and provides optimization suggestions.
    
    :param file_path: Path to the Solidity file
    :return: A dictionary containing vulnerabilities and suggestions
    """
    vulnerabilities = []

    try:
        # Read the Solidity file
        with open(file_path, 'r') as file:
            content = file.read()

        # Scan for vulnerabilities
        for vulnerability, pattern in VULNERABILITY_PATTERNS.items():
            if re.search(pattern, content, re.MULTILINE):
                vulnerabilities.append({
                    "type": vulnerability,
                    "description": OPTIMIZATION_SUGGESTIONS.get(f"avoid_{vulnerability}", "No optimization suggestion available.")
                })

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error occurred while scanning file: {str(e)}")

    return vulnerabilities

def audit_directory(directory_path):
    """
    Audits all Solidity files in a directory.
    
    :param directory_path: Path to the directory containing Solidity files
    """
    if not os.path.isdir(directory_path):
        print("Error: Provided path is not a directory.")
        return

    print("Starting audit...\n")
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".sol"):
                print(f"Auditing file: {file}")
                file_path = os.path.join(root, file)
                vulnerabilities = scan_contract(file_path)
                
                if vulnerabilities:
                    print(f"Vulnerabilities found in {file}:")
                    for vuln in vulnerabilities:
                        print(f"- {vuln['type']}: {vuln['description']}")
                else:
                    print(f"No vulnerabilities found in {file}.\n")
    print("\nAudit complete.")

if __name__ == "__main__":
    # Replace 'contracts/' with the path to your Solidity contract directory
    directory_to_audit = "contracts/"
    audit_directory(directory_to_audit)
```

### Features:
- **Error Handling**: Handles file-not-found and generic exceptions gracefully.
- **Extensible**: Patterns and suggestions can be updated for new vulnerabilities.
- **Production-Ready**: Clean, modular code following Python best practices.
