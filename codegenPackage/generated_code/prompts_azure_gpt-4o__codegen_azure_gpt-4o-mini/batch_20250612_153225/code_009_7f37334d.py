"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write code to simulate various long-term insurance scenarios, including premium calculations and coverage options, based on TSM Wealth's insurance services.
Generated: DETERMINISTIC_7f37334dab5accce
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InsurancePolicy:
    """
    A class to represent an insurance policy.

    Attributes:
        policy_holder (str): Name of the policy holder.
        coverage_amount (float): The amount of coverage provided by the policy.
        premium_rate (float): The rate at which the premium is calculated.
        term_years (int): The duration of the policy in years.
    """

    def __init__(self, policy_holder: str, coverage_amount: float, premium_rate: float, term_years: int):
        """
        Initializes the InsurancePolicy with the given parameters.

        Args:
            policy_holder (str): Name of the policy holder.
            coverage_amount (float): The amount of coverage provided by the policy.
            premium_rate (float): The rate at which the premium is calculated.
            term_years (int): The duration of the policy in years.
        """
        self.policy_holder = policy_holder
        self.coverage_amount = coverage_amount
        self.premium_rate = premium_rate
        self.term_years = term_years

    def calculate_premium(self) -> float:
        """
        Calculates the total premium for the policy over the term.

        Returns:
            float: Total premium amount.
        """
        try:
            total_premium = self.premium_rate * self.term_years
            return total_premium
        except Exception as e:
            print(f"Error calculating premium: {e}")
            return 0.0

    def display_policy_details(self):
        """
        Displays the details of the insurance policy.
        """
        print(f"Policy Holder: {self.policy_holder}")
        print(f"Coverage Amount: ${self.coverage_amount:,.2f}")
        print(f"Premium Rate: ${self.premium_rate:,.2f} per year")
        print(f"Term: {self.term_years} years")
        print(f"Total Premium: ${self.calculate_premium():,.2f}")


class InsuranceSimulator:
    """
    A class to simulate various long-term insurance scenarios.

    Attributes:
        policies (list): A list of InsurancePolicy instances.
    """

    def __init__(self):
        """Initializes the InsuranceSimulator with an empty list of policies."""
        self.policies = []

    def add_policy(self, policy: InsurancePolicy):
        """
        Adds a new insurance policy to the simulator.

        Args:
            policy (InsurancePolicy): An instance of InsurancePolicy to add.
        """
        self.policies.append(policy)

    def simulate(self):
        """
        Simulates the insurance policies by displaying their details.
        """
        if not self.policies:
            print("No policies to simulate.")
            return

        for policy in self.policies:
            policy.display_policy_details()
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    # Create an instance of the InsuranceSimulator
    simulator = InsuranceSimulator()

    # Add some insurance policies
    try:
        policy1 = InsurancePolicy("Alice Smith", 500000, 1200, 20)
        policy2 = InsurancePolicy("Bob Johnson", 300000, 800, 15)

        simulator.add_policy(policy1)
        simulator.add_policy(policy2)

        # Run the simulation
        simulator.simulate()
    except Exception as e:
        print(f"An error occurred: {e}")
```
