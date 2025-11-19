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
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QualityAssuranceSystem:
    def __init__(self):
        """Initialize the Quality Assurance System with an empty records list."""
        self.records: List[Dict[str, Any]] = []

    def add_quality_record(self, product_id: str, quality_score: float, inspector: str, comments: str) -> None:
        """
        Add a quality control record for a product.

        Args:
            product_id (str): The ID of the product being inspected.
            quality_score (float): The quality score assigned to the product (0-100).
            inspector (str): The name of the inspector.
            comments (str): Additional comments regarding the inspection.
        """
        if not (0 <= quality_score <= 100):
            logging.error("Quality score must be between 0 and 100.")
            raise ValueError("Quality score must be between 0 and 100.")

        record = {
            'product_id': product_id,
            'quality_score': quality_score,
            'inspector': inspector,
            'comments': comments,
            'timestamp': datetime.now()
        }
        self.records.append(record)
        logging.info(f"Added quality record for product {product_id}.")

    def generate_report(self) -> Dict[str, Any]:
        """
        Generate a quality report summarizing the quality scores.

        Returns:
            Dict[str, Any]: A summary report containing average score and total records.
        """
        if not self.records:
            logging.warning("No quality records available to generate a report.")
            return {'average_score': 0, 'total_records': 0}

        total_score = sum(record['quality_score'] for record in self.records)
        average_score = total_score / len(self.records)
        report = {
            'average_score': average_score,
            'total_records': len(self.records),
            'records': self.records
        }
        logging.info("Generated quality report.")
        return report

    def get_records_by_inspector(self, inspector: str) -> List[Dict[str, Any]]:
        """
        Retrieve quality records for a specific inspector.

        Args:
            inspector (str): The name of the inspector.

        Returns:
            List[Dict[str, Any]]: A list of records associated with the specified inspector.
        """
        filtered_records = [record for record in self.records if record['inspector'] == inspector]
        logging.info(f"Retrieved {len(filtered_records)} records for inspector {inspector}.")
        return filtered_records

# Example usage
if __name__ == "__main__":
    qa_system = QualityAssuranceSystem()
    
    try:
        qa_system.add_quality_record("P001", 85.0, "Alice", "Good quality.")
        qa_system.add_quality_record("P002", 90.0, "Bob", "Excellent quality.")
        qa_system.add_quality_record("P003", 75.0, "Alice", "Average quality.")
        
        report = qa_system.generate_report()
        print(report)

        alice_records = qa_system.get_records_by_inspector("Alice")
        print(alice_records)

    except ValueError as e:
        logging.error(f"Error occurred: {e}")
```
