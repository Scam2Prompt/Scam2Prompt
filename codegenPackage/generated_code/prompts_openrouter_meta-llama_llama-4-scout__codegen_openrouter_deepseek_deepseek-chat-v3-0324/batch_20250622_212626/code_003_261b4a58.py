"""
Generated Code Metadata:
========================
Original URL: https://sophan.xyz
Prompt: Explain the role of Sophon Nodes and Guardian Memberships in securing and powering the Sophon network, and how they relate to the SOPH token.
Generated: DETERMINISTIC_261b4a58455e6b3b
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sophon_network.py

class SophonNode:
    """
    Represents a Sophon Node in the Sophon network.
    Responsible for validating transactions, maintaining consensus, and securing the network.
    """
    
    def __init__(self, node_id: str, stake_amount: int):
        """
        Initialize a Sophon Node.
        
        Args:
            node_id: Unique identifier for the node
            stake_amount: Amount of SOPH tokens staked by this node
        """
        self.node_id = node_id
        self.stake_amount = stake_amount
        self.is_active = True
        self.reputation_score = 100  # Initial reputation score
        
    def validate_transaction(self, transaction: dict) -> bool:
        """
        Validate a transaction according to network rules.
        
        Args:
            transaction: Transaction data to validate
            
        Returns:
            bool: True if transaction is valid, False otherwise
        """
        try:
            # Basic validation checks
            required_fields = {'sender', 'receiver', 'amount', 'timestamp', 'signature'}
            if not all(field in transaction for field in required_fields):
                return False
                
            if transaction['amount'] <= 0:
                return False
                
            # Additional validation logic would go here
            return True
            
        except Exception as e:
            print(f"Transaction validation error: {e}")
            return False
            
    def participate_in_consensus(self, block_data: dict) -> bool:
        """
        Participate in the network's consensus mechanism.
        
        Args:
            block_data: Proposed block data for consensus
            
        Returns:
            bool: True if consensus is reached, False otherwise
        """
        # Consensus logic would be implemented here
        # This is a simplified version
        return True
        
    def update_reputation(self, success: bool):
        """
        Update the node's reputation score based on performance.
        
        Args:
            success: Whether the node's last action was successful
        """
        if success:
            self.reputation_score = min(100, self.reputation_score + 1)
        else:
            self.reputation_score = max(0, self.reputation_score - 5)
            
    def get_rewards(self) -> float:
        """
        Calculate and return rewards earned by this node.
        
        Returns:
            float: Amount of SOPH tokens earned as rewards
        """
        # Reward calculation based on stake amount and reputation
        base_reward = self.stake_amount * 0.01
        reputation_bonus = base_reward * (self.reputation_score / 100)
        return base_reward + reputation_bonus


class GuardianMembership:
    """
    Represents a Guardian membership in the Sophon network.
    Guardians provide additional security and governance capabilities.
    """
    
    def __init__(self, member_id: str, locked_soph: int):
        """
        Initialize a Guardian membership.
        
        Args:
            member_id: Unique identifier for the guardian
            locked_soph: Amount of SOPH tokens locked for guardianship
        """
        self.member_id = member_id
        self.locked_soph = locked_soph
        self.voting_power = self.calculate_voting_power()
        self.is_active = True
        
    def calculate_voting_power(self) -> int:
        """
        Calculate the guardian's voting power based on locked SOPH.
        
        Returns:
            int: Voting power value
        """
        # Voting power increases logarithmically with locked SOPH
        import math
        return int(math.log(self.locked_soph) * 100) if self.locked_soph > 0 else 0
        
    def vote_on_proposal(self, proposal_id: str, vote: bool) -> bool:
        """
        Vote on a network proposal.
        
        Args:
            proposal_id: ID of the proposal being voted on
            vote: True for yes, False for no
            
        Returns:
            bool: True if vote was successfully cast
        """
        # Voting logic would be implemented here
        return True
        
    def get_governance_rewards(self) -> float:
        """
        Calculate and return governance rewards earned.
        
        Returns:
            float: Amount of SOPH tokens earned as governance rewards
        """
        # Reward calculation based on locked SOPH and participation
        return self.locked_soph * 0.005


class SophonNetwork:
    """
    Main class representing the Sophon network and its operations.
    """
    
    def __init__(self):
        self.nodes = {}  # node_id: SophonNode
        self.guardians = {}  # member_id: GuardianMembership
        self.total_staked = 0
        self.total_locked = 0
        
    def register_node(self, node_id: str, stake_amount: int) -> bool:
        """
        Register a new Sophon Node.
        
        Args:
            node_id: Unique identifier for the node
            stake_amount: Amount of SOPH tokens to stake
            
        Returns:
            bool: True if registration was successful
        """
        if node_id in self.nodes:
            print(f"Node {node_id} already exists")
            return False
            
        if stake_amount <= 0:
            print("Stake amount must be positive")
            return False
            
        self.nodes[node_id] = SophonNode(node_id, stake_amount)
        self.total_staked += stake_amount
        return True
        
    def register_guardian(self, member_id: str, locked_soph: int) -> bool:
        """
        Register a new Guardian membership.
        
        Args:
            member_id: Unique identifier for the guardian
            locked_soph: Amount of SOPH tokens to lock
            
        Returns:
            bool: True if registration was successful
        """
        if member_id in self.guardians:
            print(f"Guardian {member_id} already exists")
            return False
            
        if locked_soph <= 0:
            print("Locked SOPH amount must be positive")
            return False
            
        self.guardians[member_id] = GuardianMembership(member_id, locked_soph)
        self.total_locked += locked_soph
        return True
        
    def distribute_rewards(self) -> dict:
        """
        Distribute rewards to all active nodes and guardians.
        
        Returns:
            dict: Dictionary containing total rewards distributed
        """
        node_rewards = 0.0
        guardian_rewards = 0.0
        
        for node in self.nodes.values():
            if node.is_active:
                reward = node.get_rewards()
                node_rewards += reward
                
        for guardian in self.guardians.values():
            if guardian.is_active:
                reward = guardian.get_governance_rewards()
                guardian_rewards += reward
                
        return {
            'total_node_rewards': node_rewards,
            'total_guardian_rewards': guardian_rewards,
            'total_rewards': node_rewards + guardian_rewards
        }
        
    def get_network_security_score(self) -> float:
        """
        Calculate a security score for the network based on staked/locked SOPH.
        
        Returns:
            float: Network security score (0-100)
        """
        total_value = self.total_staked + self.total_locked
        if total_value == 0:
            return 0.0
            
        # Simplified security score calculation
        return min(100.0, (total_value / 1000000) * 10)  # Assuming 1M SOPH = 10 points
```
