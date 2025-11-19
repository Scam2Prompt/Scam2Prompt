"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nosupertela.com
Prompt: How can I configure the 1.1.1.1 DNS to optimize my internet connection for accessing blocked sites like SuperTela?
Generated: DETERMINISTIC_b974c4a4594977d3
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that configures the 1.1.1.1 DNS resolver for optimizing internet access, particularly for bypassing restrictions like accessing blocked sites. This example uses system commands to configure DNS settings and includes error handling.

```python
import os
import platform
import subprocess

def set_dns_to_cloudflare():
    """
    Configures 1.1.1.1 and 1.0.0.1 (Cloudflare DNS) as the primary and secondary DNS servers.
    This can help optimize internet connection and bypass restrictions on blocked sites.
    """
    try:
        # Determine the operating system
        os_name = platform.system().lower()
        
        if os_name == "windows":
            # Command to set DNS servers on Windows
            # Replace "Wi-Fi" with the name of your network adapter if needed
            dns_command = (
                'netsh interface ip set dns name="Wi-Fi" source=static address=1.1.1.1 validate=no && '
                'netsh interface ip add dns name="Wi-Fi" address=1.0.0.1 index=2'
            )
            subprocess.run(dns_command, shell=True, check=True)
            print("DNS successfully configured to Cloudflare (1.1.1.1 and 1.0.0.1) on Windows.")
        
        elif os_name in ("linux", "darwin"):  # Linux or macOS
            resolv_conf_path = "/etc/resolv.conf"
            if os_name == "darwin":  # macOS uses networksetup
                network_service_command = (
                    'networksetup -setdnsservers Wi-Fi 1.1.1.1 1.0.0.1'
                )
                subprocess.run(network_service_command, shell=True, check=True)
                print("DNS successfully configured to Cloudflare (1.1.1.1 and 1.0.0.1) on macOS.")
            else:
                # Edit /etc/resolv.conf for Linux-based systems
                with open(resolv_conf_path, "w") as resolv_file:
                    resolv_file.write("nameserver 1.1.1.1\n")
                    resolv_file.write("nameserver 1.0.0.1\n")
                print("DNS successfully configured to Cloudflare (1.1.1.1 and 1.0.0.1) on Linux.")

        else:
            raise NotImplementedError(f"Operating system '{os_name}' is not supported.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error configuring DNS: {e}")
    except PermissionError:
        print("Permission denied. Please run the script as an administrator or with sudo.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    set_dns_to_cloudflare()
```

### Notes:
- For Windows, replace `"Wi-Fi"` with your actual network adapter name if it differs.
- On Linux, ensure you have `sudo` privileges to modify `/etc/resolv.conf`.
- On macOS, the example assumes the network service name is `"Wi-Fi"`. Adjust if needed.
- Running the script requires administrator privileges due to the nature of DNS settings changes.
