"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Write Python code to simulate the manufacturing process of PET bottles and jars, incorporating quality control checks as described by MM Group Nepal's focus on quality and on-time delivery.
Generated: DETERMINISTIC_61adcd799399900e
Batch ID: 20250612_145238
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
from enum import Enum
from typing import List, Dict, Optional, Tuple

class QualityStatus(Enum):
    """Enum representing possible quality statuses of a PET product."""
    PASS = "PASS"
    FAIL_DIMENSIONS = "FAIL_DIMENSIONS"
    FAIL_WEIGHT = "FAIL_WEIGHT"
    FAIL_VISUAL = "FAIL_VISUAL"
    FAIL_LEAK = "FAIL_LEAK"

class ProductType(Enum):
    """Enum representing types of PET products."""
    BOTTLE = "BOTTLE"
    JAR = "JAR"

class PETProduct:
    """Class representing a PET product (bottle or jar)."""
    
    def __init__(self, product_id: str, product_type: ProductType):
        self.product_id = product_id
        self.product_type = product_type
        self.weight = 0.0
        self.dimensions = {"height": 0.0, "diameter": 0.0}
        self.quality_status: Optional[QualityStatus] = None
        self.production_time = time.time()
    
    def __str__(self) -> str:
        return f"{self.product_type.value} {self.product_id}"

class ManufacturingLine:
    """Class representing a PET manufacturing line with quality control."""
    
    def __init__(self, line_id: str, product_type: ProductType):
        self.line_id = line_id
        self.product_type = product_type
        self.products_produced = 0
        self.products_passed = 0
        self.products_failed = 0
        self.failure_reasons: Dict[QualityStatus, int] = {
            status: 0 for status in QualityStatus if status != QualityStatus.PASS
        }
    
    def _generate_product_id(self) -> str:
        """Generate a unique product ID."""
        timestamp = int(time.time() * 1000)
        return f"{self.product_type.value[:3]}-{timestamp}-{random.randint(1000, 9999)}"
    
    def _simulate_production(self) -> PETProduct:
        """Simulate the production of a PET product."""
        product = PETProduct(
            product_id=self._generate_product_id(),
            product_type=self.product_type
        )
        
        # Simulate product characteristics based on type
        if self.product_type == ProductType.BOTTLE:
            product.weight = random.uniform(15.0, 50.0)  # grams
            product.dimensions = {
                "height": random.uniform(100.0, 300.0),  # mm
                "diameter": random.uniform(30.0, 80.0)   # mm
            }
        else:  # JAR
            product.weight = random.uniform(30.0, 200.0)  # grams
            product.dimensions = {
                "height": random.uniform(50.0, 150.0),   # mm
                "diameter": random.uniform(60.0, 120.0)  # mm
            }
        
        return product
    
    def _perform_quality_checks(self, product: PETProduct) -> QualityStatus:
        """Perform quality control checks on the product."""
        # Check dimensions
        if self.product_type == ProductType.BOTTLE:
            if not (100.0 <= product.dimensions["height"] <= 300.0):
                return QualityStatus.FAIL_DIMENSIONS
            if not (30.0 <= product.dimensions["diameter"] <= 80.0):
                return QualityStatus.FAIL_DIMENSIONS
        else:  # JAR
            if not (50.0 <= product.dimensions["height"] <= 150.0):
                return QualityStatus.FAIL_DIMENSIONS
            if not (60.0 <= product.dimensions["diameter"] <= 120.0):
                return QualityStatus.FAIL_DIMENSIONS
        
        # Check weight
        if self.product_type == ProductType.BOTTLE:
            if not (15.0 <= product.weight <= 50.0):
                return QualityStatus.FAIL_WEIGHT
        else:  # JAR
            if not (30.0 <= product.weight <= 200.0):
                return QualityStatus.FAIL_WEIGHT
        
        # Simulate visual inspection (5% chance of failure)
        if random.random() < 0.05:
            return QualityStatus.FAIL_VISUAL
        
        # Simulate leak test (3% chance of failure)
        if random.random() < 0.03:
            return QualityStatus.FAIL_LEAK
        
        return QualityStatus.PASS
    
    def produce_product(self) -> Tuple[PETProduct, QualityStatus]:
        """Produce a product and perform quality checks."""
        product = self._simulate_production()
        quality_status = self._perform_quality_checks(product)
        product.quality_status = quality_status
        
        self.products_produced += 1
        if quality_status == QualityStatus.PASS:
            self.products_passed += 1
        else:
            self.products_failed += 1
            self.failure_reasons[quality_status] += 1
        
        return product, quality_status
    
    def get_production_stats(self) -> Dict:
        """Get production statistics for the manufacturing line."""
        return {
            "line_id": self.line_id,
            "product_type": self.product_type.value,
            "total_produced": self.products_produced,
            "passed": self.products_passed,
            "failed": self.products_failed,
            "pass_rate": round(self.products_passed / self.products_produced * 100, 2) if self.products_produced > 0 else 0,
            "failure_reasons": {k.value: v for k, v in self.failure_reasons.items()}
        }

