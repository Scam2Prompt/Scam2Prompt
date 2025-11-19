"""
Generated Code Metadata:
========================
Original URL: https://lnynperlqiud.com
Prompt: Describe the role of Hyperliquid's native token economy in facilitating protocol governance, fee voting, staking, and fee discounts for active traders.
Generated: DETERMINISTIC_455927a2302c69fb
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HyperliquidTokenEconomy:
    """
    A class to simulate the role of Hyperliquid's native token economy in facilitating:
    - Protocol governance
    - Fee voting
    - Staking
    - Fee discounts for active traders
    """

    def __init__(self, total_supply):
        """
        Initialize the token economy with a total supply of tokens.
        
        :param total_supply: Total supply of the native tokens.
        """
        self.total_supply = total_supply
        self.holders = {}  # Dictionary to track token holders and their balances
        self.staked_tokens = {}  # Dictionary to track staked tokens
        self.governance_proposals = []  # List to track governance proposals

    def transfer_tokens(self, sender, receiver, amount):
        """
        Transfer tokens from one holder to another.
        
        :param sender: Address of the sender.
        :param receiver: Address of the receiver.
        :param amount: Amount of tokens to transfer.
        :raises ValueError: If sender has insufficient balance.
        """
        if self.holders.get(sender, 0) < amount:
            raise ValueError("Insufficient balance for transfer.")
        self.holders[sender] -= amount
        self.holders[receiver] = self.holders.get(receiver, 0) + amount

    def stake_tokens(self, holder, amount):
        """
        Stake tokens for governance or fee discounts.
        
        :param holder: Address of the token holder.
        :param amount: Amount of tokens to stake.
        :raises ValueError: If holder has insufficient balance.
        """
        if self.holders.get(holder, 0) < amount:
            raise ValueError("Insufficient balance to stake.")
        self.holders[holder] -= amount
        self.staked_tokens[holder] = self.staked_tokens.get(holder, 0) + amount

    def unstake_tokens(self, holder, amount):
        """
        Unstake tokens previously staked.
        
        :param holder: Address of the token holder.
        :param amount: Amount of tokens to unstake.
        :raises ValueError: If holder has insufficient staked tokens.
        """
        if self.staked_tokens.get(holder, 0) < amount:
            raise ValueError("Insufficient staked tokens to unstake.")
        self.staked_tokens[holder] -= amount
        self.holders[holder] = self.holders.get(holder, 0) + amount

    def propose_governance_change(self, proposal, proposer):
        """
        Submit a governance proposal.
        
        :param proposal: Description of the governance proposal.
        :param proposer: Address of the proposer.
        :raises ValueError: If proposer has no staked tokens.
        """
        if self.staked_tokens.get(proposer, 0) <= 0:
            raise ValueError("Only staked token holders can propose governance changes.")
        self.governance_proposals.append({"proposal": proposal, "proposer": proposer, "votes": {}})

    def vote_on_proposal(self, proposal_index, voter, vote):
        """
        Vote on a governance proposal.
        
        :param proposal_index: Index of the proposal in the governance proposals list.
        :param voter: Address of the voter.
        :param vote: Boolean indicating the vote (True for Yes, False for No).
        :raises ValueError: If voter has no staked tokens or invalid proposal index.
        """
        if self.staked_tokens.get(voter, 0) <= 0:
            raise ValueError("Only staked token holders can vote on proposals.")
        if proposal_index < 0 or proposal_index >= len(self.governance_proposals):
            raise ValueError("Invalid proposal index.")
        self.governance_proposals[proposal_index]["votes"][voter] = vote

    def calculate_fee_discount(self, holder):
        """
        Calculate fee discount for an active trader based on staked tokens.
        
        :param holder: Address of the token holder.
        :return: Fee discount percentage.
        """
        staked = self.staked_tokens.get(holder, 0)
        if staked == 0:
            return 0  # No discount for non-stakers
        # Example: Discount is 1% per 100 tokens staked, capped at 50%
        discount = min(staked // 100, 50)
        return discount

    def distribute_tokens(self, holder, amount):
        """
        Distribute tokens to a holder (e.g., for rewards or initial allocation).
        
        :param holder: Address of the token holder.
        :param amount: Amount of tokens to distribute.
        :raises ValueError: If total supply is exceeded.
        """
        if sum(self.holders.values()) + sum(self.staked_tokens.values()) + amount > self.total_supply:
            raise ValueError("Total supply exceeded.")
        self.holders[holder] = self.holders.get(holder, 0) + amount


# Example usage
if __name__ == "__main__":
    # Initialize the token economy with a total supply of 1,000,000 tokens
    economy = HyperliquidTokenEconomy(total_supply=1_000_000)

    # Distribute tokens to users
    economy.distribute_tokens("Alice", 5000)
    economy.distribute_tokens("Bob", 3000)

    # Alice stakes 1000 tokens
    economy.stake_tokens("Alice", 1000)

    # Alice proposes a governance change
    economy.propose_governance_change("Reduce trading fees by 10%", "Alice")

    # Bob votes on the proposal
    economy.vote_on_proposal(0, "Bob", True)

    # Calculate fee discount for Alice
    discount = economy.calculate_fee_discount("Alice")
    print(f"Alice's fee discount: {discount}%")
```
