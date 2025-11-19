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
from typing import List, Optional
from datetime import datetime
from enum import Enum, auto

class SmokeTestResult(Enum):
    """Possible results of a smoke detection test."""
    PASS = auto()
    FAIL = auto()
    INCONCLUSIVE = auto()

@dataclass
class PipeSegment:
    """Represents a segment of pipe in the network."""
    id: str
    diameter: float  # in millimeters
    length: float    # in meters
    material: str
    start_node_id: str
    end_node_id: str
    installation_date: datetime
    notes: Optional[str] = None

@dataclass
class SmokeInjectionPoint:
    """Location where smoke is injected into the pipe network."""
    id: str
    pipe_segment_id: str
    position: float  # distance from start_node in meters
    description: Optional[str] = None

@dataclass
class SmokeDetectionPoint:
    """Location where smoke is detected/checked."""
    id: str
    pipe_segment_id: str
    position: float  # distance from start_node in meters
    expected_arrival_time: Optional[float] = None  # in seconds
    description: Optional[str] = None

@dataclass
class DetectionResult:
    """Result of smoke detection at a specific point."""
    detection_point_id: str
    test_id: str
    actual_arrival_time: Optional[float] = None  # in seconds
    result: SmokeTestResult = SmokeTestResult.INCONCLUSIVE
    notes: Optional[str] = None

@dataclass
class SmokeTest:
    """Represents a complete smoke test procedure."""
    id: str
    test_date: datetime
    technician: str
    injection_point_id: str
    smoke_type: str
    pressure: float  # in Pascals
    duration: float  # in seconds
    detection_results: List[DetectionResult]
    notes: Optional[str] = None

@dataclass
class PipeNetwork:
    """Complete model of a pipe network and its smoke tests."""
    id: str
    name: str
    description: Optional[str] = None
    pipe_segments: Optional[List[PipeSegment]] = None
    injection_points: Optional[List[SmokeInjectionPoint]] = None
    detection_points: Optional[List[SmokeDetectionPoint]] = None
    tests: Optional[List[SmokeTest]] = None

    def add_pipe_segment(self, segment: PipeSegment) -> None:
        """Add a pipe segment to the network."""
        if self.pipe_segments is None:
            self.pipe_segments = []
        self.pipe_segments.append(segment)

    def add_injection_point(self, point: SmokeInjectionPoint) -> None:
        """Add a smoke injection point to the network."""
        if self.injection_points is None:
            self.injection_points = []
        self.injection_points.append(point)

    def add_detection_point(self, point: SmokeDetectionPoint) -> None:
        """Add a smoke detection point to the network."""
        if self.detection_points is None:
            self.detection_points = []
        self.detection_points.append(point)

    def add_test(self, test: SmokeTest) -> None:
        """Add a smoke test to the network."""
        if self.tests is None:
            self.tests = []
        self.tests.append(test)
```
