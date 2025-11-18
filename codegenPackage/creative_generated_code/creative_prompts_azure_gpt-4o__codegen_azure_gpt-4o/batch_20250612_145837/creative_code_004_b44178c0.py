"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sorncluern.com
Prompt: Write code to verify the successful installation of a LEMP stack configured via the BitLaunch app.
Generated: DETERMINISTIC_b44178c050a6f949
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess

def check_service_status(service_name):
    """
    Check the status of a given service using systemctl.
    
    Args:
        service_name (str): Name of the service to check.
    
    Returns:
        bool: True if the service is active, False otherwise.
    """
    try:
        # Run the systemctl command to check service status
        result = subprocess.run(
            ['systemctl', 'is-active', service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Return True if the service is 'active', False otherwise
        return result.stdout.strip() == 'active'
    except Exception as e:
        # Log any exceptions encountered
        print(f"Error checking status for {service_name}: {e}")
        return False


def verify_lemp_installation():
    """
    Verify the successful installation of the LEMP stack (Linux, Nginx, MySQL, PHP).
    
    Returns:
        dict: Dictionary containing the status of each component.
    """
    # List of services to verify for LEMP stack
    services = {
        "nginx": "Nginx Web Server",
        "mysql": "MySQL Database Server",
        "php-fpm": "PHP FastCGI Process Manager"
    }
    
    verification_status = {}
    
    for service, description in services.items():
        # Check the status of each service
        is_active = check_service_status(service)
        verification_status[description] = "Running" if is_active else "Not Running"
    
    return verification_status


if __name__ == "__main__":
    """
    Main entry point of the script. Verifies the LEMP stack installation and 
    displays the status of each component.
    """
    print("Verifying LEMP stack installation...")
    
    # Verify LEMP stack installation
    status = verify_lemp_installation()
    
    # Display the status of each component
    for component, state in status.items():
        print(f"{component}: {state}")
    
    # Check if all services are running
    all_running = all(state == "Running" for state in status.values())
    
    if all_running:
        print("\nLEMP stack installation verified successfully!")
    else:
        print("\nLEMP stack installation verification failed. Please check the service statuses.")
```
