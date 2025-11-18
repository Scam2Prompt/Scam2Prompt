"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write a program to recommend the best Econopure filtration system for aquaculture applications, considering water salinity and contaminant levels.
Generated: DETERMINISTIC_4570c219ae45a0db
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
# We'll use `sys` and `logging` for error handling and logging respectively.
import sys
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define Econopure filtration system recommendations
class EconopureFiltrationSystem:
    def __init__(self, name, salinity_range, contaminant_level_range):
        """
        Initialize filtration system attributes.
        
        :param name: Name of the filtration system.
        :param salinity_range: Tuple (min_salinity, max_salinity) in ppt (parts per thousand).
        :param contaminant_level_range: Tuple (min_contaminant, max_contaminant) in ppm (parts per million).
        """
        self.name = name
        self.salinity_range = salinity_range
        self.contaminant_level_range = contaminant_level_range

    def is_suitable(self, salinity, contaminant_level):
        """
        Check if the system is suitable for given salinity and contaminant levels.
        
        :param salinity: Water salinity in ppt.
        :param contaminant_level: Contaminant level in ppm.
        :return: True if suitable, False otherwise.
        """
        return (self.salinity_range[0] <= salinity <= self.salinity_range[1] and
                self.contaminant_level_range[0] <= contaminant_level <= self.contaminant_level_range[1])

# Define a function to recommend the best filtration system
def recommend_filtration_system(salinity, contaminant_level):
    """
    Recommend the best Econopure filtration system based on water salinity and contaminant levels.
    
    :param salinity: Water salinity in ppt.
    :param contaminant_level: Contaminant level in ppm.
    :return: Recommended filtration system name or a message indicating no suitable system.
    """
    try:
        # Validate inputs
        if salinity < 0 or contaminant_level < 0:
            raise ValueError("Salinity and contaminant levels must be non-negative values.")
        
        # Define available filtration systems
        systems = [
            EconopureFiltrationSystem("EconoPure Basic", (0, 10), (0, 50)),
            EconopureFiltrationSystem("EconoPure Advanced", (10, 30), (50, 100)),
            EconopureFiltrationSystem("EconoPure Pro", (30, 50), (100, 200))
        ]

        # Filter suitable systems
        suitable_systems = [system.name for system in systems if system.is_suitable(salinity, contaminant_level)]

        # Return the best recommendation or a fallback message if none are suitable
        if suitable_systems:
            logging.info("Recommendation successful.")
            return f"Recommended Filtration System(s): {', '.join(suitable_systems)}"
        else:
            return "No suitable filtration system found for given parameters."

    except ValueError as e:
        logging.error(f"Input Error: {e}")
        return str(e)
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        return "An error occurred while processing your request."

# Main function to execute the program
def main():
    """
    Main entry point for the program.
    """
    try:
        # Gather user input
        salinity = float(input("Enter water salinity (in ppt): "))
        contaminant_level = float(input("Enter contaminant level (in ppm): "))

        # Get the recommendation
        result = recommend_filtration_system(salinity, contaminant_level)

        # Print result
        print(result)

    except ValueError:
        logging.error("Invalid input. Please enter numeric values for salinity and contaminant level.")
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        logging.error(f"Unexpected error in main: {e}")
        print("Error: An unexpected error occurred.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
