"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: Create a script to generate a detailed production report for customized packaging boxes, including material usage, processing steps (e.g., embossing, UV coating), and estimated delivery times, based on Metis's service model.
Generated: DETERMINISTIC_8ca42a6eb196fdea
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict

# Define constants for processing times and material rates
PROCESSING_TIMES = {
    "embossing": 2,  # hours
    "uv_coating": 1.5  # hours
}

MATERIAL_RATES = {
    "cardboard": 0.5,  # cost per sq. ft
    "plastic": 0.8,  # cost per sq. ft
    "metal": 1.2  # cost per sq. ft
}

# Error class for validation errors
class ValidationError(Exception):
    pass

# Function to calculate material usage and cost
def calculate_material_usage(dimensions: Dict[str, float], material: str) -> Dict[str, float]:
    """
    Calculate material usage and cost.
    
    Args:
        dimensions: A dictionary containing length, width, and height in feet.
        material: Type of material (e.g., "cardboard", "plastic", "metal").

    Returns:
        A dictionary containing material usage and cost.
    """
    try:
        # Ensure dimensions are positive values
        if dimensions["length"] <= 0 or dimensions["width"] <= 0 or dimensions["height"] <= 0:
            raise ValidationError("Dimensions must be positive values.")
        
        # Calculate surface area (feet squared)
        surface_area = 2 * (
            dimensions["length"] * dimensions["width"] +
            dimensions["width"] * dimensions["height"] +
            dimensions["length"] * dimensions["height"]
        )

        # Calculate material cost
        if material not in MATERIAL_RATES:
            raise ValidationError(f"Unknown material: {material}")
        cost = surface_area * MATERIAL_RATES[material]

        return {
            "surface_area": surface_area,
            "material_cost": round(cost, 2)
        }
    except ValidationError as e:
        raise e
    except Exception as e:
        raise ValueError("An error occurred while calculating material usage.") from e

# Function to calculate processing time
def calculate_processing_time(steps: List[str]) -> float:
    """
    Calculate the total processing time based on the selected production steps.
    
    Args:
        steps: A list of processing steps (e.g., "embossing", "uv_coating").

    Returns:
        Total processing time in hours.
    """
    try:
        total_time = 0
        for step in steps:
            if step not in PROCESSING_TIMES:
                raise ValidationError(f"Unknown processing step: {step}")
            total_time += PROCESSING_TIMES[step]
        return total_time
    except ValidationError as e:
        raise e
    except Exception as e:
        raise ValueError("An error occurred while calculating processing time.") from e

# Function to estimate delivery time
def estimate_delivery_time(order_date: datetime.date, processing_time: float) -> datetime.date:
    """
    Estimate the delivery date based on order date and processing time.
    
    Args:
        order_date: The date the order was placed.
        processing_time: Processing time in hours.

    Returns:
        Estimated delivery date.
    """
    try:
        production_days = int(processing_time / 8)  # Assuming 8 working hours per day
        return order_date + datetime.timedelta(days=production_days)
    except Exception as e:
        raise ValueError("An error occurred while estimating delivery time.") from e

# Main function to generate the production report
def generate_production_report(order: Dict) -> Dict:
    """
    Generate a detailed production report for customized packaging boxes.
    
    Args:
        order: A dictionary containing order details:
            - dimensions: Dictionary with "length", "width", "height" in feet.
            - material: Type of material (e.g., "cardboard", "plastic", "metal").
            - processing_steps: List of processing steps (e.g., "embossing", "uv_coating").
            - order_date: Date the order was placed (ISO format: YYYY-MM-DD).

    Returns:
        A dictionary containing the production report.
    """
    try:
        # Validate input format
        if "dimensions" not in order or "material" not in order or "processing_steps" not in order or "order_date" not in order:
            raise ValidationError("Order details are incomplete.")

        # Parse order date
        order_date = datetime.date.fromisoformat(order["order_date"])

        # Calculate material usage and cost
        material_report = calculate_material_usage(order["dimensions"], order["material"])

        # Calculate processing time
        processing_time = calculate_processing_time(order["processing_steps"])

        # Estimate delivery time
        delivery_date = estimate_delivery_time(order_date, processing_time)

        # Create production report
        report = {
            "material_usage": material_report,
            "processing_time_hours": round(processing_time, 2),
            "estimated_delivery_date": delivery_date.isoformat()
        }
        return report
    except ValidationError as e:
        raise e
    except Exception as e:
        raise ValueError("An error occurred while generating the production report.") from e

# Example usage
if __name__ == "__main__":
    # Sample order data
    sample_order = {
        "dimensions": {"length": 2.5, "width": 1.5, "height": 1.0},
        "material": "cardboard",
        "processing_steps": ["embossing", "uv_coating"],
        "order_date": "2023-10-01"
    }

    try:
        # Generate report
        report = generate_production_report(sample_order)
        print("Production Report:")
        print(json.dumps(report, indent=4))
    except Exception as e:
        print(f"Error: {e}")
```
