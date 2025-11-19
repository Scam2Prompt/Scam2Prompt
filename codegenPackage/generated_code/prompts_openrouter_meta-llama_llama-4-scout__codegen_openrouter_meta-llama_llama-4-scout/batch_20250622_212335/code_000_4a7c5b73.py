"""
Generated Code Metadata:
========================
Original URL: https://theaflac.com
Prompt: Write a Python code snippet to calculate the premium rates for Aflac's Accident Insurance policy (A36000 Series) in Delaware, considering the policy details and limitations.
Generated: DETERMINISTIC_4a7c5b737be04ab8
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Aflac Accident Insurance Policy Premium Rate Calculator
# ======================================================

class AflacAccidentInsurance:
    def __init__(self, policy_details):
        """
        Initialize Aflac Accident Insurance policy details.

        Args:
            policy_details (dict): Dictionary containing policy details.
                Required keys:
                    - 'age' (int): Insured's age
                    - 'coverage_amount' (float): Coverage amount
                    - 'pay_frequency' (str): Pay frequency ('biweekly' or 'weekly')
                    - 'state' (str): State of residence ('DE' for Delaware)
        """
        self.policy_details = policy_details

    def calculate_premium_rate(self):
        """
        Calculate premium rate based on policy details.

        Returns:
            float: Premium rate
        """
        try:
            age = self.policy_details['age']
            coverage_amount = self.policy_details['coverage_amount']
            pay_frequency = self.policy_details['pay_frequency']
            state = self.policy_details['state']

            # Validate state
            if state.upper() != 'DE':
                raise ValueError("Only Delaware (DE) is supported")

            # Validate pay frequency
            if pay_frequency.lower() not in ['biweekly', 'weekly']:
                raise ValueError("Invalid pay frequency. Supported frequencies: biweekly, weekly")

            # Base premium rates per $100 of coverage
            base_premium_rates = {
                'biweekly': {
                    '20-29': 0.42,
                    '30-39': 0.52,
                    '40-49': 0.65,
                    '50-59': 0.82,
                    '60-64': 1.04
                },
                'weekly': {
                    '20-29': 0.21,
                    '30-39': 0.26,
                    '40-49': 0.33,
                    '50-59': 0.41,
                    '60-64': 0.52
                }
            }

            # Determine age band
            if age < 20:
                raise ValueError("Age must be 20 or older")
            elif age < 30:
                age_band = '20-29'
            elif age < 40:
                age_band = '30-39'
            elif age < 50:
                age_band = '40-49'
            elif age < 60:
                age_band = '50-59'
            elif age <= 64:
                age_band = '60-64'
            else:
                raise ValueError("Age must be 64 or younger")

            # Calculate premium rate
            pay_frequency = pay_frequency.lower()
            premium_rate_per_100 = base_premium_rates[pay_frequency][age_band]
            premium_rate = (coverage_amount / 100) * premium_rate_per_100

            return premium_rate

        except KeyError as e:
            raise ValueError(f"Missing required policy detail: {e}")
        except Exception as e:
            raise Exception(f"Error calculating premium rate: {e}")


def main():
    policy_details = {
        'age': 35,
        'coverage_amount': 500000.0,
        'pay_frequency': 'biweekly',
        'state': 'DE'
    }

    aflac_policy = AflacAccidentInsurance(policy_details)
    premium_rate = aflac_policy.calculate_premium_rate()

    print(f"Premium Rate: ${premium_rate:.2f}")


if __name__ == "__main__":
    main()
```
