"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polystack.tech
Prompt: How do I set up a cyber range using Polystack Technologies' products, specifically the VIDS and ATCC solutions?
Generated: DETERMINISTIC_6cdf77331da616dc
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for the setup
import os
import subprocess
import logging

# Configure logging for the setup process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CyberRangeSetup:
    def __init__(self, vid_path, atcc_path):
        """
        Initialize the CyberRangeSetup with paths to VIDS and ATCC solutions.

        :param vid_path: Path to the VIDS solution directory.
        :param atcc_path: Path to the ATCC solution directory.
        """
        self.vid_path = vid_path
        self.atcc_path = atcc_path

    def check_directory(self, path):
        """
        Check if the given directory exists.

        :param path: Directory path to check.
        :return: Boolean indicating the existence of the directory.
        """
        exists = os.path.isdir(path)
        logging.info(f"Checking directory: {path} - Exists: {exists}")
        return exists

    def setup_vids(self):
        """
        Set up the VIDS solution by executing the necessary commands.
        """
        if not self.check_directory(self.vid_path):
            logging.error(f"VIDS directory does not exist: {self.vid_path}")
            raise FileNotFoundError(f"VIDS directory not found: {self.vid_path}")

        # Example command to run VIDS setup (modify with actual command)
        command = f"cd {self.vid_path} && ./setup_vids.sh"
        try:
            logging.info("Setting up VIDS...")
            subprocess.run(command, shell=True, check=True)
            logging.info("VIDS setup completed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error during VIDS setup: {e}")
            raise RuntimeError("VIDS setup failed.")

    def setup_atcc(self):
        """
        Set up the ATCC solution by executing the necessary commands.
        """
        if not self.check_directory(self.atcc_path):
            logging.error(f"ATCC directory does not exist: {self.atcc_path}")
            raise FileNotFoundError(f"ATCC directory not found: {self.atcc_path}")

        # Example command to run ATCC setup (modify with actual command)
        command = f"cd {self.atcc_path} && ./setup_atcc.sh"
        try:
            logging.info("Setting up ATCC...")
            subprocess.run(command, shell=True, check=True)
            logging.info("ATCC setup completed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error during ATCC setup: {e}")
            raise RuntimeError("ATCC setup failed.")

    def setup_cyber_range(self):
        """
        Execute the complete setup of the cyber range by setting up VIDS and ATCC.
        """
        try:
            self.setup_vids()
            self.setup_atcc()
            logging.info("Cyber range setup completed successfully.")
        except Exception as e:
            logging.error(f"Cyber range setup failed: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual paths to VIDS and ATCC solutions
    vid_directory = "/path/to/vids"
    atcc_directory = "/path/to/atcc"

    # Create a CyberRangeSetup instance and initiate setup
    cyber_range_setup = CyberRangeSetup(vid_directory, atcc_directory)
    cyber_range_setup.setup_cyber_range()
```
