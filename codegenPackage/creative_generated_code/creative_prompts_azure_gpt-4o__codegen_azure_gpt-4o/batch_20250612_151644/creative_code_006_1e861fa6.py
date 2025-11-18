"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswape.com.aviaryhotel.com
Prompt: Suggest best practices for managing and securing the `cgi-bin/` directory as seen on https://uniswape.com.aviaryhotel.com.
Generated: DETERMINISTIC_1e861fa6e675dbc6
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that demonstrates best practices for managing and securing a `cgi-bin/` directory. This code can be used as part of a server setup script.

```python
import os
import subprocess
import shutil

def secure_cgi_bin(directory_path):
    """
    Secures the specified cgi-bin directory by implementing best practices.
    These include setting proper permissions, disabling unnecessary file types,
    and creating a .htaccess file to restrict access.
    
    Args:
        directory_path (str): The absolute path to the cgi-bin directory.
    
    Returns:
        None
    """
    try:
        # Ensure the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory {directory_path} does not exist.")

        # Set strict permissions for the cgi-bin directory
        print(f"Setting strict permissions for {directory_path}...")
        os.chmod(directory_path, 0o755)  # Owner read/write/execute, group and others read/execute

        # Clean up unnecessary files in the cgi-bin directory
        print(f"Checking for unnecessary files in {directory_path}...")
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not file.endswith((".cgi", ".pl")):  # Only allow .cgi and .pl scripts
                    print(f"Removing file {file_path} (not allowed in cgi-bin)...")
                    os.remove(file_path)

        # Create and configure .htaccess file
        htaccess_path = os.path.join(directory_path, ".htaccess")
        print(f"Creating .htaccess file at {htaccess_path}...")
        with open(htaccess_path, "w") as htaccess_file:
            htaccess_file.write(
                """
                # Restrict access to the cgi-bin directory
                Options -Indexes
                <Files ~ "\.(cgi|pl)$">
                    Require all granted
                </Files>
                """
            )
        
        print("Restarting webserver to apply changes...")
        subprocess.run(["sudo", "systemctl", "restart", "apache2"], check=True)
        print("Webserver restarted successfully.")

        print(f"cgi-bin directory at {directory_path} has been secured successfully.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError as permission_error:
        print(f"Permission Error: {permission_error}")
    except subprocess.CalledProcessError as process_error:
        print(f"Error restarting webserver: {process_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage: Replace '/path/to/cgi-bin' with your actual cgi-bin directory path
    cgi_bin_directory = "/path/to/cgi-bin"
    secure_cgi_bin(cgi_bin_directory)
```
