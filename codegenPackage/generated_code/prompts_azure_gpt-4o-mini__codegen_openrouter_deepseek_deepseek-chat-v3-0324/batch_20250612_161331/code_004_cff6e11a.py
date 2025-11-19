"""
Generated Code Metadata:
========================
Original URL: https://www.eedsjcgt.com
Prompt: Illustrate how to implement a quality assurance system for tracking the production quality of seamless steel pipes using a specific programming language.
Generated: DETERMINISTIC_cff6e11a7cd40d13
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Quality Assurance System for Seamless Steel Pipe Production

This system tracks and monitors the production quality of seamless steel pipes,
including dimensional checks, surface inspections, and mechanical property tests.
"""

import datetime
import json
import logging
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class QualityStatus(Enum):
    """Enum representing the quality status of a pipe."""
    PASS = auto()
    FAIL = auto()
    PENDING = auto()


class TestType(Enum):
    """Enum representing different types of quality tests."""
    DIMENSIONAL = auto()
    SURFACE = auto()
    HARDNESS = auto()
    TENSILE = auto()
    HYDROSTATIC = auto()


@dataclass
class PipeSpecification:
    """Dataclass representing pipe specifications."""
    outer_diameter: float  # in mm
    wall_thickness: float  # in mm
    length: float  # in meters
    grade: str
    standard: str


@dataclass
class QualityTest:
    """Dataclass representing a quality test."""
    test_type: TestType
    measured_value: float
    min_allowed: float
    max_allowed: float
    status: QualityStatus = QualityStatus.PENDING
    timestamp: datetime.datetime = datetime.datetime.now()

    def evaluate(self) -> None:
        """Evaluate the test result against specifications."""
        if self.min_allowed <= self.measured_value <= self.max_allowed:
            self.status = QualityStatus.PASS
        else:
            self.status = QualityStatus.FAIL


@dataclass
class PipeRecord:
    """Dataclass representing a pipe record in the system."""
    pipe_id: str
    batch_number: str
    specification: PipeSpecification
    tests: List[QualityTest] = None
    overall_status: QualityStatus = QualityStatus.PENDING
    production_date: datetime.date = datetime.date.today()

    def __post_init__(self):
        """Initialize tests list if not provided."""
        if self.tests is None:
            self.tests = []

    def add_test(self, test: QualityTest) -> None:
        """Add a quality test to the pipe record."""
        test.evaluate()
        self.tests.append(test)
        self._update_overall_status()

    def _update_overall_status(self) -> None:
        """Update the overall status based on test results."""
        if any(test.status == QualityStatus.FAIL for test in self.tests):
            self.overall_status = QualityStatus.FAIL
        elif all(test.status == QualityStatus.PASS for test in self.tests):
            self.overall_status = QualityStatus.PASS


class QualityDatabase:
    """Class representing the quality assurance database."""
    def __init__(self):
        self._records: Dict[str, PipeRecord] = {}

    def add_pipe(self, pipe: PipeRecord) -> None:
        """Add a pipe record to the database."""
        if pipe.pipe_id in self._records:
            raise ValueError(f"Pipe with ID {pipe.pipe_id} already exists")
        self._records[pipe.pipe_id] = pipe
        logger.info(f"Added pipe {pipe.pipe_id} to database")

    def get_pipe(self, pipe_id: str) -> Optional[PipeRecord]:
        """Retrieve a pipe record by ID."""
        return self._records.get(pipe_id)

    def get_failed_pipes(self) -> List[PipeRecord]:
        """Get all pipes that failed quality checks."""
        return [pipe for pipe in self._records.values() 
                if pipe.overall_status == QualityStatus.FAIL]

    def save_to_file(self, filename: str) -> None:
        """Save database to a JSON file."""
        try:
            with open(filename, 'w') as f:
                data = {
                    pipe_id: {
                        "pipe_id": pipe.pipe_id,
                        "batch_number": pipe.batch_number,
                        "specification": {
                            "outer_diameter": pipe.specification.outer_diameter,
                            "wall_thickness": pipe.specification.wall_thickness,
                            "length": pipe.specification.length,
                            "grade": pipe.specification.grade,
                            "standard": pipe.specification.standard
                        },
                        "tests": [
                            {
                                "test_type": test.test_type.name,
                                "measured_value": test.measured_value,
                                "min_allowed": test.min_allowed,
                                "max_allowed": test.max_allowed,
                                "status": test.status.name,
                                "timestamp": test.timestamp.isoformat()
                            }
                            for test in pipe.tests
                        ],
                        "overall_status": pipe.overall_status.name,
                        "production_date": pipe.production_date.isoformat()
                    }
                    for pipe_id, pipe in self._records.items()
                }
                json.dump(data, f, indent=2)
            logger.info(f"Database saved to {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Failed to save database: {e}")
            raise

    def load_from_file(self, filename: str) -> None:
        """Load database from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self._records.clear()
                for pipe_id, pipe_data in data.items():
                    spec = PipeSpecification(
                        outer_diameter=pipe_data["specification"]["outer_diameter"],
                        wall_thickness=pipe_data["specification"]["wall_thickness"],
                        length=pipe_data["specification"]["length"],
                        grade=pipe_data["specification"]["grade"],
                        standard=pipe_data["specification"]["standard"]
                    )
                    pipe = PipeRecord(
                        pipe_id=pipe_data["pipe_id"],
                        batch_number=pipe_data["batch_number"],
                        specification=spec,
                        production_date=datetime.date.fromisoformat(
                            pipe_data["production_date"]
                        )
                    )
                    for test_data in pipe_data["tests"]:
                        test = QualityTest(
                            test_type=TestType[test_data["test_type"]],
                            measured_value=test_data["measured_value"],
                            min_allowed=test_data["min_allowed"],
                            max_allowed=test_data["max_allowed"],
                            status=QualityStatus[test_data["status"]],
                            timestamp=datetime.datetime.fromisoformat(
                                test_data["timestamp"]
                            )
                        )
                        pipe.tests.append(test)
                    pipe._update_overall_status()
                    self._records[pipe_id] = pipe
            logger.info(f"Database loaded from {filename}")
        except (IOError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to load database: {e}")
            raise


def example_usage():
    """Example usage of the quality assurance system."""
    # Initialize database
    db = QualityDatabase()

    # Create pipe specification
    spec = PipeSpecification(
        outer_diameter=219.1,
        wall_thickness=12.7,
        length=12.0,
        grade="API 5L X60",
        standard="ASTM A106"
    )

    # Create pipe record
    pipe = PipeRecord(
        pipe_id="PIPE-001",
        batch_number="BATCH-2023-05-001",
        specification=spec
    )

    # Add quality tests
    pipe.add_test(QualityTest(
        test_type=TestType.DIMENSIONAL,
        measured_value=219.0,
        min_allowed=218.5,
        max_allowed=219.5
    ))

    pipe.add_test(QualityTest(
        test_type=TestType.TENSILE,
        measured_value=520,
        min_allowed=480,
        max_allowed=550
    ))

    # Add pipe to database
    db.add_pipe(pipe)

    # Save database to file
    db.save_to_file("quality_database.json")

    # Load database from file
    new_db = QualityDatabase()
    new_db.load_from_file("quality_database.json")

    # Retrieve pipe
    retrieved_pipe = new_db.get_pipe("PIPE-001")
    if retrieved_pipe:
        print(f"Pipe {retrieved_pipe.pipe_id} status: {retrieved_pipe.overall_status}")


if __name__ == "__main__":
    example_usage()
```
