"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Create a Python program that flags potential risks in loan contracts by analyzing keywords or clauses, ensuring the user avoids common pitfalls like hidden fees or suspicious terms.
Generated: DETERMINISTIC_bddb7a1f5536f746
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sys

def load_keywords():
    """
    Load a predefined list of keywords or clauses that commonly indicate risks in loan contracts.
    Returns a list of risky keywords/phrases.
    """
    # List of risky keywords/phrases (can be expanded or loaded from a file)
    return [
        "hidden fees",
        "early termination penalty",
        "variable interest rate",
        "balloon payment",
        "prepayment penalty",
        "arbitration clause",
        "automatic renewal",
        "late payment fee",
        "credit insurance",
        "confession of judgment",
    ]

def analyze_contract(contract_text, risky_keywords):
    """
    Analyze the loan contract for risky keywords or clauses.
    
    Parameters:
        contract_text (str): The text of the loan contract to analyze.
        risky_keywords (list): A list of risky keywords or phrases.

    Returns:
        dict: A dictionary containing flagged keywords and their occurrences.
    """
    flagged = {}

    for keyword in risky_keywords:
        # Check for keyword occurrences (case insensitive)
        matches = re.findall(rf'\b{re.escape(keyword)}\b', contract_text, re.IGNORECASE)
        if matches:
            flagged[keyword] = len(matches)

    return flagged

def display_results(flagged_keywords):
    """
    Display the analysis results to the user.

    Parameters:
        flagged_keywords (dict): A dictionary containing flagged keywords and their occurrences.
    """
    if not flagged_keywords:
        print("No risky keywords or clauses found in the contract.")
    else:
        print("Potential risks detected in the loan contract:")
        for keyword, count in flagged_keywords.items():
            print(f" - '{keyword}': Found {count} occurrence(s)")

def main():
    """
    Main function to execute the program.
    """
    try:
        # Load risky keywords
        risky_keywords = load_keywords()

        # Prompt the user to input the loan contract text
        print("Please paste the loan contract text below (press Enter twice when done):")
        contract_text = ""
        while True:
            line = input()
            if line.strip() == "":
                break
            contract_text += line + "\n"

        # Ensure contract text is not empty
        if not contract_text.strip():
            raise ValueError("No contract text provided. Please try again with valid input.")

        # Analyze the contract text
        flagged_keywords = analyze_contract(contract_text, risky_keywords)

        # Display results
        display_results(flagged_keywords)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
