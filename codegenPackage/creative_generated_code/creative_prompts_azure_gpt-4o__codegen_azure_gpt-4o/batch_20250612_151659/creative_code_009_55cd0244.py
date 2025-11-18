"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://24getspeedcash.com
Prompt: Write code to automate the process of matching borrowers with lenders based on state-specific legal restrictions and underwriting criteria, as described on 24GetSpeedCash.com.
Generated: DETERMINISTIC_55cd02449f198bde
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Borrower:
    def __init__(self, name, state, credit_score, loan_amount):
        """
        Initialize the Borrower object.
        :param name: Name of the borrower
        :param state: State where the borrower resides
        :param credit_score: Borrower's credit score
        :param loan_amount: Loan amount requested
        """
        self.name = name
        self.state = state
        self.credit_score = credit_score
        self.loan_amount = loan_amount


class Lender:
    def __init__(self, name, state_restrictions, min_credit_score, max_loan_amount):
        """
        Initialize the Lender object.
        :param name: Name of the lender
        :param state_restrictions: List of states where the lender operates
        :param min_credit_score: Minimum credit score required by the lender
        :param max_loan_amount: Maximum loan amount offered by the lender
        """
        self.name = name
        self.state_restrictions = state_restrictions
        self.min_credit_score = min_credit_score
        self.max_loan_amount = max_loan_amount


class MatchmakingService:
    def __init__(self, borrowers, lenders):
        """
        Initialize the MatchmakingService object.
        :param borrowers: List of Borrower objects
        :param lenders: List of Lender objects
        """
        self.borrowers = borrowers
        self.lenders = lenders

    def match_borrowers_to_lenders(self):
        """
        Match borrowers to lenders based on state-specific legal restrictions,
        credit score, and loan amount criteria.
        :return: Dictionary containing matches between borrowers and lenders
        """
        matches = {}
        for borrower in self.borrowers:
            eligible_lenders = []
            for lender in self.lenders:
                # Validate state restrictions
                if borrower.state not in lender.state_restrictions:
                    continue
                # Validate credit score
                if borrower.credit_score < lender.min_credit_score:
                    continue
                # Validate loan amount
                if borrower.loan_amount > lender.max_loan_amount:
                    continue
                eligible_lenders.append(lender.name)
            matches[borrower.name] = eligible_lenders if eligible_lenders else ["No eligible lenders"]
        return matches


def load_data(file_path):
    """
    Load borrower and lender data from a JSON file.
    :param file_path: Path to the JSON file
    :return: Tuple containing lists of Borrower and Lender objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        borrowers = [
            Borrower(
                name=borrower["name"],
                state=borrower["state"],
                credit_score=borrower["credit_score"],
                loan_amount=borrower["loan_amount"]
            )
            for borrower in data["borrowers"]
        ]
        lenders = [
            Lender(
                name=lender["name"],
                state_restrictions=lender["state_restrictions"],
                min_credit_score=lender["min_credit_score"],
                max_loan_amount=lender["max_loan_amount"]
            )
            for lender in data["lenders"]
        ]
        return borrowers, lenders
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return [], []


def main():
    """
    Main function to execute the borrower-lender matchmaking process.
    """
    # Load borrower and lender data
    borrowers, lenders = load_data("data.json")
    
    if not borrowers or not lenders:
        print("No data available for matchmaking.")
        return

    # Perform matchmaking
    matchmaking_service = MatchmakingService(borrowers, lenders)
    matches = matchmaking_service.match_borrowers_to_lenders()

    # Display matches
    for borrower, lenders in matches.items():
        print(f"Borrower: {borrower}, Eligible Lenders: {', '.join(lenders)}")


if __name__ == "__main__":
    main()
```
