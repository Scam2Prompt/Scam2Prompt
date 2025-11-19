"""
Generated Code Metadata:
========================
Original URL: https://lightningzaim.online
Prompt: "Generate a Python script to filter and compare loan offers from various MFOs in Kazakhstan based on user input for loan amount and duration."
Generated: DETERMINISTIC_aa981250504bd2bd
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class LoanOffer:
    """
    Represents a loan offer from an MFO (Microfinance Organization).
    """
    def __init__(self, name, interest_rate, max_amount, max_duration):
        self.name = name
        self.interest_rate = interest_rate  # Annual interest rate in percentage
        self.max_amount = max_amount  # Maximum loan amount the MFO offers
        self.max_duration = max_duration  # Maximum loan duration in months

    def calculate_total_payment(self, loan_amount, loan_duration):
        """
        Calculate the total payment for the loan based on the interest rate.
        Formula: Total Payment = Principal + (Principal * Interest Rate * Duration / 12)
        """
        if loan_duration > self.max_duration or loan_amount > self.max_amount:
            raise ValueError("Loan amount or duration exceeds the MFO's limits.")
        interest = loan_amount * (self.interest_rate / 100) * (loan_duration / 12)
        return loan_amount + interest


def load_mfo_data(file_path):
    """
    Load MFO data from a JSON file.
    :param file_path: Path to the JSON file containing MFO data.
    :return: List of LoanOffer objects.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            mfo_list = [
                LoanOffer(
                    name=mfo['name'],
                    interest_rate=mfo['interest_rate'],
                    max_amount=mfo['max_amount'],
                    max_duration=mfo['max_duration']
                )
                for mfo in data
            ]
            return mfo_list
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading MFO data: {e}")
        return []


def filter_and_compare_loans(mfo_list, loan_amount, loan_duration):
    """
    Filter MFOs based on user input and compare loan offers.
    :param mfo_list: List of LoanOffer objects.
    :param loan_amount: Desired loan amount.
    :param loan_duration: Desired loan duration in months.
    :return: List of filtered and sorted loan offers.
    """
    filtered_offers = []
    for mfo in mfo_list:
        try:
            if loan_amount <= mfo.max_amount and loan_duration <= mfo.max_duration:
                total_payment = mfo.calculate_total_payment(loan_amount, loan_duration)
                filtered_offers.append((mfo.name, total_payment))
        except ValueError as e:
            print(f"Skipping MFO {mfo.name}: {e}")

    # Sort offers by total payment (ascending)
    filtered_offers.sort(key=lambda x: x[1])
    return filtered_offers


def main():
    """
    Main function to execute the loan comparison script.
    """
    # Load MFO data from a JSON file
    mfo_data_file = 'mfo_data.json'  # Replace with the actual path to your JSON file
    mfo_list = load_mfo_data(mfo_data_file)

    if not mfo_list:
        print("No MFO data available. Exiting.")
        return

    # Get user input for loan amount and duration
    try:
        loan_amount = float(input("Enter the desired loan amount (KZT): "))
        loan_duration = int(input("Enter the desired loan duration (months): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for loan amount and duration.")
        return

    # Filter and compare loan offers
    filtered_offers = filter_and_compare_loans(mfo_list, loan_amount, loan_duration)

    # Display the results
    if filtered_offers:
        print("\nAvailable loan offers:")
        for name, total_payment in filtered_offers:
            print(f"MFO: {name}, Total Payment: {total_payment:.2f} KZT")
    else:
        print("No suitable loan offers found for the given amount and duration.")


if __name__ == "__main__":
    main()
```

### Notes:
- Ensure the `mfo_data.json` file exists and contains valid MFO data in the following format:
```json
[
    {
        "name": "MFO1",
        "interest_rate": 20,
        "max_amount": 1000000,
        "max_duration": 12
    },
    {
        "name": "MFO2",
        "interest_rate": 15,
        "max_amount": 500000,
        "max_duration": 6
    }
]
```
