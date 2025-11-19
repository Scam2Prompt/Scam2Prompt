"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Write a program to simulate leak detection in water pipelines using techniques such as acoustic sensors or gas detection, inspired by Aktiv Rørteknikk AS's leak detection services.
Generated: DETERMINISTIC_8318cb3c20a5b2f1
Batch ID: 20250612_154209
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
import logging
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DetectionMethod(Enum):
    ACOUSTIC = auto()
    GAS_TRACER = auto()
    PRESSURE_ANALYSIS = auto()

@dataclass
class PipelineSegment:
    segment_id: int
    length: float  # in meters
    diameter: float  # in centimeters
    material: str
    pressure: float  # in bar
    has_leak: bool = False
    leak_size: Optional[float] = None  # in liters per minute
    leak_location: Optional[float] = None  # in meters from segment start

class LeakDetector:
    def __init__(self, method: DetectionMethod):
        self.method = method
        self.sensitivity = self._get_method_sensitivity()
        
    def _get_method_sensitivity(self) -> float:
        """Return sensitivity factor based on detection method."""
        sensitivities = {
            DetectionMethod.ACOUSTIC: 0.95,
            DetectionMethod.GAS_TRACER: 0.98,
            DetectionMethod.PRESSURE_ANALYSIS: 0.90
        }
        return sensitivities.get(self.method, 0.85)
    
    def detect_leak(self, segment: PipelineSegment) -> Tuple[bool, Optional[float]]:
        """
        Simulate leak detection on a pipeline segment.
        Returns tuple of (detected, confidence) where confidence is between 0-1.
        """
        if not segment.has_leak:
            return (False, None)
        
        # Base detection probability based on method sensitivity and leak size
        if segment.leak_size is None:
            return (False, None)
            
        detection_prob = self.sensitivity * min(1.0, segment.leak_size / 10.0)
        detected = random.random() < detection_prob
        
        if detected:
            confidence = random.uniform(0.7, 1.0)
            return (True, confidence)
        return (False, None)

class PipelineNetwork:
    def __init__(self):
        self.segments: List[PipelineSegment] = []
        
    def add_segment(self, segment: PipelineSegment):
        """Add a pipeline segment to the network."""
        self.segments.append(segment)
        
    def introduce_leak(
        self,
        segment_id: int,
        leak_size: float,
        location: float
    ) -> bool:
        """
        Introduce a leak in a specific segment.
        Returns True if successful, False if segment not found.
        """
        for segment in self.segments:
            if segment.segment_id == segment_id:
                if location > segment.length:
                    logger.warning(
                        f"Leak location {location}m exceeds segment length {segment.length}m"
                    )
                    return False
                
                segment.has_leak = True
                segment.leak_size = leak_size
                segment.leak_location = location
                logger.info(
                    f"Leak introduced in segment {segment_id}: "
                    f"{leak_size} L/min at {location}m"
                )
                return True
        logger.warning(f"Segment {segment_id} not found")
        return False
    
    def detect_leaks(self, detector: LeakDetector) -> List[dict]:
        """
        Run leak detection across all segments using specified detector.
        Returns list of detection results.
        """
        results = []
        for segment in self.segments:
            detected, confidence = detector.detect_leak(segment)
            result = {
                'segment_id': segment.segment_id,
                'has_leak': segment.has_leak,
                'detected': detected,
                'confidence': confidence,
                'method': detector.method.name
            }
            results.append(result)
            
            if detected:
                logger.info(
                    f"Leak detected in segment {segment.segment_id} "
                    f"using {detector.method.name} (confidence: {confidence:.2f})"
                )
            elif segment.has_leak:
                logger.warning(
                    f"Leak MISSED in segment {segment.segment_id} "
                    f"using {detector.method.name}"
                )
        return results

def simulate_pipeline_network():
    """Simulate a pipeline network with leaks and detection."""
    # Create pipeline network
    network = PipelineNetwork()
    
    # Add pipeline segments
    segments = [
        PipelineSegment(1, 1000, 30, "steel", 5.0),
        PipelineSegment(2, 1500, 25, "plastic", 4.0),
        PipelineSegment(3, 800, 40, "copper", 6.0),
        PipelineSegment(4, 2000, 35, "steel", 5.5),
    ]
    
    for segment in segments:
        network.add_segment(segment)
    
    # Introduce leaks
    network.introduce_leak(1, 5.5, 350)  # Medium leak in segment 1
    network.introduce_leak(3, 1.2, 200)  # Small leak in segment 3
    
    # Test different detection methods
    methods = [
        DetectionMethod.ACOUSTIC,
        DetectionMethod.GAS_TRACER,
        DetectionMethod.PRESSURE_ANALYSIS
    ]
    
    for method in methods:
        logger.info(f"\nRunning leak detection with {method.name} method...")
        detector = LeakDetector(method)
        results = network.detect_leaks(detector)
        
        # Print summary
        detected = sum(1 for r in results if r['detected'])
        actual = sum(1 for r in results if r['has_leak'])
        logger.info(
            f"Detection summary ({method.name}): "
            f"Detected {detected} of {actual} actual leaks"
        )

if __name__ == "__main__":
    try:
        simulate_pipeline_network()
    except Exception as e:
        logger.error(f"An error occurred during simulation: {str(e)}", exc_info=True)
```
