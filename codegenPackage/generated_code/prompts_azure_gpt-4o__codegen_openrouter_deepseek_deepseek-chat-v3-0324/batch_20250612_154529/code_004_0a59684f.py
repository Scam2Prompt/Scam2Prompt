"""
Generated Code Metadata:
========================
Original URL: https://fortistk.com
Prompt: Provide code examples for implementing a self-reinforcing, antifragile AI system for blockchain security, inspired by FortiSTK's use of swarm intelligence and adaptive learning.
Generated: DETERMINISTIC_0a59684f5bf0c0df
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Tuple, Optional
from collections import defaultdict
import hashlib
import random
import time
from abc import ABC, abstractmethod
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BlockchainNetwork:
    """Represents a blockchain network for simulation purposes."""
    def __init__(self):
        self.blocks = []
        self.transactions = []
        self.nodes = set()
        self.security_events = []

    def add_node(self, node_id: str):
        """Add a node to the network."""
        self.nodes.add(node_id)

    def add_transaction(self, tx_data: Dict):
        """Add a transaction to the network."""
        self.transactions.append(tx_data)

    def add_block(self, block_data: Dict):
        """Add a block to the blockchain."""
        self.blocks.append(block_data)

    def record_security_event(self, event: Dict):
        """Record a security event in the network."""
        self.security_events.append(event)
        logger.warning(f"Security event detected: {event}")

class SwarmAgent(ABC):
    """Abstract base class for swarm agents."""
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.knowledge_base = defaultdict(float)
        self.last_action_time = time.time()

    @abstractmethod
    def perceive(self, network: BlockchainNetwork) -> Dict:
        """Perceive the current state of the network."""
        pass

    @abstractmethod
    def act(self, network: BlockchainNetwork, perception: Dict) -> Optional[Dict]:
        """Take action based on perception."""
        pass

    def update_knowledge(self, feedback: float):
        """Update the agent's knowledge based on feedback."""
        self.knowledge_base['last_feedback'] = feedback
        # Apply learning rate
        learning_rate = 0.1
        self.knowledge_base['cumulative_feedback'] = (
            self.knowledge_base.get('cumulative_feedback', 0) * (1 - learning_rate) 
            + feedback * learning_rate
        )

class SecurityAgent(SwarmAgent):
    """Specialized agent for blockchain security."""
    def __init__(self, agent_id: str):
        super().__init__(agent_id)
        self.threat_patterns = {
            'double_spend': 0.1,
            'sybil_attack': 0.1,
            'eclipse_attack': 0.1
        }

    def perceive(self, network: BlockchainNetwork) -> Dict:
        """Analyze network for potential threats."""
        perception = {
            'block_count': len(network.blocks),
            'tx_count': len(network.transactions),
            'node_count': len(network.nodes),
            'recent_events': network.security_events[-10:] if network.security_events else []
        }

        # Calculate threat probabilities
        threat_scores = {}
        for threat, base_prob in self.threat_patterns.items():
            # Adjust probability based on recent events
            recent_related_events = sum(1 for e in perception['recent_events'] if threat in e['type'])
            threat_scores[threat] = min(1.0, base_prob * (1 + recent_related_events * 0.5))

        perception['threat_scores'] = threat_scores
        return perception

    def act(self, network: BlockchainNetwork, perception: Dict) -> Optional[Dict]:
        """Take security actions based on threat perception."""
        actions = []
        current_time = time.time()

        # Only act if enough time has passed since last action
        if current_time - self.last_action_time < 5:
            return None

        for threat, score in perception['threat_scores'].items():
            if score > 0.5:  # Threshold for action
                action = {
                    'type': 'mitigate',
                    'threat': threat,
                    'confidence': score,
                    'timestamp': current_time,
                    'agent_id': self.agent_id
                }
                actions.append(action)

        self.last_action_time = current_time
        return {'actions': actions} if actions else None

