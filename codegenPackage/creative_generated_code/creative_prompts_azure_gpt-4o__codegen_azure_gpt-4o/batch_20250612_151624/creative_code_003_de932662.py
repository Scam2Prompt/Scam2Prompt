"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Develop a Python script to calculate additional costs for relocating appliances like sinks or ovens during cabinetry installation, referencing the considerations mentioned on the United Cabinetry site.
Generated: DETERMINISTIC_de932662db76c324
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate additional costs for relocating appliances during cabinetry installation.
The costs are based on typical considerations for relocating sinks or ovens, such as plumbing, electrical work, and labor.
"""

import logging


# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate_relocation_cost(appliance_type, distance_to_move, plumbing_required, electrical_required):
    """
    Calculate the cost of relocating an appliance during cabinetry installation.

    Parameters:
        appliance_type (str): Type of appliance ('sink' or 'oven').
        distance_to_move (int): Distance to move the appliance in feet.
        plumbing_required (bool): Whether plumbing work is required for relocation.
        electrical_required (bool): Whether electrical work is required for relocation.

    Returns:
        float: Total cost of relocation.
    """
    try:
        # Base cost per appliance type
        base_cost = 0
        if appliance_type.lower() == "sink":
            base_cost = 200  # Base cost for relocating a sink
        elif appliance_type.lower() == "oven":
            base_cost = 150  # Base cost for relocating an oven
        else:
            raise ValueError("Invalid appliance type. Must be 'sink' or 'oven'.")
        
        # Distance cost multiplier (e.g., $10 per foot)
        distance_cost = distance_to_move * 10
        
        # Plumbing and electrical costs
        plumbing_cost = 150 if plumbing_required else 0
        electrical_cost = 100 if electrical_required else 0
        
        # Calculate total cost
        total_cost = base_cost + distance_cost + plumbing_cost + electrical_cost
        
        logging.info("Relocation cost calculated successfully.")
        return total_cost
    
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    """
    Main function for testing the script and calculating relocation costs.
    """
    try:
        # Example input
        appliance_type = "sink"
        distance_to_move = 5  # in feet
        plumbing_required = True
        electrical_required = False
        
        # Calculate and print the relocation cost
        cost = calculate_relocation_cost(
            appliance_type,
            distance_to_move,
            plumbing_required,
            electrical_required
        )
        
        if cost is not None:
            print(f"The total relocation cost for the {appliance_type} is: ${cost:.2f}")
        else:
            print("Failed to calculate relocation cost. Please check the logs for details.")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")
```
