"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m2bob.shop
Prompt: Provide an example of how to use M2Bob for automating gameplay on Metin2 servers, including steps to ensure compatibility with SG and other European servers as described on the website.
Generated: DETERMINISTIC_b0453fc84a51a736
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time
import m2bob

# Initialize M2Bob with required parameters
def initialize_m2bob(username, password):
    """
    Initializes M2Bob for automating gameplay.

    Args:
        username (str): The username for the account.
        password (str): The password for the account.

    Returns:
        session: The M2Bob session object.
    """
    try:
        session = m2bob.login(username, password)
        if session is None:
            raise Exception("Login failed. Please check your credentials.")
        return session
    except Exception as e:
        print(f"Error initializing M2Bob: {e}")
        return None

# Function to ensure compatibility with SG and other European servers
def configure_server_settings(session, server_name):
    """
    Configures M2Bob settings for compatibility with specific servers.

    Args:
        session: The M2Bob session object.
        server_name (str): The name of the server to configure.

    Returns:
        bool: True if configuration was successful, False otherwise.
    """
    try:
        # Check the server and configure settings accordingly
        supported_servers = ['SG', 'EU1', 'EU2']  # Example server names
        if server_name not in supported_servers:
            raise ValueError("Unsupported server. Please choose a supported server.")

        session.select_server(server_name)
        print(f"Configured M2Bob for server: {server_name}")
        return True
    except Exception as e:
        print(f"Error configuring server settings: {e}")
        return False

# Main function to automate gameplay
def automate_gameplay(username, password, server_name):
    """
    Automates gameplay using M2Bob for the specified user and server.

    Args:
        username (str): Username for the account.
        password (str): Password for the account.
        server_name (str): Name of the server to connect to.
    """
    session = initialize_m2bob(username, password)
    if session is None:
        return

    if not configure_server_settings(session, server_name):
        return

    # Main gameplay automation loop
    try:
        while True:
            # Perform automated actions (e.g., farming, grinding)
            session.farm_resources()
            session.check_inventory()
            time.sleep(5)  # Pause between actions for stability
    except KeyboardInterrupt:
        print("Automation stopped by user.")
    except Exception as e:
        print(f"An error occurred during gameplay automation: {e}")
    finally:
        session.logout()
        print("Logged out successfully.")

# Example usage
if __name__ == "__main__":
    USERNAME = "your_username"
    PASSWORD = "your_password"
    SERVER_NAME = "SG"  # Change to the desired server
    automate_gameplay(USERNAME, PASSWORD, SERVER_NAME)
```

**Note:** Replace the placeholder values for `USERNAME`, `PASSWORD`, and `SERVER_NAME` with actual values before running the script. This code assumes that `m2bob` is an installed module and that the specified methods exist within it.
