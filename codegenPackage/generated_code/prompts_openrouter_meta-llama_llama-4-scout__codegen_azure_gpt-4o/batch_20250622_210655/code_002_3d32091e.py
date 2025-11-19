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

def get_service_type():
    """
    Prompt the user to select a service type.
    Returns:
        str: The selected service type.
    """
    print("Select a service type:")
    print("1. Plumbing")
    print("2. Heating")
    
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice == 1:
            return "Plumbing"
        elif choice == 2:
            return "Heating"
        else:
            print("Invalid choice. Please select 1 or 2.")
            return get_service_type()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_service_type()

def get_service_details(service_type):
    """
    Prompt the user to provide details about the selected service.
    Args:
        service_type (str): The type of service selected.
    Returns:
        dict: A dictionary containing service details.
    """
    print(f"\nYou selected {service_type}. Please provide the following details:")
    try:
        hours_required = float(input("Enter the estimated hours required for the job: "))
        material_cost = float(input("Enter the estimated cost of materials ($): "))
        urgency = input("Is the service urgent? (yes/no): ").strip().lower()
        
        if urgency not in ["yes", "no"]:
            print("Invalid input for urgency. Please enter 'yes' or 'no'.")
            return get_service_details(service_type)
        
        return {
            "hours_required": hours_required,
            "material_cost": material_cost,
            "urgency": urgency
        }
    except ValueError:
        print("Invalid input. Please enter numeric values for hours and material cost.")
        return get_service_details(service_type)

def calculate_estimate(service_details):
    """
    Calculate the total estimate based on service details.
    Args:
        service_details (dict): A dictionary containing service details.
    Returns:
        float: The total estimated cost.
    """
    hourly_rate = 50.0  # Base hourly rate ($)
    urgency_multiplier = 1.5 if service_details["urgency"] == "yes" else 1.0
    
    labor_cost = service_details["hours_required"] * hourly_rate * urgency_multiplier
    total_cost = labor_cost + service_details["material_cost"]
    
    return total_cost

def main():
    """
    Main function to execute the service estimate process.
    """
    print("Welcome to the Plumbing and Heating Service Estimator!")
    
    try:
        service_type = get_service_type()
        service_details = get_service_details(service_type)
        total_estimate = calculate_estimate(service_details)
        
        print("\n--- Estimate Summary ---")
        print(f"Service Type: {service_type}")
        print(f"Hours Required: {service_details['hours_required']}")
        print(f"Material Cost: ${service_details['material_cost']:.2f}")
        print(f"Urgency: {'Urgent' if service_details['urgency'] == 'yes' else 'Standard'}")
        print(f"Total Estimated Cost: ${total_estimate:.2f}")
        print("------------------------")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
