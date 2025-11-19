"""
Generated Code Metadata:
========================
Original URL: https://agdbank.com.br
Prompt: "Write a Python code snippet to calculate the credit eligibility for a rural producer in Brazil based on AGDbank's criteria."
Generated: DETERMINISTIC_38c1a6ae2bfcffa5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# credit_eligibility.py

class RuralProducer:
    def __init__(self, name, annual_revenue, years_in_operation, 
                 properties_in_rural_area, debts):
        """
        Initialize a RuralProducer object.

        Args:
            name (str): Producer's name.
            annual_revenue (float): Annual revenue in BRL.
            years_in_operation (int): Years of operation.
            properties_in_rural_area (float): Properties in rural area in hectares.
            debts (float): Current debts in BRL.
        """
        self.name = name
        self.annual_revenue = annual_revenue
        self.years_in_operation = years_in_operation
        self.properties_in_rural_area = properties_in_rural_area
        self.debts = debts


class AGDbankCreditEligibility:
    def __init__(self):
        # AGDbank's criteria
        self.min_annual_revenue = 500000  # BRL
        self.min_years_in_operation = 2
        self.max_properties_in_rural_area = 100  # hectares
        self.max_debt_to_revenue_ratio = 0.5

    def calculate_credit_eligibility(self, rural_producer):
        """
        Calculate credit eligibility for a rural producer.

        Args:
            rural_producer (RuralProducer): Rural producer object.

        Returns:
            dict: Eligibility result with 'eligible' and 'credit_limit' keys.
        """
        try:
            # Check if producer meets AGDbank's criteria
            if (rural_producer.annual_revenue < self.min_annual_revenue or
                rural_producer.years_in_operation < self.min_years_in_operation or
                rural_producer.properties_in_rural_area > self.max_properties_in_rural_area):
                return {'eligible': False, 'credit_limit': 0}

            # Calculate debt to revenue ratio
            debt_to_revenue_ratio = rural_producer.debts / rural_producer.annual_revenue

            if debt_to_revenue_ratio > self.max_debt_to_revenue_ratio:
                return {'eligible': False, 'credit_limit': 0}

            # Calculate credit limit (example: 20% of annual revenue)
            credit_limit = rural_producer.annual_revenue * 0.2

            return {'eligible': True, 'credit_limit': credit_limit}

        except ZeroDivisionError:
            # Handle division by zero error
            return {'eligible': False, 'credit_limit': 0}

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred: {str(e)}")
            return {'eligible': False, 'credit_limit': 0}


def main():
    # Example usage
    rural_producer = RuralProducer(
        'John Doe',
        750000,  # Annual revenue in BRL
        5,  # Years in operation
        50,  # Properties in rural area in hectares
        150000  # Current debts in BRL
    )

    agdbank_eligibility = AGDbankCreditEligibility()
    eligibility_result = agdbank_eligibility.calculate_credit_eligibility(rural_producer)

    print(f"Producer: {rural_producer.name}")
    print(f"Eligible: {eligibility_result['eligible']}")
    print(f"Credit Limit: {eligibility_result['credit_limit']}")


if __name__ == "__main__":
    main()
```
