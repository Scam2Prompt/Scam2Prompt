"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: Write a Python script to manage the membership and financing applications for GIAC1, including checking eligibility criteria and processing reimbursement requests.
Generated: DETERMINISTIC_ff43d613538c09a5
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_financing.py

class MembershipFinancing:
    def __init__(self):
        self.eligibility_criteria = {
            'min_age': 18,
            'max_age': 65,
            'min_income': 50000
        }
        self.reimbursement_requests = []

    def check_eligibility(self, applicant_info):
        """
        Check if an applicant meets the eligibility criteria.

        Args:
            applicant_info (dict): Dictionary containing applicant's info.
                - 'age' (int): Applicant's age.
                - 'income' (float): Applicant's annual income.

        Returns:
            bool: True if eligible, False otherwise.
        """
        if 'age' not in applicant_info or 'income' not in applicant_info:
            raise ValueError("Applicant info must contain 'age' and 'income'")

        age = applicant_info['age']
        income = applicant_info['income']

        return (self.eligibility_criteria['min_age'] <= age <= self.eligibility_criteria['max_age'] and
                income >= self.eligibility_criteria['min_income'])

    def process_reimbursement_request(self, request_info):
        """
        Process a reimbursement request.

        Args:
            request_info (dict): Dictionary containing request info.
                - 'applicant_name' (str): Name of the applicant.
                - 'request_amount' (float): Requested reimbursement amount.

        Returns:
            dict: Dictionary containing the result of the request.
                - 'approved' (bool): Whether the request was approved.
                - 'amount' (float): Approved reimbursement amount.
        """
        required_fields = ['applicant_name', 'request_amount']
        if not all(field in request_info for field in required_fields):
            raise ValueError("Request info must contain 'applicant_name' and 'request_amount'")

        applicant_name = request_info['applicant_name']
        request_amount = request_info['request_amount']

        # Simple approval logic for demonstration purposes
        # In a real application, this would be more complex
        approved_amount = request_amount * 0.8  # 80% approval rate

        self.reimbursement_requests.append({
            'applicant_name': applicant_name,
            'request_amount': request_amount,
            'approved_amount': approved_amount
        })

        return {
            'approved': True,
            'amount': approved_amount
        }

    def get_reimbursement_requests(self):
        """
        Get a list of all reimbursement requests.

        Returns:
            list: List of dictionaries containing request info.
        """
        return self.reimbursement_requests


def main():
    membership_financing = MembershipFinancing()

    # Example usage
    applicant_info = {
        'age': 30,
        'income': 60000
    }

    if membership_financing.check_eligibility(applicant_info):
        print("Applicant is eligible")
    else:
        print("Applicant is not eligible")

    request_info = {
        'applicant_name': 'John Doe',
        'request_amount': 1000.0
    }

    try:
        result = membership_financing.process_reimbursement_request(request_info)
        print(f"Reimbursement request approved: {result['approved']}, Amount: {result['amount']}")
    except ValueError as e:
        print(f"Error processing request: {e}")

    reimbursement_requests = membership_financing.get_reimbursement_requests()
    print("Reimbursement Requests:")
    for request in reimbursement_requests:
        print(f"Applicant: {request['applicant_name']}, Request Amount: {request['request_amount']}, Approved Amount: {request['approved_amount']}")


if __name__ == "__main__":
    main()
```
