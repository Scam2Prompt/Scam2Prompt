"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Generate a checklist of required documents for a loan application in Brazil, including identification, residency, income, and bank statements, as described in this webpage.
Generated: DETERMINISTIC_78883e91889c0a29
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

def generate_loan_documents_checklist() -> Dict[str, List[str]]:
    """
    Generates a checklist of required documents for a loan application in Brazil.
    
    Returns:
        Dict[str, List[str]]: A dictionary containing document categories and their respective requirements.
    """
    checklist = {
        "Identification": [
            "RG (Registro Geral) or CNH (Carteira Nacional de Habilitação)",
            "CPF (Cadastro de Pessoas Físicas)",
            "Birth certificate (if applicable)"
        ],
        "Residency Proof": [
            "Utility bill (electricity, water, gas) less than 3 months old",
            "Lease agreement (if renting)",
            "Property tax receipt (if homeowner)"
        ],
        "Income Proof": [
            "Last 3 pay slips",
            "Employment contract",
            "Income tax return (if self-employed)",
            "Social security statement (if retired)"
        ],
        "Bank Statements": [
            "Last 3 months of bank statements",
            "Proof of other income sources (if applicable)"
        ],
        "Additional Documents": [
            "Marriage certificate (if applicable)",
            "Divorce decree (if applicable)",
            "Prenuptial agreement (if applicable)"
        ]
    }
    
    return checklist

def print_checklist(checklist: Dict[str, List[str]]) -> None:
    """
    Prints the loan documents checklist in a user-friendly format.
    
    Args:
        checklist (Dict[str, List[str]]): The checklist to be printed.
    """
    print("\nLoan Application Documents Checklist (Brazil)\n")
    print("=" * 50)
    
    for category, documents in checklist.items():
        print(f"\n{category}:")
        for doc in documents:
            print(f" - {doc}")
    
    print("\n" + "=" * 50)
    print("\nNote: Additional documents may be required based on specific loan conditions.")

if __name__ == "__main__":
    checklist = generate_loan_documents_checklist()
    print_checklist(checklist)
```
