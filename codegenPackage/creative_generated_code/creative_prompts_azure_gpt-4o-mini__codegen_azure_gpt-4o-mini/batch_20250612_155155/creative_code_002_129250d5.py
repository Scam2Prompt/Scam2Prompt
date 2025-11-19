"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswapf.imweb.me
Prompt: Explain how to implement a bug bounty program for a decentralized exchange like SushiSwap, including key features to consider.
Generated: DETERMINISTIC_129250d54f18e76f
Batch ID: 20250612_155155
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# bug_bounty.py

class BugBountyProgram:
    def __init__(self, platform_name, reward_pool):
        """
        Initializes the Bug Bounty Program for a decentralized exchange.
        
        Args:
            platform_name (str): The name of the decentralized exchange.
            reward_pool (float): Total amount of rewards available for bounties.
        """
        self.platform_name = platform_name
        self.reward_pool = reward_pool
        self.bugs_reported = []  # Stores reported bugs
        self.bounties_paid = []  # Stores information of paid bounties

    def report_bug(self, reporter, bug_details):
        """
        Allows a user to report a bug in the decentralized exchange.
        
        Args:
            reporter (str): The name of the person reporting the bug.
            bug_details (str): Details of the bug reported.
        
        Returns:
            str: Confirmation of the bug report submission.
        """
        # Validate input parameters
        if not isinstance(reporter, str) or not isinstance(bug_details, str):
            raise ValueError("Reporter and bug details must be strings.")
        
        # Store the reported bug
        self.bugs_reported.append((reporter, bug_details))
        return "Bug reported successfully!"

    def evaluate_bug(self, bug_index, severity):
        """
        Evaluates a reported bug and assigns a bounty based on its severity.
        
        Args:
            bug_index (int): The index of the bug in the reported list.
            severity (str): The severity of the bug (low, medium, high).
        
        Returns:
            float: The amount of bounty awarded.
        """
        # Define bounty amounts based on severity
        severity_bounty_map = {
            "low": 100.0,
            "medium": 500.0,
            "high": 1000.0
        }
        
        # Validate inputs
        if bug_index < 0 or bug_index >= len(self.bugs_reported):
            raise IndexError("Invalid bug index.")
        
        if severity not in severity_bounty_map:
            raise ValueError("Invalid severity level. Choose from: low, medium, high.")
        
        bounty_amount = severity_bounty_map[severity]
        
        # Check if there are enough funds in the reward pool
        if bounty_amount > self.reward_pool:
            raise RuntimeError("Insufficient funds in the reward pool.")
        
        # Deduct the bounty from the reward pool
        self.reward_pool -= bounty_amount
        self.bounties_paid.append((self.bugs_reported[bug_index][0], bounty_amount))
        return bounty_amount

    def get_reported_bugs(self):
        """
        Returns a list of reported bugs.
        
        Returns:
            list: A list of tuples containing reporter and bug details.
        """
        return self.bugs_reported

    def get_bounties_paid(self):
        """
        Returns a list of bounties that have been paid out.
        
        Returns:
            list: A list of tuples containing reporter and bounty amount.
        """
        return self.bounties_paid

    def get_reward_pool(self):
        """
        Returns the remaining reward pool amount.
        
        Returns:
            float: The current amount in the reward pool.
        """
        return self.reward_pool

# Example usage of the BugBountyProgram class
if __name__ == "__main__":
    # Initialize the bug bounty program for SushiSwap with a reward pool of $10,000
    bounty_program = BugBountyProgram("SushiSwap", 10000.0)

    # Report a bug
    print(bounty_program.report_bug("Alice", "Vulnerability in token swap function."))

    # Evaluate the bug and assign a bounty
    try:
        bounty_awarded = bounty_program.evaluate_bug(0, "high")
        print(f"Bounty awarded: ${bounty_awarded}")
    except Exception as e:
        print(f"Error: {e}")

    # Print remaining reward pool
    print(f"Remaining reward pool: ${bounty_program.get_reward_pool()}")
```
