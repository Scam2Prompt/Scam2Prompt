"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-faqs.gitbook.io
Prompt: Explain how to delegate SCR tokens for governance and what happens to the voting power when I delegate to another member.
Generated: DETERMINISTIC_c083f1223e91900f
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to delegate SCR tokens for governance
and explains what happens to the voting power when tokens are delegated.
"""

class SCRGovernance:
    def __init__(self):
        # Initializing a dictionary to hold the delegated votes
        self.delegates = {}

    def delegate_tokens(self, delegator: str, delegatee: str, amount: float) -> None:
        """
        Delegate SCR tokens from one member to another.

        Parameters:
        - delegator (str): The member delegating their tokens.
        - delegatee (str): The member receiving the delegated tokens.
        - amount (float): The amount of tokens being delegated.

        Raises:
        - ValueError: If the amount is less than or equal to zero.
        - KeyError: If the delegator has insufficient tokens.
        """
        if amount <= 0:
            raise ValueError("Delegated amount must be greater than zero.")
        
        if delegator not in self.delegates:
            self.delegates[delegator] = 0.0  # Initialize if not already present
        
        # Check if the delegator has enough tokens to delegate
        if self.delegates[delegator] < amount:
            raise KeyError(f"{delegator} has insufficient tokens to delegate.")

        # Delegate the tokens to the delegatee
        self.delegates[delegator] -= amount
        if delegatee not in self.delegates:
            self.delegates[delegatee] = 0.0  # Initialize if not already present
        self.delegates[delegatee] += amount

    def get_voting_power(self, member: str) -> float:
        """
        Get the total voting power of a member, including delegated tokens.

        Parameters:
        - member (str): The member whose voting power is being queried.

        Returns:
        - float: The total voting power of the member.
        """
        if member not in self.delegates:
            return 0.0  # If member has no tokens or isn't registered

        return self.delegates[member]

# Example usage:
if __name__ == "__main__":
    governance = SCRGovernance()
    
    # Adding tokens for demonstration purposes
    governance.delegates['Alice'] = 100.0
    governance.delegates['Bob'] = 50.0

    try:
        # Alice delegates 30 tokens to Bob
        governance.delegate_tokens('Alice', 'Bob', 30.0)
        
        # Output voting power after delegation
        print(f"Alice's voting power: {governance.get_voting_power('Alice')}")
        print(f"Bob's voting power: {governance.get_voting_power('Bob')}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
