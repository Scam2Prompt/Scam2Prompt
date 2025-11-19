"""
Generated Code Metadata:
========================
Original URL: https://scroll-faqs.gitbook.io
Prompt: Explain how to delegate SCR tokens for governance and what happens to the voting power when I delegate to another member.
Generated: DETERMINISTIC_c083f1223e91900f
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto

class GovernanceError(Exception):
    """Base class for governance-related errors."""
    pass

class InvalidDelegationError(GovernanceError):
    """Raised when delegation is invalid."""
    pass

class TokenStatus(Enum):
    """Represents the status of SCR tokens."""
    ACTIVE = auto()
    LOCKED = auto()
    BURNED = auto()

@dataclass
class TokenHolder:
    """Represents a holder of SCR tokens."""
    address: str
    balance: int
    status: TokenStatus
    delegated_to: Optional[str] = None
    voting_power: int = 0

class GovernanceContract:
    """Smart contract for SCR token governance."""
    
    def __init__(self):
        self.holders: Dict[str, TokenHolder] = {}
        
    def register_holder(self, address: str, initial_balance: int) -> None:
        """Register a new token holder."""
        if address in self.holders:
            raise GovernanceError(f"Holder {address} already registered")
        self.holders[address] = TokenHolder(
            address=address,
            balance=initial_balance,
            status=TokenStatus.ACTIVE
        )
        self._update_voting_power(address)
        
    def delegate_tokens(self, delegator: str, delegatee: str) -> None:
        """
        Delegate voting power to another address.
        
        Args:
            delegator: Address of the token holder delegating their voting power
            delegatee: Address receiving the delegated voting power
            
        Raises:
            InvalidDelegationError: If delegation is not possible
        """
        if delegator not in self.holders:
            raise InvalidDelegationError(f"Delegator {delegator} not found")
        if delegatee not in self.holders:
            raise InvalidDelegationError(f"Delegatee {delegatee} not found")
        if delegator == delegatee:
            raise InvalidDelegationError("Cannot delegate to self")
        if self.holders[delegator].status != TokenStatus.ACTIVE:
            raise InvalidDelegationError("Only active tokens can be delegated")
            
        # Clear previous delegation if exists
        if self.holders[delegator].delegated_to:
            previous_delegatee = self.holders[delegator].delegated_to
            self.holders[previous_delegatee].voting_power -= self.holders[delegator].balance
            
        # Set new delegation
        self.holders[delegator].delegated_to = delegatee
        self.holders[delegatee].voting_power += self.holders[delegator].balance
        
    def _update_voting_power(self, address: str) -> None:
        """Update voting power for a holder and their delegates."""
        holder = self.holders[address]
        
        if holder.delegated_to:
            # If holder has delegated, their voting power is zero
            holder.voting_power = 0
            # Update delegatee's voting power
            self.holders[holder.delegated_to].voting_power += holder.balance
        else:
            # If not delegated, voting power equals balance
            holder.voting_power = holder.balance
            
    def get_voting_power(self, address: str) -> int:
        """Get current voting power for an address."""
        if address not in self.holders:
            raise GovernanceError(f"Address {address} not found")
        return self.holders[address].voting_power
    
    def revoke_delegation(self, delegator: str) -> None:
        """Revoke an existing delegation."""
        if delegator not in self.holders:
            raise GovernanceError(f"Delegator {delegator} not found")
            
        if not self.holders[delegator].delegated_to:
            raise InvalidDelegationError(f"No active delegation for {delegator}")
            
        delegatee = self.holders[delegator].delegated_to
        self.holders[delegatee].voting_power -= self.holders[delegator].balance
        self.holders[delegator].delegated_to = None
        self.holders[delegator].voting_power = self.holders[delegator].balance
```
