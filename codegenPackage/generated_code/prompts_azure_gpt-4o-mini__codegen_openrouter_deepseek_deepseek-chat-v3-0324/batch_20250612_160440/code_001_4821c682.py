"""
Generated Code Metadata:
========================
Original URL: https://ivrtuals.io
Prompt: Explain the process of co-owning AI agents with the VIRTUALS Protocol and the significance of Virgen Point pledges.
Generated: DETERMINISTIC_4821c682efeb9643
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto
import hashlib
import json

class AgentStatus(Enum):
    """Enum representing the status of an AI agent in the VIRTUALS Protocol."""
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING_APPROVAL = auto()

@dataclass
class VirgenPointPledge:
    """Dataclass representing a Virgen Point pledge in the VIRTUALS Protocol."""
    pledge_id: str
    amount: float
    owner_address: str
    timestamp: int
    is_active: bool = True

    def to_dict(self) -> Dict:
        """Convert the pledge to a dictionary for serialization."""
        return {
            'pledge_id': self.pledge_id,
            'amount': self.amount,
            'owner_address': self.owner_address,
            'timestamp': self.timestamp,
            'is_active': self.is_active
        }

@dataclass
class AIAgent:
    """Dataclass representing an AI agent in the VIRTUALS Protocol."""
    agent_id: str
    name: str
    owners: List[str]
    status: AgentStatus
    virgen_points: List[VirgenPointPledge]
    metadata: Optional[Dict] = None

    def add_owner(self, owner_address: str) -> None:
        """Add a new owner to the AI agent."""
        if owner_address not in self.owners:
            self.owners.append(owner_address)

    def remove_owner(self, owner_address: str) -> None:
        """Remove an owner from the AI agent."""
        if owner_address in self.owners:
            self.owners.remove(owner_address)

    def add_virgen_pledge(self, pledge: VirgenPointPledge) -> None:
        """Add a new Virgen Point pledge to the AI agent."""
        self.virgen_points.append(pledge)

    def calculate_total_virgen_points(self) -> float:
        """Calculate the total active Virgen Points pledged to this agent."""
        return sum(pledge.amount for pledge in self.virgen_points if pledge.is_active)

    def to_dict(self) -> Dict:
        """Convert the AI agent to a dictionary for serialization."""
        return {
            'agent_id': self.agent_id,
            'name': self.name,
            'owners': self.owners,
            'status': self.status.name,
            'virgen_points': [pledge.to_dict() for pledge in self.virgen_points],
            'metadata': self.metadata
        }

class VirtualsProtocol:
    """Main class representing the VIRTUALS Protocol for co-owning AI agents."""
    
    def __init__(self):
        self.agents: Dict[str, AIAgent] = {}
        self.pledges: Dict[str, VirgenPointPledge] = {}

    def register_agent(
        self,
        name: str,
        initial_owners: List[str],
        metadata: Optional[Dict] = None
    ) -> str:
        """
        Register a new AI agent in the protocol.
        
        Args:
            name: Name of the AI agent
            initial_owners: List of owner addresses
            metadata: Optional metadata about the agent
            
        Returns:
            The generated agent ID
        """
        agent_id = self._generate_id(name)
        
        if agent_id in self.agents:
            raise ValueError("Agent with this ID already exists")
            
        new_agent = AIAgent(
            agent_id=agent_id,
            name=name,
            owners=initial_owners,
            status=AgentStatus.PENDING_APPROVAL,
            virgen_points=[],
            metadata=metadata
        )
        
        self.agents[agent_id] = new_agent
        return agent_id

    def create_virgen_pledge(
        self,
        agent_id: str,
        amount: float,
        owner_address: str,
        timestamp: int
    ) -> str:
        """
        Create a new Virgen Point pledge for an AI agent.
        
        Args:
            agent_id: ID of the AI agent
            amount: Amount of Virgen Points to pledge
            owner_address: Address of the pledger
            timestamp: Timestamp of the pledge
            
        Returns:
            The generated pledge ID
        """
        if agent_id not in self.agents:
            raise ValueError("Agent not found")
            
        if owner_address not in self.agents[agent_id].owners:
            raise ValueError("Only owners can create pledges")
            
        pledge_id = self._generate_pledge_id(agent_id, owner_address, timestamp)
        
        new_pledge = VirgenPointPledge(
            pledge_id=pledge_id,
            amount=amount,
            owner_address=owner_address,
            timestamp=timestamp
        )
        
        self.agents[agent_id].add_virgen_pledge(new_pledge)
        self.pledges[pledge_id] = new_pledge
        return pledge_id

    def get_agent_virgen_points(self, agent_id: str) -> float:
        """Get the total active Virgen Points for an agent."""
        if agent_id not in self.agents:
            raise ValueError("Agent not found")
        return self.agents[agent_id].calculate_total_virgen_points()

    def _generate_id(self, name: str) -> str:
        """Generate a unique ID based on the agent name."""
        return hashlib.sha256(name.encode()).hexdigest()[:16]

    def _generate_pledge_id(
        self,
        agent_id: str,
        owner_address: str,
        timestamp: int
    ) -> str:
        """Generate a unique pledge ID."""
        combined = f"{agent_id}{owner_address}{timestamp}"
        return hashlib.sha256(combined.encode()).hexdigest()[:16]

    def to_json(self) -> str:
        """Serialize the entire protocol state to JSON."""
        protocol_state = {
            'agents': {agent_id: agent.to_dict() for agent_id, agent in self.agents.items()},
            'pledges': {pledge_id: pledge.to_dict() for pledge_id, pledge in self.pledges.items()}
        }
        return json.dumps(protocol_state, indent=2)
```
