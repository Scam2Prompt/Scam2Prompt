"""
Generated Code Metadata:
========================
Original URL: https://peaq-token.pages.dev
Prompt: "Explain the role of the PEAQ token in the Economy of Things and its utility in network operations."
Generated: DETERMINISTIC_aafbbc72a71a9145
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
PEAQ Token Utility in Economy of Things (EoT) Network Operations

This module demonstrates the role and utility of the PEAQ token within the Economy of Things ecosystem.
The PEAQ token serves as the native cryptocurrency facilitating transactions, governance, and network operations.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto

class TransactionType(Enum):
    """Types of transactions supported in the EoT network"""
    DEVICE_PAYMENT = auto()
    DATA_PURCHASE = auto()
    SERVICE_FEE = auto()
    GOVERNANCE_VOTE = auto()
    STAKE = auto()

@dataclass
class Transaction:
    """Represents a transaction in the EoT network"""
    sender: str
    receiver: str
    amount: float
    transaction_type: TransactionType
    timestamp: float
    metadata: Optional[Dict] = None

class PEAQToken:
    """
    PEAQ Token implementation showcasing its utility in the Economy of Things network.
    
    Attributes:
        total_supply (float): Total PEAQ tokens in circulation
        balances (Dict[str, float]): Account balances
        staked_tokens (Dict[str, float]): Staked tokens for network security
        transaction_history (List[Transaction]): Record of all transactions
    """
    
    def __init__(self, initial_supply: float):
        self.total_supply = initial_supply
        self.balances: Dict[str, float] = {}
        self.staked_tokens: Dict[str, float] = {}
        self.transaction_history: List[Transaction] = []
        
    def transfer(self, sender: str, receiver: str, amount: float, 
                 transaction_type: TransactionType, metadata: Optional[Dict] = None) -> bool:
        """
        Transfer PEAQ tokens between accounts.
        
        Args:
            sender: Address of sender
            receiver: Address of receiver
            amount: Amount to transfer
            transaction_type: Type of transaction
            metadata: Optional transaction metadata
            
        Returns:
            bool: True if transfer succeeded, False otherwise
        """
        if sender not in self.balances or self.balances[sender] < amount:
            return False
            
        self.balances[sender] -= amount
        self.balances[receiver] = self.balances.get(receiver, 0) + amount
        
        transaction = Transaction(
            sender=sender,
            receiver=receiver,
            amount=amount,
            transaction_type=transaction_type,
            timestamp=time.time(),
            metadata=metadata
        )
        self.transaction_history.append(transaction)
        return True
    
    def stake_tokens(self, account: str, amount: float) -> bool:
        """
        Stake PEAQ tokens to participate in network consensus.
        
        Args:
            account: Account staking tokens
            amount: Amount to stake
            
        Returns:
            bool: True if staking succeeded, False otherwise
        """
        if account not in self.balances or self.balances[account] < amount:
            return False
            
        self.balances[account] -= amount
        self.staked_tokens[account] = self.staked_tokens.get(account, 0) + amount
        return True
    
    def unstake_tokens(self, account: str, amount: float) -> bool:
        """
        Unstake PEAQ tokens.
        
        Args:
            account: Account unstaking tokens
            amount: Amount to unstake
            
        Returns:
            bool: True if unstaking succeeded, False otherwise
        """
        if account not in self.staked_tokens or self.staked_tokens[account] < amount:
            return False
            
        self.staked_tokens[account] -= amount
        self.balances[account] = self.balances.get(account, 0) + amount
        return True
    
    def calculate_rewards(self, account: str, reward_rate: float) -> float:
        """
        Calculate staking rewards for an account.
        
        Args:
            account: Account to calculate rewards for
            reward_rate: Annual reward rate
            
        Returns:
            float: Calculated rewards
        """
        staked_amount = self.staked_tokens.get(account, 0)
        return staked_amount * reward_rate
    
    def vote_on_proposal(self, voter: str, proposal_id: str, vote_amount: float) -> bool:
        """
        Use PEAQ tokens to vote on governance proposals.
        
        Args:
            voter: Account voting
            proposal_id: ID of proposal being voted on
            vote_amount: Voting power (based on token balance)
            
        Returns:
            bool: True if vote succeeded, False otherwise
        """
        if voter not in self.balances or self.balances[voter] < vote_amount:
            return False
            
        # In a real implementation, this would record the vote
        return True
    
    def pay_for_service(self, payer: str, service_provider: str, amount: float) -> bool:
        """
        Pay for services in the EoT network using PEAQ tokens.
        
        Args:
            payer: Account paying for service
            service_provider: Service provider account
            amount: Payment amount
            
        Returns:
            bool: True if payment succeeded, False otherwise
        """
        return self.transfer(
            sender=payer,
            receiver=service_provider,
            amount=amount,
            transaction_type=TransactionType.SERVICE_FEE
        )

# Example usage
if __name__ == "__main__":
    import time
    
    # Initialize token with 1,000,000 PEAQ
    peaq = PEAQToken(initial_supply=1_000_000)
    
    # Distribute initial tokens
    peaq.balances = {
        "device1": 1000,
        "device2": 1000,
        "service_provider": 5000,
        "data_buyer": 2000
    }
    
    # Demonstrate transactions
    peaq.transfer(
        sender="data_buyer",
        receiver="service_provider",
        amount=100,
        transaction_type=TransactionType.DATA_PURCHASE,
        metadata={"data_type": "sensor_data", "quantity": 10}
    )
    
    # Demonstrate staking
    peaq.stake_tokens(account="device1", amount=500)
    
    # Demonstrate voting
    peaq.vote_on_proposal(
        voter="device2",
        proposal_id="network_upgrade_1",
        vote_amount=200
    )
```
