"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://technicalpower.us
Prompt: Create a diagnostic tool for identifying the six most common causes of data center downtime (e.g., UPS battery failure, accidental EPO, etc.) using the insights provided by Technical Power Service, Inc.
Generated: DETERMINISTIC_3b15a504222e9203
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class DataCenterDiagnosticTool:
    """
    A diagnostic tool for identifying the six most common causes of data center downtime.
    This tool provides guidance on pinpointing issues based on user input.
    """

    def __init__(self):
        # Initialize the logger
        self.logger = logging.getLogger("DataCenterDiagnosticTool")
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # List of common causes of downtime
        self.downtime_causes = [
            "UPS Battery Failure",
            "Accidental Emergency Power Off (EPO)",
            "Overheating of Servers or Equipment",
            "Network Connectivity Issues",
            "Human Error in Configuration or Maintenance",
            "Cooling System Failures"
        ]

    def perform_diagnosis(self):
        """
        Performs a diagnosis based on user input, suggesting potential causes of downtime.
        """
        try:
            self.logger.info("Starting diagnostic tool...")
            print("Welcome to the Data Center Diagnostic Tool!")
            print("Please answer the following questions to diagnose potential issues.")

            # Questions for diagnosis
            questions = {
                "Are you experiencing unexpected power shutdowns?": ["UPS Battery Failure", "Accidental Emergency Power Off (EPO)"],
                "Are server temperatures unusually high?": ["Overheating of Servers or Equipment", "Cooling System Failures"],
                "Is network connectivity disrupted?": ["Network Connectivity Issues"],
                "Are there signs of misconfiguration or maintenance errors?": ["Human Error in Configuration or Maintenance"]
            }

            potential_causes = set()

            for question, causes in questions.items():
                user_response = input(f"{question} (yes/no): ").strip().lower()

                if user_response == 'yes':
                    potential_causes.update(causes)

            # Display diagnostic results
            if potential_causes:
                print("\nPotential Causes of Downtime:")
                for cause in potential_causes:
                    print(f"- {cause}")
            else:
                print("\nNo potential causes identified based on your input.")
            self.logger.info("Diagnostic completed.")
        except Exception as e:
            self.logger.error(f"An error occurred during diagnosis: {e}")
            print("An error occurred while running the diagnostic tool. Please try again later.")

    def show_common_causes(self):
        """
        Displays the six most common causes of downtime.
        """
        print("\nSix Most Common Causes of Data Center Downtime:")
        for cause in self.downtime_causes:
            print(f"- {cause}")

    @staticmethod
    def validate_input(prompt):
        """
        Validates user input for yes/no questions.
        """
        while True:
            response = input(prompt).strip().lower()
            if response in ['yes', 'no']:
                return response
            print("Invalid input. Please enter 'yes' or 'no'.")

# Entry point for the tool
if __name__ == "__main__":
    tool = DataCenterDiagnosticTool()
    tool.show_common_causes()
    tool.perform_diagnosis()
```
