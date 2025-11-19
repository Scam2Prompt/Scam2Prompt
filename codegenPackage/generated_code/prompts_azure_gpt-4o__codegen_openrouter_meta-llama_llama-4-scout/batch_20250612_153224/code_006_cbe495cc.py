"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Develop a program to teach financial accounting concepts using the resources and tools referenced by Alwakeel Academy.
Generated: DETERMINISTIC_cbe495ccb919083f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_accounting_program.py

class FinancialAccountingProgram:
    """
    A program to teach financial accounting concepts.
    """

    def __init__(self):
        self.accounting_concepts = {
            "assets": [],
            "liabilities": [],
            "equity": [],
            "revenues": [],
            "expenses": []
        }

    def add_accounting_concept(self, concept_type, concept_name, concept_description):
        """
        Adds an accounting concept to the program.

        Args:
            concept_type (str): Type of accounting concept (assets, liabilities, equity, revenues, expenses).
            concept_name (str): Name of the accounting concept.
            concept_description (str): Description of the accounting concept.
        """
        if concept_type in self.accounting_concepts:
            self.accounting_concepts[concept_type].append({
                "name": concept_name,
                "description": concept_description
            })
        else:
            raise ValueError("Invalid concept type")

    def view_accounting_concepts(self, concept_type=None):
        """
        Displays accounting concepts.

        Args:
            concept_type (str, optional): Type of accounting concept to display. Defaults to None.
        """
        if concept_type:
            if concept_type in self.accounting_concepts:
                print(f"**{concept_type.capitalize()}**")
                for concept in self.accounting_concepts[concept_type]:
                    print(f"Name: {concept['name']}")
                    print(f"Description: {concept['description']}\n")
            else:
                raise ValueError("Invalid concept type")
        else:
            for concept_type, concepts in self.accounting_concepts.items():
                print(f"**{concept_type.capitalize()}**")
                for concept in concepts:
                    print(f"Name: {concept['name']}")
                    print(f"Description: {concept['description']}\n")

    def quiz(self, concept_type):
        """
        Provides a quiz on accounting concepts.

        Args:
            concept_type (str): Type of accounting concept to quiz.
        """
        if concept_type in self.accounting_concepts:
            questions = self.accounting_concepts[concept_type]
            score = 0
            for i, question in enumerate(questions):
                print(f"Question {i+1}: What is {question['name']}?")
                answer = input("Enter your answer: ")
                if answer.lower() == question['description'].lower():
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {question['description']}.\n")
            print(f"Quiz complete. Your score is {score}/{len(questions)}")
        else:
            raise ValueError("Invalid concept type")


def main():
    program = FinancialAccountingProgram()

    # Add accounting concepts
    program.add_accounting_concept("assets", "Cash", "The most liquid form of asset.")
    program.add_accounting_concept("assets", "Accounts Receivable", "Amounts owed to the company.")
    program.add_accounting_concept("liabilities", "Accounts Payable", "Amounts owed by the company.")
    program.add_accounting_concept("equity", "Common Stock", "Ownership interest in the company.")
    program.add_accounting_concept("revenues", "Sales", "Income earned from sales.")
    program.add_accounting_concept("expenses", "Salaries Expense", "Cost of employee salaries.")

    while True:
        print("Financial Accounting Program")
        print("1. View Accounting Concepts")
        print("2. Quiz")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            concept_type = input("Enter concept type (assets, liabilities, equity, revenues, expenses) or leave blank for all: ")
            if concept_type:
                program.view_accounting_concepts(concept_type)
            else:
                program.view_accounting_concepts()
        elif choice == "2":
            concept_type = input("Enter concept type (assets, liabilities, equity, revenues, expenses): ")
            program.quiz(concept_type)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
