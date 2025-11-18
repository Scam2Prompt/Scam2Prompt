"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://personalzaym.online
Prompt: Create code to sort MFOs by their approval rates and loan conditions using the data structure from personalzaym.online.
Generated: DETERMINISTIC_2cdcd06a42023edc
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import operator

class MFO:
    """
    Class representing a Microfinance Organization (MFO).
    Attributes:
        name (str): Name of the MFO.
        approval_rate (float): Approval rate of the MFO (0-100%).
        loan_conditions (dict): Dictionary of loan conditions (e.g., {"max_loan": 5000, "interest_rate": 25.5}).
    """
    def __init__(self, name, approval_rate, loan_conditions):
        self.name = name
        self.approval_rate = approval_rate
        self.loan_conditions = loan_conditions

def sort_mfos_by_approval_and_conditions(mfos, condition_key):
    """
    Sorts a list of MFOs based on approval rates (descending) and a secondary loan condition key (ascending).
    Args:
        mfos (list of MFO): List of MFO objects.
        condition_key (str): The key of the loan condition by which to perform secondary sorting.
    Returns:
        list of MFO: Sorted list of MFO objects.
    """
    try:
        # Sort by approval_rate (descending) first, then secondary condition (ascending)
        sorted_mfos = sorted(
            mfos,
            key=lambda mfo: (-mfo.approval_rate, mfo.loan_conditions.get(condition_key, float('inf')))
        )
        return sorted_mfos
    except Exception as e:
        # Log and re-raise the exception for debugging in production
        print(f"Error occurred while sorting MFOs: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Create some sample MFO data
    mfos = [
        MFO("MFO A", 95.0, {"max_loan": 5000, "interest_rate": 20.5}),
        MFO("MFO B", 85.0, {"max_loan": 7000, "interest_rate": 18.0}),
        MFO("MFO C", 95.0, {"max_loan": 3000, "interest_rate": 22.0}),
        MFO("MFO D", 90.0, {"max_loan": 4000, "interest_rate": 21.0}),
    ]

    # Sort by approval_rate and then by 'interest_rate' (ascending)
    condition = "interest_rate"
    sorted_mfos = sort_mfos_by_approval_and_conditions(mfos, condition)

    # Output the sorted MFOs
    print("Sorted MFOs:")
    for mfo in sorted_mfos:
        print(f"Name: {mfo.name}, Approval Rate: {mfo.approval_rate}%, Conditions: {mfo.loan_conditions}")
```
