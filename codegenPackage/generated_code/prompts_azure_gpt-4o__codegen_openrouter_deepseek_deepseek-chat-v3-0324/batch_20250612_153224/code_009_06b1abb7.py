"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: Write a program to manage resource allocation in a fully equipped call center environment, incorporating the features mentioned in The Hashtag Consultants' services.
Generated: DETERMINISTIC_06b1abb7280c0e1e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AgentSkill(Enum):
    """Enum representing different skills that call center agents might have."""
    CUSTOMER_SERVICE = "Customer Service"
    TECHNICAL_SUPPORT = "Technical Support"
    SALES = "Sales"
    BILLING = "Billing"
    ESCALATION = "Escalation"

class AgentStatus(Enum):
    """Enum representing different statuses of call center agents."""
    AVAILABLE = "Available"
    ON_CALL = "On Call"
    BREAK = "Break"
    TRAINING = "Training"
    OFFLINE = "Offline"

class CallPriority(Enum):
    """Enum representing different priorities of calls."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class ResourceType(Enum):
    """Enum representing different types of resources in the call center."""
    AGENT = "Agent"
    WORKSTATION = "Workstation"
    HEADSET = "Headset"
    SOFTWARE_LICENSE = "Software License"

class Call:
    """Class representing a call in the call center."""
    
    def __init__(self, call_id: str, customer_id: str, priority: CallPriority, 
                 required_skills: List[AgentSkill], timestamp: datetime = None):
        self.call_id = call_id
        self.customer_id = customer_id
        self.priority = priority
        self.required_skills = required_skills
        self.timestamp = timestamp if timestamp else datetime.now()
        self.assigned_agent: Optional[Agent] = None
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    def assign_agent(self, agent: 'Agent') -> None:
        """Assign an agent to this call."""
        self.assigned_agent = agent
        self.start_time = datetime.now()

    def end_call(self) -> None:
        """Mark the call as ended."""
        if not self.assigned_agent:
            raise ValueError("Cannot end call that has no assigned agent")
        self.end_time = datetime.now()

    def duration(self) -> Optional[float]:
        """Calculate call duration in seconds."""
        if not self.start_time or not self.end_time:
            return None
        return (self.end_time - self.start_time).total_seconds()

class Resource:
    """Base class representing a resource in the call center."""
    
    def __init__(self, resource_id: str, resource_type: ResourceType):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.is_allocated = False

    def allocate(self) -> None:
        """Mark the resource as allocated."""
        if self.is_allocated:
            raise ValueError(f"Resource {self.resource_id} is already allocated")
        self.is_allocated = True

    def release(self) -> None:
        """Mark the resource as released."""
        if not self.is_allocated:
            raise ValueError(f"Resource {self.resource_id} is not allocated")
        self.is_allocated = False

class Agent(Resource):
    """Class representing a call center agent."""
    
    def __init__(self, agent_id: str, name: str, skills: List[AgentSkill]):
        super().__init__(agent_id, ResourceType.AGENT)
        self.name = name
        self.skills = skills
        self.status = AgentStatus.AVAILABLE
        self.current_call: Optional[Call] = None

    def assign_call(self, call: Call) -> None:
        """Assign a call to this agent."""
        if self.status != AgentStatus.AVAILABLE:
            raise ValueError(f"Agent {self.name} is not available")
        if not all(skill in self.skills for skill in call.required_skills):
            raise ValueError(f"Agent {self.name} lacks required skills for call {call.call_id}")
        
        self.current_call = call
        self.status = AgentStatus.ON_CALL
        call.assign_agent(self)
        logger.info(f"Assigned call {call.call_id} to agent {self.name}")

    def end_call(self) -> None:
        """End the current call."""
        if not self.current_call:
            raise ValueError("Agent has no active call to end")
        
        self.current_call.end_call()
        logger.info(f"Call {self.current_call.call_id} ended. Duration: {self.current_call.duration()} seconds")
        self.current_call = None
        self.status = AgentStatus.AVAILABLE

    def set_status(self, status: AgentStatus) -> None:
        """Set the agent's status."""
        if status == AgentStatus.ON_CALL and not self.current_call:
            raise ValueError("Cannot set status to ON_CALL without an active call")
        self.status = status
        logger.info(f"Agent {self.name} status changed to {status.value}")

