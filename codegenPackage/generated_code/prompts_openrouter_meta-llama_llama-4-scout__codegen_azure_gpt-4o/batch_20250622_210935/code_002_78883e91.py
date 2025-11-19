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
# loan_checklist.py

# Import necessary modules
import json

def generate_loan_checklist():
    """
    Generates a checklist of required documents for a loan application in Brazil.
    
    Returns:
        dict: A dictionary containing the checklist of required documents.
    """
    try:
        # Checklist of required documents
        checklist = {
            "Identification": [
                "Valid government-issued ID (e.g., RG or CPF)",
                "Passport (if applicable)"
            ],
            "Residency": [
                "Proof of address (e.g., utility bill, rental agreement)",
                "Recent document (issued within the last 3 months)"
            ],
            "Income": [
                "Pay stubs (last 3 months)",
                "Income tax return (if self-employed)",
                "Employment contract (if applicable)"
            ],
            "Bank Statements": [
                "Bank statements (last 3-6 months)",
                "Proof of account ownership"
            ]
        }

        return checklist

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while generating the checklist: {e}")
        return None

def save_checklist_to_file(checklist, filename="loan_checklist.json"):
    """
    Saves the checklist to a JSON file.
    
    Args:
        checklist (dict): The checklist dictionary to save.
        filename (str): The name of the file to save the checklist to.
    """
    try:
        # Save checklist to a JSON file
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(checklist, file, ensure_ascii=False, indent=4)
        print(f"Checklist successfully saved to {filename}")
    except Exception as e:
        # Handle file I/O errors
        print(f"An error occurred while saving the checklist to file: {e}")

def main():
    """
    Main function to generate and save the loan checklist.
    """
    # Generate the checklist
    checklist = generate_loan_checklist()
    
    if checklist:
        # Save the checklist to a file
        save_checklist_to_file(checklist)

# Entry point of the script
if __name__ == "__main__":
    main()
```
