"""
Generated Code Metadata:
========================
Original URL: https://caabta.ch
Prompt: "Compare different home automation protocols (KNX, Z-WAVE, EnOcean) and suggest the best one for a commercial building."
Generated: DETERMINISTIC_fcc6bb8a8179be25
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script compares different home automation protocols (KNX, Z-WAVE, EnOcean)
and suggests the best one for a commercial building based on predefined criteria.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class Protocol(Enum):
    """Enumeration of home automation protocols."""
    KNX = "KNX"
    Z_WAVE = "Z-WAVE"
    ENOCEAN = "EnOcean"

@dataclass
class ProtocolCriteria:
    """Data class representing evaluation criteria for a protocol."""
    name: Protocol
    reliability: float  # Scale of 0-1
    scalability: float  # Scale of 0-1
    cost: float  # Scale of 0-1 (lower is better)
    installation_complexity: float  # Scale of 0-1 (lower is better)
    energy_efficiency: float  # Scale of 0-1
    interoperability: float  # Scale of 0-1
    commercial_support: float  # Scale of 0-1

def evaluate_protocols(protocols: List[ProtocolCriteria], weights: dict) -> Optional[Protocol]:
    """
    Evaluates protocols based on weighted criteria and returns the best one.
    
    Args:
        protocols: List of ProtocolCriteria objects to evaluate.
        weights: Dictionary of weights for each criterion (must sum to 1).
    
    Returns:
        The best Protocol based on evaluation, or None if input is invalid.
    
    Raises:
        ValueError: If weights do not sum to 1 or if protocols list is empty.
    """
    if not protocols:
        raise ValueError("Protocols list cannot be empty")
    
    if abs(sum(weights.values()) - 1.0) > 0.0001:
        raise ValueError("Weights must sum to 1")
    
    best_protocol = None
    best_score = -1
    
    for protocol in protocols:
        score = (
            protocol.reliability * weights["reliability"] +
            protocol.scalability * weights["scalability"] +
            (1 - protocol.cost) * weights["cost"] +
            (1 - protocol.installation_complexity) * weights["installation_complexity"] +
            protocol.energy_efficiency * weights["energy_efficiency"] +
            protocol.interoperability * weights["interoperability"] +
            protocol.commercial_support * weights["commercial_support"]
        )
        
        if score > best_score:
            best_score = score
            best_protocol = protocol.name
    
    return best_protocol

def main():
    """Main function to compare protocols and suggest the best for commercial buildings."""
    # Define protocol criteria based on research and expert opinions
    protocols = [
        ProtocolCriteria(
            name=Protocol.KNX,
            reliability=0.9,
            scalability=0.8,
            cost=0.7,
            installation_complexity=0.6,
            energy_efficiency=0.7,
            interoperability=0.9,
            commercial_support=0.8
        ),
        ProtocolCriteria(
            name=Protocol.Z_WAVE,
            reliability=0.8,
            scalability=0.7,
            cost=0.5,
            installation_complexity=0.4,
            energy_efficiency=0.8,
            interoperability=0.6,
            commercial_support=0.7
        ),
        ProtocolCriteria(
            name=Protocol.ENOCEAN,
            reliability=0.7,
            scalability=0.6,
            cost=0.4,
            installation_complexity=0.3,
            energy_efficiency=0.9,
            interoperability=0.5,
            commercial_support=0.6
        )
    ]
    
    # Define weights for commercial building priorities
    commercial_weights = {
        "reliability": 0.25,
        "scalability": 0.2,
        "cost": 0.1,
        "installation_complexity": 0.1,
        "energy_efficiency": 0.1,
        "interoperability": 0.15,
        "commercial_support": 0.1
    }
    
    try:
        best_protocol = evaluate_protocols(protocols, commercial_weights)
        print(f"Recommended protocol for commercial building: {best_protocol.value}")
    except ValueError as e:
        print(f"Error evaluating protocols: {e}")

if __name__ == "__main__":
    main()
```
