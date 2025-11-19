"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Generate code for conducting laboratory tests on rock and granular soils based on the testing services offered by the Geotechnical Center.
Generated: DETERMINISTIC_775b463a0e65dffe
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Optional, Dict, List, Union
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SoilType(Enum):
    """Enumeration of soil types."""
    COHESIVE = "Cohesive"
    GRANULAR = "Granular"
    ROCK = "Rock"
    MIXED = "Mixed"

class TestType(Enum):
    """Enumeration of available geotechnical tests."""
    GRAIN_SIZE_ANALYSIS = "Grain Size Analysis"
    ATTERBERG_LIMITS = "Atterberg Limits"
    PROCTOR_COMPACTION = "Proctor Compaction"
    DIRECT_SHEAR = "Direct Shear"
    TRIAXIAL = "Triaxial"
    CONSOLIDATION = "Consolidation"
    PERMEABILITY = "Permeability"
    UNCONFINED_COMPRESSION = "Unconfined Compression"
    POINT_LOAD = "Point Load"
    SLAB_TEST = "Slab Test"

@dataclass
class Sample:
    """Class representing a soil/rock sample."""
    sample_id: str
    soil_type: SoilType
    description: Optional[str] = None
    depth: Optional[float] = None
    location: Optional[str] = None

@dataclass
class TestResult:
    """Class representing test results."""
    test_type: TestType
    sample_id: str
    parameters: Dict[str, Union[float, str]]
    passed: bool
    notes: Optional[str] = None

class GeotechnicalLab:
    """Class representing a geotechnical laboratory."""
    
    def __init__(self):
        self.samples: Dict[str, Sample] = {}
        self.test_results: List[TestResult] = []
    
    def register_sample(self, sample: Sample) -> bool:
        """Register a new sample in the laboratory."""
        if sample.sample_id in self.samples:
            logger.error(f"Sample with ID {sample.sample_id} already exists.")
            return False
        
        self.samples[sample.sample_id] = sample
        logger.info(f"Sample {sample.sample_id} registered successfully.")
        return True
    
    def perform_test(self, test_type: TestType, sample_id: str, 
                    parameters: Dict[str, Union[float, str]]) -> Optional[TestResult]:
        """Perform a test on a registered sample."""
        if sample_id not in self.samples:
            logger.error(f"Sample with ID {sample_id} not found.")
            return None
        
        sample = self.samples[sample_id]
        
        # Validate test compatibility with soil type
        if not self._validate_test_compatibility(test_type, sample.soil_type):
            logger.error(f"Test {test_type.value} is not compatible with soil type {sample.soil_type.value}.")
            return None
        
        # Perform test (simulated)
        logger.info(f"Performing {test_type.value} on sample {sample_id}...")
        
        # Generate test result (simulated)
        passed = True  # Assume test passes by default
        result = TestResult(
            test_type=test_type,
            sample_id=sample_id,
            parameters=parameters,
            passed=passed
        )
        
        self.test_results.append(result)
        logger.info(f"Test completed for sample {sample_id}.")
        return result
    
    def _validate_test_compatibility(self, test_type: TestType, soil_type: SoilType) -> bool:
        """Validate if a test is compatible with the soil type."""
        compatibility = {
            TestType.GRAIN_SIZE_ANALYSIS: [SoilType.GRANULAR, SoilType.MIXED],
            TestType.ATTERBERG_LIMITS: [SoilType.COHESIVE, SoilType.MIXED],
            TestType.PROCTOR_COMPACTION: [SoilType.COHESIVE, SoilType.GRANULAR, SoilType.MIXED],
            TestType.DIRECT_SHEAR: [SoilType.COHESIVE, SoilType.GRANULAR, SoilType.MIXED],
            TestType.TRIAXIAL: [SoilType.COHESIVE, SoilType.GRANULAR, SoilType.MIXED],
            TestType.CONSOLIDATION: [SoilType.COHESIVE, SoilType.MIXED],
            TestType.PERMEABILITY: [SoilType.COHESIVE, SoilType.GRANULAR, SoilType.MIXED],
            TestType.UNCONFINED_COMPRESSION: [SoilType.COHESIVE, SoilType.MIXED],
            TestType.POINT_LOAD: [SoilType.ROCK],
            TestType.SLAB_TEST: [SoilType.ROCK]
        }
        
        return soil_type in compatibility.get(test_type, [])
    
    def get_test_results(self, sample_id: Optional[str] = None) -> List[TestResult]:
        """Retrieve test results, optionally filtered by sample ID."""
        if sample_id:
            if sample_id not in self.samples:
                logger.error(f"Sample with ID {sample_id} not found.")
                return []
            return [result for result in self.test_results if result.sample_id == sample_id]
        return self.test_results
    
    def export_results(self, file_path: str, sample_id: Optional[str] = None) -> bool:
        """Export test results to a JSON file."""
        results = self.get_test_results(sample_id)
        
        if not results:
            logger.error("No results to export.")
            return False
        
        try:
            with open(file_path, 'w') as f:
                json.dump([result.__dict__ for result in results], f, indent=4, default=str)
            logger.info(f"Results exported successfully to {file_path}.")
            return True
        except Exception as e:
            logger.error(f"Failed to export results: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    lab = GeotechnicalLab()
    
    # Register samples
    sample1 = Sample(
        sample_id="S001",
        soil_type=SoilType.COHESIVE,
        description="Clay sample from 2m depth",
        depth=2.0,
        location="Site A"
    )
    
    sample2 = Sample(
        sample_id="S002",
        soil_type=SoilType.ROCK,
        description="Sandstone core sample",
        depth=5.5,
        location="Site B"
    )
    
    lab.register_sample(sample1)
    lab.register_sample(sample2)
    
    # Perform tests
    lab.perform_test(
        test_type=TestType.ATTERBERG_LIMITS,
        sample_id="S001",
        parameters={
            "liquid_limit": 45.2,
            "plastic_limit": 22.1,
            "plasticity_index": 23.1
        }
    )
    
    lab.perform_test(
        test_type=TestType.POINT_LOAD,
        sample_id="S002",
        parameters={
            "load_at_failure": 12.5,
            "strength_index": 3.2
        }
    )
    
    # Export results
    lab.export_results("test_results.json")
```
