"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahadevent.com
Prompt: Illustrate how to implement a quality assurance check in a supply chain management system using Mahadev Enterprise's sourcing principles.
Generated: DETERMINISTIC_96894cfc8e5fb49d
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Supplier:
    """Class representing a supplier in the supply chain."""
    
    def __init__(self, name: str, quality_score: float):
        self.name = name
        self.quality_score = quality_score

class QualityAssurance:
    """Class to perform quality assurance checks on suppliers."""
    
    def __init__(self, suppliers: List[Supplier]):
        self.suppliers = suppliers

    def check_supplier_quality(self) -> Dict[str, Any]:
        """Check the quality of suppliers and return a report."""
        report = {}
        
        for supplier in self.suppliers:
            logging.info(f"Checking quality for supplier: {supplier.name}")
            try:
                if not self.validate_supplier(supplier):
                    raise ValueError(f"Supplier {supplier.name} failed validation.")
                report[supplier.name] = self.assess_quality(supplier)
            except Exception as e:
                logging.error(f"Error checking supplier {supplier.name}: {e}")
                report[supplier.name] = "Error"
        
        return report

    def validate_supplier(self, supplier: Supplier) -> bool:
        """Validate supplier's quality score."""
        if not (0 <= supplier.quality_score <= 100):
            logging.warning(f"Quality score for supplier {supplier.name} is out of bounds: {supplier.quality_score}")
            return False
        return True

    def assess_quality(self, supplier: Supplier) -> str:
        """Assess the quality of a supplier based on their quality score."""
        if supplier.quality_score >= 90:
            return "Excellent"
        elif supplier.quality_score >= 75:
            return "Good"
        elif supplier.quality_score >= 50:
            return "Average"
        else:
            return "Poor"

# Example usage
if __name__ == "__main__":
    suppliers = [
        Supplier("Supplier A", 95),
        Supplier("Supplier B", 85),
        Supplier("Supplier C", 45),
        Supplier("Supplier D", 110)  # Invalid quality score for demonstration
    ]

    qa_system = QualityAssurance(suppliers)
    quality_report = qa_system.check_supplier_quality()
    
    logging.info("Quality Assurance Report:")
    for supplier_name, quality in quality_report.items():
        logging.info(f"{supplier_name}: {quality}")
```
