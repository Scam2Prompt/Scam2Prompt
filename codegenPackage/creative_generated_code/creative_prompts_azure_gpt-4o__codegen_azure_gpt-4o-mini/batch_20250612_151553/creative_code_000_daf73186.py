"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indexappl.rf.gd
Prompt: Write a Python script to deploy a web application on a hosting platform that supports Python, referencing iFastNet's hosting features like unlimited bandwidth and free SSL.
Generated: DETERMINISTIC_daf73186dd2be234
Batch ID: 20250612_151553
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
import sys

def deploy_web_app(local_directory, remote_directory, ftp_host, ftp_user, ftp_password):
    """
    Deploys a web application to iFastNet's hosting platform via FTP.

    Parameters:
    local_directory (str): The local path of the web application to deploy.
    remote_directory (str): The remote path on the hosting server.
    ftp_host (str): FTP host provided by the hosting platform.
    ftp_user (str): FTP username for authentication.
    ftp_password (str): FTP password for authentication.
    """
    
    # Check if local directory exists
    if not os.path.exists(local_directory):
        print(f"Error: Local directory '{local_directory}' does not exist.")
        sys.exit(1)

    # Change to the local directory
    os.chdir(local_directory)

    try:
        # Upload files using lftp, which is a robust FTP client
        subprocess.run(
            [
                "lftp",
                "-f",  # Read commands from the script
                "-e",
                f"set ftp:passive-mode on; mirror -R . {remote_directory}; quit",
                f"ftp://{ftp_user}:{ftp_password}@{ftp_host}"
            ],
            check=True
        )
        print("Deployment to iFastNet completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during deployment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Define parameters for deployment
    LOCAL_DIRECTORY = "/path/to/local/webapp"  # Local path to the web application
    REMOTE_DIRECTORY = "/path/to/remote/directory"  # Remote path on the server
    FTP_HOST = "ftp.yourdomain.com"  # Your FTP host
    FTP_USER = "your_username"  # Your FTP user
    FTP_PASSWORD = "your_password"  # Your FTP password

    # Call the deployment function
    deploy_web_app(LOCAL_DIRECTORY, REMOTE_DIRECTORY, FTP_HOST, FTP_USER, FTP_PASSWORD)
```

Make sure to install `lftp` on your system and replace the placeholder values (local and remote paths, FTP credentials) with actual values before running the script.
