"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syr-whistler.com
Prompt: Recommend libraries or tools for debugging CGI scripts in the "cgi-bin" directory on a Linux server.
Generated: DETERMINISTIC_bb9fcef97529c78a
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# CGI Debugging Tools and Libraries for Linux Servers

# Import necessary modules
import os
import sys
import logging
import cgi

# Set up basic logging configuration
logging.basicConfig(level=logging.DEBUG, 
                    filename='/var/log/cgi-bin/debug.log', 
                    filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_cgi_script(script_name):
    """
    Executes a CGI script located in the cgi-bin directory.

    Args:
        script_name (str): The name of the CGI script to execute.

    Raises:
        FileNotFoundError: If the script does not exist in the cgi-bin directory.
        PermissionError: If there are insufficient permissions to execute the script.
    """

    # Define the cgi-bin directory
    cgi_bin_dir = '/usr/lib/cgi-bin'
    script_path = os.path.join(cgi_bin_dir, script_name)

    try:
        # Check if the script exists
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script {script_name} not found in {cgi_bin_dir}.")

        # Check execute permissions
        if not os.access(script_path, os.X_OK):
            raise PermissionError(f"Script {script_name} is not executable.")

        # Log the execution attempt
        logging.debug(f"Executing script: {script_path}")

        # Execute the script
        result = os.system(script_path)

        # Log the result of execution
        if result == 0:
            logging.info(f"Script {script_name} executed successfully.")
        else:
            logging.error(f"Script {script_name} failed with exit code {result}.")

    except Exception as e:
        logging.exception(e)
        print(f"Content-Type: text/plain\n")
        print(f"Error: {str(e)}")

# Example usage: running a CGI script named 'example.py'
if __name__ == "__main__":
    run_cgi_script('example.py')
```

This code serves as a template for running CGI scripts, including logging and error handling. It is designed to be placed within a CGI script and will log debugging information to a specified log file. You can customize the `logging` configuration, script path, and other parameters as needed.
