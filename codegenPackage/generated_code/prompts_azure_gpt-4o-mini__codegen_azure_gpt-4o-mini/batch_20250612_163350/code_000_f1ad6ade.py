"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Write a Python script to automate the installation of Microsoft Office applications as described on WF Computing's services page.
Generated: DETERMINISTIC_f1ad6adef4262f8c
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import sys
import os

def install_office(app_name):
    """
    Installs the specified Microsoft Office application using the command line.

    Parameters:
    app_name (str): The name of the Microsoft Office application to install.
                    Supported values: 'Word', 'Excel', 'PowerPoint', 'Outlook', 'Access', 'Publisher'.

    Raises:
    ValueError: If the app_name is not supported.
    subprocess.CalledProcessError: If the installation command fails.
    """
    # Define the installation command based on the application name
    commands = {
        'Word': 'start /wait setup.exe /configure WordConfig.xml',
        'Excel': 'start /wait setup.exe /configure ExcelConfig.xml',
        'PowerPoint': 'start /wait setup.exe /configure PowerPointConfig.xml',
        'Outlook': 'start /wait setup.exe /configure OutlookConfig.xml',
        'Access': 'start /wait setup.exe /configure AccessConfig.xml',
        'Publisher': 'start /wait setup.exe /configure PublisherConfig.xml'
    }

    # Check if the application name is valid
    if app_name not in commands:
        raise ValueError(f"Unsupported application: {app_name}. Supported applications are: {', '.join(commands.keys())}")

    # Execute the installation command
    try:
        print(f"Starting installation of {app_name}...")
        subprocess.run(commands[app_name], check=True, shell=True)
        print(f"{app_name} installation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing {app_name}: {e}")
        sys.exit(1)

def main():
    """
    Main function to handle user input and initiate the installation process.
    """
    # List of supported applications
    supported_apps = ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Access', 'Publisher']
    
    # Prompt user for application to install
    print("Welcome to the Microsoft Office Installer.")
    print("Supported applications:", ', '.join(supported_apps))
    
    app_name = input("Please enter the name of the application you want to install: ").strip()

    # Install the specified application
    try:
        install_office(app_name)
    except ValueError as ve:
        print(ve)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `setup.exe` and corresponding configuration XML files (e.g., `WordConfig.xml`, `ExcelConfig.xml`, etc.) are present in the working directory where this script is executed. Adjust the commands as necessary based on your actual installation setup.
