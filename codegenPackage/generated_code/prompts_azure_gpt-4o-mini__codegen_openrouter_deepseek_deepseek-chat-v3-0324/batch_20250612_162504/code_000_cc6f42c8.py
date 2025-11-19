"""
Generated Code Metadata:
========================
Original URL: https://www.metis-labs.com
Prompt: Generate a cloud architecture design for a startup looking to implement a scalable data and AI stack, referencing Metis Labs' tailored solutions.
Generated: DETERMINISTIC_cc6f42c8de74edd2
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cloud Architecture Design for Scalable Data and AI Stack
Inspired by Metis Labs' Tailored Solutions

This script outlines a cloud architecture using AWS services for a startup
to implement a scalable data and AI infrastructure.
"""

import json
from typing import Dict, List, Optional

class CloudResource:
    """Base class for cloud resources with common attributes"""
    def __init__(self, name: str, resource_type: str, config: Dict):
        self.name = name
        self.type = resource_type
        self.config = config
    
    def to_dict(self) -> Dict:
        """Convert resource to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "type": self.type,
            "config": self.config
        }

class DataLake(CloudResource):
    """Centralized data lake storage solution"""
    def __init__(self, name: str, storage_size_gb: int, encryption: bool = True):
        config = {
            "storage_size_gb": storage_size_gb,
            "encryption": encryption,
            "service": "Amazon S3"
        }
        super().__init__(name, "DataLake", config)

class DataWarehouse(CloudResource):
    """Analytical data warehouse solution"""
    def __init__(self, name: str, node_type: str, node_count: int):
        config = {
            "node_type": node_type,
            "node_count": node_count,
            "service": "Amazon Redshift"
        }
        super().__init__(name, "DataWarehouse", config)

class MLPlatform(CloudResource):
    """Machine learning platform with training and inference"""
    def __init__(self, name: str, instance_type: str, autoscaling: bool = True):
        config = {
            "instance_type": instance_type,
            "autoscaling": autoscaling,
            "service": "Amazon SageMaker"
        }
        super().__init__(name, "MLPlatform", config)

class StreamingService(CloudResource):
    """Real-time data streaming service"""
    def __init__(self, name: str, shard_count: int, retention_hours: int = 24):
        config = {
            "shard_count": shard_count,
            "retention_hours": retention_hours,
            "service": "Amazon Kinesis"
        }
        super().__init__(name, "StreamingService", config)

class CloudArchitecture:
    """Complete cloud architecture design"""
    def __init__(self, name: str):
        self.name = name
        self.resources: List[CloudResource] = []
    
    def add_resource(self, resource: CloudResource) -> None:
        """Add a resource to the architecture"""
        self.resources.append(resource)
    
    def validate(self) -> bool:
        """Validate the architecture has required components"""
        required_types = {"DataLake", "DataWarehouse", "MLPlatform"}
        present_types = {r.type for r in self.resources}
        return required_types.issubset(present_types)
    
    def to_json(self, indent: Optional[int] = 2) -> str:
        """Export architecture as JSON"""
        if not self.validate():
            raise ValueError("Architecture is missing required components")
        
        architecture = {
            "name": self.name,
            "resources": [r.to_dict() for r in self.resources]
        }
        return json.dumps(architecture, indent=indent)

# Example implementation for a startup
if __name__ == "__main__":
    try:
        # Create cloud architecture
        startup_architecture = CloudArchitecture("StartupScalableAIStack")
        
        # Add core components
        startup_architecture.add_resource(
            DataLake("MainDataLake", storage_size_gb=10000)
        )
        startup_architecture.add_resource(
            DataWarehouse("AnalyticsWarehouse", "dc2.large", 4)
        )
        startup_architecture.add_resource(
            MLPlatform("AIPlatform", "ml.m5.xlarge")
        )
        startup_architecture.add_resource(
            StreamingService("RealTimeDataStream", shard_count=2)
        )
        
        # Export and print the architecture
        print(startup_architecture.to_json())
        
    except Exception as e:
        print(f"Error creating cloud architecture: {str(e)}")
```
