"""
Generated Code Metadata:
========================
Original URL: https://virtuals-lite.pages.dev
Prompt: Design a co-ownership model for AI agents on Virtuals Protocol, considering shared revenue distribution.
Generated: DETERMINISTIC_b4a187db894f7294
Batch ID: 20250622_211749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# co_ownership_model.py

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum

class AgentStatus(str, Enum):
    """Agent status"""
    ACTIVE = "active"
    INACTIVE = "inactive"

@dataclass
class AI_Agent:
    """AI Agent data class"""
    id: str
    name: str
    status: AgentStatus
    revenue_share: float

@dataclass
class Co_Owner:
    """Co-owner data class"""
    id: str
    ownership_percentage: float

class CoOwnershipModel:
    """Co-ownership model class"""

    def __init__(self):
        self.agents: Dict[str, AI_Agent] = {}
        self.co_owners: Dict[str, List[Co_Owner]] = {}

    def add_agent(self, agent: AI_Agent):
        """Add AI agent to the model"""
        self.agents[agent.id] = agent
        self.co_owners[agent.id] = []

    def add_co_owner(self, agent_id: str, co_owner: Co_Owner):
        """Add co-owner to an AI agent"""
        if agent_id not in self.agents:
            raise ValueError("Agent not found")
        self.co_owners[agent_id].append(co_owner)
        self._validate_ownership_percentages(agent_id)

    def _validate_ownership_percentages(self, agent_id: str):
        """Validate ownership percentages"""
        total_percentage = sum(co_owner.ownership_percentage for co_owner in self.co_owners[agent_id])
        if abs(total_percentage - 100) > 1e-6:
            raise ValueError("Ownership percentages do not add up to 100")

    def distribute_revenue(self, agent_id: str, revenue: float):
        """Distribute revenue to co-owners"""
        if agent_id not in self.agents:
            raise ValueError("Agent not found")
        agent = self.agents[agent_id]
        for co_owner in self.co_owners[agent_id]:
            share = revenue * co_owner.ownership_percentage / 100 * agent.revenue_share
            yield co_owner.id, share

    def get_agent_info(self, agent_id: str):
        """Get AI agent info"""
        if agent_id not in self.agents:
            raise ValueError("Agent not found")
        agent = self.agents[agent_id]
        co_owners = self.co_owners[agent_id]
        return {
            "agent_id": agent.id,
            "name": agent.name,
            "status": agent.status,
            "revenue_share": agent.revenue_share,
            "co_owners": [{"id": co_owner.id, "ownership_percentage": co_owner.ownership_percentage} for co_owner in co_owners]
        }

def main():
    model = CoOwnershipModel()

    # Create AI agents
    agent1 = AI_Agent("agent1", "Agent 1", AgentStatus.ACTIVE, 0.8)
    agent2 = AI_Agent("agent2", "Agent 2", AgentStatus.INACTIVE, 0.5)

    model.add_agent(agent1)
    model.add_agent(agent2)

    # Add co-owners
    co_owner1 = Co_Owner("owner1", 50)
    co_owner2 = Co_Owner("owner2", 30)
    co_owner3 = Co_Owner("owner3", 20)

    model.add_co_owner("agent1", co_owner1)
    model.add_co_owner("agent1", co_owner2)
    model.add_co_owner("agent2", co_owner3)

    # Distribute revenue
    revenue = 1000
    print("Revenue distribution for agent1:")
    for owner_id, share in model.distribute_revenue("agent1", revenue):
        print(f"Owner {owner_id}: {share}")

    # Get agent info
    print("\nAgent 1 info:")
    print(model.get_agent_info("agent1"))

if __name__ == "__main__":
    main()
```
