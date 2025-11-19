"""
Generated Code Metadata:
========================
Original URL: https://bafybeidkluyc2gkefycv52fvj3nk7xoueso5zyflbwmt7hgzgicddg3hxy.ipfs.dweb.link
Prompt: "Recommend a suitable io.net cluster configuration for a large-scale language model training task, considering factors like GPU type, memory, and connectivity performance."
Generated: DETERMINISTIC_4c4e8648fcc6f329
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class GPUConfig:
    """Configuration for GPU specifications."""
    name: str
    vram_gb: int
    bandwidth_gbps: float
    cuda_cores: int
    price_per_hour: float

@dataclass
class NodeConfig:
    """Configuration for a single node in the cluster."""
    gpu_type: GPUConfig
    gpu_count: int
    cpu_cores: int
    system_memory_gb: int
    network_bandwidth_gbps: float

@dataclass
class ClusterConfig:
    """Full cluster configuration."""
    nodes: List[NodeConfig]
    total_gpus: int
    estimated_cost_per_hour: float
    estimated_training_time_days: float

def get_available_gpu_configs() -> List[GPUConfig]:
    """Returns available GPU configurations."""
    return [
        GPUConfig(
            name="NVIDIA A100 80GB",
            vram_gb=80,
            bandwidth_gbps=2039,
            cuda_cores=6912,
            price_per_hour=3.50
        ),
        GPUConfig(
            name="NVIDIA H100 80GB",
            vram_gb=80,
            bandwidth_gbps=3000,
            cuda_cores=14592,
            price_per_hour=5.00
        ),
        GPUConfig(
            name="NVIDIA V100 32GB",
            vram_gb=32,
            bandwidth_gbps=900,
            cuda_cores=5120,
            price_per_hour=2.00
        ),
    ]

def recommend_cluster(
    model_size_billion: int,
    batch_size: int,
    training_data_size_tb: int,
    budget_per_hour: Optional[float] = None,
    min_vram_per_gpu: Optional[int] = None
) -> ClusterConfig:
    """
    Recommends a cluster configuration based on training requirements.
    
    Args:
        model_size_billion: Size of the model in billions of parameters
        batch_size: Desired batch size for training
        training_data_size_tb: Size of training dataset in TB
        budget_per_hour: Optional hourly budget constraint
        min_vram_per_gpu: Optional minimum VRAM per GPU requirement
        
    Returns:
        Recommended ClusterConfig
    """
    available_gpus = get_available_gpu_configs()
    
    # Filter GPUs based on constraints
    candidate_gpus = available_gpus
    if min_vram_per_gpu:
        candidate_gpus = [g for g in candidate_gpus if g.vram_gb >= min_vram_per_gpu]
    
    # Estimate required VRAM per GPU
    estimated_vram_per_gpu = (model_size_billion * 1.5) / batch_size  # Simplified estimation
    
    # Further filter GPUs based on VRAM requirements
    candidate_gpus = [g for g in candidate_gpus if g.vram_gb >= estimated_vram_per_gpu]
    
    if not candidate_gpus:
        raise ValueError("No suitable GPUs found for the given requirements")
    
    # Select best GPU based on bandwidth (proxy for performance)
    selected_gpu = max(candidate_gpus, key=lambda g: g.bandwidth_gbps)
    
    # Estimate number of GPUs needed based on data size
    estimated_gpus = max(8, min(64, int(training_data_size_tb * 2)))
    
    # Adjust for budget if specified
    if budget_per_hour:
        max_gpus = int(budget_per_hour / selected_gpu.price_per_hour)
        estimated_gpus = min(estimated_gpus, max_gpus)
    
    # Create node configuration (8 GPUs per node is common)
    nodes_per_gpu = 8
    node_count = (estimated_gpus + nodes_per_gpu - 1) // nodes_per_gpu
    actual_gpus = node_count * nodes_per_gpu
    
    nodes = [
        NodeConfig(
            gpu_type=selected_gpu,
            gpu_count=nodes_per_gpu,
            cpu_cores=64,
            system_memory_gb=512,
            network_bandwidth_gbps=100
        )
        for _ in range(node_count)
    ]
    
    # Estimate training time (simplified)
    training_time_days = (model_size_billion * training_data_size_tb) / (actual_gpus * selected_gpu.bandwidth_gbps * 0.1)
    
    return ClusterConfig(
        nodes=nodes,
        total_gpus=actual_gpus,
        estimated_cost_per_hour=actual_gpus * selected_gpu.price_per_hour,
        estimated_training_time_days=max(1, training_time_days)
    )

def main():
    parser = argparse.ArgumentParser(description="Cluster Configuration Recommender for LLM Training")
    parser.add_argument("--model_size", type=int, required=True, help="Model size in billions of parameters")
    parser.add_argument("--batch_size", type=int, required=True, help="Training batch size")
    parser.add_argument("--data_size", type=int, required=True, help="Training data size in TB")
    parser.add_argument("--budget", type=float, help="Optional hourly budget constraint")
    parser.add_argument("--min_vram", type=int, help="Optional minimum VRAM per GPU in GB")
    
    args = parser.parse_args()
    
    try:
        config = recommend_cluster(
            model_size_billion=args.model_size,
            batch_size=args.batch_size,
            training_data_size_tb=args.data_size,
            budget_per_hour=args.budget,
            min_vram_per_gpu=args.min_vram
        )
        
        print("\nRecommended Cluster Configuration:")
        print(f"GPU Type: {config.nodes[0].gpu_type.name}")
        print(f"Total GPUs: {config.total_gpus}")
        print(f"Nodes: {len(config.nodes)}")
        print(f"GPUs per Node: {config.nodes[0].gpu_count}")
        print(f"Estimated Cost/Hour: ${config.estimated_cost_per_hour:.2f}")
        print(f"Estimated Training Time: {config.estimated_training_time_days:.1f} days")
        
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
