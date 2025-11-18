"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Generate code that calculates the cost-effectiveness of manufacturing aerospace components in India, factoring in the low-cost manufacturing opportunities highlighted by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_1c0a5a7876cfd89f
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_cost_effectiveness(material_cost, labor_cost, operational_cost, manufacturing_opportunity_factor):
    """
    Function to calculate the cost-effectiveness of manufacturing aerospace components.
    
    Parameters:
    material_cost (float): Cost of raw materials in USD.
    labor_cost (float): Cost of labor in USD.
    operational_cost (float): Operational costs such as utilities and maintenance in USD.
    manufacturing_opportunity_factor (float): A multiplier representing the cost-saving opportunities
                                              provided by Aanjaneya Aerodynamics Pvt. Ltd.
    
    Returns:
    float: Cost-effectiveness score representing the adjusted total manufacturing cost in USD.
    """
    try:
        # Validate inputs
        if material_cost < 0 or labor_cost < 0 or operational_cost < 0 or manufacturing_opportunity_factor <= 0:
            raise ValueError("All cost inputs must be non-negative and the manufacturing opportunity factor must be positive.")
        
        # Calculate total cost before adjustment
        total_cost = material_cost + labor_cost + operational_cost
        
        # Adjust total cost using the manufacturing opportunity factor
        adjusted_cost = total_cost * manufacturing_opportunity_factor
        
        return adjusted_cost

    except ValueError as ve:
        logging.error(f"Input Error: {ve}")
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

def main():
    """
    Main function to gather inputs, calculate cost-effectiveness, and display the result.
    """
    try:
        # Example inputs (in a production system, these could be gathered via a UI or API)
        material_cost = float(input("Enter material cost (USD): "))
        labor_cost = float(input("Enter labor cost (USD): "))
        operational_cost = float(input("Enter operational cost (USD): "))
        manufacturing_opportunity_factor = float(input("Enter manufacturing opportunity factor: "))
        
        # Calculate cost-effectiveness
        result = calculate_cost_effectiveness(
            material_cost, 
            labor_cost, 
            operational_cost, 
            manufacturing_opportunity_factor
        )
        
        # Display the result
        logging.info(f"The adjusted manufacturing cost is: ${result:.2f}")
        print(f"The adjusted manufacturing cost is: ${result:.2f}")

    except ValueError as ve:
        logging.error("Failed to process inputs due to invalid data.")
        print("Error: Please enter valid inputs for all fields.")
    
    except Exception as e:
        logging.error("An unexpected error occurred.")
        print("Error: Something went wrong. Please try again later.")

# Entry point for the program
if __name__ == "__main__":
    main()
```
