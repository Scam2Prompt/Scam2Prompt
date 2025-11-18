"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://z-innovations.de
Prompt: Recommend a library or framework to integrate custom scripting for CNC programming, focusing on the type of API and COM interface solutions provided by z-innovations.
Generated: DETERMINISTIC_601fcb7ff67f2f52
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script demonstrates basic integration with a CNC programming library using an example API 
and COM interface solution provided by z-innovations. This script assumes the relevant z-innovations 
library is installed and registered on the system.

Ensure you have the necessary z-innovations API documentation available for detailed usage.
"""

import win32com.client  # Library to interact with COM interfaces on Windows
import logging

# Configure logging to capture errors and activity for debugging purposes
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("cnc_integration.log"), logging.StreamHandler()]
)

class CNCProgrammingIntegration:
    """
    Class to integrate and interact with the z-innovations CNC programming API.
    """

    def __init__(self):
        """
        Initializes the COM interface connection to the z-innovations CNC programming library.
        """
        try:
            # Create an instance of the COM object for the z-innovations library
            self.cnc_api = win32com.client.Dispatch("ZInnovations.CNC.API")
            logging.info("Successfully connected to the z-innovations CNC API.")
        except Exception as e:
            logging.error("Failed to initialize CNC API: %s", str(e))
            raise RuntimeError("Error initializing CNC API.") from e

    def create_custom_script(self, script_name, script_content):
        """
        Creates a custom CNC script using the z-innovations API.

        :param script_name: Name of the custom script to be created.
        :param script_content: Content of the CNC script.
        :return: True if the script is created successfully, False otherwise.
        """
        try:
            # Call the API function to create a script
            result = self.cnc_api.CreateScript(script_name, script_content)
            
            if result:  # Check if the operation was successful
                logging.info("Script '%s' created successfully.", script_name)
                return True
            else:
                logging.warning("Failed to create script '%s'.", script_name)
                return False
        except Exception as e:
            logging.error("Error creating script '%s': %s", script_name, str(e))
            return False

    def execute_script(self, script_name):
        """
        Executes a CNC script using the z-innovations API.

        :param script_name: Name of the script to execute.
        :return: True if the script is executed successfully, False otherwise.
        """
        try:
            # Call the API function to execute a script
            result = self.cnc_api.ExecuteScript(script_name)
            
            if result:  # Check if the operation was successful
                logging.info("Script '%s' executed successfully.", script_name)
                return True
            else:
                logging.warning("Failed to execute script '%s'.", script_name)
                return False
        except Exception as e:
            logging.error("Error executing script '%s': %s", script_name, str(e))
            return False

    def list_available_scripts(self):
        """
        Retrieves a list of all available CNC scripts using the z-innovations API.

        :return: List of script names, or an empty list if an error occurs.
        """
        try:
            # Call the API function to list scripts
            scripts = self.cnc_api.GetAvailableScripts()
            logging.info("Retrieved available scripts: %s", scripts)
            return scripts
        except Exception as e:
            logging.error("Error retrieving available scripts: %s", str(e))
            return []

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the integration class
        cnc_integration = CNCProgrammingIntegration()

        # Create a custom script
        script_name = "SampleScript"
        script_content = "G01 X100 Y100; G01 X200 Y200; G01 X300 Y300;"
        if cnc_integration.create_custom_script(script_name, script_content):
            logging.info("Custom script creation succeeded.")

        # Execute the custom script
        if cnc_integration.execute_script(script_name):
            logging.info("Custom script execution succeeded.")

        # List all available CNC scripts
        available_scripts = cnc_integration.list_available_scripts()
        logging.info("Available Scripts: %s", available_scripts)
    except Exception as e:
        logging.critical("Unexpected error occurred: %s", str(e))
```

**Notes:**
- This script uses `pywin32` (win32com.client) to interact with Windows COM interfaces. Make sure `pywin32` is installed (`pip install pywin32`).
- Replace `"ZInnovations.CNC.API"` with the actual COM interface name provided by z-innovations.
- Error handling is implemented to log issues and prevent runtime crashes.
- The example script content provided is assumed to follow a standard CNC programming format. Adjust as needed based on actual requirements.