class Workstation(Resource):
    """Class representing a workstation in the call center."""
    
    def __init__(self, workstation_id: str, location: str):
        super().__init__(workstation_id, ResourceType.WORKSTATION)
        self.location = location
        self.assigned_agent: Optional[Agent] = None

    def assign_agent(self, agent: Agent) -> None:
        """Assign an agent to this workstation."""
        if self.assigned_agent:
            raise ValueError(f"Workstation {self.resource_id} is already assigned to agent {self.assigned_agent.name}")
        self.assigned_agent = agent
        self.allocate()
        logger.info(f"Assigned agent {agent.name} to workstation {self.resource_id}")

    def release_agent(self) -> None:
        """Release the agent from this workstation."""
        if not self.assigned_agent:
            raise ValueError(f"Workstation {self.resource_id} has no assigned agent")
        logger.info(f"Released agent {self.assigned_agent.name} from workstation {self.resource_id}")
        self.assigned_agent = None
        self.release()

class AllocationStrategy(ABC):
    """Abstract base class for resource allocation strategies."""
    
    @abstractmethod
    def allocate_resources(self, call: Call, agents: List[Agent], resources: Dict[ResourceType, List[Resource]]) -> Tuple[Optional[Agent], List[Resource]]:
        """Allocate resources for a call."""
        pass

class PriorityBasedAllocation(AllocationStrategy):
    """Priority-based resource allocation strategy."""
    
    def allocate_resources(self, call: Call, agents: List[Agent], resources: Dict[ResourceType, List[Resource]]) -> Tuple[Optional[Agent], List[Resource]]:
        """Allocate resources based on call priority and agent skills."""
        allocated_resources = []
        
        # Find available agents with required skills
        suitable_agents = [
            agent for agent in agents 
            if agent.status == AgentStatus.AVAILABLE and 
            all(skill in agent.skills for skill in call.required_skills)
        ]
        
        if not suitable_agents:
            logger.warning(f"No available agents with required skills for call {call.call_id}")
            return None, []
        
        # Sort agents by skill match (more skills first) and availability
        suitable_agents.sort(key=lambda a: len(a.skills), reverse=True)
        
        # Select the first available agent
        selected_agent = suitable_agents[0]
        
        # Allocate workstation
        workstations = resources.get(ResourceType.WORKSTATION, [])
        available_workstations = [ws for ws in workstations if not ws.is_allocated]
        
        if not available_workstations:
            logger.warning(f"No available workstations for call {call.call_id}")
            return None, []
        
        selected_workstation = available_workstations[0]
        selected_workstation.assign_agent(selected_agent)
        allocated_resources.append(selected_workstation)
        
        # Allocate headset
        headsets = resources.get(ResourceType.HEADSET, [])
        available_headsets = [hs for hs in headsets if not hs.is_allocated]
        
        if available_headsets:
            selected_headset = available_headsets[0]
            selected_headset.allocate()
            allocated_resources.append(selected_headset)
        else:
            logger.warning(f"No available headsets for call {call.call_id}")
        
        return selected_agent, allocated_resources

class CallCenter:
    """Class representing a call center with resource management."""
    
    def __init__(self, allocation_strategy: AllocationStrategy = None):
        self.agents: List[Agent] = []
        self.resources: Dict[ResourceType, List[Resource]] = {
            ResourceType.WORKSTATION: [],
            ResourceType.HEADSET: [],
            ResourceType.SOFTWARE_LICENSE: []
        }
        self.active_calls: List[Call] = []
        self.call
