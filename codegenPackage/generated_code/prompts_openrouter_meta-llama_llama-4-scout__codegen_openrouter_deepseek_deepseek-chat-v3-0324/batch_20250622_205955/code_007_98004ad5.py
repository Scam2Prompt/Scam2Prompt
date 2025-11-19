"""
Generated Code Metadata:
========================
Original URL: https://nepmigration.pages.dev
Prompt: Explain how Neo's on-chain governance model works and how GAS rewards are distributed to voters and committee members.
Generated: DETERMINISTIC_98004ad59b514f57
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that demonstrates Neo's on-chain governance model and GAS reward distribution through a simplified simulation:

```python
class NeoGovernanceModel:
    """
    A simplified simulation of Neo's on-chain governance model and GAS distribution.
    """
    
    def __init__(self):
        self.committee_members = []
        self.voters = {}
        self.total_staked_neo = 0
        self.total_gas_generated = 0
        self.current_block_height = 0
        
    def add_committee_member(self, address, staked_neo):
        """
        Add a committee member with their staked NEO amount.
        
        Args:
            address (str): Committee member's address
            staked_neo (float): Amount of NEO staked by this member
        """
        self.committee_members.append({
            'address': address,
            'staked_neo': staked_neo,
            'votes_received': 0
        })
        self.total_staked_neo += staked_neo
        
    def add_voter(self, address, staked_neo, voted_member=None):
        """
        Add a voter with their staked NEO and optional vote.
        
        Args:
            address (str): Voter's address
            staked_neo (float): Amount of NEO staked by this voter
            voted_member (str, optional): Address of committee member voted for
        """
        self.voters[address] = {
            'staked_neo': staked_neo,
            'voted_member': voted_member
        }
        self.total_staked_neo += staked_neo
        
        if voted_member:
            self._add_vote_to_member(voted_member, staked_neo)
            
    def _add_vote_to_member(self, member_address, vote_weight):
        """
        Internal method to add votes to a committee member.
        
        Args:
            member_address (str): Committee member's address
            vote_weight (float): Voting power to add
        """
        for member in self.committee_members:
            if member['address'] == member_address:
                member['votes_received'] += vote_weight
                break
                
    def generate_gas(self, amount):
        """
        Simulate GAS generation for distribution.
        
        Args:
            amount (float): Amount of GAS generated in this period
        """
        self.total_gas_generated += amount
        
    def distribute_gas_rewards(self):
        """
        Distribute GAS rewards to voters and committee members.
        
        Returns:
            dict: Dictionary of rewards distributed
        """
        if self.total_staked_neo == 0:
            return {}
            
        total_rewards = self.total_gas_generated
        voter_rewards = total_rewards * 0.8  # 80% to voters
        committee_rewards = total_rewards * 0.2  # 20% to committee
        
        voter_distribution = {}
        committee_distribution = {}
        
        # Distribute to voters based on stake and vote weight
        for voter_addr, voter_data in self.voters.items():
            if voter_data['voted_member']:
                stake_ratio = voter_data['staked_neo'] / self.total_staked_neo
                voter_distribution[voter_addr] = voter_rewards * stake_ratio
                
        # Distribute to committee members based on votes received
        total_votes = sum(m['votes_received'] for m in self.committee_members)
        if total_votes > 0:
            for member in self.committee_members:
                vote_ratio = member['votes_received'] / total_votes
                committee_distribution[member['address']] = committee_rewards * vote_ratio
                
        # Reset gas for next period
        self.total_gas_generated = 0
        
        return {
            'voter_rewards': voter_distribution,
            'committee_rewards': committee_distribution
        }
        
    def vote(self, voter_address, committee_member_address):
        """
        Simulate a voter casting a vote for a committee member.
        
        Args:
            voter_address (str): Address of the voter
            committee_member_address (str): Address of committee member being voted for
        """
        if voter_address not in self.voters:
            raise ValueError("Voter not registered")
            
        # Remove previous vote weight if exists
        prev_vote = self.voters[voter_address]['voted_member']
        if prev_vote:
            self._add_vote_to_member(prev_vote, -self.voters[voter_address]['staked_neo'])
            
        # Add new vote
        self.voters[voter_address]['voted_member'] = committee_member_address
        self._add_vote_to_member(committee_member_address, self.voters[voter_address]['staked_neo'])


# Example usage
if __name__ == "__main__":
    governance = NeoGovernanceModel()
    
    # Add committee members
    governance.add_committee_member("committee1", 1000)
    governance.add_committee_member("committee2", 1500)
    
    # Add voters
    governance.add_voter("voter1", 500, "committee1")
    governance.add_voter("voter2", 750, "committee2")
    governance.add_voter("voter3", 300, "committee1")
    
    # Simulate GAS generation
    governance.generate_gas(100)
    
    # Distribute rewards
    rewards = governance.distribute_gas_rewards()
    print("Rewards distributed:", rewards)
    
    # Simulate voting change
    governance.vote("voter1", "committee2")
    governance.generate_gas(100)
    new_rewards = governance.distribute_gas_rewards()
    print("New rewards after vote change:", new_rewards)
```
