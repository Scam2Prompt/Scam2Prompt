"""
Generated Code Metadata:
========================
Original URL: https://algorewards.com
Prompt: Design a voting system using the Algorand Governance API that allows users to vote on proposals and earn rewards for participating in the governance process.
Generated: DETERMINISTIC_55316f5c0582c6ad
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future import transaction
from typing import Dict, List, Optional, Tuple

# Configuration
ALGOD_TOKEN = "YOUR_ALGOD_TOKEN"
ALGOD_ADDRESS = "YOUR_ALGOD_ADDRESS"
GOVERNANCE_APP_ID = 0  # Replace with actual governance app ID
VOTE_TOKEN_ASSET_ID = 0  # Replace with actual vote token asset ID
REWARD_ASSET_ID = 0  # Replace with actual reward asset ID

# Initialize Algod client
algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

class VotingSystem:
    def __init__(self):
        self.proposals: Dict[int, Dict] = {}
        self.voters: Dict[str, Dict] = {}

    def create_proposal(self, creator_mnemonic: str, title: str, description: str, options: List[str]) -> int:
        """
        Create a new governance proposal.
        
        Args:
            creator_mnemonic: Mnemonic of proposal creator
            title: Proposal title
            description: Proposal description
            options: List of voting options
            
        Returns:
            Proposal ID
        """
        try:
            private_key = mnemonic.to_private_key(creator_mnemonic)
            sender = account.address_from_private_key(private_key)
            
            # In a real implementation, this would create an on-chain proposal
            proposal_id = len(self.proposals) + 1
            self.proposals[proposal_id] = {
                'id': proposal_id,
                'title': title,
                'description': description,
                'options': options,
                'votes': {option: 0 for option in options},
                'creator': sender,
                'status': 'active'
            }
            
            return proposal_id
        except Exception as e:
            raise Exception(f"Failed to create proposal: {str(e)}")

    def cast_vote(self, voter_mnemonic: str, proposal_id: int, option: str) -> str:
        """
        Cast a vote on a proposal.
        
        Args:
            voter_mnemonic: Mnemonic of voter
            proposal_id: ID of proposal to vote on
            option: Selected voting option
            
        Returns:
            Transaction ID
        """
        try:
            if proposal_id not in self.proposals:
                raise ValueError("Proposal does not exist")
                
            if option not in self.proposals[proposal_id]['options']:
                raise ValueError("Invalid voting option")
                
            private_key = mnemonic.to_private_key(voter_mnemonic)
            sender = account.address_from_private_key(private_key)
            
            # Check if voter has voting tokens
            account_info = algod_client.account_info(sender)
            has_vote_token = any(
                asset['asset-id'] == VOTE_TOKEN_ASSET_ID 
                for asset in account_info.get('assets', [])
            )
            
            if not has_vote_token:
                raise ValueError("Voter does not hold voting tokens")
                
            # Record vote (in real implementation, this would be an on-chain transaction)
            self.proposals[proposal_id]['votes'][option] += 1
            
            # Track voter participation
            if sender not in self.voters:
                self.voters[sender] = {'votes': 0, 'rewards_claimed': False}
            self.voters[sender]['votes'] += 1
            
            # Simulate transaction ID
            return "simulated_tx_id"
        except Exception as e:
            raise Exception(f"Failed to cast vote: {str(e)}")

    def distribute_rewards(self, admin_mnemonic: str) -> Dict[str, str]:
        """
        Distribute rewards to eligible voters.
        
        Args:
            admin_mnemonic: Mnemonic of admin distributing rewards
            
        Returns:
            Dictionary of reward transactions
        """
        try:
            private_key = mnemonic.to_private_key(admin_mnemonic)
            sender = account.address_from_private_key(private_key)
            
            reward_txs = {}
            
            for voter_address, voter_data in self.voters.items():
                if voter_data['votes'] > 0 and not voter_data['rewards_claimed']:
                    # In real implementation, this would send reward tokens
                    # For simulation, we just record the action
                    reward_txs[voter_address] = f"reward_{voter_address}"
                    self.voters[voter_address]['rewards_claimed'] = True
            
            return reward_txs
        except Exception as e:
            raise Exception(f"Failed to distribute rewards: {str(e)}")

    def get_proposal(self, proposal_id: int) -> Optional[Dict]:
        """
        Get proposal details.
        
        Args:
            proposal_id: ID of proposal to retrieve
            
        Returns:
            Proposal details or None if not found
        """
        return self.proposals.get(proposal_id)

    def get_voter_info(self, voter_address: str) -> Optional[Dict]:
        """
        Get voter participation information.
        
        Args:
            voter_address: Address of voter
            
        Returns:
            Voter information or None if not found
        """
        return self.voters.get(voter_address)

# Example usage
if __name__ == "__main__":
    voting_system = VotingSystem()
    
    # Admin creates a proposal
    admin_mnemonic = "your admin mnemonic here"
    proposal_id = voting_system.create_proposal(
        admin_mnemonic,
        "Protocol Upgrade",
        "Proposal to upgrade protocol to version 2.0",
        ["Yes", "No", "Abstain"]
    )
    
    # Voters cast votes
    voter1_mnemonic = "voter 1 mnemonic here"
    voter2_mnemonic = "voter 2 mnemonic here"
    
    try:
        voting_system.cast_vote(voter1_mnemonic, proposal_id, "Yes")
        voting_system.cast_vote(voter2_mnemonic, proposal_id, "No")
    except Exception as e:
        print(f"Voting failed: {str(e)}")
    
    # Distribute rewards
    rewards = voting_system.distribute_rewards(admin_mnemonic)
    print(f"Rewards distributed: {rewards}")
    
    # Get proposal results
    proposal = voting_system.get_proposal(proposal_id)
    print(f"Proposal results: {proposal['votes']}")
```
