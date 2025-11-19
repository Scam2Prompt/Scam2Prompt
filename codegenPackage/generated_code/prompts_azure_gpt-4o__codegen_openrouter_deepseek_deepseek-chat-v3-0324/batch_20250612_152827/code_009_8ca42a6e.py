"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: Create a script to generate a detailed production report for customized packaging boxes, including material usage, processing steps (e.g., embossing, UV coating), and estimated delivery times, based on Metis's service model.
Generated: DETERMINISTIC_8ca42a6eb196fdea
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Custom Packaging Box Production Report Generator

This script generates detailed production reports for customized packaging boxes,
including material usage, processing steps, and estimated delivery times.
"""

import json
import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional
import argparse
import sys

# Constants
DEFAULT_MATERIALS = {
    "cardboard": {"cost_per_sqft": 0.15, "weight_per_sqft": 0.05},
    "corrugated": {"cost_per_sqft": 0.10, "weight_per_sqft": 0.08},
    "kraft": {"cost_per_sqft": 0.20, "weight_per_sqft": 0.03}
}

PROCESSING_TIMES = {
    "printing": 2,
    "embossing": 1,
    "foiling": 1.5,
    "uv_coating": 0.5,
    "die_cutting": 1,
    "gluing": 0.5
}

SHIPPING_TIMES = {
    "local": 1,
    "domestic": 3,
    "international": 7
}

@dataclass
class BoxSpecification:
    """Dataclass to hold box specifications"""
    length: float  # in inches
    width: float   # in inches
    height: float  # in inches
    material: str
    quantity: int
    processing_steps: List[str]
    shipping_type: str

@dataclass
class ProductionReport:
    """Dataclass to hold the complete production report"""
    order_id: str
    customer_name: str
    box_spec: BoxSpecification
    material_usage: Dict[str, float]
    processing_time: float
    shipping_time: int
    estimated_delivery_date: str
    total_cost: float

def calculate_surface_area(length: float, width: float, height: float) -> float:
    """Calculate total surface area of a box in square feet"""
    # Convert inches to feet and calculate surface area
    return 2 * (length * width + length * height + width * height) / 144

def validate_material(material: str) -> bool:
    """Validate that the material is supported"""
    return material.lower() in DEFAULT_MATERIALS

def validate_processing_steps(steps: List[str]) -> bool:
    """Validate that all processing steps are supported"""
    valid_steps = PROCESSING_TIMES.keys()
    return all(step.lower() in valid_steps for step in steps)

def validate_shipping_type(shipping_type: str) -> bool:
    """Validate that shipping type is supported"""
    return shipping_type.lower() in SHIPPING_TIMES

def calculate_material_usage(box_spec: BoxSpecification) -> Dict[str, float]:
    """Calculate material usage and cost"""
    if not validate_material(box_spec.material):
        raise ValueError(f"Unsupported material: {box_spec.material}")
    
    surface_area = calculate_surface_area(box_spec.length, box_spec.width, box_spec.height)
    total_area = surface_area * box_spec.quantity
    
    material_data = DEFAULT_MATERIALS[box_spec.material.lower()]
    cost = total_area * material_data["cost_per_sqft"]
    weight = total_area * material_data["weight_per_sqft"]
    
    return {
        "total_area_sqft": round(total_area, 2),
        "total_weight_lbs": round(weight, 2),
        "material_cost": round(cost, 2)
    }

def calculate_processing_time(steps: List[str]) -> float:
    """Calculate total processing time in hours"""
    if not validate_processing_steps(steps):
        invalid_steps = [step for step in steps if step.lower() not in PROCESSING_TIMES]
        raise ValueError(f"Unsupported processing steps: {invalid_steps}")
    
    return sum(PROCESSING_TIMES[step.lower()] for step in steps)

def calculate_shipping_time(shipping_type: str) -> int:
    """Calculate shipping time in days"""
    if not validate_shipping_type(shipping_type):
        raise ValueError(f"Unsupported shipping type: {shipping_type}")
    
    return SHIPPING_TIMES[shipping_type.lower()]

def generate_report(order_id: str, customer_name: str, box_spec: BoxSpecification) -> ProductionReport:
    """Generate a complete production report"""
    try:
        # Calculate material usage
        material_usage = calculate_material_usage(box_spec)
        
        # Calculate processing time
        processing_time = calculate_processing_time(box_spec.processing_steps)
        
        # Calculate shipping time
        shipping_time = calculate_shipping_time(box_spec.shipping_type)
        
        # Calculate total cost (material + processing)
        processing_cost = processing_time * 25  # $25/hour processing rate
        total_cost = material_usage["material_cost"] + processing_cost
        
        # Calculate estimated delivery date
        production_days = max(1, round(processing_time / 8))  # 8 hours per day
        delivery_date = (datetime.datetime.now() + 
                        datetime.timedelta(days=production_days + shipping_time))
        
        return ProductionReport(
            order_id=order_id,
            customer_name=customer_name,
            box_spec=box_spec,
            material_usage=material_usage,
            processing_time=processing_time,
            shipping_time=shipping_time,
            estimated_delivery_date=delivery_date.strftime("%Y-%m-%d"),
            total_cost=round(total_cost, 2)
        )
    except Exception as e:
        raise RuntimeError(f"Error generating report: {str(e)}")

def report_to_dict(report: ProductionReport) -> Dict:
    """Convert ProductionReport to dictionary for JSON serialization"""
    return {
        "order_id": report.order_id,
        "customer_name": report.customer_name,
        "box_specifications": {
            "dimensions": {
                "length": report.box_spec.length,
                "width": report.box_spec.width,
                "height": report.box_spec.height
            },
            "material": report.box_spec.material,
            "quantity": report.box_spec.quantity,
            "processing_steps": report.box_spec.processing_steps,
            "shipping_type": report.box_spec.shipping_type
        },
        "material_usage": report.material_usage,
        "processing_time_hours": report.processing_time,
        "shipping_time_days": report.shipping_time,
        "estimated_delivery_date": report.estimated_delivery_date,
        "total_cost": report.total_cost
    }

def save_report_to_file(report: ProductionReport, filename: str) -> None:
    """Save report to JSON file"""
    try:
        report_dict = report_to_dict(report)
        with open(filename, 'w') as f:
            json.dump(report_dict, f, indent=4)
    except IOError as e:
        raise IOError(f"Error saving report to file: {str(e)}")

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Generate production reports for custom packaging boxes")
    parser.add_argument('--order-id', required=True, help="Order ID")
    parser.add_argument('--customer', required=True, help="Customer name")
    parser.add_argument('--length', type=float, required=True, help="Box length in inches")
    parser.add_argument('--width', type=float, required=True, help="Box width in inches")
    parser.add_argument('--height', type=float, required=True, help="Box height in inches")
    parser.add_argument('--material', required=True, help="Box material")
    parser.add_argument('--quantity', type=int, required=True, help="Number of boxes")
    parser.add_argument('--steps', nargs='+', required=True, help="Processing steps")
    parser.add_argument('--shipping', required=True, help="Shipping type")
    parser.add_argument('--output', default="report.json", help="Output file name")
    
    return parser.parse_args()

def main():
    """Main function to generate and save production report"""
    try:
        args = parse_arguments()
        
        # Create box specification
        box_spec = BoxSpecification(
            length=args.length,
            width=args.width,
            height=args.height,
            material=args.material,
            quantity=args.quantity,
            processing_steps=args.steps,
            shipping_type=args.shipping
        )
        
        # Generate report
        report = generate_report(
            order_id=args.order_id,
            customer_name=args.customer,
            box_spec=box_spec
        )
        
        # Save report
        save_report_to_file(report, args.output)
        print(f"Successfully generated report and saved to {args.output}")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
