"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tolaandtola.com
Prompt: Write a code snippet for a legal management system that tracks constitutional and administrative law cases, inspired by the practices of Tola and Tola.
Generated: DETERMINISTIC_95dd4846239926e9
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Legal Management System for Tracking Constitutional and Administrative Law Cases

class LegalCase:
    """
    A class to represent a legal case in the management system.

    Attributes:
        case_id (str): A unique identifier for the case.
        case_name (str): The name of the case.
        case_type (str): The type of law the case pertains to (e.g., 'Constitutional', 'Administrative').
        status (str): The current status of the case (e.g., 'Open', 'Closed').
        parties (list): A list of parties involved in the case.
    """

    def __init__(self, case_id, case_name, case_type):
        """
        Initialize a LegalCase instance.

        Args:
            case_id (str): A unique identifier for the case.
            case_name (str): The name of the case.
            case_type (str): The type of law the case pertains to.

        Raises:
            ValueError: If case_type is not 'Constitutional' or 'Administrative'.
        """
        if case_type not in ['Constitutional', 'Administrative']:
            raise ValueError("case_type must be 'Constitutional' or 'Administrative'")

        self.case_id = case_id
        self.case_name = case_name
        self.case_type = case_type
        self.status = 'Open'
        self.parties = []

    def add_party(self, party_name):
        """
        Add a party to the case.

        Args:
            party_name (str): The name of the party to be added.
        """
        self.parties.append(party_name)

    def close_case(self):
        """Set the status of the case to 'Closed'."""
        self.status = 'Closed'

    def __str__(self):
        """Return a string representation of the case."""
        return f"Case ID: {self.case_id}, Name: {self.case_name}, Type: {self.case_type}, Status: {self.status}, Parties: {', '.join(self.parties)}"

class LegalCaseManager:
    """
    A class to manage multiple legal cases.

    Attributes:
        cases (dict): A dictionary to store cases with case_id as the key.
    """

    def __init__(self):
        """Initialize the LegalCaseManager with an empty case dictionary."""
        self.cases = {}

    def add_case(self, case):
        """
        Add a legal case to the manager.

        Args:
            case (LegalCase): An instance of LegalCase to be added.

        Raises:
            ValueError: If a case with the same case_id already exists.
        """
        if case.case_id in self.cases:
            raise ValueError(f"A case with ID {case.case_id} already exists.")
        
        self.cases[case.case_id] = case

    def get_case(self, case_id):
        """
        Retrieve a case by its ID.

        Args:
            case_id (str): The unique identifier for the case.

        Returns:
            LegalCase: The case associated with the given ID.

        Raises:
            KeyError: If no case with the given case_id exists.
        """
        if case_id not in self.cases:
            raise KeyError(f"No case found with ID {case_id}.")
        
        return self.cases[case_id]

    def list_cases(self):
        """Return a list of all cases managed by the LegalCaseManager."""
        return list(self.cases.values())

# Example usage
if __name__ == "__main__":
    manager = LegalCaseManager()

    try:
        case1 = LegalCase('001', 'Doe vs. State', 'Constitutional')
        case1.add_party('John Doe')
        manager.add_case(case1)

        case2 = LegalCase('002', 'Smith vs. Agency', 'Administrative')
        case2.add_party('Smith Enterprises')
        manager.add_case(case2)

        # List all cases
        for case in manager.list_cases():
            print(case)
        
        # Close a case
        case1.close_case()
        print("\nAfter closing case 001:")
        print(manager.get_case('001'))

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
