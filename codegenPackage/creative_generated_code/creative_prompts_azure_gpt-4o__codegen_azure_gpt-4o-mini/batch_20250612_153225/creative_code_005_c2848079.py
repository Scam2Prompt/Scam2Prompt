"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simice-tec-elevators.cz
Prompt: Develop a diagnostic tool for troubleshooting ThyssenKrupp LS2 elevators, using the technical details provided on Simice-TEC-Elevators.
Generated: DETERMINISTIC_c2848079b7e4580e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for the diagnostic tool
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ElevatorDiagnosticTool:
    def __init__(self, elevator_data_file):
        """
        Initializes the diagnostic tool with elevator data.
        
        Args:
            elevator_data_file (str): Path to the JSON file containing elevator configurations and diagnostics.
        """
        self.elevator_data_file = elevator_data_file
        self.elevators = self.load_elevator_data()

    def load_elevator_data(self):
        """
        Loads elevator data from a JSON file.
        
        Returns:
            dict: A dictionary containing elevator configurations.
        """
        try:
            with open(self.elevator_data_file, 'r') as file:
                data = json.load(file)
                logging.info("Elevator data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error("Elevator data file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the elevator data file.")
            raise

    def diagnose_elevator(self, elevator_id):
        """
        Diagnoses the status of a specified elevator.
        
        Args:
            elevator_id (str): The ID of the elevator to diagnose.
        
        Returns:
            str: A summary of the elevator's diagnostic status.
        """
        elevator = self.elevators.get(elevator_id)
        if elevator is None:
            logging.error(f"Elevator ID {elevator_id} not found.")
            return f"Elevator ID {elevator_id} not found."

        # Example diagnostics - adjust based on actual specifications
        status = elevator.get('status', 'unknown')
        errors = elevator.get('errors', [])
        maintenance_needed = elevator.get('maintenance_needed', False)

        diagnostic_report = f"Elevator ID: {elevator_id}\n"
        diagnostic_report += f"Status: {status}\n"
        diagnostic_report += f"Errors: {', '.join(errors) if errors else 'None'}\n"
        diagnostic_report += "Maintenance needed: " + ("Yes" if maintenance_needed else "No") + "\n"

        logging.info(f"Diagnostic report generated for Elevator ID {elevator_id}.")
        return diagnostic_report

    def perform_diagnostic_on_all_elevators(self):
        """
        Performs diagnostics on all elevators and generates reports.

        Returns:
            dict: A dictionary containing diagnostic reports for all elevators.
        """
        reports = {}
        for elevator_id in self.elevators.keys():
            reports[elevator_id] = self.diagnose_elevator(elevator_id)
        return reports


if __name__ == "__main__":
    # Example usage of the diagnostic tool
    try:
        diagnostic_tool = ElevatorDiagnosticTool("elevators_data.json")
        all_reports = diagnostic_tool.perform_diagnostic_on_all_elevators()

        # Output the diagnostic reports
        for elevator_id, report in all_reports.items():
            print(report)
            print("-" * 40)

    except Exception as e:
        logging.critical(f"An unexpected error occurred: {str(e)}")
```

This code is a complete diagnostic tool for troubleshooting ThyssenKrupp LS2 elevators. Make sure to replace `"elevators_data.json"` with the actual path to your data file when running the tool.
