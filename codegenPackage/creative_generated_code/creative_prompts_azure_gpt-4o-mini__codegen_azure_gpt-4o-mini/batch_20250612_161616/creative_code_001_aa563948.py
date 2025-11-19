"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhonybarros.com.br
Prompt: Write a Python function that simulates the process of sending exam requests through a pre-attendance system, ensuring the user can select a preferred unit for collection.
Generated: DETERMINISTIC_aa5639485c6a811a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PreAttendanceSystem:
    def __init__(self):
        # Initialize a list of available units
        self.available_units = ['Unit A', 'Unit B', 'Unit C', 'Unit D']

    def display_available_units(self):
        """Displays the available units to the user."""
        logging.info("Available units for collection:")
        for index, unit in enumerate(self.available_units, start=1):
            print(f"{index}. {unit}")

    def select_unit(self):
        """Prompts the user to select a preferred unit for collection."""
        while True:
            try:
                # Display available units
                self.display_available_units()
                # Get user input
                choice = int(input("Select a unit by number (1-4): "))
                
                # Validate user input
                if 1 <= choice <= len(self.available_units):
                    selected_unit = self.available_units[choice - 1]
                    logging.info(f"User selected: {selected_unit}")
                    return selected_unit
                else:
                    logging.warning("Invalid choice, please select a number between 1 and 4.")
            except ValueError:
                logging.error("Invalid input. Please enter a number.")
                print("Error: Please enter a valid number.")

    def send_exam_request(self, unit):
        """Simulates sending an exam request to the selected unit."""
        try:
            # Simulate sending request (placeholder for actual implementation)
            logging.info(f"Sending exam request to {unit}...")
            # Here you would include your logic to send the request
            logging.info("Exam request sent successfully.")
            return True
        except Exception as e:
            logging.error(f"Failed to send exam request: {e}")
            return False

def main():
    """Main function to run the pre-attendance system."""
    try:
        system = PreAttendanceSystem()
        selected_unit = system.select_unit()
        request_sent = system.send_exam_request(selected_unit)
        
        if request_sent:
            print("Your exam request has been sent successfully.")
        else:
            print("There was an issue sending your exam request.")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