class PETManufacturingFacility:
    """Class representing a PET manufacturing facility with multiple lines."""
    
    def __init__(self, name: str):
        self.name = name
        self.manufacturing_lines: List[ManufacturingLine] = []
    
    def add_manufacturing_line(self, line_id: str, product_type: ProductType) -> None:
        """Add a manufacturing line to the facility."""
        self.manufacturing_lines.append(
            ManufacturingLine(line_id, product_type)
        )
    
    def run_production_cycle(self, num_products: int) -> None:
        """Run a production cycle across all lines."""
        print(f"\nStarting production cycle at {self.name}...")
        print(f"Target: {num_products} products per line\n")
        
        for line in self.manufacturing_lines:
            print(f"Line {line.line_id} producing {line.product_type.value}S...")
            for _ in range(num_products):
                product, status = line.produce_product()
                if status != QualityStatus.PASS:
                    print(f"  ! {product} failed quality check: {status.value}")
            
            stats = line.get_production_stats()
            print(f"\nLine {line.line_id} production complete:")
            print(f"  Total produced: {stats['total_produced']}")
            print(f"  Passed: {stats['passed']} ({stats['pass_rate']}%)")
            print(f"  Failed: {stats['failed']}")
            print("  Failure reasons:")
            for reason, count in stats["failure_reasons"].items():
                print(f"    - {reason}: {count}")
            print()
    
    def get_facility_stats(self) -> Dict:
        """Get overall statistics for the manufacturing facility."""
        total_produced = sum(line.products_produced for line in self.manufacturing_lines)
        total_passed = sum(line.products_passed for line in self.manufacturing_lines)
        
        return {
            "facility_name": self.name,
            "total_lines": len(self.manufacturing_lines),
            "total_produced": total_produced,
            "total_passed": total_passed,
            "total_failed": total_produced - total_passed,
            "overall_pass_rate": round(total_passed / total_produced * 100, 2) if total_produced > 0 else 0
        }

def main():
    """Main function to simulate PET manufacturing process."""
    # Create manufacturing facility
    mm_group_nepal = PETManufacturingFacility("MM Group Nepal PET Manufacturing")
    
    # Add production lines
    mm_group_nepal.add_manufacturing_line("LINE-1", ProductType.BOTTLE)
    mm_group_nepal.add_manufacturing_line("LINE-2", ProductType.JAR)
    mm_group_nepal.add_manufacturing_line("LINE-3", ProductType.BOTTLE)
    
    # Run production cycles
    try:
        mm_group_nepal.run_production_cycle(1000)
        
        # Print facility statistics
        facility_stats = mm_group_nepal.get_facility_stats()
        print("\nFACILITY PRODUCTION SUMMARY:")
        print(f"Facility: {facility_stats['facility_name']}")
        print(f"Production lines: {facility_stats['total_lines']}")
        print(f"Total products produced: {fac
