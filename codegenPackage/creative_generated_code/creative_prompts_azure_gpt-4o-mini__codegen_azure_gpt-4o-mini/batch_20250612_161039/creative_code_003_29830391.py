"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Explain how to set up a bug bounty program using the resources mentioned in Karl Franklyn Aparece's blog, focusing on HackerOne and Bugcrowd.
Generated: DETERMINISTIC_29830391478d8a54
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BugBountyProgram:
    """
    A class to manage the setup of a bug bounty program using HackerOne and Bugcrowd.
    """

    def __init__(self, platform):
        """
        Initializes the BugBountyProgram with a specific platform.

        Parameters:
        platform (str): The platform to be used for the bug bounty program (HackerOne/Bugcrowd).
        """
        self.platform = platform.lower()
        self.valid_platforms = ['hackerone', 'bugcrowd']

        # Validate the platform
        if self.platform not in self.valid_platforms:
            raise ValueError(f"Invalid platform. Choose from: {self.valid_platforms}")

    def create_program(self, program_name, description, rewards):
        """
        Sets up a new bug bounty program.

        Parameters:
        program_name (str): Name of the bug bounty program.
        description (str): Description of the program.
        rewards (dict): A dictionary detailing the rewards for different types of vulnerabilities.

        Returns:
        dict: A summary of the created program.

        Raises:
        ValueError: If any required parameter is missing or rewards are improperly defined.
        """
        if not program_name or not description or not rewards:
            raise ValueError("Program name, description, and rewards are required.")

        # Validate rewards structure
        if not isinstance(rewards, dict):
            raise ValueError("Rewards should be a dictionary with vulnerability types as keys.")

        # Example of structure for rewards: {'Critical': 500, 'High': 300, 'Medium': 100, 'Low': 50}
        for severity, amount in rewards.items():
            if not isinstance(amount, (int, float)) or amount < 0:
                raise ValueError(f"Invalid reward amount for {severity}: {amount}")

        # Create program summary
        program_summary = {
            'platform': self.platform,
            'program_name': program_name,
            'description': description,
            'rewards': rewards,
            'status': 'Created'
        }
        
        # Here, you would typically call the platform's API to create the program.
        # For now, we just return the summary for demonstration purposes.
        return program_summary

    def run(self):
        """
        Runs the setup process for a bug bounty program.
        
        Example Setup:
        - Platform: HackerOne
        - Program Name: Internal Security Program
        - Description: A program to identify vulnerabilities in our internal applications.
        - Rewards: {'Critical': 500, 'High': 300, 'Medium': 100, 'Low': 50}

        Returns:
        dict: The summary of the created bug bounty program.
        """
        try:
            program_name = "Internal Security Program"
            description = "A program to identify vulnerabilities in our internal applications."
            rewards = {
                'Critical': 500,
                'High': 300,
                'Medium': 100,
                'Low': 50
            }
            return self.create_program(program_name, description, rewards)
        except (ValueError, Exception) as e:
            print(f"Error occurred while setting up the bug bounty program: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    try:
        bug_bounty = BugBountyProgram("HackerOne")
        program_details = bug_bounty.run()
        if program_details:
            print("Bug Bounty Program Created Successfully:")
            print(program_details)
    except Exception as e:
        print(f"Failed to set up the bug bounty program: {e}")
```
