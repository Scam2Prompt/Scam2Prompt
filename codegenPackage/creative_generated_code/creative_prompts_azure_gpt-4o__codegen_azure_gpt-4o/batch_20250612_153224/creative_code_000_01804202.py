"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write Python code to calculate the cost of cleaning and disinfecting poultry farming buildings based on the size of the building and specific services, as described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_01804202f23a93b3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the cost of cleaning and disinfecting poultry farming buildings based on the size of the building
and specific services selected. It uses pre-defined rates for each service type.
"""

# Constants for service costs (in EUR per square meter)
CLEANING_COST = 1.5  # Cost for cleaning per square meter
DISINFECTION_COST = 2.0  # Cost for disinfection per square meter
ADDITIONAL_SERVICE_COST = 0.8  # Cost for each additional service per square meter

def calculate_cost(building_size, services_selected):
    """
    Calculate the total cost of cleaning and disinfecting poultry farming buildings.

    Parameters:
        building_size (float): The size of the building in square meters.
        services_selected (list): List of selected services. Options are:
            - 'cleaning'
            - 'disinfection'
            - 'additional_service'

    Returns:
        float: The total cost in EUR.
    """
    if building_size <= 0:
        raise ValueError("Building size must be greater than zero.")
    
    # Validate services_selected input
    valid_services = {'cleaning', 'disinfection', 'additional_service'}
    if not all(service in valid_services for service in services_selected):
        raise ValueError(f"Invalid service(s) selected. Valid options are: {valid_services}")
    
    # Calculate costs based on selected services and building size
    total_cost = 0.0
    if 'cleaning' in services_selected:
        total_cost += building_size * CLEANING_COST
    if 'disinfection' in services_selected:
        total_cost += building_size * DISINFECTION_COST
    if 'additional_service' in services_selected:
        total_cost += building_size * ADDITIONAL_SERVICE_COST
    
    return round(total_cost, 2)  # Return the cost rounded to 2 decimal points

def main():
    """
    Main function to interact with the user and calculate cleaning/disinfection costs.
    """
    print("Welcome to the Poultry Farming Building Cleaning Calculator!")
    
    try:
        # Take user input for building size
        building_size = float(input("Enter the size of the building in square meters: "))
        
        # Take user input for services selected
        print("Select services to be performed (comma-separated). Options are: cleaning, disinfection, additional_service")
        services_input = input("Enter selected services: ").strip().lower()
        services_selected = [service.strip() for service in services_input.split(',')]
        
        # Calculate the total cost
        total_cost = calculate_cost(building_size, services_selected)
        print(f"The total cost for cleaning and disinfecting the building is: €{total_cost}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
