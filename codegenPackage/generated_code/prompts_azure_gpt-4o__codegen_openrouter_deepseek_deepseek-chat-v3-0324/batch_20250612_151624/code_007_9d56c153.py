"""
Generated Code Metadata:
========================
Original URL: https://dogedrop.org
Prompt: Write code to generate a secure Tor hidden service address for a whistleblower server, similar to the demo server example provided on WeDrop.org.
Generated: DETERMINISTIC_9d56c153af1a88f5
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Generates a secure Tor hidden service address for a whistleblower server.
"""

import os
import subprocess
import shutil
import stat
import secrets
import string
from pathlib import Path

# Configuration
HIDDEN_SERVICE_DIR = "/var/lib/tor/hidden_service/"
ONION_ADDRESS_FILE = os.path.join(HIDDEN_SERVICE_DIR, "hostname")
PRIVATE_KEY_FILE = os.path.join(HIDDEN_SERVICE_DIR, "private_key")
TORRC_PATH = "/etc/tor/torrc"
SERVICE_PORT = 80
HIDDEN_SERVICE_PORT = 80

def generate_random_password(length=32):
    """Generate a secure random password."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def setup_hidden_service():
    """Configure and start a Tor hidden service."""
    try:
        # Create hidden service directory with secure permissions
        Path(HIDDEN_SERVICE_DIR).mkdir(parents=True, exist_ok=True)
        os.chmod(HIDDEN_SERVICE_DIR, 0o700)

        # Generate Tor configuration
        torrc_content = f"""
HiddenServiceDir {HIDDEN_SERVICE_DIR}
HiddenServicePort {HIDDEN_SERVICE_PORT} 127.0.0.1:{SERVICE_PORT}
HiddenServiceVersion 3
"""

        # Backup existing torrc if it exists
        if os.path.exists(TORRC_PATH):
            shutil.copy2(TORRC_PATH, f"{TORRC_PATH}.bak")

        # Write new torrc
        with open(TORRC_PATH, 'w') as f:
            f.write(torrc_content)

        # Restart Tor service to apply changes
        subprocess.run(["systemctl", "restart", "tor"], check=True)

        # Wait for onion address to be generated
        max_attempts = 10
        for _ in range(max_attempts):
            if os.path.exists(ONION_ADDRESS_FILE):
                break
            time.sleep(1)
        else:
            raise RuntimeError("Failed to generate onion address")

        # Read onion address
        with open(ONION_ADDRESS_FILE, 'r') as f:
            onion_address = f.read().strip()

        # Set secure permissions for private key
        if os.path.exists(PRIVATE_KEY_FILE):
            os.chmod(PRIVATE_KEY_FILE, 0o600)

        return onion_address

    except Exception as e:
        print(f"Error setting up hidden service: {e}")
        raise

def main():
    """Main function to generate and display hidden service information."""
    try:
        print("Setting up Tor hidden service...")
        onion_address = setup_hidden_service()
        admin_password = generate_random_password()

        print("\n=== Whistleblower Server Configuration ===")
        print(f"Onion Address: {onion_address}")
        print(f"Admin Password: {admin_password}")
        print("\nImportant: Store the admin password securely as it cannot be recovered!")
        print(f"Hidden service files are stored in: {HIDDEN_SERVICE_DIR}")

    except Exception as e:
        print(f"Fatal error: {e}")
        exit(1)

if __name__ == "__main__":
    import time
    main()
```
