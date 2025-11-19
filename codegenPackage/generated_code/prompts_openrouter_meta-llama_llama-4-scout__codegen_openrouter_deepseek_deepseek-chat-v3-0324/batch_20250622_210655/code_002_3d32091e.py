"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: "Generate a Python script to calculate estimates for plumbing and heating services based on customer input, similar to Flammedeauinc's 3-step process for service requests."
Generated: DETERMINISTIC_3d32091e87611c75
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from typing import Dict, List, Optional, Tuple

class ServiceType(Enum):
    PLUMBING = "Plumbing"
    HEATING = "Heating"

class ServiceRequest:
    def __init__(self, service_type: ServiceType, description: str, urgency: str):
        self.service_type = service_type
        self.description = description
        self.urgency = urgency

class CostEstimator:
    BASE_RATES = {
        ServiceType.PLUMBING: 75.00,
        ServiceType.HEATING: 100.00
    }
    
    URGENCY_MULTIPLIERS = {
        "low": 1.0,
        "medium": 1.5,
        "high": 2.0
    }
    
    MATERIAL_COSTS = {
        ServiceType.PLUMBING: {
            "pipe_repair": 25.00,
            "faucet_replacement": 45.00,
            "toilet_repair": 60.00
        },
        ServiceType.HEATING: {
            "thermostat_replacement": 50.00,
            "boiler_repair": 120.00,
            "radiator_repair": 80.00
        }
    }
    
    @classmethod
    def estimate_cost(cls, request: ServiceRequest, materials: List[str]) -> Tuple[float, Dict[str, float]]:
        """
        Calculate the estimated cost for a service request.
        
        Args:
            request: ServiceRequest object containing service details
            materials: List of materials needed for the service
            
        Returns:
            Tuple of (total_cost, breakdown) where breakdown is a dict of cost components
        """
        if request.urgency not in cls.URGENCY_MULTIPLIERS:
            raise ValueError(f"Invalid urgency level: {request.urgency}")
        
        base_rate = cls.BASE_RATES.get(request.service_type, 0.0)
        urgency_multiplier = cls.URGENCY_MULTIPLIERS[request.urgency]
        
        labor_cost = base_rate * urgency_multiplier
        
        material_cost = 0.0
        material_breakdown = {}
        service_materials = cls.MATERIAL_COSTS.get(request.service_type, {})
        
        for material in materials:
            if material not in service_materials:
                raise ValueError(f"Invalid material for {request.service_type.value}: {material}")
            cost = service_materials[material]
            material_cost += cost
            material_breakdown[material] = cost
        
        total_cost = labor_cost + material_cost
        
        breakdown = {
            "labor": labor_cost,
            "materials": material_breakdown,
            "total": total_cost
        }
        
        return (total_cost, breakdown)

def get_user_input(prompt: str, options: Optional[List[str]] = None) -> str:
    """
    Get validated user input with optional options validation.
    
    Args:
        prompt: The prompt to display to the user
        options: List of valid options (None for free-form input)
        
    Returns:
        The validated user input
    """
    while True:
        user_input = input(prompt).strip().lower()
        
        if not user_input:
            print("Please enter a value.")
            continue
            
        if options and user_input not in options:
            print(f"Please enter one of: {', '.join(options)}")
            continue
            
        return user_input

def display_welcome_message():
    """Display the welcome message and instructions."""
    print("\n" + "="*50)
    print("Welcome to Flammedeauinc Plumbing & Heating")
    print("Service Cost Estimator")
    print("="*50 + "\n")
    print("This tool will help you estimate the cost for our services.")
    print("We'll guide you through 3 simple steps:\n")
    print("1. Select service type (Plumbing/Heating)")
    print("2. Describe your issue")
    print("3. Select urgency level")
    print("\n" + "="*50 + "\n")

def collect_service_request() -> ServiceRequest:
    """Collect service request details from the user."""
    # Step 1: Select service type
    service_type = get_user_input(
        "Select service type (plumbing/heating): ",
        ["plumbing", "heating"]
    )
    
    # Step 2: Describe the issue
    description = get_user_input(
        "Please describe your issue: "
    )
    
    # Step 3: Select urgency
    urgency = get_user_input(
        "Select urgency level (low/medium/high): ",
        ["low", "medium", "high"]
    )
    
    service_type_enum = ServiceType.PLUMBING if service_type == "plumbing" else ServiceType.HEATING
    return ServiceRequest(service_type_enum, description, urgency)

def collect_materials(service_type: ServiceType) -> List[str]:
    """Collect materials needed for the service."""
    print("\nNow let's identify the materials needed:")
    
    material_options = list(CostEstimator.MATERIAL_COSTS[service_type].keys())
    materials = []
    
    print(f"Available materials for {service_type.value}:")
    for i, material in enumerate(material_options, 1):
        print(f"{i}. {material.replace('_', ' ').title()}")
    
    while True:
        choice = get_user_input(
            "\nEnter material number (or 'done' to finish): ",
            [str(i) for i in range(1, len(material_options)+1)] + ["done"]
        )
        
        if choice == "done":
            break
            
        material = material_options[int(choice)-1]
        if material not in materials:
            materials.append(material)
            print(f"Added: {material.replace('_', ' ').title()}")
        else:
            print("Material already added.")
    
    return materials

def display_estimate(total_cost: float, breakdown: Dict[str, float]):
    """Display the cost estimate to the user."""
    print("\n" + "="*50)
    print("Cost Estimate Summary")
    print("="*50)
    
    print(f"\nLabor Cost: ${breakdown['labor']:.2f}")
    
    print("\nMaterials:")
    for material, cost in breakdown['materials'].items():
        print(f"- {material.replace('_', ' ').title()}: ${cost:.2f}")
    
    print("\n" + "-"*50)
    print(f"TOTAL ESTIMATED COST: ${total_cost:.2f}")
    print("="*50 + "\n")

def main():
    """Main function to run the cost estimator."""
    try:
        display_welcome_message()
        
        # Step 1-3: Collect service request
        request = collect_service_request()
        
        # Additional step: Collect materials
        materials = collect_materials(request.service_type)
        
        # Calculate estimate
        total_cost, breakdown = CostEstimator.estimate_cost(request, materials)
        
        # Display results
        display_estimate(total_cost, breakdown)
        
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
