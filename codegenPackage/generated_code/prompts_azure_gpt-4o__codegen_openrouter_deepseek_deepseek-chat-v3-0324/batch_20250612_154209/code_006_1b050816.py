"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Develop an algorithm for strategic cleaning of new and old water pipelines, incorporating the principles of plug cleaning as described by Aktiv Rørteknikk AS.
Generated: DETERMINISTIC_1b050816558a3ada
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Dict, Tuple, Optional
from enum import Enum

class PipelineStatus(Enum):
    NEW = "new"
    OLD = "old"
    CRITICAL = "critical"

class CleaningMethod(Enum):
    PLUG_CLEANING = "plug_cleaning"
    HIGH_PRESSURE = "high_pressure"
    CHEMICAL = "chemical"

class Pipeline:
    def __init__(self, id: str, age: int, diameter: float, length: float, status: PipelineStatus):
        self.id = id
        self.age = age
        self.diameter = diameter
        self.length = length
        self.status = status
        self.last_cleaned = None
        self.contamination_level = 0.0
    
    def update_contamination(self, level: float):
        """Update contamination level (0.0 to 1.0 scale)"""
        self.contamination_level = max(0.0, min(1.0, level))
    
    def set_last_cleaned(self, timestamp: str):
        """Set last cleaned timestamp"""
        self.last_cleaned = timestamp
    
    def get_priority_score(self) -> float:
        """Calculate priority score based on pipeline characteristics"""
        age_factor = min(self.age / 50, 1.0)  # Normalize age factor
        status_factor = {
            PipelineStatus.NEW: 0.2,
            PipelineStatus.OLD: 0.7,
            PipelineStatus.CRITICAL: 1.0
        }[self.status]
        
        return (0.4 * age_factor + 
                0.3 * status_factor + 
                0.3 * self.contamination_level)

class PipelineCleaningScheduler:
    def __init__(self):
        self.pipelines = {}
        self.cleaning_methods = {
            PipelineStatus.NEW: CleaningMethod.PLUG_CLEANING,
            PipelineStatus.OLD: CleaningMethod.HIGH_PRESSURE,
            PipelineStatus.CRITICAL: CleaningMethod.CHEMICAL
        }
    
    def add_pipeline(self, pipeline: Pipeline):
        """Add a pipeline to the scheduler"""
        if pipeline.id in self.pipelines:
            raise ValueError(f"Pipeline with ID {pipeline.id} already exists")
        self.pipelines[pipeline.id] = pipeline
    
    def get_optimal_cleaning_order(self) -> List[Tuple[Pipeline, CleaningMethod]]:
        """Get optimal cleaning order based on priority scores"""
        if not self.pipelines:
            return []
        
        # Create priority queue (max heap using negative scores)
        priority_queue = []
        for pipeline in self.pipelines.values():
            score = pipeline.get_priority_score()
            heapq.heappush(priority_queue, (-score, pipeline.id))
        
        # Generate cleaning order with appropriate method
        cleaning_order = []
        while priority_queue:
            neg_score, pipeline_id = heapq.heappop(priority_queue)
            pipeline = self.pipelines[pipeline_id]
            method = self.cleaning_methods[pipeline.status]
            cleaning_order.append((pipeline, method))
        
        return cleaning_order
    
    def simulate_cleaning(self, pipeline_id: str, timestamp: str) -> bool:
        """Simulate cleaning a pipeline and update its state"""
        if pipeline_id not in self.pipelines:
            raise ValueError(f"Pipeline with ID {pipeline_id} not found")
        
        pipeline = self.pipelines[pipeline_id]
        pipeline.set_last_cleaned(timestamp)
        pipeline.update_contamination(0.0)  # Reset contamination after cleaning
        return True
    
    def get_cleaning_method(self, pipeline: Pipeline) -> CleaningMethod:
        """Get recommended cleaning method for a pipeline"""
        return self.cleaning_methods[pipeline.status]

# Example usage
if __name__ == "__main__":
    scheduler = PipelineCleaningScheduler()
    
    # Add sample pipelines
    scheduler.add_pipeline(Pipeline(
        id="pipe-001",
        age=5,
        diameter=0.5,
        length=100.0,
        status=PipelineStatus.NEW
    ))
    
    scheduler.add_pipeline(Pipeline(
        id="pipe-002",
        age=30,
        diameter=0.8,
        length=200.0,
        status=PipelineStatus.OLD
    ))
    
    scheduler.add_pipeline(Pipeline(
        id="pipe-003",
        age=45,
        diameter=1.2,
        length=150.0,
        status=PipelineStatus.CRITICAL
    ))
    
    # Update contamination levels
    scheduler.pipelines["pipe-001"].update_contamination(0.3)
    scheduler.pipelines["pipe-002"].update_contamination(0.7)
    scheduler.pipelines["pipe-003"].update_contamination(0.9)
    
    # Get and print cleaning order
    cleaning_order = scheduler.get_optimal_cleaning_order()
    for pipeline, method in cleaning_order:
        print(f"Pipeline {pipeline.id} (status: {pipeline.status.value}, contamination: {pipeline.contamination_level:.1f}) - Method: {method.value}")
```
