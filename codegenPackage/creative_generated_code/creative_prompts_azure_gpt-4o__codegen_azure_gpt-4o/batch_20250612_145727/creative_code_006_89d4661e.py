"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nosupertela.com
Prompt: Develop a script to automate the process of switching DNS to 1.1.1.1 when accessing streaming platforms like SuperTela, ensuring stable and unrestricted connectivity.
Generated: DETERMINISTIC_89d4661e61b2d2ba
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import platform
import subprocess
import os
import sys

def is_admin():
    """
    Check if the script is being run with administrative privileges.
    """
    if os.name == 'nt':  # Windows
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() == 1
        except Exception:
            return False
    elif os.name == 'posix':  # macOS/Unix/Linux
        return os.geteuid() == 0
    else:
        raise NotImplementedError("Unsupported operating system.")

def switch_dns_to_cloudflare():
    """
    Switch system DNS to Cloudflare's public DNS (1.1.1.1 and 1.0.0.1).
    """
    system_os = platform.system()

    try:
        if system_os == "Windows":
            # Set DNS for Windows
            print("Switching DNS to Cloudflare on Windows...")
            subprocess.run([
                "netsh", "interface", "ip", "set", "dns", "name=Wi-Fi",
                "source=static", "address=1.1.1.1"
            ], check=True)
            subprocess.run([
                "netsh", "interface", "ip", "add", "dns", "name=Wi-Fi",
                "address=1.0.0.1", "index=2"
            ], check=True)

        elif system_os == "Darwin":  # macOS
            # Set DNS for macOS
            print("Switching DNS to Cloudflare on macOS...")
            subprocess.run([
                "networksetup", "-setdnsservers", "Wi-Fi", "1.1.1.1", "1.0.0.1"
            ], check=True)

        elif system_os == "Linux":
            # Set DNS for Linux
            print("Switching DNS to Cloudflare on Linux...")
            resolv_conf_path = "/etc/resolv.conf"
            backup_path = "/etc/resolv.conf.backup"

            # Backup existing resolv.conf
            if not os.path.exists(backup_path):
                print("Creating a backup of /etc/resolv.conf...")
                subprocess.run(["cp", resolv_conf_path, backup_path], check=True)

            with open(resolv_conf_path, "w") as resolv_conf:
                resolv_conf.write("nameserver 1.1.1.1\n")
                resolv_conf.write("nameserver 1.0.0.1\n")

        else:
            raise NotImplementedError(f"Unsupported operating system: {system_os}")

        print("DNS successfully switched to Cloudflare (1.1.1.1, 1.0.0.1).")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting DNS: {e}")
        sys.exit(1)

def check_streaming_access():
    """
    Check if a streaming platform like SuperTela is accessible.
    """
    print("Checking connectivity to SuperTela...")
    try:
        response = subprocess.run(
            ["ping", "-c", "3", "supertela.com"],  # Replace with actual domain
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if response.returncode == 0:
            print("SuperTela is accessible.")
        else:
            print("Failed to access SuperTela. Please check your network.")
    except Exception as e:
        print(f"Error during connectivity check: {e}")
        sys.exit(1)

def main():
    """
    Main function to switch DNS and ensure streaming platform access.
    """
    if not is_admin():
        print("This script must be run with administrative privileges.")
        sys.exit(1)

    try:
        switch_dns_to_cloudflare()
        check_streaming_access()
    except NotImplementedError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
