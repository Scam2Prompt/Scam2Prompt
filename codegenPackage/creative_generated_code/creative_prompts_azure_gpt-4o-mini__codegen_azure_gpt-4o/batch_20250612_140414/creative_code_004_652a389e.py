"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trysonicsolutions.com
Prompt: Explain how ultrasonic cleaning can extend the lifespan of filters in the plastics industry and provide a case study example.
Generated: DETERMINISTIC_652a389ec81bce40
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script explains how ultrasonic cleaning can extend the lifespan of filters in the plastics industry
and provides a case study example via a simulated data analysis. The script is designed to be production-ready,
clean, and well-commented.
"""

import logging
import json

# Setting up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("ultrasonic_cleaning.log"),
        logging.StreamHandler()
    ]
)

def ultrasonic_cleaning_effectiveness(filters_data):
    """
    Simulates the effectiveness of ultrasonic cleaning on industrial filters.

    Parameters:
        filters_data (list): List of dictionaries containing filter data.
        
    Returns:
        updated_filters (list): List of dictionaries with updated filter lifespan data.
    """
    try:
        updated_filters = []
        for filter_item in filters_data:
            # Extracting filter details
            filter_id = filter_item.get("filter_id")
            original_lifespan = filter_item.get("original_lifespan")
            cleaning_frequency = filter_item.get("cleaning_frequency")
            
            if filter_id is None or original_lifespan is None or cleaning_frequency is None:
                raise ValueError(f"Invalid data for filter: {filter_item}")
            
            # Simulating the lifespan extension after ultrasonic cleaning
            # Assumption: Each ultrasonic cleaning extends lifespan by 10%
            extended_lifespan = original_lifespan * (1 + (cleaning_frequency * 0.10))
            updated_filters.append({
                "filter_id": filter_id,
                "original_lifespan": original_lifespan,
                "cleaning_frequency": cleaning_frequency,
                "extended_lifespan": round(extended_lifespan, 2)
            })
        
        logging.info("Ultrasonic cleaning effectiveness calculated successfully.")
        return updated_filters
    
    except Exception as e:
        logging.error(f"An error occurred during calculation: {e}")
        raise

def generate_case_study():
    """
    Generates a case study example for ultrasonic cleaning effectiveness.
    
    Returns:
        case_study_results (list): Simulated case study data with extended filter lifespan.
    """
    try:
        # Example data for filters in the plastics industry
        filters_data = [
            {"filter_id": 1, "original_lifespan": 1000, "cleaning_frequency": 5},
            {"filter_id": 2, "original_lifespan": 1500, "cleaning_frequency": 3},
            {"filter_id": 3, "original_lifespan": 1200, "cleaning_frequency": 4}
        ]
        
        # Calculate the effectiveness of ultrasonic cleaning
        case_study_results = ultrasonic_cleaning_effectiveness(filters_data)

        # Save the case study results to a JSON file
        with open("case_study_results.json", "w") as file:
            json.dump(case_study_results, file, indent=4)
        
        logging.info("Case study results generated and saved successfully.")
        return case_study_results
    
    except Exception as e:
        logging.error(f"An error occurred while generating the case study: {e}")
        raise

def main():
    """
    Main function to execute the script logic.
    """
    try:
        logging.info("Starting the ultrasonic cleaning analysis script.")

        # Generate and display the case study example
        results = generate_case_study()
        print("Case Study Results:")
        for result in results:
            print(result)
        
        logging.info("Script executed successfully.")
    
    except Exception as e:
        logging.critical(f"Script execution failed: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
