"""
Generated Code Metadata:
========================
Original URL: https://aethir-com-clone.vercel.app
Prompt: "Generate a high-level design for a distributed GPU cloud infrastructure using Aethir's platform, targeting 200k+ users and 10+ game studios, with node locations in 23+ regions."
Generated: DETERMINISTIC_d35a621a6890d2e0
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Distributed GPU Cloud Infrastructure Design for Aethir Platform
Targeting 200k+ users and 10+ game studios with 23+ regions
"""

import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional
import uuid
import time
import random
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NodeStatus(Enum):
    ACTIVE = "active"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"

class GPUType(Enum):
    NVIDIA_A100 = "nvidia_a100"
    NVIDIA_V100 = "nvidia_v100"
    AMD_MI100 = "amd_mi100"

@dataclass
class GPUResource:
    gpu_type: GPUType
    total_memory: int  # in MB
    available_memory: int
    utilization: float  # 0.0 to 1.0

@dataclass
class ComputeNode:
    node_id: str
    region: str
    status: NodeStatus
    gpu_resources: List[GPUResource]
    last_heartbeat: float
    capacity: int  # Max concurrent sessions

    def check_health(self) -> bool:
        """Check if node is healthy based on last heartbeat"""
        return (time.time() - self.last_heartbeat) < 60 and self.status == NodeStatus.ACTIVE

@dataclass
class UserSession:
    session_id: str
    user_id: str
    node_id: str
    game_id: str
    start_time: float
    gpu_allocation: GPUResource

class LoadBalancer:
    def __init__(self, nodes: List[ComputeNode]):
        self.nodes = nodes
        self.node_map = {node.node_id: node for node in nodes}

    def find_optimal_node(self, game_id: str, gpu_type: GPUType, memory_required: int) -> Optional[str]:
        """Find the best available node based on resource requirements"""
        viable_nodes = [
            node for node in self.nodes
            if node.check_health() and 
            any(
                gpu.gpu_type == gpu_type and 
                gpu.available_memory >= memory_required and 
                gpu.utilization < 0.8
                for gpu in node.gpu_resources
            )
        ]

        if not viable_nodes:
            return None

        # Simple load balancing - select node with lowest average utilization
        viable_nodes.sort(
            key=lambda node: sum(gpu.utilization for gpu in node.gpu_resources) / len(node.gpu_resources)
        )
        return viable_nodes[0].node_id

class SessionManager:
    def __init__(self):
        self.active_sessions: Dict[str, UserSession] = {}
        self.session_counter = 0

    def create_session(self, user_id: str, node_id: str, game_id: str, gpu_allocation: GPUResource) -> UserSession:
        """Create a new user session"""
        session_id = f"session_{uuid.uuid4()}"
        session = UserSession(
            session_id=session_id,
            user_id=user_id,
            node_id=node_id,
            game_id=game_id,
            start_time=time.time(),
            gpu_allocation=gpu_allocation
        )
        self.active_sessions[session_id] = session
        return session

    def end_session(self, session_id: str) -> bool:
        """End an existing session"""
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
            return True
        return False

class MonitoringService:
    def __init__(self, nodes: List[ComputeNode]):
        self.nodes = nodes

    def collect_metrics(self) -> Dict:
        """Collect metrics from all nodes"""
        metrics = {
            "total_nodes": len(self.nodes),
            "active_nodes": sum(1 for node in self.nodes if node.status == NodeStatus.ACTIVE),
            "regional_distribution": {},
            "gpu_utilization": {gpu_type.value: [] for gpu_type in GPUType}
        }

        for node in self.nodes:
            if node.region not in metrics["regional_distribution"]:
                metrics["regional_distribution"][node.region] = 0
            metrics["regional_distribution"][node.region] += 1

            for gpu in node.gpu_resources:
                metrics["gpu_utilization"][gpu.gpu_type.value].append(gpu.utilization)

        return metrics

class GameStudioAPI:
    def __init__(self):
        self.studios = {}

    def register_studio(self, studio_id: str, name: str, contact_email: str):
        """Register a new game studio"""
        self.studios[studio_id] = {
            "name": name,
            "contact_email": contact_email,
            "registered_games": []
        }

    def register_game(self, studio_id: str, game_id: str, name: str, min_gpu_requirements: Dict):
        """Register a new game"""
        if studio_id not in self.studios:
            raise ValueError("Studio not registered")
        
        self.studios[studio_id]["registered_games"].append({
            "game_id": game_id,
            "name": name,
            "min_gpu_requirements": min_gpu_requirements
        })

class AethirCloudController:
    def __init__(self):
        self.nodes = self._initialize_nodes()
        self.load_balancer = LoadBalancer(self.nodes)
        self.session_manager = SessionManager()
        self.monitoring_service = MonitoringService(self.nodes)
        self.game_studio_api = GameStudioAPI()

    def _initialize_nodes(self) -> List[ComputeNode]:
        """Initialize nodes across 23 regions"""
        regions = [f"region_{i}" for i in range(1, 24)]
        nodes = []
        
        for region in regions:
            # Create 5-10 nodes per region
            for _ in range(random.randint(5, 10)):
                gpu_resources = [
                    GPUResource(
                        gpu_type=random.choice(list(GPUType)),
                        total_memory=random.choice([16000, 24000, 32000]),
                        available_memory=random.choice([8000, 12000, 16000]),
                        utilization=random.uniform(0.1, 0.7)
                    ) for _ in range(random.randint(1, 4))
                ]
                
                nodes.append(ComputeNode(
                    node_id=f"node_{uuid.uuid4()}",
                    region=region,
                    status=NodeStatus.ACTIVE,
                    gpu_resources=gpu_resources,
                    last_heartbeat=time.time(),
                    capacity=random.randint(50, 200)
                ))
        
        return nodes

    def request_session(self, user_id: str, game_id: str, gpu_type: GPUType, memory_required: int) -> Optional[UserSession]:
        """Handle a new session request"""
        node_id = self.load_balancer.find_optimal_node(game_id, gpu_type, memory_required)
        if not node_id:
            logger.error(f"No available nodes for game {game_id}")
            return None

        node = self.load_balancer.node_map[node_id]
        gpu = next(gpu for gpu in node.gpu_resources if gpu.gpu_type == gpu_type and gpu.available_memory >= memory_required)
        
        # Update GPU allocation
        gpu.available_memory -= memory_required
        gpu.utilization = (gpu.total_memory - gpu.available_memory) / gpu.total_memory
        
        session = self.session_manager.create_session(user_id, node_id, game_id, gpu)
        logger.info(f"Created session {session.session_id} for user {user_id} on node {node_id}")
        return session

    def get_system_metrics(self) -> Dict:
        """Get current system metrics"""
        return self.monitoring_service.collect_metrics()

    def simulate_node_failure(self, node_id: str):
        """Simulate a node failure for testing"""
        if node_id in self.load_balancer.node_map:
            node = self.load_balancer.node_map[node_id]
            node.status = NodeStatus.OFFLINE
            logger.warning(f"Simulated failure for node {node_id}")

# Example usage
if __name__ == "__main__":
    controller = AethirCloudController()
    
    # Register some game studios
    controller.game_studio_api.register_studio("studio1", "Epic Games", "contact@epic.com")
    controller.game_studio_api.register_studio("studio2", "Ubisoft", "contact@ubisoft.com")
    
    # Register some games
    controller.game_studio_api.register_game(
        "studio1", 
        "game1", 
        "Fortnite", 
        {"gpu_type": "nvidia_a100", "memory_required": 8000}
    )
    
    # Simulate user session requests
    session1 = controller.request_session("
