"""
Generated Code Metadata:
========================
Original URL: https://fortistk.com
Prompt: Generate a detailed architecture diagram and code snippets for building a decentralized collective of AI agents, similar to FortiSTK's model, to monitor blockchain activities and detect threats.
Generated: DETERMINISTIC_8fa9b5c52422ba98
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Decentralized AI Agent Collective for Blockchain Threat Monitoring

# Core Agent Class
class AIAgent:
    """
    Base class for decentralized AI agents monitoring blockchain activities.
    """
    
    def __init__(self, agent_id, blockchain_network, reputation_score=1.0):
        """
        Initialize an AI agent with unique ID and blockchain network connection.
        
        Args:
            agent_id (str): Unique identifier for the agent
            blockchain_network (str): Blockchain network to monitor
            reputation_score (float): Initial reputation score (0.0-1.0)
        """
        self.agent_id = agent_id
        self.blockchain_network = blockchain_network
        self.reputation_score = reputation_score
        self.peers = set()
        self.threat_detection_models = {}
        self.initialize_models()
        
    def initialize_models(self):
        """Initialize threat detection models for the agent."""
        self.threat_detection_models = {
            'transaction_anomaly': self.load_model('transaction_anomaly'),
            'smart_contract_vulnerability': self.load_model('smart_contract_vulnerability'),
            'network_attack': self.load_model('network_attack')
        }
    
    def load_model(self, model_type):
        """Load a pre-trained threat detection model."""
        # In production, this would load actual ML models
        return f"{model_type}_model_loaded"
    
    def monitor_transaction(self, tx_data):
        """
        Monitor a blockchain transaction for potential threats.
        
        Args:
            tx_data (dict): Transaction data to analyze
            
        Returns:
            dict: Threat analysis results
        """
        try:
            anomaly_score = self.analyze_transaction(tx_data)
            threat_level = self.determine_threat_level(anomaly_score)
            
            return {
                'agent_id': self.agent_id,
                'transaction_hash': tx_data.get('hash'),
                'anomaly_score': anomaly_score,
                'threat_level': threat_level,
                'confidence': self.reputation_score * 0.9  # Weighted by reputation
            }
        except Exception as e:
            self.handle_error(e)
            return {'error': str(e)}
    
    def analyze_transaction(self, tx_data):
        """Analyze transaction using threat detection models."""
        # Simplified analysis - production would use actual ML inference
        return sum(ord(c) for c in tx_data.get('hash', '')) % 100 / 100
    
    def determine_threat_level(self, score):
        """Determine threat level based on anomaly score."""
        if score > 0.8:
            return 'critical'
        elif score > 0.6:
            return 'high'
        elif score > 0.4:
            return 'medium'
        return 'low'
    
    def handle_error(self, error):
        """Handle errors and adjust reputation score accordingly."""
        print(f"Agent {self.agent_id} error: {error}")
        self.reputation_score = max(0, self.reputation_score - 0.05)
    
    def connect_to_peer(self, peer_agent):
        """Connect to another agent in the collective."""
        self.peers.add(peer_agent)
    
    def share_intelligence(self, threat_data):
        """
        Share threat intelligence with connected peers.
        
        Args:
            threat_data (dict): Threat information to share
        """
        for peer in self.peers:
            try:
                peer.receive_intelligence(threat_data)
            except Exception as e:
                print(f"Failed to share with {peer.agent_id}: {e}")
    
    def receive_intelligence(self, threat_data):
        """
        Receive threat intelligence from another agent.
        
        Args:
            threat_data (dict): Threat information received
        """
        # Process received intelligence and update models if needed
        print(f"Agent {self.agent_id} received threat data: {threat_data}")
        self.reputation_score = min(1.0, self.reputation_score + 0.01)

# Collective Management Class
class AgentCollective:
    """
    Manages a decentralized collective of AI agents.
    """
    
    def __init__(self, blockchain_network):
        self.blockchain_network = blockchain_network
        self.agents = {}
        self.consensus_threshold = 0.6  # Minimum consensus percentage
        
    def register_agent(self, agent):
        """Register a new agent to the collective."""
        if agent.agent_id in self.agents:
            raise ValueError(f"Agent {agent.agent_id} already registered")
        
        self.agents[agent.agent_id] = agent
        self._connect_to_random_peers(agent, min(3, len(self.agents)))
        
    def _connect_to_random_peers(self, agent, num_peers):
        """Connect agent to random peers in the collective."""
        if len(self.agents) <= 1:
            return
            
        other_agents = [a for a in self.agents.values() if a != agent]
        peers = random.sample(other_agents, min(num_peers, len(other_agents)))
        
        for peer in peers:
            agent.connect_to_peer(peer)
            peer.connect_to_peer(agent)
    
    def analyze_transaction(self, tx_data):
        """
        Perform decentralized analysis of a transaction.
        
        Args:
            tx_data (dict): Transaction data to analyze
            
        Returns:
            dict: Consensus-based threat assessment
        """
        results = []
        for agent in self.agents.values():
            try:
                result = agent.monitor_transaction(tx_data)
                if 'error' not in result:
                    results.append(result)
            except Exception as e:
                print(f"Agent {agent.agent_id} failed: {e}")
        
        return self._reach_consensus(results)
    
    def _reach_consensus(self, agent_results):
        """
        Reach consensus among agents' threat assessments.
        
        Args:
            agent_results (list): List of individual agent results
            
        Returns:
            dict: Consensus result with threat level and confidence
        """
        if not agent_results:
            return {'threat_level': 'unknown', 'confidence': 0.0}
        
        # Group by threat level and calculate weighted confidence
        threat_counts = {}
        total_weight = 0.0
        
        for result in agent_results:
            level = result['threat_level']
            weight = result['confidence']
            
            if level not in threat_counts:
                threat_counts[level] = 0.0
            threat_counts[level] += weight
            total_weight += weight
        
        if total_weight == 0:
            return {'threat_level': 'unknown', 'confidence': 0.0}
        
        # Normalize and find consensus
        normalized = {k: v/total_weight for k, v in threat_counts.items()}
        max_level = max(normalized.items(), key=lambda x: x[1])
        
        if max_level[1] >= self.consensus_threshold:
            return {
                'threat_level': max_level[0],
                'confidence': max_level[1],
                'consensus_reached': True
            }
        
        # No clear consensus - return weighted average
        return {
            'threat_level': 'uncertain',
            'confidence': max_level[1],
            'consensus_reached': False,
            'detailed_breakdown': normalized
        }

# Blockchain Monitor Class
class BlockchainMonitor:
    """
    Monitors blockchain for transactions and coordinates agent analysis.
    """
    
    def __init__(self, collective, rpc_endpoint):
        self.collective = collective
        self.rpc_endpoint = rpc_endpoint
        self.last_processed_block = 0
        self.threat_history = []
    
    def start_monitoring(self):
        """Start continuous blockchain monitoring."""
        while True:
            try:
                latest_block = self._get_latest_block()
                if latest_block > self.last_processed_block:
                    self._process_new_blocks()
            except Exception as e:
                print(f"Monitoring error: {e}")
                time.sleep(10)  # Backoff on error
    
    def _get_latest_block(self):
        """Get latest block number from blockchain node."""
        # In production, this would make an actual RPC call
        return self.last_processed_block + 1
    
    def _process_new_blocks(self):
        """Process new blocks since last check."""
        # Simulate getting new transactions
        new_transactions = [
            {'hash': f'tx{random.randint(1000,9999)}', 'value': random.randint(1, 100)},
            {'hash': f'tx{random.randint(1000,9999)}', 'value': random.randint(1, 100)}
        ]
        
        for tx in new_transactions:
            result = self.collective.analyze_transaction(tx)
            self._handle_threat_result(tx, result)
        
        self.last_processed_block += 1
    
    def _handle_threat_result(self, tx_data, threat_result):
        """Handle threat detection results."""
        record = {
            'transaction': tx_data,
            'analysis': threat_result,
            'timestamp': datetime.datetime.now().isoformat()
        }
        self.threat_history.append(record)
        
        if threat_result.get('threat_level') in ['high
