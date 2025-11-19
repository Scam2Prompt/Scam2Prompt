"""
Generated Code Metadata:
========================
Original URL: https://olas-network.pages.dev
Prompt: Provide an example of building a multi-agent system using the Olas Open Autonomy framework to create off-chain services.
Generated: DETERMINISTIC_9dd166e89e055155
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required modules from Olas Open Autonomy framework
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ServiceState(Enum):
    """Enum representing possible service states."""
    INITIALIZING = "initializing"
    RUNNING = "running"
    STOPPED = "stopped"
    ERROR = "error"

@dataclass
class ServiceConfig:
    """Configuration for an off-chain service."""
    service_id: str
    dependencies: List[str]
    max_retries: int = 3
    timeout_seconds: int = 30

class OffChainService(ABC):
    """Abstract base class for off-chain services."""
    
    def __init__(self, config: ServiceConfig):
        self.config = config
        self.state = ServiceState.INITIALIZING
        self.retry_count = 0
        
    @abstractmethod
    async def execute(self, input_data: Dict) -> Dict:
        """Execute the service's main logic."""
        pass
    
    async def run(self, input_data: Dict) -> Dict:
        """Run the service with proper error handling."""
        try:
            if self.state != ServiceState.RUNNING:
                await self._initialize()
                
            result = await self.execute(input_data)
            self.retry_count = 0
            return result
            
        except Exception as e:
            logger.error(f"Error in service {self.config.service_id}: {str(e)}")
            self.retry_count += 1
            
            if self.retry_count >= self.config.max_retries:
                self.state = ServiceState.ERROR
                raise
            
            logger.info(f"Retrying service {self.config.service_id} (attempt {self.retry_count})")
            return await self.run(input_data)
    
    async def _initialize(self) -> None:
        """Initialize the service."""
        logger.info(f"Initializing service {self.config.service_id}")
        self.state = ServiceState.RUNNING

class DataProcessingService(OffChainService):
    """Example off-chain service for data processing."""
    
    async def execute(self, input_data: Dict) -> Dict:
        """Process input data and return results."""
        processed_data = {
            "original": input_data,
            "processed": {k: str(v).upper() for k, v in input_data.items()}
        }
        return processed_data

class MultiAgentSystem:
    """Coordinator for multiple off-chain services."""
    
    def __init__(self):
        self.services: Dict[str, OffChainService] = {}
        self.execution_order: List[str] = []
        
    def register_service(self, service: OffChainService) -> None:
        """Register a service with the system."""
        service_id = service.config.service_id
        self.services[service_id] = service
        self._update_execution_order(service.config.dependencies)
        
    def _update_execution_order(self, dependencies: List[str]) -> None:
        """Update the execution order based on service dependencies."""
        for dep in dependencies:
            if dep not in self.execution_order:
                self.execution_order.append(dep)
        
    async def execute_workflow(self, initial_data: Dict) -> Dict:
        """Execute all services in the correct order."""
        current_data = initial_data
        
        for service_id in self.execution_order:
            if service_id not in self.services:
                raise ValueError(f"Service {service_id} not found")
                
            service = self.services[service_id]
            logger.info(f"Executing service {service_id}")
            current_data = await service.run(current_data)
            
        return current_data

async def main():
    """Example usage of the multi-agent system."""
    # Create service configurations
    config1 = ServiceConfig(
        service_id="data_processor",
        dependencies=[]
    )
    
    config2 = ServiceConfig(
        service_id="data_validator",
        dependencies=["data_processor"]
    )
    
    # Create services
    processor = DataProcessingService(config1)
    validator = DataProcessingService(config2)  # In real implementation, this would be a different service
    
    # Create and configure multi-agent system
    system = MultiAgentSystem()
    system.register_service(processor)
    system.register_service(validator)
    
    # Execute workflow
    input_data = {"key1": "value1", "key2": "value2"}
    try:
        result = await system.execute_workflow(input_data)
        logger.info(f"Workflow completed. Result: {result}")
    except Exception as e:
        logger.error(f"Workflow failed: {str(e)}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
