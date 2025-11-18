"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmakers.co.nz
Prompt: Provide a script or steps to disable Microsoft Edge from opening PDF files by default, following the instructions on the Webmakers website.
Generated: DETERMINISTIC_bbaba6675f728cc6
Batch ID: 20250612_154400
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
import sys

def disable_edge_pdf_default():
    """
    Disables Microsoft Edge from opening PDF files by default on Windows.
    This function modifies the Windows Registry to change the default PDF
    handler to another application, such as Adobe Acrobat Reader.
    """

    # Define the path to the registry command
    command = [
        "reg", "add", 
        r"HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\pdf\UserChoice", 
        "/v", "ProgId", 
        "/t", "REG_SZ", 
        "/d", "AcroExch.Document",  # This is the ProgId for Adobe Acrobat Reader
        "/f"
    ]

    try:
        # Execute the command to modify the registry
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check the result of the command
        if result.returncode == 0:
            print("Successfully changed the default PDF handler to Adobe Acrobat Reader.")
        else:
            print("Failed to change the default PDF handler.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while modifying the registry: {e.stderr.decode().strip()}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Ensure the script is being run as an administrator
    if not is_admin():
        print("Please run this script as an administrator.")
        sys.exit(1)

    disable_edge_pdf_default()

def is_admin():
    """
    Checks if the script is running with administrative privileges.
    Returns True if the script has admin rights, otherwise False.
    """
    try:
        return os.getuid() == 0  # Unix/Linux
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin()  # Windows

```
