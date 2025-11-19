"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Develop a plan for verifying and testing an existing electrical system to ensure compliance with current safety standards and regulations.
Generated: DETERMINISTIC_36e807b16f6318d4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum

class TestStatus(Enum):
    PASSED = "Passed"
    FAILED = "Failed"
    PENDING = "Pending"
    NOT_APPLICABLE = "N/A"

class ElectricalSystemTest:
    """Class to manage electrical system verification and testing."""
    
    def __init__(self, system_id: str, standards: list):
        """
        Initialize the electrical system test.
        
        Args:
            system_id: Unique identifier for the electrical system
            standards: List of safety standards to comply with (e.g., ['IEC 60364', 'NFPA 70'])
        """
        self.system_id = system_id
        self.standards = standards
        self.tests = []
        self.test_date = datetime.now().strftime("%Y-%m-%d")
        self.tester_name = ""
        self.final_report = {}
        
    def add_test(self, test_name: str, procedure: str, requirement: str):
        """
        Add a test to be performed.
        
        Args:
            test_name: Name of the test
            procedure: Description of test procedure
            requirement: Standard requirement being tested
        """
        self.tests.append({
            "test_name": test_name,
            "procedure": procedure,
            "requirement": requirement,
            "status": TestStatus.PENDING.value,
            "notes": "",
            "timestamp": ""
        })
    
    def perform_test(self, test_index: int, status: TestStatus, notes: str = ""):
        """
        Record test results.
        
        Args:
            test_index: Index of the test in the tests list
            status: Result of the test (PASSED/FAILED)
            notes: Any additional notes about the test
        """
        if test_index < 0 or test_index >= len(self.tests):
            raise IndexError("Test index out of range")
            
        self.tests[test_index]["status"] = status.value
        self.tests[test_index]["notes"] = notes
        self.tests[test_index]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def set_tester(self, name: str):
        """Set the name of the person performing the tests."""
        self.tester_name = name
    
    def generate_report(self):
        """Generate final compliance report."""
        passed_tests = sum(1 for test in self.tests if test["status"] == TestStatus.PASSED.value)
        failed_tests = sum(1 for test in self.tests if test["status"] == TestStatus.FAILED.value)
        
        self.final_report = {
            "system_id": self.system_id,
            "test_date": self.test_date,
            "tester": self.tester_name,
            "standards": self.standards,
            "summary": {
                "total_tests": len(self.tests),
                "passed": passed_tests,
                "failed": failed_tests,
                "compliance_percentage": (passed_tests / len(self.tests)) * 100 if self.tests else 0
            },
            "detailed_results": self.tests
        }
        return self.final_report
    
    def save_report(self, filename: str):
        """Save the report to a JSON file."""
        if not self.final_report:
            self.generate_report()
            
        with open(filename, 'w') as f:
            json.dump(self.final_report, f, indent=4)
    
    def load_report(self, filename: str):
        """Load a report from JSON file."""
        with open(filename, 'r') as f:
            self.final_report = json.load(f)
        return self.final_report

# Example usage
if __name__ == "__main__":
    # Initialize test for a system
    system_test = ElectricalSystemTest(
        system_id="ES-2023-001",
        standards=["IEC 60364", "NFPA 70"]
    )
    
    # Set tester name
    system_test.set_tester("John Doe")
    
    # Add tests to be performed
    system_test.add_test(
        "Ground Continuity Test",
        "Measure resistance between equipment ground and main grounding point",
        "IEC 60364-4-41"
    )
    
    system_test.add_test(
        "Insulation Resistance Test",
        "Measure insulation resistance between live conductors and earth",
        "IEC 60364-6-61"
    )
    
    system_test.add_test(
        "Circuit Breaker Trip Test",
        "Verify proper operation of circuit breakers under overload conditions",
        "NFPA 70 Article 240"
    )
    
    # Perform tests
    try:
        system_test.perform_test(0, TestStatus.PASSED, "Resistance measured at 0.2 ohms")
        system_test.perform_test(1, TestStatus.PASSED, "Insulation resistance > 1MΩ")
        system_test.perform_test(2, TestStatus.FAILED, "Breaker failed to trip at 125% rated current")
    except IndexError as e:
        print(f"Error performing test: {e}")
    
    # Generate and save report
    report = system_test.generate_report()
    system_test.save_report("electrical_system_compliance_report.json")
```
