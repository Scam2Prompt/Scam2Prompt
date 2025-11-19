"""
Generated Code Metadata:
========================
Original URL: https://mahadevent.com
Prompt: Illustrate how to implement a quality assurance check in a supply chain management system using Mahadev Enterprise's sourcing principles.
Generated: DETERMINISTIC_96894cfc8e5fb49d
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Quality Assurance Check for Supply Chain Management System
Based on Mahadev Enterprise's Sourcing Principles

This module implements quality checks for products in a supply chain,
ensuring they meet the defined standards before approval.
"""

import logging
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QualityStatus(Enum):
    """Enum representing possible quality check statuses"""
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    QUARANTINE = "Quarantine"

class Product:
    """Class representing a product in the supply chain"""
    
    def __init__(self, product_id: str, name: str, batch_number: str, 
                 supplier: str, production_date: datetime):
        """
        Initialize a product with basic information
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            batch_number: Batch number for traceability
            supplier: Name of the supplier
            production_date: Date when product was manufactured
        """
        self.product_id = product_id
        self.name = name
        self.batch_number = batch_number
        self.supplier = supplier
        self.production_date = production_date
        self.quality_status = QualityStatus.PENDING
        self.quality_check_date = None
        self.defects = []
        
    def add_defect(self, defect_description: str, severity: str):
        """Record a defect found during quality check"""
        self.defects.append({
            'description': defect_description,
            'severity': severity,
            'timestamp': datetime.now()
        })

class QualityChecker:
    """Implements quality checks based on Mahadev Enterprise's principles"""
    
    def __init__(self, standards: Dict):
        """
        Initialize quality checker with standards
        
        Args:
            standards: Dictionary containing quality standards
        """
        self.standards = standards
        self.required_checks = [
            self.check_expiry,
            self.check_packaging,
            self.check_quantity,
            self.check_documentation,
            self.check_visual_inspection
        ]
    
    def perform_quality_check(self, product: Product) -> QualityStatus:
        """
        Perform all required quality checks on a product
        
        Args:
            product: Product to be checked
            
        Returns:
            QualityStatus: Result of the quality check
        """
        try:
            if not product:
                raise ValueError("Product cannot be None")
                
            logger.info(f"Starting quality check for product {product.product_id}")
            
            # Perform all checks
            for check in self.required_checks:
                check(product)
                
            # Determine final status based on defects
            if not product.defects:
                product.quality_status = QualityStatus.APPROVED
            elif any(d['severity'] == 'critical' for d in product.defects):
                product.quality_status = QualityStatus.REJECTED
            else:
                product.quality_status = QualityStatus.QUARANTINE
                
            product.quality_check_date = datetime.now()
            logger.info(f"Quality check completed. Status: {product.quality_status.value}")
            return product.quality_status
            
        except Exception as e:
            logger.error(f"Error during quality check: {str(e)}")
            product.quality_status = QualityStatus.QUARANTINE
            return product.quality_status
    
    def check_expiry(self, product: Product):
        """Check if product is within expiry period"""
        expiry_period = self.standards.get('expiry_period_days', 365)
        shelf_life = (datetime.now() - product.production_date).days
        
        if shelf_life > expiry_period:
            product.add_defect(
                "Product exceeds maximum shelf life",
                "critical"
            )
    
    def check_packaging(self, product: Product):
        """Check if packaging meets standards"""
        packaging_standard = self.standards.get('packaging', {})
        
        # In a real implementation, this would check actual packaging
        # Here we simulate a random check
        import random
        if random.random() < 0.1:  # 10% chance of packaging defect
            product.add_defect(
                "Packaging damaged or not according to standards",
                "moderate"
            )
    
    def check_quantity(self, product: Product):
        """Check if quantity matches order"""
        # In a real implementation, this would compare with order data
        pass
    
    def check_documentation(self, product: Product):
        """Verify all required documentation is present"""
        required_docs = self.standards.get('required_documents', [])
        
        # Simulate missing documentation check
        if 'certificate_of_analysis' in required_docs:
            import random
            if random.random() < 0.05:  # 5% chance of missing doc
                product.add_defect(
                    "Missing certificate of analysis",
                    "moderate"
                )
    
    def check_visual_inspection(self, product: Product):
        """Perform visual inspection for obvious defects"""
        # Simulate visual inspection
        import random
        if random.random() < 0.15:  # 15% chance of visual defect
            product.add_defect(
                "Minor visual imperfections",
                "minor"
            )

class SupplyChainManager:
    """Manages quality assurance process in the supply chain"""
    
    def __init__(self):
        """Initialize with default standards"""
        self.standards = {
            'expiry_period_days': 180,
            'packaging': {
                'type': 'standard',
                'requirements': ['tamper-proof', 'moisture-resistant']
            },
            'required_documents': [
                'certificate_of_analysis',
                'safety_data_sheet',
                'origin_certificate'
            ]
        }
        self.quality_checker = QualityChecker(self.standards)
        self.products = []
    
    def receive_product(self, product: Product) -> QualityStatus:
        """
        Receive a product and perform quality check
        
        Args:
            product: Product to be received
            
        Returns:
            QualityStatus: Result of the quality check
        """
        self.products.append(product)
        return self.quality_checker.perform_quality_check(product)
    
    def get_products_by_status(self, status: QualityStatus) -> List[Product]:
        """
        Get all products with a specific quality status
        
        Args:
            status: QualityStatus to filter by
            
        Returns:
            List of products with matching status
        """
        return [p for p in self.products if p.quality_status == status]

# Example usage
if __name__ == "__main__":
    # Initialize supply chain manager
    scm = SupplyChainManager()
    
    # Create a sample product
    sample_product = Product(
        product_id="PROD-001",
        name="Organic Cotton T-Shirt",
        batch_number="BATCH-2023-05-001",
        supplier="Mahadev Textiles",
        production_date=datetime(2023, 5, 1)
    )
    
    # Receive and check the product
    status = scm.receive_product(sample_product)
    print(f"Product quality status: {status.value}")
    
    # Display defects if any
    if sample_product.defects:
        print("\nDefects found:")
        for defect in sample_product.defects:
            print(f"- {defect['description']} (Severity: {defect['severity']})")
```
