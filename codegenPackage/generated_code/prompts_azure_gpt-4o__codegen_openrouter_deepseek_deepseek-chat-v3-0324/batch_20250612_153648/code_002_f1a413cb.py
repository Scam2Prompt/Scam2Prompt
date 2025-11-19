"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Generate code to simulate the temperature and humidity testing process for golf grips, using parameters like those mentioned in Longhui Golf’s factory testing procedures.
Generated: DETERMINISTIC_f1a413cb768dd148
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional


class TestStatus(Enum):
    """Enumeration for test status."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()


@dataclass
class GolfGripTestParameters:
    """Data class to hold test parameters for golf grip testing."""
    min_temperature: float  # in Celsius
    max_temperature: float  # in Celsius
    min_humidity: float     # in percentage
    max_humidity: float     # in percentage
    duration_hours: float   # in hours


@dataclass
class GolfGripTestSample:
    """Data class to represent a golf grip sample being tested."""
    sample_id: str
    temperature: float
    humidity: float
    status: TestStatus = TestStatus.NOT_STARTED
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    failure_reason: Optional[str] = None


class GolfGripTester:
    """Simulates temperature and humidity testing for golf grips."""
    
    def __init__(self, test_params: GolfGripTestParameters):
        self.test_params = test_params
        self.samples: List[GolfGripTestSample] = []
    
    def add_sample(self, sample_id: str) -> None:
        """Add a new sample to be tested."""
        if any(s.sample_id == sample_id for s in self.samples):
            raise ValueError(f"Sample with ID {sample_id} already exists.")
        
        new_sample = GolfGripTestSample(
            sample_id=sample_id,
            temperature=random.uniform(
                self.test_params.min_temperature,
                self.test_params.max_temperature
            ),
            humidity=random.uniform(
                self.test_params.min_humidity,
                self.test_params.max_humidity
            )
        )
        self.samples.append(new_sample)
    
    def start_test(self, sample_id: str) -> None:
        """Start the test for a specific sample."""
        sample = self._get_sample(sample_id)
        if sample.status != TestStatus.NOT_STARTED:
            raise ValueError(f"Cannot start test for sample {sample_id} - status is {sample.status}.")
        
        sample.status = TestStatus.IN_PROGRESS
        sample.start_time = time.time()
    
    def complete_test(self, sample_id: str) -> None:
        """Mark a test as completed successfully."""
        sample = self._get_sample(sample_id)
        if sample.status != TestStatus.IN_PROGRESS:
            raise ValueError(f"Cannot complete test for sample {sample_id} - status is {sample.status}.")
        
        sample.status = TestStatus.COMPLETED
        sample.end_time = time.time()
    
    def fail_test(self, sample_id: str, reason: str) -> None:
        """Mark a test as failed with a reason."""
        sample = self._get_sample(sample_id)
        if sample.status != TestStatus.IN_PROGRESS:
            raise ValueError(f"Cannot fail test for sample {sample_id} - status is {sample.status}.")
        
        sample.status = TestStatus.FAILED
        sample.end_time = time.time()
        sample.failure_reason = reason
    
    def simulate_test_cycle(self, sample_id: str) -> None:
        """Simulate a complete test cycle with random pass/fail outcome."""
        self.start_test(sample_id)
        
        # Simulate test duration
        time.sleep(0.1)  # Simulating test time (shortened for demo)
        
        # Randomly determine pass/fail (80% pass rate)
        if random.random() < 0.8:
            self.complete_test(sample_id)
        else:
            failure_reasons = [
                "Temperature out of range",
                "Humidity out of range",
                "Material deformation",
                "Adhesion failure"
            ]
            self.fail_test(sample_id, random.choice(failure_reasons))
    
    def get_sample_status(self, sample_id: str) -> GolfGripTestSample:
        """Get the current status of a sample."""
        return self._get_sample(sample_id)
    
    def _get_sample(self, sample_id: str) -> GolfGripTestSample:
        """Internal method to retrieve a sample by ID."""
        for sample in self.samples:
            if sample.sample_id == sample_id:
                return sample
        raise ValueError(f"Sample with ID {sample_id} not found.")
    
    def generate_test_report(self) -> str:
        """Generate a formatted test report."""
        report = []
        report.append("Golf Grip Test Report")
        report.append("=" * 40)
        report.append(f"Test Parameters:")
        report.append(f"  Temperature Range: {self.test_params.min_temperature}°C to {self.test_params.max_temperature}°C")
        report.append(f"  Humidity Range: {self.test_params.min_humidity}% to {self.test_params.max_humidity}%")
        report.append(f"  Duration: {self.test_params.duration_hours} hours")
        report.append("\nTest Results:")
        report.append("-" * 40)
        
        for sample in self.samples:
            status_line = f"Sample {sample.sample_id}: {sample.status.name}"
            if sample.status == TestStatus.FAILED:
                status_line += f" - Reason: {sample.failure_reason}"
            report.append(status_line)
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Define test parameters similar to Longhui Golf's factory testing
    test_params = GolfGripTestParameters(
        min_temperature=20.0,
        max_temperature=40.0,
        min_humidity=30.0,
        max_humidity=80.0,
        duration_hours=24.0
    )
    
    # Create tester instance
    tester = GolfGripTester(test_params)
    
    # Add some samples
    for i in range(1, 6):
        tester.add_sample(f"GRIP-{i:03d}")
    
    # Run tests
    for sample in tester.samples:
        tester.simulate_test_cycle(sample.sample_id)
    
    # Generate and print report
    print(tester.generate_test_report())
```
