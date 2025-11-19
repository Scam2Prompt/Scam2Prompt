"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: Create a sample insurance policy quoting tool that incorporates features highlighted by Tempus, such as life, auto, and health insurance options.
Generated: DETERMINISTIC_446ec07260fd3234
Batch ID: 20250612_163156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InsurancePolicy:
    """Class to represent an insurance policy with various options."""
    
    def __init__(self, policy_type, coverage_amount, premium):
        """
        Initialize an insurance policy.

        Args:
            policy_type (str): Type of insurance (life, auto, health).
            coverage_amount (float): Amount of coverage for the policy.
            premium (float): Monthly premium for the policy.
        """
        self.policy_type = policy_type
        self.coverage_amount = coverage_amount
        self.premium = premium

    def to_dict(self):
        """Convert the policy to a dictionary for easy serialization."""
        return {
            'policy_type': self.policy_type,
            'coverage_amount': self.coverage_amount,
            'premium': self.premium
        }

class QuotingTool:
    """Class to handle insurance policy quoting."""
    
    def __init__(self):
        """Initialize the quoting tool with available options."""
        self.policies = []

    def add_policy(self, policy):
        """
        Add a new insurance policy to the quoting tool.

        Args:
            policy (InsurancePolicy): The insurance policy to add.
        """
        if not isinstance(policy, InsurancePolicy):
            raise ValueError("Invalid policy type. Must be an instance of InsurancePolicy.")
        self.policies.append(policy)

    def generate_quote(self):
        """Generate a quote for all added policies."""
        if not self.policies:
            raise ValueError("No policies available to generate a quote.")
        
        quotes = [policy.to_dict() for policy in self.policies]
        return json.dumps(quotes, indent=4)

def main():
    """Main function to demonstrate the quoting tool."""
    try:
        # Create an instance of the quoting tool
        quoting_tool = QuotingTool()

        # Add various insurance policies
        quoting_tool.add_policy(InsurancePolicy("life", 100000, 150))
        quoting_tool.add_policy(InsurancePolicy("auto", 25000, 100))
        quoting_tool.add_policy(InsurancePolicy("health", 50000, 200))

        # Generate and print the quote
        quote = quoting_tool.generate_quote()
        print("Insurance Policy Quotes:")
        print(quote)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
