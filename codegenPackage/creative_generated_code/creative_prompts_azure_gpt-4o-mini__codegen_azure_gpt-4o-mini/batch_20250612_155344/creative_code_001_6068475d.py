"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sitemaps.worldlibertyyfinancial.com
Prompt: What are the best practices for creating a privacy policy for a financial services API?
Generated: DETERMINISTIC_6068475d593bf78d
Batch ID: 20250612_155344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrivacyPolicy:
    """
    A class to represent a privacy policy for a financial services API.
    """

    def __init__(self, company_name, api_name):
        """
        Initializes the PrivacyPolicy with the name of the company and the API.

        Args:
            company_name (str): The name of the company.
            api_name (str): The name of the API.
        """
        self.company_name = company_name
        self.api_name = api_name
        self.policies = []

    def add_policy(self, policy):
        """
        Adds a new policy to the privacy policy list.

        Args:
            policy (str): A description of the policy.

        Raises:
            ValueError: If the policy is empty.
        """
        if not policy.strip():
            raise ValueError("Policy description cannot be empty.")
        self.policies.append(policy)

    def remove_policy(self, policy):
        """
        Removes a policy from the privacy policy list.

        Args:
            policy (str): The policy to remove.

        Raises:
            ValueError: If the policy is not found in the list.
        """
        try:
            self.policies.remove(policy)
        except ValueError:
            raise ValueError("Policy not found in the list.")

    def display_policy(self):
        """
        Displays the privacy policy.

        Returns:
            str: A formatted string containing the company and API name along with the policies.
        """
        policy_text = f"Privacy Policy for {self.company_name} - {self.api_name}\n"
        policy_text += "=" * (len(policy_text) - 1) + "\n"
        if self.policies:
            for index, policy in enumerate(self.policies, start=1):
                policy_text += f"{index}. {policy}\n"
        else:
            policy_text += "No policies added yet.\n"
        return policy_text


# Example usage:
if __name__ == "__main__":
    try:
        # Create a new privacy policy instance
        privacy_policy = PrivacyPolicy("Example Corp", "Example API")

        # Add policies
        privacy_policy.add_policy("We collect user data to provide better services.")
        privacy_policy.add_policy("User data is stored securely with encryption.")
        privacy_policy.add_policy("Users have the right to access their data at any time.")

        # Display the current privacy policy
        print(privacy_policy.display_policy())

        # Remove a policy
        privacy_policy.remove_policy("Users have the right to access their data at any time.")

        # Display the updated privacy policy
        print(privacy_policy.display_policy())

    except ValueError as e:
        print(f"Error: {e}")
```
