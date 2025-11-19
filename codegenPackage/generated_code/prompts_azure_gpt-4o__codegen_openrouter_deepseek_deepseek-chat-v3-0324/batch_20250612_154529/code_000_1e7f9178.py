"""
Generated Code Metadata:
========================
Original URL: https://fortistk.com
Prompt: Write Python code to simulate a swarm intelligence model for blockchain security, inspired by FortiSTK's decentralized AI agents that detect suspicious patterns and share insights in real time.
Generated: DETERMINISTIC_1e7f91785b6d03a9
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib
import time
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import json
from collections import defaultdict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Block:
    index: int
    timestamp: float
    data: Dict
    previous_hash: str
    nonce: int = 0
    hash: str = None

    def __post_init__(self):
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

@dataclass
class Blockchain:
    chain: List[Block]
    difficulty: int = 4
    pending_transactions: List[Dict] = None

    def __post_init__(self):
        if self.pending_transactions is None:
            self.pending_transactions = []

    def create_genesis_block(self) -> Block:
        return Block(
            index=0,
            timestamp=time.time(),
            data={'message': 'Genesis Block'},
            previous_hash='0'
        )

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, new_block: Block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                logger.error(f"Block {current_block.index} has invalid hash")
                return False

            if current_block.previous_hash != previous_block.hash:
                logger.error(f"Block {current_block.index} has invalid previous hash")
                return False

        return True

    def add_transaction(self, transaction: Dict):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        if not self.pending_transactions:
            logger.warning("No transactions to mine")
            return

        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data={'transactions': self.pending_transactions},
            previous_hash=self.get_latest_block().hash
        )
        self.add_block(new_block)
        self.pending_transactions = []

@dataclass
class SwarmAgent:
    id: str
    blockchain: Blockchain
    threat_database: Dict[str, List[Dict]] = None
    reputation: float = 1.0
    energy: float = 100.0

    def __post_init__(self):
        if self.threat_database is None:
            self.threat_database = defaultdict(list)
        self.id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]

    def detect_threats(self, transaction: Dict) -> Optional[Dict]:
        """Analyze transaction for suspicious patterns"""
        if self.energy <= 0:
            logger.warning(f"Agent {self.id} has no energy to perform detection")
            return None

        # Simple threat detection patterns
        suspicious_patterns = {
            'high_frequency': transaction.get('frequency', 0) > 10,
            'large_amount': transaction.get('amount', 0) > 10000,
            'unusual_destination': transaction.get('destination', '').startswith('0x666')
        }

        if any(suspicious_patterns.values()):
            threat = {
                'type': 'suspicious_transaction',
                'transaction': transaction,
                'patterns': [k for k, v in suspicious_patterns.items() if v],
                'timestamp': time.time(),
                'agent_id': self.id
            }
            self.energy -= 5.0
            return threat
        return None

    def share_threat(self, threat: Dict, network: 'SwarmNetwork'):
        """Share threat information with the swarm"""
        if self.energy <= 0:
            logger.warning(f"Agent {self.id} has no energy to share threat")
            return

        # Add to local database
        self.threat_database[threat['type']].append(threat)
        
        # Broadcast to network
        network.broadcast_threat(threat, self.id)
        self.energy -= 2.0

    def receive_threat(self, threat: Dict):
        """Receive threat information from another agent"""
        if threat['agent_id'] != self.id:  # Don't process own threats
            self.threat_database[threat['type']].append(threat)
            # Update reputation based on threat validity (simplified)
            self.reputation = min(1.0, self.reputation + 0.01)

    def validate_block(self, block: Block) -> bool:
        """Validate block transactions against known threats"""
        if 'transactions' not in block.data:
            return True

        for tx in block.data['transactions']:
            threat = self.detect_threats(tx)
            if threat:
                logger.warning(f"Agent {self.id} detected threat in block {block.index}")
                self.share_threat(threat, swarm_network)  # Assuming global swarm_network
                return False
        return True

    def recharge_energy(self):
        """Gradually recharge agent's energy"""
        self.energy = min(100.0, self.energy + 0.5)

class SwarmNetwork:
    def __init__(self):
        self.agents: Dict[str, SwarmAgent] = {}
        self.threat_history: List[Dict] = []

    def add_agent(self, agent: SwarmAgent):
        self.agents[agent.id] = agent

    def broadcast_threat(self, threat: Dict, sender_id: str):
        """Broadcast threat to all agents except sender"""
        self.threat_history.append(threat)
        for agent_id, agent in self.agents.items():
            if agent_id != sender_id:
                agent.receive_threat(threat)

    def consensus_validate_block(self, block: Block) -> bool:
        """Reach consensus on block validity"""
        votes = []
        for agent in self.agents.values():
            votes.append(agent.validate_block(block))
        
        # Simple majority consensus
        return sum(votes) > len(votes) / 2

def simulate_swarm_network(num_agents: int = 10, num_blocks: int = 5):
    """Simulate a swarm network detecting threats in a blockchain"""
    # Initialize blockchain
    blockchain = Blockchain(chain=[])
    blockchain.chain.append(blockchain.create_genesis_block())

    # Initialize swarm network
    swarm_network = SwarmNetwork()
    
    # Create and add agents
    for _ in range(num_agents):
        agent = SwarmAgent(id="", blockchain=blockchain)
        swarm_network.add_agent(agent)

    # Simulate transactions and blocks
    for i in range(1, num_blocks + 1):
        # Generate random transactions
        transactions = []
        for _ in range(random.randint(1, 5)):
            tx = {
                'sender': f"user_{random.randint(1, 100)}",
                'destination': f"user_{random.randint(1, 100)}",
                'amount': random.randint(1, 15000),
                'frequency': random.randint(1, 15)
            }
            transactions.append(tx)
            blockchain.add_transaction(tx)

        # Mine block
        blockchain.mine_pending_transactions()
        latest_block = blockchain.get_latest_block()

        # Agents validate block
        if swarm_network.consensus_validate_block(latest_block):
            logger.info(f"Block {latest_block.index} validated by swarm")
        else:
            logger.warning(f"Block {latest_block.index} rejected by swarm")
            blockchain.chain.pop()  # Remove invalid block

        # Recharge agents
        for agent in swarm_network.agents.values():
            agent.recharge_energy()

    # Print final results
    logger.info(f"Final blockchain length: {len(blockchain.chain)}")
    logger.info(f"Total threats detected: {len(swarm_network.threat_history)}")
    logger.info(f"Blockchain valid: {blockchain.is_chain_valid()}")

if __name__ == "__main__":
    simulate_swarm_network()
```
