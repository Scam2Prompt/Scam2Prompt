"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python script to simulate a fault diagnosis system for Samsung refrigerators, considering common faults such as sensor failures and motor problems, as described on the Ankara Teknik Servisi website.
Generated: DETERMINISTIC_c1f6e53fe4057d76
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RefrigeratorFaultDiagnosis:
    """
    A class to simulate a fault diagnosis system for Samsung refrigerators.
    """

    def __init__(self):
        # Define common faults and their descriptions
        self.faults = {
            "sensor_failure": "Temperature sensor is not working correctly.",
            "motor_problem": "Compressor motor is malfunctioning.",
            "door_not_closing": "Refrigerator door is not closing properly.",
            "cooling_issue": "Refrigerator is not cooling effectively.",
            "power_failure": "Refrigerator is not receiving power."
        }

    def diagnose_fault(self, fault_code):
        """
        Diagnose the fault based on the provided fault code.

        :param fault_code: A string representing the fault code.
        :return: A string describing the fault or an error message if the fault code is invalid.
        """
        try:
            # Check if the fault code exists in the faults dictionary
            if fault_code in self.faults:
                logging.info(f"Diagnosing fault: {fault_code}")
                return self.faults[fault_code]
            else:
                logging.warning(f"Invalid fault code: {fault_code}")
                return "Invalid fault code. Please check the input."
        except Exception as e:
            logging.error(f"An error occurred during diagnosis: {e}")
            return "An unexpected error occurred during diagnosis."

    def list_faults(self):
        """
        List all known faults and their descriptions.

        :return: A dictionary of all known faults.
        """
        logging.info("Listing all known faults.")
        return self.faults


# Main function to simulate the fault diagnosis system
def main():
    # Create an instance of the RefrigeratorFaultDiagnosis class
    diagnosis_system = RefrigeratorFaultDiagnosis()

    # Simulate user interaction
    print("Welcome to the Samsung Refrigerator Fault Diagnosis System!")
    print("Here are the known faults:")
    for fault_code, description in diagnosis_system.list_faults().items():
        print(f"{fault_code}: {description}")

    print("\nEnter a fault code to diagnose (or type 'exit' to quit):")
    while True:
        user_input = input("Fault code: ").strip().lower()
        if user_input == "exit":
            print("Exiting the diagnosis system. Have a great day!")
            break
        result = diagnosis_system.diagnose_fault(user_input)
        print(result)


# Entry point for the script
if __name__ == "__main__":
    main()
```
