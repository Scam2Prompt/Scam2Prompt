"""
Generated Code Metadata:
========================
Original URL: https://mahadevent.com
Prompt: Design a quality assurance system for an agricultural commodities manufacturing company like Mahadev Enterprise, incorporating principles of quality control and testing.
Generated: DETERMINISTIC_a208b02cb0eb9db8
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime
from typing import List, Dict, Optional

class QualityControlSystem:
    """
    A quality assurance system for agricultural commodities manufacturing.
    Implements quality control checks, testing procedures, and reporting.
    """

    def __init__(self):
        self.batch_records: Dict[str, Dict] = {}
        self.quality_standards = {
            'moisture_content': {'min': 8.0, 'max': 12.0},
            'foreign_matter': {'max': 2.0},
            'purity': {'min': 98.0},
            'defects': {'max': 5.0}
        }
        self.test_methods = {
            'moisture_content': self._test_moisture_content,
            'foreign_matter': self._test_foreign_matter,
            'purity': self._test_purity,
            'defects': self._test_defects
        }

    def create_batch_record(self, product_name: str, batch_id: str, quantity: float) -> bool:
        """
        Create a new batch record for quality testing.
        
        Args:
            product_name: Name of the agricultural product
            batch_id: Unique identifier for the batch
            quantity: Quantity in kilograms
            
        Returns:
            bool: True if batch created successfully, False if batch ID exists
        """
        if batch_id in self.batch_records:
            return False
            
        self.batch_records[batch_id] = {
            'product_name': product_name,
            'batch_id': batch_id,
            'quantity': quantity,
            'test_results': {},
            'status': 'Pending',
            'created_at': datetime.now().isoformat(),
            'approved_by': None
        }
        return True

    def run_quality_tests(self, batch_id: str) -> bool:
        """
        Run all quality tests on a batch.
        
        Args:
            batch_id: ID of the batch to test
            
        Returns:
            bool: True if tests completed, False if batch not found
        """
        if batch_id not in self.batch_records:
            return False
            
        batch = self.batch_records[batch_id]
        test_results = {}
        
        for test_name, test_method in self.test_methods.items():
            test_results[test_name] = test_method()
            
        batch['test_results'] = test_results
        batch['status'] = self._determine_batch_status(test_results)
        return True

    def _test_moisture_content(self) -> float:
        """Simulate moisture content test (8-12% is acceptable)"""
        return round(random.uniform(7.5, 13.0), 2)

    def _test_foreign_matter(self) -> float:
        """Simulate foreign matter test (max 2% allowed)"""
        return round(random.uniform(0.5, 3.0), 2)

    def _test_purity(self) -> float:
        """Simulate purity test (min 98% required)"""
        return round(random.uniform(97.0, 99.9), 2)

    def _test_defects(self) -> float:
        """Simulate defects test (max 5% allowed)"""
        return round(random.uniform(1.0, 6.0), 2)

    def _determine_batch_status(self, test_results: Dict[str, float]) -> str:
        """
        Determine if batch passes quality standards based on test results.
        
        Args:
            test_results: Dictionary of test results
            
        Returns:
            str: 'Approved' if all tests pass, 'Rejected' otherwise
        """
        for test_name, result in test_results.items():
            standard = self.quality_standards[test_name]
            
            if 'min' in standard and result < standard['min']:
                return 'Rejected'
            if 'max' in standard and result > standard['max']:
                return 'Rejected'
                
        return 'Approved'

    def approve_batch(self, batch_id: str, approver: str) -> bool:
        """
        Approve a batch that has passed quality tests.
        
        Args:
            batch_id: ID of the batch to approve
            approver: Name of the approving authority
            
        Returns:
            bool: True if approved, False if batch not found or not approved
        """
        if batch_id not in self.batch_records:
            return False
            
        batch = self.batch_records[batch_id]
        if batch['status'] != 'Approved':
            return False
            
        batch['approved_by'] = approver
        return True

    def get_batch_report(self, batch_id: str) -> Optional[Dict]:
        """
        Generate a quality report for a batch.
        
        Args:
            batch_id: ID of the batch to report on
            
        Returns:
            Optional[Dict]: Batch report if found, None otherwise
        """
        if batch_id not in self.batch_records:
            return None
            
        batch = self.batch_records[batch_id]
        return {
            'batch_id': batch['batch_id'],
            'product_name': batch['product_name'],
            'quantity': batch['quantity'],
            'status': batch['status'],
            'test_results': batch['test_results'],
            'created_at': batch['created_at'],
            'approved_by': batch['approved_by']
        }

    def get_failed_batches(self) -> List[Dict]:
        """
        Get all batches that failed quality control.
        
        Returns:
            List[Dict]: List of failed batch records
        """
        return [
            batch for batch in self.batch_records.values()
            if batch['status'] == 'Rejected'
        ]


# Example usage
if __name__ == "__main__":
    qa_system = QualityControlSystem()
    
    # Create a new batch
    qa_system.create_batch_record("Organic Wheat", "WHT-2023-001", 5000)
    
    # Run quality tests
    qa_system.run_quality_tests("WHT-2023-001")
    
    # Approve if passed
    if qa_system.approve_batch("WHT-2023-001", "QA Manager"):
        print("Batch approved successfully")
    else:
        print("Batch failed quality checks")
    
    # Generate report
    report = qa_system.get_batch_report("WHT-2023-001")
    print("Batch Report:", report)
```
