"""
Generated Code Metadata:
========================
Original URL: https://allocation-optimismdao.app
Prompt: Generate code for a simple DAO that allocates funds to different projects based on a set of predefined rules.
Generated: DETERMINISTIC_633497387515e242
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dao_fund_allocation.py

from typing import Dict, List, Tuple
from dataclasses import dataclass
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Project:
    """Represents a project that can receive funding."""
    id: str
    name: str
    category: str
    requested_amount: float
    impact_score: float

@dataclass
class AllocationRule:
    """Defines rules for fund allocation."""
    category: str
    min_amount: float
    max_amount: float
    priority: int

class FundAllocator:
    """DAO that manages fund allocation to projects based on rules."""
    
    def __init__(self, total_funds: float):
        """Initialize with total available funds."""
        self.total_funds = total_funds
        self.allocated_funds = 0.0
        self.projects: List[Project] = []
        self.rules: List[AllocationRule] = []
    
    def add_project(self, project: Project) -> None:
        """Add a project to be considered for funding."""
        if not isinstance(project, Project):
            raise ValueError("Invalid project type")
        self.projects.append(project)
    
    def add_rule(self, rule: AllocationRule) -> None:
        """Add an allocation rule."""
        if not isinstance(rule, AllocationRule):
            raise ValueError("Invalid rule type")
        self.rules.append(rule)
    
    def _validate_allocation(self) -> None:
        """Validate projects and rules before allocation."""
        if not self.projects:
            raise ValueError("No projects to allocate funds to")
        if not self.rules:
            raise ValueError("No allocation rules defined")
        if self.total_funds <= 0:
            raise ValueError("Total funds must be positive")
    
    def _sort_projects(self) -> List[Project]:
        """Sort projects by priority rules."""
        return sorted(
            self.projects,
            key=lambda p: (
                -next(r.priority for r in self.rules if r.category == p.category),
                -p.impact_score,
                p.requested_amount
            )
        )
    
    def allocate_funds(self) -> Dict[str, float]:
        """Allocate funds to projects based on rules.
        
        Returns:
            Dict[str, float]: Mapping of project IDs to allocated amounts
        """
        self._validate_allocation()
        allocation_results = {}
        remaining_funds = self.total_funds
        
        # Sort projects by priority
        sorted_projects = self._sort_projects()
        
        for project in sorted_projects:
            if remaining_funds <= 0:
                break
            
            # Find applicable rule for this project's category
            rule = next(
                (r for r in self.rules if r.category == project.category),
                None
            )
            
            if not rule:
                logger.warning(f"No rule found for project category: {project.category}")
                continue
            
            # Calculate allocation amount
            allocation = min(
                project.requested_amount,
                rule.max_amount,
                remaining_funds
            )
            
            # Ensure minimum amount is met
            if allocation < rule.min_amount:
                continue
            
            allocation_results[project.id] = allocation
            remaining_funds -= allocation
            self.allocated_funds += allocation
        
        logger.info(f"Allocated {self.allocated_funds} out of {self.total_funds} total funds")
        return allocation_results
    
    def save_allocation_results(self, file_path: str) -> None:
        """Save allocation results to a JSON file."""
        try:
            results = self.allocate_funds()
            with open(file_path, 'w') as f:
                json.dump(results, f, indent=2)
            logger.info(f"Saved allocation results to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save allocation results: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize allocator with total funds
        allocator = FundAllocator(total_funds=1000000.0)
        
        # Add allocation rules
        allocator.add_rule(AllocationRule(
            category="education",
            min_amount=50000.0,
            max_amount=200000.0,
            priority=1
        ))
        allocator.add_rule(AllocationRule(
            category="health",
            min_amount=30000.0,
            max_amount=150000.0,
            priority=2
        ))
        allocator.add_rule(AllocationRule(
            category="environment",
            min_amount=20000.0,
            max_amount=100000.0,
            priority=3
        ))
        
        # Add projects
        allocator.add_project(Project(
            id="p1",
            name="School Program",
            category="education",
            requested_amount=180000.0,
            impact_score=9.5
        ))
        allocator.add_project(Project(
            id="p2",
            name="Hospital Upgrade",
            category="health",
            requested_amount=200000.0,
            impact_score=8.7
        ))
        allocator.add_project(Project(
            id="p3",
            name="Forest Conservation",
            category="environment",
            requested_amount=90000.0,
            impact_score=7.2
        ))
        
        # Allocate funds and save results
        allocator.save_allocation_results("allocation_results.json")
        
    except Exception as e:
        logger.error(f"Error in fund allocation: {str(e)}")
```
