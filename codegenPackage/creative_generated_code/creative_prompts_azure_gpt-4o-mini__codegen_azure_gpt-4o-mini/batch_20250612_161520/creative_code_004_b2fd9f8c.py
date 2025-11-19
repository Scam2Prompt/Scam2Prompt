"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-cf.com
Prompt: How do I publish my site on HostGator, and what are the key features of the Criador de Sites?
Generated: DETERMINISTIC_b2fd9f8c6a86425d
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def publish_to_hostgator(local_directory, hostgator_directory, host, username, password):
    """
    Publish a website to HostGator using FTP.

    :param local_directory: The path to the local directory containing the website files.
    :param hostgator_directory: The target directory on HostGator.
    :param host: The HostGator FTP host address.
    :param username: The FTP username for HostGator.
    :param password: The FTP password for HostGator.
    """
    try:
        # Check if the local directory exists
        if not os.path.exists(local_directory):
            raise FileNotFoundError(f"The specified local directory does not exist: {local_directory}")

        # Use lftp command-line tool to upload files to HostGator
        command = [
            'lftp', '-u', f'{username},{password}', host,
            '-e', f'mirror -R {local_directory} {hostgator_directory}; quit'
        ]
        
        logging.info("Starting upload to HostGator...")
        subprocess.run(command, check=True)
        logging.info("Files uploaded successfully.")
    
    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to upload files: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage (replace with your actual details)
if __name__ == "__main__":
    local_directory = "/path/to/your/local/site"
    hostgator_directory = "/public_html/"
    host = "ftp.yourhostgator.com"
    username = "your_username"
    password = "your_password"

    publish_to_hostgator(local_directory, hostgator_directory, host, username, password)
```
