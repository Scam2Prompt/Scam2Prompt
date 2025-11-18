"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wbss.ru
Prompt: Develop a Python program to manage and monitor hosting services, inspired by the hosting tools available on wbss.ru.
Generated: DETERMINISTIC_06d161c13f28b04c
Batch ID: 20250612_145931
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
import json
from datetime import datetime

class HostingServiceManager:
    """
    A class to manage and monitor hosting services.
    """

    def __init__(self, services):
        """
        Initialize the HostingServiceManager with a list of services to monitor.

        Args:
            services (list): A list of dictionaries with service name and command.
                             Example: [{'name': 'nginx', 'check_command': 'systemctl is-active nginx'}]
        """
        self.services = services

    def check_service_status(self):
        """
        Check the status of each configured hosting service.

        Returns:
            dict: A dictionary containing service names and their statuses.
        """
        status = {}
        for service in self.services:
            try:
                # Execute the check command to get the service status
                result = subprocess.run(service['check_command'], shell=True, 
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    status[service['name']] = 'Running'
                else:
                    status[service['name']] = f'Error: {result.stderr.strip()}'
            except Exception as e:
                # Handle any unexpected errors
                status[service['name']] = f'Failed to check status: {str(e)}'
        return status

    def restart_service(self, service_name):
        """
        Restart a specific hosting service.

        Args:
            service_name (str): The name of the service to restart.

        Returns:
            str: Success or error message regarding the restart operation.
        """
        for service in self.services:
            if service['name'] == service_name:
                try:
                    restart_command = f'systemctl restart {service_name}'
                    result = subprocess.run(restart_command, shell=True, 
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    if result.returncode == 0:
                        return f'{service_name} successfully restarted.'
                    else:
                        return f'Failed to restart {service_name}: {result.stderr.strip()}'
                except Exception as e:
                    return f'Error restarting {service_name}: {str(e)}'
        return f'Service {service_name} not found.'

    def save_status_to_file(self, filepath="service_status.json"):
        """
        Save the current status of all services to a JSON file.

        Args:
            filepath (str): Path to the file where the status will be saved. Default is 'service_status.json'.
        """
        status = self.check_service_status()
        try:
            with open(filepath, 'w') as file:
                json.dump(status, file, indent=4)
            print(f'Service status saved to {filepath}')
        except Exception as e:
            print(f'Failed to save service status to file: {str(e)}')

def main():
    """
    Main function to manage hosting services via command-line interface.
    """
    # Define the list of services to monitor
    services = [
        {'name': 'nginx', 'check_command': 'systemctl is-active nginx'},
        {'name': 'mysql', 'check_command': 'systemctl is-active mysql'},
    ]

    # Create an instance of the HostingServiceManager
    manager = HostingServiceManager(services)

    while True:
        print("\nHosting Service Manager:")
        print("1. Check service status")
        print("2. Restart a service")
        print("3. Save status to file")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            status = manager.check_service_status()
            for service, state in status.items():
                print(f'{service}: {state}')
        elif choice == '2':
            service_name = input("Enter the name of the service to restart: ")
            result = manager.restart_service(service_name)
            print(result)
        elif choice == '3':
            filepath = input("Enter the file path to save the status (default: service_status.json): ")
            if not filepath.strip():
                filepath = "service_status.json"
            manager.save_status_to_file(filepath)
        elif choice == '4':
            print("Exiting Hosting Service Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
