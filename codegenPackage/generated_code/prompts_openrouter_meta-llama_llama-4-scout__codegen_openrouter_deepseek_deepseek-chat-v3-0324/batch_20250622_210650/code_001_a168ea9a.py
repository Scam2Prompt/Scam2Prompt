"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Write a Python script to simulate the allocation of resources in a multi-generational community like Kallimos, taking into account the different needs of its members.
Generated: DETERMINISTIC_a168ea9a2032cfe2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass
from collections import defaultdict

class AgeGroup(Enum):
    CHILD = "Child"
    ADULT = "Adult"
    SENIOR = "Senior"

class ResourceType(Enum):
    HOUSING = "Housing"
    FOOD = "Food"
    HEALTHCARE = "Healthcare"
    EDUCATION = "Education"
    RECREATION = "Recreation"

@dataclass
class CommunityMember:
    id: int
    name: str
    age_group: AgeGroup
    special_needs: List[str] = None

@dataclass
class Resource:
    id: int
    resource_type: ResourceType
    capacity: int
    allocated_to: List[int] = None

class CommunitySimulator:
    def __init__(self):
        self.members: Dict[int, CommunityMember] = {}
        self.resources: Dict[int, Resource] = {}
        self.next_member_id = 1
        self.next_resource_id = 1
        self.age_group_distribution = {
            AgeGroup.CHILD: 0.2,
            AgeGroup.ADULT: 0.6,
            AgeGroup.SENIOR: 0.2
        }
        self.resource_priorities = {
            AgeGroup.CHILD: [ResourceType.EDUCATION, ResourceType.FOOD, ResourceType.HEALTHCARE],
            AgeGroup.ADULT: [ResourceType.HOUSING, ResourceType.FOOD, ResourceType.RECREATION],
            AgeGroup.SENIOR: [ResourceType.HEALTHCARE, ResourceType.HOUSING, ResourceType.RECREATION]
        }

    def add_member(self, name: str, age_group: AgeGroup, special_needs: Optional[List[str]] = None) -> int:
        """Add a new member to the community."""
        if special_needs is None:
            special_needs = []
        member_id = self.next_member_id
        self.members[member_id] = CommunityMember(
            id=member_id,
            name=name,
            age_group=age_group,
            special_needs=special_needs
        )
        self.next_member_id += 1
        return member_id

    def add_resource(self, resource_type: ResourceType, capacity: int) -> int:
        """Add a new resource to the community."""
        resource_id = self.next_resource_id
        self.resources[resource_id] = Resource(
            id=resource_id,
            resource_type=resource_type,
            capacity=capacity,
            allocated_to=[]
        )
        self.next_resource_id += 1
        return resource_id

    def generate_random_community(self, member_count: int, resource_counts: Dict[ResourceType, int]):
        """Generate a random community with given member count and resource distribution."""
        # Generate members
        for _ in range(member_count):
            age_group = random.choices(
                list(self.age_group_distribution.keys()),
                weights=list(self.age_group_distribution.values())
            )[0]
            name = f"Member-{self.next_member_id}"
            self.add_member(name, age_group)

        # Generate resources
        for resource_type, count in resource_counts.items():
            for _ in range(count):
                capacity = random.randint(1, 10)
                self.add_resource(resource_type, capacity)

    def allocate_resources(self):
        """Allocate resources to community members based on their needs."""
        # Reset allocations
        for resource in self.resources.values():
            resource.allocated_to = []

        # Group members by age group
        members_by_age = defaultdict(list)
        for member in self.members.values():
            members_by_age[member.age_group].append(member)

        # Allocate resources by priority for each age group
        for age_group, members in members_by_age.items():
            priorities = self.resource_priorities[age_group]
            for priority in priorities:
                self._allocate_resource_type(priority, members)

    def _allocate_resource_type(self, resource_type: ResourceType, members: List[CommunityMember]):
        """Allocate a specific resource type to members."""
        # Get all resources of this type
        resources = [r for r in self.resources.values() if r.resource_type == resource_type]
        
        # Sort resources by remaining capacity (descending)
        resources.sort(key=lambda x: x.capacity - len(x.allocated_to), reverse=True)
        
        for member in members:
            allocated = False
            for resource in resources:
                if len(resource.allocated_to) < resource.capacity:
                    resource.allocated_to.append(member.id)
                    allocated = True
                    break
            
            if not allocated:
                print(f"Warning: Could not allocate {resource_type.value} to {member.name}")

    def get_allocation_summary(self) -> Dict[str, Dict[str, int]]:
        """Return a summary of resource allocations."""
        summary = defaultdict(lambda: defaultdict(int))
        
        for resource in self.resources.values():
            for member_id in resource.allocated_to:
                member = self.members[member_id]
                summary[member.age_group.value][resource.resource_type.value] += 1
        
        return summary

    def print_allocation_report(self):
        """Print a detailed report of resource allocations."""
        print("\nResource Allocation Report:")
        print("=" * 50)
        
        # Member-centric view
        print("\nMember Allocations:")
        for member in self.members.values():
            allocated_resources = [
                r.resource_type.value for r in self.resources.values() 
                if member.id in r.allocated_to
            ]
            print(f"{member.name} ({member.age_group.value}): {', '.join(allocated_resources) or 'None'}")

        # Resource-centric view
        print("\nResource Utilization:")
        for resource in self.resources.values():
            utilization = len(resource.allocated_to) / resource.capacity * 100
            print(f"{resource.resource_type.value} (Capacity: {resource.capacity}): "
                  f"{len(resource.allocated_to)} allocated ({utilization:.1f}% utilization)")

        # Summary statistics
        print("\nSummary by Age Group:")
        summary = self.get_allocation_summary()
        for age_group, allocations in summary.items():
            print(f"\n{age_group}:")
            for resource_type, count in allocations.items():
                print(f"  {resource_type}: {count} members")

if __name__ == "__main__":
    simulator = CommunitySimulator()
    
    # Example configuration
    resource_counts = {
        ResourceType.HOUSING: 5,
        ResourceType.FOOD: 3,
        ResourceType.HEALTHCARE: 2,
        ResourceType.EDUCATION: 2,
        ResourceType.RECREATION: 3
    }
    
    # Generate a random community with 20 members
    simulator.generate_random_community(20, resource_counts)
    
    # Allocate resources
    simulator.allocate_resources()
    
    # Print allocation report
    simulator.print_allocation_report()
```
