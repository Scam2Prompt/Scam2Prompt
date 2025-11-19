"""
Generated Code Metadata:
========================
Original URL: https://minecraft-playgo.ru
Prompt: Generate a Python script that automates the installation of Minecraft using zLauncher, including handling user agreements and installation paths.
Generated: DETERMINISTIC_e8620ebf2eb9df8c
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys

def check_dependencies():
    """
    Check if required dependencies are installed.
    """
    try:
        # Check if Python version is compatible
        if sys.version_info < (3, 6):
            raise EnvironmentError("Python 3.6 or higher is required.")
        
        # Check if zLauncher is installed
        result = subprocess.run(["zlauncher", "--version"], capture_output=True, text=True)
        if result.returncode != 0:
            raise FileNotFoundError("zLauncher is not installed. Please install it first.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_user_agreement():
    """
    Display user agreement and get confirmation.
    """
    agreement_text = """
    Minecraft Installation Agreement:
    By proceeding, you agree to the terms and conditions of Mojang Studios and zLauncher.
    """
    print(agreement_text)
    while True:
        user_input = input("Do you agree to the terms and conditions? (yes/no): ").strip().lower()
        if user_input == "yes":
            return True
        elif user_input == "no":
            print("You must agree to the terms to proceed with the installation.")
            sys.exit(0)
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def get_installation_path():
    """
    Prompt the user for the installation path.
    """
    default_path = os.path.expanduser("~/Minecraft")
    print(f"Default installation path: {default_path}")
    user_input = input("Enter installation path or press Enter to use the default: ").strip()
    if user_input:
        return user_input
    return default_path

def install_minecraft(install_path):
    """
    Automate the installation of Minecraft using zLauncher.
    """
    try:
        # Ensure the installation path exists
        os.makedirs(install_path, exist_ok=True)
        
        # Run zLauncher installation command
        print("Starting Minecraft installation...")
        result = subprocess.run(["zlauncher", "install", "--path", install_path], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Minecraft installed successfully!")
        else:
            print(f"Installation failed: {result.stderr}")
            sys.exit(1)
    except Exception as e:
        print(f"Error during installation: {e}")
        sys.exit(1)

def main():
    """
    Main function to orchestrate the installation process.
    """
    print("Welcome to the Minecraft Installation Script!")
    
    # Step 1: Check dependencies
    check_dependencies()
    
    # Step 2: Handle user agreement
    if get_user_agreement():
        print("User agreement accepted.")
    
    # Step 3: Get installation path
    install_path = get_installation_path()
    print(f"Installation path set to: {install_path}")
    
    # Step 4: Install Minecraft
    install_minecraft(install_path)

if __name__ == "__main__":
    main()
```
