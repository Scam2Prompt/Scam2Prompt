"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogem.life
Prompt: Generate code using the `paramiko` library to connect to a remote server via SSH and check the server's configuration files for errors.
Generated: DETERMINISTIC_a090cf07575640cc
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import paramiko

def check_server_config(hostname, port, username, password, config_files):
    """
    Connects to a remote server via SSH and checks the specified configuration files for errors.
    
    Args:
        hostname (str): The hostname or IP address of the remote server.
        port (int): The SSH port to connect to (default SSH port is 22).
        username (str): The username for SSH authentication.
        password (str): The password for SSH authentication.
        config_files (list): List of file paths to check for errors on the server.
    
    Returns:
        dict: A dictionary with file paths as keys and their respective error messages (if any) as values.
    """
    results = {}  # Store the results of the file checks

    # Create an SSH client instance
    ssh_client = paramiko.SSHClient()

    # Automatically add unknown host keys (production environments should enforce stricter key policies)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        ssh_client.connect(hostname=hostname, port=port, username=username, password=password)
        print(f"Successfully connected to {hostname}")

        # Iterate through the list of configuration files
        for file_path in config_files:
            try:
                # Construct the shell command to check the configuration file
                command = f"cat {file_path}; echo 'Status: $?'"  # You can replace `cat` with specific validation commands

                # Execute the command on the remote server
                stdin, stdout, stderr = ssh_client.exec_command(command)

                # Fetch the command output
                output = stdout.read().decode('utf-8').strip()
                error_output = stderr.read().decode('utf-8').strip()

                # Check the exit status from the output
                if "Status: 0" in output:  # Assuming 0 means no error in the file
                    results[file_path] = "No errors found"
                else:
                    results[file_path] = f"Error detected: {error_output.strip() or 'Unknown error'}"

            except Exception as file_check_error:
                results[file_path] = str(file_check_error)

    except Exception as connection_error:
        print(f"Failed to connect to {hostname}: {connection_error}")
        results["connection_error"] = str(connection_error)

    finally:
        # Ensure the SSH connection is closed
        ssh_client.close()
        print("SSH connection closed")

    return results


# Example usage
if __name__ == "__main__":
    # Replace with your server details and configuration files to check
    HOSTNAME = "192.168.1.100"
    PORT = 22
    USERNAME = "admin"
    PASSWORD = "password123"
    CONFIG_FILES = ["/etc/nginx/nginx.conf", "/etc/ssh/sshd_config"]

    # Run the function and print the results
    results = check_server_config(HOSTNAME, PORT, USERNAME, PASSWORD, CONFIG_FILES)
    for file, status in results.items():
        print(f"{file}: {status}")
```
