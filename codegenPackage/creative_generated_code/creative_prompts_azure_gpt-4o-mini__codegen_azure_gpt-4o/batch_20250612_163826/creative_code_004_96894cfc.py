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
"""
Supply Chain Quality Assurance Check
Author: [Your Name]
Date: [Current Date]
Description: This script implements a quality assurance check in a supply chain management system
using Mahadev Enterprise's sourcing principles. The core functionality is to validate product batches
against predefined standards and log results for follow-up actions.
"""

import logging
from typing import List, Dict

# Setup logging for QA report
logging.basicConfig(
    filename="quality_assurance.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class QualityAssuranceError(Exception):
    """Custom error class for QA failures."""
    pass

class QualityAssuranceCheck:
    """
    Class to perform quality assurance checks on product batches.
    """

    def __init__(self, standards: Dict[str, Dict[str, float]]):
        """
        Initialize the QA check with predefined standards.

        :param standards: Dictionary defining acceptable standards for each product type.
                          Example: {"ProductA": {"min_quality": 90.0, "max_defects": 5}}
        """
        self.standards = standards

    def check_batch(self, product_type: str, batch: Dict[str, float]) -> bool:
        """
        Perform QA check on a batch.

        :param product_type: The type of product being checked.
        :param batch: Dictionary containing batch details. Example: {"quality_score": 92.0, "defect_count": 4}
        :return: True if batch passes QA, False otherwise.
        """
        if product_type not in self.standards:
            raise QualityAssuranceError(f"Standards for product type '{product_type}' are not defined.")
        
        # Retrieve standards for the product type
        standards = self.standards[product_type]

        # Check quality score
        quality_score = batch.get("quality_score", 0)
        if quality_score < standards["min_quality"]:
            logging.warning(f"Batch failed QA: Quality score {quality_score} is below minimum standard {standards['min_quality']}.")
            return False

        # Check defect count
        defect_count = batch.get("defect_count", 0)
        if defect_count > standards["max_defects"]:
            logging.warning(f"Batch failed QA: Defect count {defect_count} exceeds maximum allowed defects {standards['max_defects']}.")
            return False

        # Batch passed QA
        logging.info(f"Batch passed QA for product type '{product_type}'.")
        return True

def main():
    """
    Main function to simulate QA checks on batches.
    """
    # Define standards for products
    standards = {
        "ProductA": {"min_quality": 90.0, "max_defects": 5},
        "ProductB": {"min_quality": 85.0, "max_defects": 3},
    }

    # Initialize the QA checker
    qa_checker = QualityAssuranceCheck(standards)

    # Example batches to be checked
    batches = [
        {"product_type": "ProductA", "batch_data": {"quality_score": 92.0, "defect_count": 4}},
        {"product_type": "ProductA", "batch_data": {"quality_score": 88.0, "defect_count": 7}},
        {"product_type": "ProductB", "batch_data": {"quality_score": 87.0, "defect_count": 2}},
        {"product_type": "ProductB", "batch_data": {"quality_score": 80.0, "defect_count": 4}},
    ]

    # Perform QA checks on batches
    for batch in batches:
        try:
            product_type = batch["product_type"]
            batch_data = batch["batch_data"]

            result = qa_checker.check_batch(product_type, batch_data)
            if result:
                print(f"Batch for '{product_type}' passed QA.")
            else:
                print(f"Batch for '{product_type}' failed QA.")
        except QualityAssuranceError as e:
            logging.error(e)
            print(f"Error during QA: {e}")

if __name__ == "__main__":
    main()
```