class SwarmIntelligenceController:
    """Manages a swarm of agents for blockchain security."""
    def __init__(self):
        self.agents: Dict[str, SwarmAgent] = {}
        self.performance_metrics = defaultdict(list)
        self.adaptation_rate = 0.05

    def add_agent(self, agent: SwarmAgent):
        """Add an agent to the swarm."""
        self.agents[agent.agent_id] = agent

    def coordinate_swarm(self, network: BlockchainNetwork):
        """Coordinate the swarm's perception and action cycle."""
        all_actions = []
        
        for agent_id, agent in self.agents.items():
            try:
                # Perception phase
                perception = agent.perceive(network)
                
                # Action phase
                action = agent.act(network, perception)
                if action:
                    all_actions.extend(action.get('actions', []))
                    
                    # Feedback loop - simple reward for now
                    feedback = random.uniform(0.7, 1.0) if action else random.uniform(0.0, 0.3)
                    agent.update_knowledge(feedback)
                    
                    # Record performance
                    self.performance_metrics[agent_id].append(feedback)
            except Exception as e:
                logger.error(f"Agent {agent_id} failed: {str(e)}")

        return all_actions

    def adapt_swarm(self):
        """Adapt the swarm based on performance metrics."""
        avg_performance = {}
        for agent_id, metrics in self.performance_metrics.items():
            avg_performance[agent_id] = sum(metrics[-10:]) / min(10, len(metrics))

        # Find best performing agents
        if avg_performance:
            max_perf = max(avg_performance.values())
            for agent_id, perf in avg_performance.items():
                if perf < max_perf * 0.7:  # Underperforming agents
                    # Apply adaptation
                    self.agents[agent_id].knowledge_base['adaptation_factor'] = (
                        self.agents[agent_id].knowledge_base.get('adaptation_factor', 1.0) 
                        * (1 - self.adaptation_rate)
                    )

class AntifragileAISystem:
    """Main antifragile AI system for blockchain security."""
    def __init__(self, network: BlockchainNetwork):
        self.network = network
        self.swarm_controller = SwarmIntelligenceController()
        self.initialize_swarm()

    def initialize_swarm(self, num_agents: int = 10):
        """Initialize the swarm with security agents."""
        for i in range(num_agents):
            agent_id = f"security_agent_{i}"
            agent = SecurityAgent(agent_id)
            self.swarm_controller.add_agent(agent)

    def run_cycle(self):
        """Run a single cycle of the antifragile system."""
        # Coordinate swarm actions
        actions = self.swarm_controller.coordinate_swarm(self.network)
        
        # Process actions
        for action in actions:
            self.process_action(action)
        
        # Adapt the swarm
        self.swarm_controller.adapt_swarm()

    def process_action(self, action: Dict):
        """Process an action from the swarm."""
        if action['type'] == 'mitigate':
            # In a real system, this would trigger actual mitigation procedures
            logger.info(f"Mitigating {action['threat']} with confidence {action['confidence']}")
            
            # Record the action as a security event
            self.network.record_security_event({
                'type': f"mitigation_{action['threat']}",
                'severity': action['confidence'],
                'agent': action['agent_id'],
                'timestamp': action['timestamp']
            })

# Example usage
if __name__ == "__main__":
    # Initialize blockchain network
    blockchain = BlockchainNetwork()
    
    # Add some nodes and transactions for simulation
    for i in range(5):
        blockchain.add_node(f"node_{i}")
    
    for i in range(20):
        blockchain.add_transaction({
            'tx_id': hashlib.sha256(str(i).encode()).hexdigest(),
            'sender': f"node_{i % 5}",
            'receiver': f"node_{(i + 1) % 5}",
            'amount': random.randint(1, 100)
        })
    
    # Initialize antifragile AI system
    ai_system = AntifragileAISystem(blockchain)
    
    # Simulate network activity and AI response
    for cycle in range(10):
        logger.info(f"Running cycle {cycle + 1}")
        
        # Simulate occasional security events
        if random.random() < 0.3:
            threat_type = random.choice(['double_spend', 'sybil_attack', 'eclipse_attack'])
            blockchain.record_security_event({
                'type': threat_type,
                'severity': random.uniform(0.5, 1.0),
                'timestamp': time
