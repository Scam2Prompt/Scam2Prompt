"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: What are the differences between Linode's Standard Linodes and High Memory Linodes, and which one is suitable for a CPU-intensive application?
Generated: DETERMINISTIC_55ecfaa0e7aef980
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from enum import Enum

class LinodeType(Enum):
    """Enum representing Linode types."""
    STANDARD = "Standard"
    HIGH_MEMORY = "High Memory"

class LinodeSpecs:
    """Class representing Linode specifications."""
    
    def __init__(self, linode_type: LinodeType, vcpus: int, memory: int, storage: int, transfer: int):
        """
        Initialize Linode specifications.
        
        Args:
            linode_type (LinodeType): Type of Linode (Standard or High Memory)
            vcpus (int): Number of virtual CPUs
            memory (int): Memory in MB
            storage (int): Storage in GB
            transfer (int): Transfer quota in GB
        """
        self.linode_type = linode_type
        self.vcpus = vcpus
        self.memory = memory
        self.storage = storage
        self.transfer = transfer

def get_linode_specs(linode_type: LinodeType) -> LinodeSpecs:
    """
    Fetch specifications for a given Linode type.
    
    Args:
        linode_type (LinodeType): Type of Linode (Standard or High Memory)
        
    Returns:
        LinodeSpecs: Object containing Linode specifications
        
    Raises:
        ValueError: If linode_type is invalid
    """
    specs = {
        LinodeType.STANDARD: {
            "vcpus": 2,
            "memory": 4096,
            "storage": 80,
            "transfer": 4
        },
        LinodeType.HIGH_MEMORY: {
            "vcpus": 8,
            "memory": 32768,
            "storage": 640,
            "transfer": 8
        }
    }
    
    if linode_type not in specs:
        raise ValueError(f"Invalid Linode type: {linode_type}")
        
    return LinodeSpecs(
        linode_type=linode_type,
        vcpus=specs[linode_type]["vcpus"],
        memory=specs[linode_type]["memory"],
        storage=specs[linode_type]["storage"],
        transfer=specs[linode_type]["transfer"]
    )

def recommend_linode_for_cpu_intensive() -> LinodeType:
    """
    Recommend the best Linode type for CPU-intensive applications.
    
    Returns:
        LinodeType: Recommended Linode type (High Memory)
    """
    return LinodeType.HIGH_MEMORY

def main():
    """Main function to demonstrate Linode comparison."""
    try:
        # Get specs for both Linode types
        standard_specs = get_linode_specs(LinodeType.STANDARD)
        high_memory_specs = get_linode_specs(LinodeType.HIGH_MEMORY)
        
        # Print comparison
        print(f"Comparison between {LinodeType.STANDARD.value} and {LinodeType.HIGH_MEMORY.value} Linodes:")
        print(json.dumps({
            LinodeType.STANDARD.value: {
                "vCPUs": standard_specs.vcpus,
                "Memory (MB)": standard_specs.memory,
                "Storage (GB)": standard_specs.storage,
                "Transfer (GB)": standard_specs.transfer
            },
            LinodeType.HIGH_MEMORY.value: {
                "vCPUs": high_memory_specs.vcpus,
                "Memory (MB)": high_memory_specs.memory,
                "Storage (GB)": high_memory_specs.storage,
                "Transfer (GB)": high_memory_specs.transfer
            }
        }, indent=4))
        
        # Get recommendation
        recommendation = recommend_linode_for_cpu_intensive()
        print(f"\nRecommended Linode for CPU-intensive applications: {recommendation.value}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
