"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancepro.epizy.com
Prompt: Create a Python script to test multiple versions of PHP on a hosting service that supports both Python and PHP.
Generated: DETERMINISTIC_dbffec59f2e6c029
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import os
import sys
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PHPVersionTester:
    def __init__(self, php_versions, test_script_path):
        """
        Initializes the PHPVersionTester with the specified PHP versions and test script path.

        :param php_versions: List of PHP versions to test.
        :param test_script_path: Path to the PHP script to run for testing.
        """
        self.php_versions = php_versions
        self.test_script_path = test_script_path

    def run_test(self, php_version):
        """
        Runs the test script using the specified PHP version.

        :param php_version: The PHP version to use for testing.
        :return: Output of the test script and any errors encountered.
        """
        try:
            # Build the command to run the PHP script with the specified version
            command = [f'php{php_version}', self.test_script_path]
            logging.info(f"Running test for PHP version: {php_version}")
            
            # Execute the command and capture the output
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            if result.returncode != 0:
                logging.error(f"Error running PHP {php_version}: {result.stderr.strip()}")
                return None, result.stderr.strip()
            
            logging.info(f"Output for PHP {php_version}: {result.stdout.strip()}")
            return result.stdout.strip(), None
            
        except Exception as e:
            logging.exception(f"An exception occurred while testing PHP {php_version}: {e}")
            return None, str(e)

    def test_versions(self):
        """
        Tests all specified PHP versions by running the test script.
        """
        for version in self.php_versions:
            output, error = self.run_test(version)
            if error:
                logging.error(f"Test failed for PHP {version}: {error}")
            else:
                logging.info(f"Test completed successfully for PHP {version}")

if __name__ == "__main__":
    # List of PHP versions to test
    php_versions_to_test = ['7.4', '8.0', '8.1', '8.2']

    # Path to the PHP test script (update with your actual path)
    php_test_script = 'path/to/your/test_script.php'
    
    # Check if the test script exists
    if not os.path.exists(php_test_script):
        logging.error("The test script does not exist. Please check the provided path.")
        sys.exit(1)

    # Create an instance of PHPVersionTester and run tests
    tester = PHPVersionTester(php_versions=php_versions_to_test, test_script_path=php_test_script)
    tester.test_versions()
```
