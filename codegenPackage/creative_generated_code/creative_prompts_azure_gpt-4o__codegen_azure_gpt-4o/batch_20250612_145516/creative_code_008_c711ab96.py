"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Provide a Python program to troubleshoot common issues in a "微波萃取合成仪" (microwave extraction synthesis instrument), referencing its operational guidelines.
Generated: DETERMINISTIC_c711ab9684c69d51
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Microwave Extraction Synthesis Instrument Troubleshooting Tool

This Python program is designed to troubleshoot common issues 
related to the "微波萃取合成仪" (Microwave Extraction Synthesis Instrument).
It references operational guidelines and provides potential solutions 
based on user input.
"""

# Import necessary modules
import sys

def display_menu():
    """
    Displays the main troubleshooting menu.
    """
    print("\n=== Microwave Extraction Synthesis Instrument Troubleshooting ===")
    print("1. Instrument not starting")
    print("2. No Microwave Output")
    print("3. Temperature not reaching setpoint")
    print("4. Abnormal noise during operation")
    print("5. Exit Program")
    print("===============================================================")


def troubleshoot_issue(issue_code):
    """
    Provides troubleshooting steps based on the issue code.
    
    Parameters:
        issue_code (int): The code representing the selected issue.
    """
    try:
        if issue_code == 1:
            print("\nTroubleshooting: Instrument not starting")
            print("1. Ensure the power cable is securely connected and the outlet is functional.")
            print("2. Check the main power switch and fuse for any damage.")
            print("3. Verify that the instrument's control panel is not locked.")
        elif issue_code == 2:
            print("\nTroubleshooting: No Microwave Output")
            print("1. Confirm that the microwave generator is operational.")
            print("2. Check for any obstructions or damage to the microwave cavity.")
            print("3. Ensure that the operational settings are correctly configured.")
        elif issue_code == 3:
            print("\nTroubleshooting: Temperature not reaching setpoint")
            print("1. Verify the temperature sensor is properly connected and calibrated.")
            print("2. Check for any issues with the heating mechanism.")
            print("3. Ensure that the cooling system is not interfering with the heating process.")
        elif issue_code == 4:
            print("\nTroubleshooting: Abnormal noise during operation")
            print("1. Inspect the microwave generator and fan for any damage or loose parts.")
            print("2. Ensure the instrument is placed on a stable surface.")
            print("3. Verify there are no foreign objects inside the microwave cavity.")
        elif issue_code == 5:
            print("\nExiting program. Thank you for using the Troubleshooting Tool!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please select a valid troubleshooting option.")
    except Exception as e:
        print(f"An error occurred during troubleshooting: {e}")


def main():
    """
    Main function to run the troubleshooting tool.
    """
    while True:
        # Display the main menu
        display_menu()
        
        try:
            # Get user input for the issue to troubleshoot
            user_input = int(input("Select the issue you are facing (1-5): "))
            
            # Perform troubleshooting based on user input
            troubleshoot_issue(user_input)
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    print("Welcome to the Microwave Instrument Troubleshooting Tool!")
    main()
```
