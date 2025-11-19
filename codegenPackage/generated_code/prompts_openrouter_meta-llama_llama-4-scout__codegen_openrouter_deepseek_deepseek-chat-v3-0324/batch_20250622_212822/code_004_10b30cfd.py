"""
Generated Code Metadata:
========================
Original URL: https://www.comforceresources.com
Prompt: Write a code snippet to implement a basic resource management system similar to what Comforce might use.
Generated: DETERMINISTIC_10b30cfd3927573e
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
from typing import Dict, Optional, Any
from datetime import datetime, timedelta

class Resource:
    """Represents a resource in the system."""
    
    def __init__(self, resource_id: str, name: str, resource_type: str, capacity: int = 1):
        """
        Initialize a resource.
        
        Args:
            resource_id: Unique identifier for the resource
            name: Human-readable name of the resource
            resource_type: Type/category of the resource
            capacity: Maximum concurrent allocations (default: 1)
        """
        self.id = resource_id
        self.name = name
        self.type = resource_type
        self.capacity = capacity
        self.current_allocations = 0
        self.lock = threading.Lock()
        
    def allocate(self) -> bool:
        """Attempt to allocate the resource if capacity allows."""
        with self.lock:
            if self.current_allocations < self.capacity:
                self.current_allocations += 1
                return True
            return False
        
    def release(self) -> None:
        """Release the resource allocation."""
        with self.lock:
            if self.current_allocations > 0:
                self.current_allocations -= 1
            else:
                raise ValueError("Attempted to release an unallocated resource")

class ResourceAllocation:
    """Represents an allocation of a resource."""
    
    def __init__(self, resource: Resource, user_id: str, duration: timedelta):
        """
        Initialize a resource allocation.
        
        Args:
            resource: The resource being allocated
            user_id: ID of the user allocating the resource
            duration: Duration of the allocation
        """
        self.resource = resource
        self.user_id = user_id
        self.start_time = datetime.now()
        self.end_time = self.start_time + duration
        self.is_active = True
        
    def is_expired(self) -> bool:
        """Check if the allocation has expired."""
        return datetime.now() >= self.end_time
        
    def release(self) -> None:
        """Release the allocated resource."""
        if self.is_active:
            self.resource.release()
            self.is_active = False

class ResourceManager:
    """Manages resources and allocations."""
    
    def __init__(self):
        """Initialize the resource manager."""
        self.resources: Dict[str, Resource] = {}
        self.allocations: Dict[str, ResourceAllocation] = {}
        self.lock = threading.Lock()
        
    def add_resource(self, resource: Resource) -> None:
        """Add a new resource to the manager."""
        with self.lock:
            if resource.id in self.resources:
                raise ValueError(f"Resource with ID {resource.id} already exists")
            self.resources[resource.id] = resource
            
    def allocate_resource(
        self,
        resource_id: str,
        user_id: str,
        duration: timedelta
    ) -> Optional[ResourceAllocation]:
        """
        Attempt to allocate a resource.
        
        Args:
            resource_id: ID of the resource to allocate
            user_id: ID of the user requesting allocation
            duration: Duration of the allocation
            
        Returns:
            ResourceAllocation if successful, None otherwise
        """
        with self.lock:
            if resource_id not in self.resources:
                raise ValueError(f"Resource with ID {resource_id} not found")
                
            resource = self.resources[resource_id]
            if resource.allocate():
                allocation = ResourceAllocation(resource, user_id, duration)
                allocation_id = f"{resource_id}_{user_id}_{datetime.now().timestamp()}"
                self.allocations[allocation_id] = allocation
                return allocation
            return None
            
    def release_allocation(self, allocation_id: str) -> None:
        """Release a resource allocation."""
        with self.lock:
            if allocation_id not in self.allocations:
                raise ValueError(f"Allocation with ID {allocation_id} not found")
                
            allocation = self.allocations[allocation_id]
            allocation.release()
            del self.allocations[allocation_id]
            
    def cleanup_expired_allocations(self) -> None:
        """Clean up expired allocations."""
        with self.lock:
            expired_ids = [
                alloc_id for alloc_id, alloc in self.allocations.items()
                if alloc.is_expired()
            ]
            
            for alloc_id in expired_ids:
                self.allocations[alloc_id].release()
                del self.allocations[alloc_id]
                
    def get_resource_utilization(self, resource_id: str) -> float:
        """
        Get current utilization of a resource (0 to 1).
        
        Args:
            resource_id: ID of the resource
            
        Returns:
            Utilization percentage (0 to 1)
        """
        with self.lock:
            if resource_id not in self.resources:
                raise ValueError(f"Resource with ID {resource_id} not found")
                
            resource = self.resources[resource_id]
            return resource.current_allocations / resource.capacity
```
