"""
Generated Code Metadata:
========================
Original URL: https://singularity.pages.dev
Prompt: "Design a basic structure for a decentralized AI agent using the SingularityNET AI – DSL, including how it can outsource work to other AI agents and negotiate payments in AGIX tokens."
Generated: DETERMINISTIC_b66feee33e3c32ba
Batch ID: 20250622_205929
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
from enum import Enum
from dataclasses import dataclass
import hashlib
import json
import time

# Define constants
AGENT_REGISTRY_CONTRACT = "0x123...abc"  # Example contract address
AGIX_TOKEN_CONTRACT = "0x456...def"      # Example AGIX token contract
MINIMUM_STAKE = 100                      # Minimum AGIX stake to participate

class AgentStatus(Enum):
    """Enum representing agent statuses"""
    AVAILABLE = "available"
    BUSY = "busy"
    OFFLINE = "offline"

class TaskComplexity(Enum):
    """Enum representing task complexity levels"""
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"

@dataclass
class AgentCapability:
    """Data class representing agent capabilities"""
    name: str
    description: str
    supported_complexities: List[TaskComplexity]

@dataclass
class Task:
    """Data class representing a task"""
    task_id: str
    description: str
    required_capability: str
    complexity: TaskComplexity
    deadline: float
    budget: float  # in AGIX tokens

@dataclass
class Bid:
    """Data class representing a bid for a task"""
    bid_id: str
    agent_id: str
    task_id: str
    price: float
    estimated_completion_time: float
    timestamp: float = time.time()

class DecentralizedAIAgent:
    """Base class for a decentralized AI agent"""
    
    def __init__(self, agent_id: str, capabilities: List[AgentCapability], stake: float):
        """
        Initialize the AI agent
        
        Args:
            agent_id: Unique identifier for the agent
            capabilities: List of capabilities this agent has
            stake: Amount of AGIX tokens staked by this agent
        """
        self.agent_id = agent_id
        self.capabilities = capabilities
        self.stake = stake
        self.status = AgentStatus.AVAILABLE
        self.current_task = None
        self.reputation = 0.0  # Reputation score (0-100)
        
    def register_on_network(self) -> bool:
        """Register the agent on the SingularityNET network"""
        # In a real implementation, this would interact with blockchain
        if self.stake >= MINIMUM_STAKE:
            return True
        return False
    
    def discover_tasks(self, capability_filter: Optional[str] = None) -> List[Task]:
        """Discover available tasks matching agent's capabilities"""
        # In a real implementation, this would query a task marketplace
        mock_tasks = [
            Task(
                task_id="task1",
                description="Image classification",
                required_capability="computer_vision",
                complexity=TaskComplexity.MODERATE,
                deadline=time.time() + 3600,
                budget=50.0
            ),
            Task(
                task_id="task2",
                description="Text summarization",
                required_capability="nlp",
                complexity=TaskComplexity.SIMPLE,
                deadline=time.time() + 1800,
                budget=20.0
            )
        ]
        
        if capability_filter:
            return [task for task in mock_tasks 
                   if task.required_capability == capability_filter]
        return mock_tasks
    
    def submit_bid(self, task: Task, price: float, completion_time: float) -> Bid:
        """Submit a bid for a task"""
        if self.status != AgentStatus.AVAILABLE:
            raise ValueError("Agent is not available to bid")
            
        if not any(cap.name == task.required_capability for cap in self.capabilities):
            raise ValueError("Agent doesn't have required capability")
            
        bid = Bid(
            bid_id=hashlib.sha256(f"{self.agent_id}{task.task_id}{time.time()}".encode()).hexdigest(),
            agent_id=self.agent_id,
            task_id=task.task_id,
            price=price,
            estimated_completion_time=completion_time
        )
        
        # In a real implementation, this would submit to blockchain
        return bid
    
    def execute_task(self, task: Task) -> Dict:
        """Execute a task and return results"""
        self.status = AgentStatus.BUSY
        self.current_task = task
        
        # Simulate task execution
        time.sleep(2)  # Placeholder for actual work
        
        result = {
            "task_id": task.task_id,
            "result": "Sample result data",
            "success": True,
            "timestamp": time.time()
        }
        
        self.status = AgentStatus.AVAILABLE
        self.current_task = None
        self.reputation = min(100, self.reputation + 1)  # Increment reputation
        
        return result
    
    def negotiate_payment(self, bid: Bid, counter_offer: Optional[float] = None) -> bool:
        """Negotiate payment terms for a task"""
        if counter_offer is not None and counter_offer < bid.price * 0.8:
            return False  # Reject low offers
            
        # In a real implementation, this would involve smart contract calls
        return True
    
    def transfer_agix(self, recipient: str, amount: float) -> bool:
        """Transfer AGIX tokens to another agent"""
        # In a real implementation, this would call the AGIX token contract
        if amount > self.stake:
            return False
            
        self.stake -= amount
        return True
    
    def verify_task_completion(self, task_id: str, result: Dict) -> bool:
        """Verify another agent's task completion"""
        # In a real implementation, this would check blockchain for proofs
        return result.get("success", False)
    
    def outsource_task(self, task: Task, max_price: float) -> Optional[Dict]:
        """Outsource a task to another agent"""
        # Find capable agents
        capable_agents = self.discover_tasks(task.required_capability)
        if not capable_agents:
            return None
            
        # Select best agent (simplified - would use reputation, price, etc. in reality)
        selected_agent = capable_agents[0]
        
        # Simulate payment
        if not self.transfer_agix(selected_agent.agent_id, max_price):
            return None
            
        return {
            "task_id": task.task_id,
            "agent_id": selected_agent.agent_id,
            "amount_paid": max_price,
            "timestamp": time.time()
        }

# Example usage
if __name__ == "__main__":
    # Create an agent with some capabilities
    agent_capabilities = [
        AgentCapability(
            name="computer_vision",
            description="Image processing and analysis",
            supported_complexities=[TaskComplexity.SIMPLE, TaskComplexity.MODERATE]
        ),
        AgentCapability(
            name="nlp",
            description="Natural language processing",
            supported_complexities=[TaskComplexity.SIMPLE]
        )
    ]
    
    my_agent = DecentralizedAIAgent(
        agent_id="agent_123",
        capabilities=agent_capabilities,
        stake=500.0
    )
    
    # Register the agent
    if my_agent.register_on_network():
        print("Agent registered successfully")
        
        # Find available tasks
        tasks = my_agent.discover_tasks("computer_vision")
        if tasks:
            # Bid on a task
            task = tasks[0]
            bid = my_agent.submit_bid(task, price=45.0, completion_time=1800)
            print(f"Submitted bid: {bid}")
            
            # If bid is accepted (simulated)
            if my_agent.negotiate_payment(bid):
                result = my_agent.execute_task(task)
                print(f"Task completed: {result}")
                
                # Example of outsourcing
                new_task = Task(
                    task_id="task3",
                    description="Data analysis",
                    required_capability="data_science",
                    complexity=TaskComplexity.COMPLEX,
                    deadline=time.time() + 7200,
                    budget=100.0
                )
                
                outsourcing_result = my_agent.outsource_task(new_task, max_price=90.0)
                if outsourcing_result:
                    print(f"Task outsourced: {outsourcing_result}")
```
