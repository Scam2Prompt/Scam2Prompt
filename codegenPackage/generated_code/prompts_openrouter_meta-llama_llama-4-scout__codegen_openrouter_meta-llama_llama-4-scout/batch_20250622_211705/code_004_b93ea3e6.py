"""
Generated Code Metadata:
========================
Original URL: https://quickzaem.online
Prompt: Develop a function to calculate the total cost of a microloan from a Kazakhstani MFO, given the loan amount, term, and interest rate, and provide a list of MFOs with their respective rates.
Generated: DETERMINISTIC_b93ea3e6f1616939
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# microloan_calculator.py

class MicrofinanceOrganization:
    """Represents a Kazakhstani MFO with its interest rate."""

    def __init__(self, name, interest_rate):
        """
        Initializes an MFO object.

        Args:
            name (str): Name of the MFO.
            interest_rate (float): Interest rate of the MFO as a decimal.
        """
        self.name = name
        self.interest_rate = interest_rate


def calculate_microloan_cost(loan_amount, term, interest_rate):
    """
    Calculates the total cost of a microloan.

    Args:
        loan_amount (float): The initial loan amount.
        term (int): The loan term in days.
        interest_rate (float): The annual interest rate as a decimal.

    Returns:
        float: The total cost of the microloan.

    Raises:
        ValueError: If loan amount, term, or interest rate is invalid.
    """
    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")
    if term <= 0:
        raise ValueError("Term must be greater than zero.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    # Convert term from days to years
    term_in_years = term / 365

    # Calculate the total cost using the formula: A = P * (1 + r * t)
    total_cost = loan_amount * (1 + interest_rate * term_in_years)

    return total_cost


def get_kazakhstani_mfos():
    """
    Returns a list of Kazakhstani MFOs with their respective interest rates.

    Returns:
        list[MicrofinanceOrganization]: A list of MFO objects.
    """
    mfos = [
        MicrofinanceOrganization("Fond Mikro", 0.18),  # 18% interest rate
        MicrofinanceOrganization("KazMicroFinance", 0.20),  # 20% interest rate
        MicrofinanceOrganization("MicroCredit", 0.22),  # 22% interest rate
    ]

    return mfos


def main():
    # Example usage
    loan_amount = 100000  # 100,000 KZT
    term = 180  # 180 days
    interest_rate = 0.20  # 20% annual interest rate

    try:
        total_cost = calculate_microloan_cost(loan_amount, term, interest_rate)
        print(f"Total cost of the microloan: {total_cost:.2f} KZT")

        mfos = get_kazakhstani_mfos()
        print("\nList of Kazakhstani MFOs with their interest rates:")
        for mfo in mfos:
            print(f"{mfo.name}: {mfo.interest_rate * 100}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
