"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogedrop.org
Prompt: Write Python code to deploy a Globaleaks whistleblower server on a rented cloud server, as described on WeDrop.org, ensuring anonymity and safety for reporting sources.
Generated: DETERMINISTIC_93011f4b68c652ac
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys
import os

def install_globaleaks():
    """
    Installs and configures the Globaleaks whistleblower server on a rented cloud server.
    Ensures all dependencies are installed and the environment is secure for anonymity and reporting.
    """
    try:
        print("Updating package lists...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        print("Installing dependencies...")
        dependencies = [
            "software-properties-common", 
            "curl", 
            "apt-transport-https"
        ]
        subprocess.run(["sudo", "apt-get", "install", "-y"] + dependencies, check=True)

        print("Adding Globaleaks repository...")
        # Add the Globaleaks repository for installation
        subprocess.run(["sudo", "add-apt-repository", "-y", "ppa:globaleaks/ppa"], check=True)

        print("Updating package lists after adding repository...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        print("Installing Globaleaks...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "globaleaks"], check=True)

        print("Setting up Globaleaks...")
        subprocess.run(["sudo", "globaleaks"], check=True)

        print("Globaleaks installation and setup complete.")
        print("You can access the web interface of Globaleaks by navigating to the IP address of your server.")
        print("Ensure proper firewall and anonymity configurations are in place.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred during execution: {e}")
        sys.exit(1)
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        sys.exit(1)

def configure_firewall():
    """
    Configures the server firewall to ensure anonymity and security for reporting sources.
    """
    try:
        print("Configuring UFW firewall...")

        # Enable UFW firewall
        subprocess.run(["sudo", "ufw", "enable"], check=True)

        print("Allowing SSH traffic...")
        # Allow SSH traffic
        subprocess.run(["sudo", "ufw", "allow", "ssh"], check=True)

        print("Allowing HTTPS traffic...")
        # Allow HTTPS traffic for web interface access
        subprocess.run(["sudo", "ufw", "allow", "https"], check=True)

        print("Blocking other traffic...")
        # Deny other traffic
        subprocess.run(["sudo", "ufw", "default", "deny"], check=True)

        print("Firewall configuration complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during firewall configuration: {e}")
        sys.exit(1)
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        sys.exit(1)

def configure_tor():
    """
    Configures Tor to provide anonymity for the Globaleaks server.
    """
    try:
        print("Installing Tor...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "tor"], check=True)

        print("Setting up Tor configuration...")
        tor_config_path = "/etc/tor/torrc"
        
        # Append HiddenService configuration to torrc file
        with open(tor_config_path, "a") as tor_config:
            tor_config.write("\n")
            tor_config.write("# Hidden Service configuration for Globaleaks\n")
            tor_config.write("HiddenServiceDir /var/lib/tor/hidden_service/\n")
            tor_config.write("HiddenServicePort 80 127.0.0.1:8080\n")
        
        print("Restarting Tor service...")
        subprocess.run(["sudo", "systemctl", "restart", "tor"], check=True)

        print("Tor configuration complete.")
        print("Your Globaleaks server is now accessible via an Onion address.")
        print("Check the /var/lib/tor/hidden_service/hostname file for the Onion address.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during Tor configuration: {e}")
        sys.exit(1)
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        sys.exit(1)

def main():
    """
    Main function to deploy and configure Globaleaks whistleblower server.
    """
    print("Starting Globaleaks server deployment...")
    
    install_globaleaks()
    configure_firewall()
    configure_tor()
    
    print("Globaleaks server deployment complete.")
    print("Ensure to regularly update the server and monitor for security patches.")

if __name__ == "__main__":
    main()
```
