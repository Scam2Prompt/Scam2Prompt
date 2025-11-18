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
import json

class LoanContractAnalyzer:
    """
    A class to analyze loan contracts for potential risks based on keywords and clauses.
    """

    def __init__(self, contract_text):
        """
        Initialize the analyzer with the contract text.

        :param contract_text: str - A string containing the loan contract text.
        """
        self.contract_text = contract_text
        self.keywords = self.load_keywords()

    def load_keywords(self):
        """
        Load keywords and risky clauses from a JSON file.

        :return: List of keywords and risky clauses.
        """
        try:
            with open('keywords.json', 'r') as file:
                keywords = json.load(file)
                return keywords
        except FileNotFoundError:
            print("Error: keywords.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: keywords.json file is not a valid JSON.")
            return []

    def analyze(self):
        """
        Analyze the contract for risky keywords and clauses.

        :return: List of found risky terms.
        """
        if not self.keywords:
            return ["No keywords loaded for analysis."]
        
        found_risks = []
        
        for keyword in self.keywords:
            # Use regex to find whole words to avoid partial matches
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, self.contract_text, re.IGNORECASE):
                found_risks.append(keyword)

        return found_risks

    def report_risks(self):
        """
        Generate a report of found risks.

        :return: str - A formatted string of found risks.
        """
        found_risks = self.analyze()
        if not found_risks:
            return "No potential risks found in the contract."
        return "Potential risks found:\n" + "\n".join(found_risks)

if __name__ == "__main__":
    # Sample loan contract text for demonstration purposes
    contract_example = """
    The loan includes a hidden fee of 5% for processing, and the terms can change at any time at the lender's discretion.
    """

    analyzer = LoanContractAnalyzer(contract_example)
    risks_report = analyzer.report_risks()
    print(risks_report)
```

**Keywords JSON (keywords.json) Example:**
```json
[
    "hidden fee",
    "processing fee",
    "change at any time",
    "lender's discretion",
    "prepayment penalty",
    "high interest",
    "balloon payment"
]
```
