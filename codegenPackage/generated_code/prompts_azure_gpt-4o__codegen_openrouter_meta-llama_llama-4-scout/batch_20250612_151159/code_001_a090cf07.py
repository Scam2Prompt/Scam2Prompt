"""
Generated Code Metadata:
========================
Original URL: https://dogem.life
Prompt: Generate code using the `paramiko` library to connect to a remote server via SSH and check the server's configuration files for errors.
Generated: DETERMINISTIC_a090cf07575640cc
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import paramiko
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_server(hostname: str, username: str, password: str, port: int = 22) -> paramiko.SSHClient:
    """
    Establish a connection to a remote server via SSH.

    Args:
        hostname (str): The hostname or IP address of the remote server.
        username (str): The username to use for the SSH connection.
        password (str): The password to use for the SSH connection.
        port (int): The port to use for the SSH connection (default: 22).

    Returns:
        paramiko.SSHClient: An SSH client object connected to the remote server.

    Raises:
        paramiko.AuthenticationException: If authentication fails.
        paramiko.SSHException: If an SSH error occurs.
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=hostname, username=username, password=password, port=port)
        logger.info(f"Connected to {hostname} via SSH")
        return ssh_client
    except paramiko.AuthenticationException:
        logger.error(f"Authentication failed for {username} on {hostname}")
        raise
    except paramiko.SSHException as e:
        logger.error(f"SSH error: {e}")
        raise

def check_config_files(ssh_client: paramiko.SSHClient, config_files: list[str]) -> dict[str, str]:
    """
    Check the server's configuration files for errors.

    Args:
        ssh_client (paramiko.SSHClient): An SSH client object connected to the remote server.
        config_files (list[str]): A list of configuration file paths to check.

    Returns:
        dict[str, str]: A dictionary containing the file paths as keys and error messages as values.
    """
    errors = {}

    for file in config_files:
        try:
            stdin, stdout, stderr = ssh_client.exec_command(f"cat {file} | grep -v '^#' | grep -v '^\\s*$' | wc -l")
            output = stdout.read().decode().strip()
            error_output = stderr.read().decode().strip()

            if error_output:
                errors[file] = error_output
            elif int(output) > 0:
                stdin, stdout, stderr = ssh_client.exec_command(f"cat {file} | grep -v '^#' | grep -v '^\\s*$'")
                output = stdout.read().decode().strip()
                errors[file] = output
        except paramiko.SSHException as e:
            logger.error(f"SSH error: {e}")
            errors[file] = str(e)

    return errors

def main():
    hostname = "example.com"
    username = "username"
    password = "password"
    config_files = ["/etc/ssh/sshd_config", "/etc/network/interfaces"]

    try:
        ssh_client = connect_to_server(hostname, username, password)
        errors = check_config_files(ssh_client, config_files)

        if errors:
            logger.error("Configuration file errors:")
            for file, error in errors.items():
                logger.error(f"{file}: {error}")
        else:
            logger.info("No configuration file errors found")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        if 'ssh_client' in locals():
            ssh_client.close()

if __name__ == "__main__":
    main()
```
