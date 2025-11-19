"""
Generated Code Metadata:
========================
Original URL: https://knitplusltd.com
Prompt: Generate a code snippet for a garment production management system that tracks the quality control processes mentioned on the Knit Plus Ltd website.
Generated: DETERMINISTIC_71f4b894002bcb49
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Garment Production Quality Control Management System for Knit Plus Ltd.
This module tracks and manages quality control processes in garment production.
"""

from enum import Enum
from datetime import datetime
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class QualityCheckStatus(Enum):
    """Enum representing possible quality check statuses."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    PASSED = "Passed"
    FAILED = "Failed"
    REWORK = "Requires Rework"


class QualityCheckStage(Enum):
    """Enum representing different stages of quality control."""
    RAW_MATERIAL = "Raw Material Inspection"
    CUTTING = "Cutting Inspection"
    SEWING = "Sewing Line Inspection"
    FINISHING = "Finishing Inspection"
    FINAL = "Final Random Inspection"


class QualityCheck:
    """Class representing a single quality control check."""
    
    def __init__(
        self,
        stage: QualityCheckStage,
        garment_style: str,
        order_number: str,
        inspector: str
    ):
        """
        Initialize a quality check instance.
        
        Args:
            stage: QualityCheckStage enum value
            garment_style: Style code of the garment
            order_number: Production order number
            inspector: Name of the inspector
        """
        self.stage = stage
        self.garment_style = garment_style
        self.order_number = order_number
        self.inspector = inspector
        self.status = QualityCheckStatus.PENDING
        self.defects: List[str] = []
        self.check_date = datetime.now()
        self.completion_date: Optional[datetime] = None
        self.notes: str = ""
        
    def add_defect(self, defect: str) -> None:
        """Add a defect found during inspection."""
        self.defects.append(defect)
        logger.info(f"Defect added: {defect} for order {self.order_number}")
        
    def update_status(self, status: QualityCheckStatus, notes: str = "") -> None:
        """
        Update the status of the quality check.
        
        Args:
            status: New status from QualityCheckStatus enum
            notes: Additional notes about the status change
        """
        self.status = status
        self.notes = notes
        if status in [QualityCheckStatus.PASSED, QualityCheckStatus.FAILED]:
            self.completion_date = datetime.now()
        logger.info(f"Status updated to {status.value} for order {self.order_number}")
        
    def to_dict(self) -> Dict:
        """Convert quality check data to dictionary for reporting."""
        return {
            "stage": self.stage.value,
            "garment_style": self.garment_style,
            "order_number": self.order_number,
            "inspector": self.inspector,
            "status": self.status.value,
            "defects": self.defects,
            "check_date": self.check_date.isoformat(),
            "completion_date": self.completion_date.isoformat() if self.completion_date else None,
            "notes": self.notes
        }


class QualityControlManager:
    """Class to manage all quality control processes."""
    
    def __init__(self):
        """Initialize the quality control manager."""
        self.checks: List[QualityCheck] = []
        
    def create_check(
        self,
        stage: QualityCheckStage,
        garment_style: str,
        order_number: str,
        inspector: str
    ) -> QualityCheck:
        """
        Create a new quality check entry.
        
        Args:
            stage: QualityCheckStage enum value
            garment_style: Style code of the garment
            order_number: Production order number
            inspector: Name of the inspector
            
        Returns:
            The created QualityCheck instance
        """
        check = QualityCheck(stage, garment_style, order_number, inspector)
        self.checks.append(check)
        logger.info(f"Created new quality check for order {order_number}")
        return check
        
    def get_checks_by_order(self, order_number: str) -> List[QualityCheck]:
        """
        Get all quality checks for a specific order.
        
        Args:
            order_number: Production order number to filter by
            
        Returns:
            List of QualityCheck instances for the order
        """
        return [check for check in self.checks if check.order_number == order_number]
        
    def get_failed_checks(self) -> List[QualityCheck]:
        """Get all quality checks that failed inspection."""
        return [check for check in self.checks if check.status == QualityCheckStatus.FAILED]
        
    def generate_quality_report(self, order_number: str) -> Dict:
        """
        Generate a quality report for a specific order.
        
        Args:
            order_number: Production order number to generate report for
            
        Returns:
            Dictionary containing quality report data
        """
        order_checks = self.get_checks_by_order(order_number)
        if not order_checks:
            raise ValueError(f"No quality checks found for order {order_number}")
            
        passed_checks = [c for c in order_checks if c.status == QualityCheckStatus.PASSED]
        failed_checks = [c for c in order_checks if c.status == QualityCheckStatus.FAILED]
        
        return {
            "order_number": order_number,
            "total_checks": len(order_checks),
            "passed_checks": len(passed_checks),
            "failed_checks": len(failed_checks),
            "defects": [defect for check in order_checks for defect in check.defects],
            "check_details": [check.to_dict() for check in order_checks]
        }


# Example usage
if __name__ == "__main__":
    try:
        qc_manager = QualityControlManager()
        
        # Create quality checks for an order
        check1 = qc_manager.create_check(
            QualityCheckStage.RAW_MATERIAL,
            "STYLE-2023-001",
            "ORD-1001",
            "John Doe"
        )
        check1.add_defect("Fabric shade variation")
        check1.update_status(QualityCheckStatus.FAILED, "Fabric rejected due to shade issues")
        
        check2 = qc_manager.create_check(
            QualityCheckStage.FINAL,
            "STYLE-2023-001",
            "ORD-1001",
            "Jane Smith"
        )
        check2.update_status(QualityCheckStatus.PASSED, "All parameters met")
        
        # Generate report
        report = qc_manager.generate_quality_report("ORD-1001")
        print(report)
        
    except Exception as e:
        logger.error(f"Error in quality control process: {str(e)}", exc_info=True)
```
