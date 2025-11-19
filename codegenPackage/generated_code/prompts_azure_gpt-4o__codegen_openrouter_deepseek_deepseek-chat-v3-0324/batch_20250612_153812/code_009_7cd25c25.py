"""
Generated Code Metadata:
========================
Original URL: https://register-doublezero.com
Prompt: Write code to implement a crypto-economic security guarantee system for a decentralized network using DoubleZero's physical infrastructure layer principles.
Generated: DETERMINISTIC_7cd25c2547b145f5
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import time
from enum import Enum, auto
import random

class SecurityLevel(Enum):
    """Enum representing different security levels for infrastructure nodes."""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

@dataclass
class Node:
    """Represents a physical infrastructure node in the network."""
    node_id: str
    security_level: SecurityLevel
    stake_amount: float
    last_active: float
    is_active: bool = True

    def verify_activity(self) -> bool:
        """Check if node is still active based on last activity time."""
        current_time = time.time()
        max_inactive_time = {
            SecurityLevel.LOW: 300,    # 5 minutes
            SecurityLevel.MEDIUM: 600, # 10 minutes
            SecurityLevel.HIGH: 1800   # 30 minutes
        }.get(self.security_level, 300)
        
        self.is_active = (current_time - self.last_active) <= max_inactive_time
        return self.is_active

class SecurityGuaranteeSystem:
    """Implements crypto-economic security guarantees for a decentralized network."""
    
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.slashing_conditions: Dict[str, float] = {
            "inactivity": 0.01,    # 1% of stake for inactivity
            "misbehavior": 0.05,   # 5% of stake for misbehavior
            "security_breach": 0.1 # 10% of stake for security breach
        }
        self.reward_rates: Dict[SecurityLevel, float] = {
            SecurityLevel.LOW: 0.05,
            SecurityLevel.MEDIUM: 0.08,
            SecurityLevel.HIGH: 0.12
        }
    
    def register_node(self, node_id: str, security_level: SecurityLevel, stake_amount: float) -> bool:
        """Register a new node with the security system."""
        if node_id in self.nodes:
            return False
        
        self.nodes[node_id] = Node(
            node_id=node_id,
            security_level=security_level,
            stake_amount=stake_amount,
            last_active=time.time()
        )
        return True
    
    def update_node_activity(self, node_id: str) -> bool:
        """Update a node's last active timestamp."""
        if node_id not in self.nodes:
            return False
        
        self.nodes[node_id].last_active = time.time()
        return True
    
    def verify_network_security(self) -> Tuple[int, int]:
        """Verify all nodes' activity and return active/inactive counts."""
        active = 0
        inactive = 0
        
        for node in self.nodes.values():
            if node.verify_activity():
                active += 1
            else:
                inactive += 1
                self.slash_stake(node.node_id, "inactivity")
        
        return active, inactive
    
    def slash_stake(self, node_id: str, reason: str) -> bool:
        """Slash a node's stake for violating security conditions."""
        if node_id not in self.nodes or reason not in self.slashing_conditions:
            return False
        
        node = self.nodes[node_id]
        slash_percentage = self.slashing_conditions[reason]
        slash_amount = node.stake_amount * slash_percentage
        node.stake_amount -= slash_amount
        return True
    
    def calculate_rewards(self) -> Dict[str, float]:
        """Calculate rewards for all active nodes based on their security level."""
        rewards = {}
        active_nodes = [node for node in self.nodes.values() if node.is_active]
        
        if not active_nodes:
            return rewards
        
        total_stake = sum(node.stake_amount for node in active_nodes)
        
        for node in active_nodes:
            reward_rate = self.reward_rates[node.security_level]
            stake_ratio = node.stake_amount / total_stake
            rewards[node.node_id] = reward_rate * stake_ratio
        
        return rewards
    
    def get_network_security_score(self) -> float:
        """Calculate a composite security score for the entire network."""
        if not self.nodes:
            return 0.0
        
        total_score = 0.0
        total_stake = 0.0
        
        for node in self.nodes.values():
            weight = node.stake_amount
            security_weight = {
                SecurityLevel.LOW: 0.5,
                SecurityLevel.MEDIUM: 0.8,
                SecurityLevel.HIGH: 1.0
            }.get(node.security_level, 0.5)
            
            total_score += weight * security_weight * (1 if node.is_active else 0.2)
            total_stake += weight
        
        return (total_score / total_stake) if total_stake > 0 else 0.0
    
    def generate_proof_of_security(self, node_id: str) -> Optional[str]:
        """Generate a cryptographic proof of security for a node."""
        if node_id not in self.nodes:
            return None
        
        node = self.nodes[node_id]
        if not node.is_active:
            return None
        
        data = {
            "node_id": node_id,
            "security_level": node.security_level.name,
            "stake_amount": node.stake_amount,
            "timestamp": time.time()
        }
        
        json_data = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(json_data).hexdigest()

def simulate_network_activity(system: SecurityGuaranteeSystem, num_nodes: int = 100):
    """Simulate network activity for testing purposes."""
    for i in range(num_nodes):
        security_level = random.choice(list(SecurityLevel))
        stake = random.uniform(100, 10000)
        node_id = f"node_{i}"
        system.register_node(node_id, security_level, stake)
        
        # Randomly make some nodes inactive
        if random.random() < 0.1:  # 10% chance of inactivity
            system.nodes[node_id].last_active = time.time() - 1000
        else:
            system.update_node_activity(node_id)

# Example usage
if __name__ == "__main__":
    security_system = SecurityGuaranteeSystem()
    simulate_network_activity(security_system, 50)
    
    active, inactive = security_system.verify_network_security()
    print(f"Active nodes: {active}, Inactive nodes: {inactive}")
    
    rewards = security_system.calculate_rewards()
    print(f"Rewards distribution: {rewards}")
    
    security_score = security_system.get_network_security_score()
    print(f"Network security score: {security_score:.2f}")
    
    sample_node = next(iter(security_system.nodes.keys()))
    proof = security_system.generate_proof_of_security(sample_node)
    print(f"Security proof for node {sample_node}: {proof}")
```
