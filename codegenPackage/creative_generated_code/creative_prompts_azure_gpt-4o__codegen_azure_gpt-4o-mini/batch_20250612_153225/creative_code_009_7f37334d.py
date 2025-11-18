"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Write code to simulate various long-term insurance scenarios, including premium calculations and coverage options, based on TSM Wealth's insurance services.
Generated: DETERMINISTIC_7f37334dab5accce
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsurancePolicy:
    """
    A class to represent an insurance policy.
    
    Attributes
    ----------
    policy_holder : str
        Name of the person holding the policy.
    coverage_amount : float
        Total amount covered by the policy.
    premium_rate : float
        Monthly premium rate as a percentage of coverage amount.
    term_length : int
        Duration of the policy in years.
    """

    def __init__(self, policy_holder, coverage_amount, premium_rate, term_length):
        """
        Initializes an InsurancePolicy instance.

        Parameters
        ----------
        policy_holder : str
            Name of the policy holder.
        coverage_amount : float
            Total coverage amount.
        premium_rate : float
            Monthly premium rate as a percentage.
        term_length : int
            Duration of the policy in years.
        """
        self.policy_holder = policy_holder
        self.coverage_amount = coverage_amount
        self.premium_rate = premium_rate
        self.term_length = term_length

    def calculate_monthly_premium(self):
        """
        Calculates the monthly premium based on coverage amount and premium rate.

        Returns
        -------
        float
            The monthly premium amount.
        """
        try:
            monthly_premium = (self.coverage_amount * self.premium_rate) / 100
            return monthly_premium
        except Exception as e:
            print(f"Error calculating monthly premium: {e}")
            return None

    def calculate_total_premium(self):
        """
        Calculates the total premium over the term of the policy.

        Returns
        -------
        float
            The total premium amount over the term.
        """
        try:
            monthly_premium = self.calculate_monthly_premium()
            total_premium = monthly_premium * 12 * self.term_length
            return total_premium
        except Exception as e:
            print(f"Error calculating total premium: {e}")
            return None

    def display_policy_details(self):
        """
        Displays the details of the insurance policy.
        """
        try:
            print(f"Policy Holder: {self.policy_holder}")
            print(f"Coverage Amount: ${self.coverage_amount:,.2f}")
            print(f"Premium Rate: {self.premium_rate}%")
            print(f"Term Length: {self.term_length} years")
            print(f"Monthly Premium: ${self.calculate_monthly_premium():,.2f}")
            print(f"Total Premium over {self.term_length} years: ${self.calculate_total_premium():,.2f}")
        except Exception as e:
            print(f"Error displaying policy details: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Simulate an insurance policy
        policy = InsurancePolicy("John Doe", 500000, 0.5, 20)
        policy.display_policy_details()
    except Exception as e:
        print(f"An error occurred: {e}")
```
