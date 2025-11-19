"""
Generated Code Metadata:
========================
Original URL: https://hyperlane.cc
Prompt: Describe the security model of Hyperlane, including its modular validator system and customizable security settings for each chain.
Generated: DETERMINISTIC_ba8418b704f6f702
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hyperlane Security Model Implementation

This module implements the security model of Hyperlane, including:
- Modular validator system
- Customizable security settings per chain
- Interchain message verification
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
import hashlib
import json

class HyperlaneSecurityError(Exception):
    """Base exception for Hyperlane security-related errors"""
    pass

class InvalidValidatorSetError(HyperlaneSecurityError):
    """Raised when validator set is invalid"""
    pass

class InsufficientSecurityError(HyperlaneSecurityError):
    """Raised when security requirements aren't met"""
    pass

@dataclass
class Validator:
    """Represents a validator in the Hyperlane network"""
    address: str
    weight: int  # Voting power weight
    metadata: Dict[str, str]  # Additional validator info

@dataclass
class ChainSecurityConfig:
    """Security configuration for a specific chain"""
    threshold: float  # Required threshold for message verification (0-1)
    validator_set: List[Validator]  # Validators for this chain
    max_message_size: int  # Maximum allowed message size in bytes
    required_confirmations: int  # Number of confirmations needed

class HyperlaneSecurityModel:
    """
    Implements Hyperlane's security model with modular validators
    and chain-specific security configurations.
    """
    
    def __init__(self):
        self.chain_configs: Dict[str, ChainSecurityConfig] = {}
    
    def add_chain_config(self, chain_id: str, config: ChainSecurityConfig) -> None:
        """Add or update security configuration for a chain"""
        self._validate_config(config)
        self.chain_configs[chain_id] = config
    
    def _validate_config(self, config: ChainSecurityConfig) -> None:
        """Validate a chain security configuration"""
        if not 0 < config.threshold <= 1:
            raise InvalidValidatorSetError("Threshold must be between 0 and 1")
        
        if not config.validator_set:
            raise InvalidValidatorSetError("Validator set cannot be empty")
        
        total_weight = sum(v.weight for v in config.validator_set)
        if total_weight <= 0:
            raise InvalidValidatorSetError("Total validator weight must be positive")
    
    def verify_message(
        self,
        chain_id: str,
        message: bytes,
        signatures: Dict[str, bytes],
        confirmations: int = 1
    ) -> bool:
        """
        Verify an interchain message against the chain's security requirements.
        
        Args:
            chain_id: Identifier for the destination chain
            message: The message content to verify
            signatures: Dictionary of validator addresses to their signatures
            confirmations: Number of confirmations the message has
            
        Returns:
            bool: True if verification passes, False otherwise
            
        Raises:
            InsufficientSecurityError: If security requirements aren't met
        """
        if chain_id not in self.chain_configs:
            raise InsufficientSecurityError(f"No security config for chain {chain_id}")
        
        config = self.chain_configs[chain_id]
        
        if len(message) > config.max_message_size:
            raise InsufficientSecurityError("Message exceeds maximum size")
        
        if confirmations < config.required_confirmations:
            raise InsufficientSecurityError("Insufficient confirmations")
        
        # Calculate total voting power from signatures
        total_weight = 0
        validators = {v.address: v for v in config.validator_set}
        
        for address, sig in signatures.items():
            if address not in validators:
                continue
            
            # In a real implementation, this would verify the actual signature
            if self._verify_signature(message, sig, address):
                total_weight += validators[address].weight
        
        total_possible_weight = sum(v.weight for v in config.validator_set)
        approval_ratio = total_weight / total_possible_weight
        
        if approval_ratio < config.threshold:
            raise InsufficientSecurityError(
                f"Approval ratio {approval_ratio} below threshold {config.threshold}"
            )
        
        return True
    
    def _verify_signature(self, message: bytes, signature: bytes, address: str) -> bool:
        """
        Verify a message signature (placeholder implementation).
        In production, this would use proper cryptographic verification.
        """
        # This is a simplified placeholder - real implementation would:
        # 1. Hash the message
        # 2. Verify the signature against the validator's public key
        return True
    
    def get_validator_set(self, chain_id: str) -> List[Validator]:
        """Get the validator set for a chain"""
        if chain_id not in self.chain_configs:
            raise InvalidValidatorSetError(f"No validators for chain {chain_id}")
        return self.chain_configs[chain_id].validator_set
    
    def get_security_config(self, chain_id: str) -> ChainSecurityConfig:
        """Get the full security configuration for a chain"""
        if chain_id not in self.chain_configs:
            raise InvalidValidatorSetError(f"No config for chain {chain_id}")
        return self.chain_configs[chain_id]
```
