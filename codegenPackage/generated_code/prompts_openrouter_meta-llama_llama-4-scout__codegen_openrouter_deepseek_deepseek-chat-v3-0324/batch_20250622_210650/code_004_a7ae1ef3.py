"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Develop a use case for Aayra International Limited's material engineering services, including testing and certification of materials for the plastics industry in Africa.
Generated: DETERMINISTIC_a7ae1ef335be908c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Aayra International Limited - Material Engineering Services
This module provides a use case for material testing and certification services
for the plastics industry in Africa.
"""

import datetime
from enum import Enum
from typing import List, Optional, Dict
from dataclasses import dataclass


class MaterialType(Enum):
    """Enumeration of material types supported for testing"""
    POLYETHYLENE = "Polyethylene"
    POLYPROPYLENE = "Polypropylene"
    PVC = "Polyvinyl Chloride"
    PET = "Polyethylene Terephthalate"
    OTHER = "Other"


class TestType(Enum):
    """Enumeration of available test types"""
    TENSILE_STRENGTH = "Tensile Strength"
    IMPACT_RESISTANCE = "Impact Resistance"
    THERMAL_STABILITY = "Thermal Stability"
    CHEMICAL_RESISTANCE = "Chemical Resistance"
    DENSITY = "Density"
    MELT_FLOW_INDEX = "Melt Flow Index"


class CertificationStatus(Enum):
    """Status of certification process"""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"


@dataclass
class MaterialSample:
    """Data class representing a material sample"""
    sample_id: str
    material_type: MaterialType
    supplier: str
    batch_number: str
    received_date: datetime.date
    quantity: float
    unit: str = "kg"


@dataclass
class TestResult:
    """Data class representing test results"""
    test_id: str
    test_type: TestType
    sample_id: str
    result_value: float
    unit: str
    test_date: datetime.date
    technician: str
    notes: Optional[str] = None


@dataclass
class Certification:
    """Data class representing certification details"""
    certification_id: str
    sample_id: str
    tests_performed: List[TestType]
    overall_result: bool
    issue_date: datetime.date
    expiry_date: datetime.date
    status: CertificationStatus
    certifying_officer: str
    notes: Optional[str] = None


class MaterialTestingService:
    """Core service for material testing and certification"""
    
    def __init__(self):
        self.samples: Dict[str, MaterialSample] = {}
        self.test_results: Dict[str, TestResult] = {}
        self.certifications: Dict[str, Certification] = {}
    
    def register_sample(self, sample: MaterialSample) -> str:
        """Register a new material sample for testing"""
        if sample.sample_id in self.samples:
            raise ValueError(f"Sample ID {sample.sample_id} already exists")
        
        self.samples[sample.sample_id] = sample
        return sample.sample_id
    
    def perform_test(self, test: TestResult) -> str:
        """Perform a test on a registered sample"""
        if test.sample_id not in self.samples:
            raise ValueError(f"Sample ID {test.sample_id} not found")
        
        self.test_results[test.test_id] = test
        return test.test_id
    
    def generate_certification(self, sample_id: str, tests: List[TestType], 
                              certifying_officer: str) -> Certification:
        """Generate certification based on test results"""
        if sample_id not in self.samples:
            raise ValueError(f"Sample ID {sample_id} not found")
        
        # Check all required tests have been performed
        sample_tests = [
            t for t in self.test_results.values() 
            if t.sample_id == sample_id and t.test_type in tests
        ]
        
        if len(sample_tests) != len(tests):
            missing = set(tests) - {t.test_type for t in sample_tests}
            raise ValueError(f"Missing test results for: {missing}")
        
        # Determine overall result (pass/fail)
        # This would be based on business rules - simplified here
        overall_result = all(t.result_value > 0 for t in sample_tests)  # Simplified condition
        
        certification = Certification(
            certification_id=f"CERT-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}",
            sample_id=sample_id,
            tests_performed=tests,
            overall_result=overall_result,
            issue_date=datetime.date.today(),
            expiry_date=datetime.date.today() + datetime.timedelta(days=365),
            status=CertificationStatus.COMPLETED if overall_result else CertificationStatus.FAILED,
            certifying_officer=certifying_officer
        )
        
        self.certifications[certification.certification_id] = certification
        return certification
    
    def get_certification_status(self, certification_id: str) -> CertificationStatus:
        """Check the status of a certification"""
        if certification_id not in self.certifications:
            raise ValueError(f"Certification ID {certification_id} not found")
        
        return self.certifications[certification_id].status
    
    def get_sample_tests(self, sample_id: str) -> List[TestResult]:
        """Get all test results for a sample"""
        return [t for t in self.test_results.values() if t.sample_id == sample_id]


# Example usage
if __name__ == "__main__":
    service = MaterialTestingService()
    
    # Register a sample
    sample = MaterialSample(
        sample_id="SAMP-001",
        material_type=MaterialType.POLYETHYLENE,
        supplier="Plastico Africa",
        batch_number="BATCH-2023-001",
        received_date=datetime.date.today(),
        quantity=5.0
    )
    service.register_sample(sample)
    
    # Perform tests
    test1 = TestResult(
        test_id="TEST-001",
        test_type=TestType.TENSILE_STRENGTH,
        sample_id="SAMP-001",
        result_value=32.5,
        unit="MPa",
        test_date=datetime.date.today(),
        technician="John Doe"
    )
    service.perform_test(test1)
    
    test2 = TestResult(
        test_id="TEST-002",
        test_type=TestType.IMPACT_RESISTANCE,
        sample_id="SAMP-001",
        result_value=45.2,
        unit="kJ/m²",
        test_date=datetime.date.today(),
        technician="Jane Smith"
    )
    service.perform_test(test2)
    
    # Generate certification
    certification = service.generate_certification(
        sample_id="SAMP-001",
        tests=[TestType.TENSILE_STRENGTH, TestType.IMPACT_RESISTANCE],
        certifying_officer="Dr. James Wilson"
    )
    
    print(f"Certification generated: {certification.certification_id}")
    print(f"Status: {certification.status}")
    print(f"Overall result: {'Pass' if certification.overall_result else 'Fail'}")
```
