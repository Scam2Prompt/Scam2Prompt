"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Create a data model for storing and analyzing data from smoke testing of pipe networks, including information about pipe layout, smoke injection points, and detection results.
Generated: DETERMINISTIC_1600e7aebd00bf7c
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class SmokeTestStatus(Enum):
    """Enum for smoke test status"""
    PASSED = 1
    FAILED = 2
    PENDING = 3

@dataclass
class PipeSegment:
    """Data class for pipe segment"""
    id: int
    length: float  # in meters
    diameter: float  # in centimeters
    material: str

@dataclass
class SmokeInjectionPoint:
    """Data class for smoke injection point"""
    id: int
    pipe_segment_id: int
    location: float  # in meters from pipe segment start

@dataclass
class DetectionResult:
    """Data class for detection result"""
    id: int
    smoke_injection_point_id: int
    detection_time: str  # in ISO 8601 format
    concentration: float  # in parts per million

@dataclass
class SmokeTest:
    """Data class for smoke test"""
    id: int
    pipe_segments: List[PipeSegment]
    smoke_injection_points: List[SmokeInjectionPoint]
    detection_results: List[DetectionResult]
    status: SmokeTestStatus

class PipeNetwork:
    """Class for pipe network"""
    def __init__(self):
        self.pipe_segments = []
        self.smoke_tests = []

    def add_pipe_segment(self, pipe_segment: PipeSegment):
        """Add pipe segment to pipe network"""
        self.pipe_segments.append(pipe_segment)

    def add_smoke_test(self, smoke_test: SmokeTest):
        """Add smoke test to pipe network"""
        self.smoke_tests.append(smoke_test)

    def get_smoke_test(self, smoke_test_id: int) -> SmokeTest:
        """Get smoke test by id"""
        for smoke_test in self.smoke_tests:
            if smoke_test.id == smoke_test_id:
                return smoke_test
        raise ValueError(f"Smoke test with id {smoke_test_id} not found")

def main():
    try:
        # Create pipe network
        pipe_network = PipeNetwork()

        # Create pipe segments
        pipe_segment1 = PipeSegment(1, 100.0, 50.0, "PVC")
        pipe_segment2 = PipeSegment(2, 200.0, 75.0, "Metal")

        # Add pipe segments to pipe network
        pipe_network.add_pipe_segment(pipe_segment1)
        pipe_network.add_pipe_segment(pipe_segment2)

        # Create smoke injection points
        smoke_injection_point1 = SmokeInjectionPoint(1, 1, 20.0)
        smoke_injection_point2 = SmokeInjectionPoint(2, 2, 50.0)

        # Create detection results
        detection_result1 = DetectionResult(1, 1, "2022-01-01T12:00:00", 10.0)
        detection_result2 = DetectionResult(2, 2, "2022-01-01T13:00:00", 20.0)

        # Create smoke test
        smoke_test = SmokeTest(1, [pipe_segment1, pipe_segment2], [smoke_injection_point1, smoke_injection_point2], [detection_result1, detection_result2], SmokeTestStatus.PASSED)

        # Add smoke test to pipe network
        pipe_network.add_smoke_test(smoke_test)

        # Get smoke test
        retrieved_smoke_test = pipe_network.get_smoke_test(1)
        print(retrieved_smoke_test)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
