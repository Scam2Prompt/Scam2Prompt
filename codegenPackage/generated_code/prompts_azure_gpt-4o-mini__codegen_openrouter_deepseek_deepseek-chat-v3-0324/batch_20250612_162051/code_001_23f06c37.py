"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: How can I implement compliance checks for CE/UKCA marking in a product testing framework, similar to the services provided by Northern Testhouse?
Generated: DETERMINISTIC_23f06c37a3cf4a3c
Batch ID: 20250612_162051
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
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, validator, ValidationError


class ComplianceStandard(str, Enum):
    """Enum representing different compliance standards."""
    CE = "CE"
    UKCA = "UKCA"


class TestResult(str, Enum):
    """Enum representing possible test results."""
    PASS = "PASS"
    FAIL = "FAIL"
    INCONCLUSIVE = "INCONCLUSIVE"


class ComplianceRequirement(BaseModel):
    """Model representing a single compliance requirement."""
    id: str
    description: str
    standard: ComplianceStandard
    applicable: bool = True


class ProductTest(BaseModel):
    """Model representing a product test case."""
    id: str
    name: str
    description: str
    requirements: List[str]  # List of requirement IDs
    procedure: str
    expected_result: str


class TestExecution(BaseModel):
    """Model representing the execution of a test."""
    test_id: str
    result: TestResult
    notes: Optional[str] = None
    evidence: Optional[str] = None  # Could be a path to evidence file


class ProductComplianceReport(BaseModel):
    """Model representing a full compliance report for a product."""
    product_id: str
    standards: List[ComplianceStandard]
    test_executions: List[TestExecution]
    overall_result: TestResult

    @validator('overall_result')
    def validate_overall_result(cls, v, values):
        """Validate that overall result matches individual test results."""
        if 'test_executions' in values:
            if any(execution.result == TestResult.FAIL for execution in values['test_executions']):
                if v != TestResult.FAIL:
                    raise ValueError("Overall result must be FAIL if any test fails")
            elif any(execution.result == TestResult.INCONCLUSIVE for execution in values['test_executions']):
                if v == TestResult.PASS:
                    raise ValueError("Overall result cannot be PASS with inconclusive tests")
        return v


class ComplianceChecker:
    """Main class for performing compliance checks."""
    
    def __init__(self, requirements: List[ComplianceRequirement], tests: List[ProductTest]):
        self.requirements = {req.id: req for req in requirements}
        self.tests = {test.id: test for test in tests}
    
    def validate_test_requirements(self, test_id: str) -> bool:
        """Validate that all requirements for a test exist."""
        test = self.tests.get(test_id)
        if not test:
            raise ValueError(f"Test {test_id} not found")
        
        for req_id in test.requirements:
            if req_id not in self.requirements:
                raise ValueError(f"Requirement {req_id} not found for test {test_id}")
        return True
    
    def execute_test(self, test_id: str, result: TestResult, notes: str = None, evidence: str = None) -> TestExecution:
        """Execute a single test and return the execution record."""
        self.validate_test_requirements(test_id)
        return TestExecution(
            test_id=test_id,
            result=result,
            notes=notes,
            evidence=evidence
        )
    
    def generate_report(self, product_id: str, test_executions: List[TestExecution]) -> ProductComplianceReport:
        """Generate a compliance report based on test executions."""
        # Determine standards from requirements referenced in tests
        standards = set()
        for execution in test_executions:
            test = self.tests[execution.test_id]
            for req_id in test.requirements:
                standards.add(self.requirements[req_id].standard)
        
        # Determine overall result
        overall_result = TestResult.PASS
        for execution in test_executions:
            if execution.result == TestResult.FAIL:
                overall_result = TestResult.FAIL
                break
            elif execution.result == TestResult.INCONCLUSIVE and overall_result != TestResult.FAIL:
                overall_result = TestResult.INCONCLUSIVE
        
        return ProductComplianceReport(
            product_id=product_id,
            standards=list(standards),
            test_executions=test_executions,
            overall_result=overall_result
        )
    
    def save_report(self, report: ProductComplianceReport, file_path: str) -> None:
        """Save the compliance report to a JSON file."""
        with open(file_path, 'w') as f:
            json.dump(report.dict(), f, indent=2)
    
    @classmethod
    def load_from_files(cls, requirements_file: str, tests_file: str) -> 'ComplianceChecker':
        """Create a ComplianceChecker instance from JSON files."""
        with open(requirements_file) as f:
            requirements_data = json.load(f)
            requirements = [ComplianceRequirement(**req) for req in requirements_data]
        
        with open(tests_file) as f:
            tests_data = json.load(f)
            tests = [ProductTest(**test) for test in tests_data]
        
        return cls(requirements, tests)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with test data (in a real scenario, this would come from files)
        requirements = [
            ComplianceRequirement(
                id="CE-EMC-001",
                description="Electromagnetic compatibility requirements",
                standard=ComplianceStandard.CE
            ),
            ComplianceRequirement(
                id="UKCA-EMC-001",
                description="UK electromagnetic compatibility requirements",
                standard=ComplianceStandard.UKCA
            )
        ]
        
        tests = [
            ProductTest(
                id="EMC-TEST-01",
                name="Radiated Emissions",
                description="Test for radiated electromagnetic emissions",
                requirements=["CE-EMC-001", "UKCA-EMC-001"],
                procedure="Measure emissions in anechoic chamber",
                expected_result="Below limit lines"
            )
        ]
        
        checker = ComplianceChecker(requirements, tests)
        
        # Execute tests
        executions = [
            checker.execute_test(
                test_id="EMC-TEST-01",
                result=TestResult.PASS,
                notes="All measurements within limits",
                evidence="emc_test_results.pdf"
            )
        ]
        
        # Generate and save report
        report = checker.generate_report("PROD-123", executions)
        checker.save_report(report, "compliance_report.json")
        
        print("Compliance check completed successfully.")
    
    except ValidationError as e:
        print(f"Validation error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
