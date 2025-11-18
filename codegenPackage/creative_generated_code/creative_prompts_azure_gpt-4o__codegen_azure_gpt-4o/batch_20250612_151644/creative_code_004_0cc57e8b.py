"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://complyaml.com
Prompt: Develop a beginner-friendly interactive training module in Python for AML compliance, similar to the methods described on ComplyAML's website.
Generated: DETERMINISTIC_0cc57e8b11ba13c7
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def clear_console():
    """
    Clears the console screen for a cleaner user interface.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def display_welcome_message():
    """
    Displays the welcome message for the training module.
    """
    print("Welcome to the AML Compliance Training Module!")
    print("This interactive training will guide you through key concepts.")
    print("Type your responses when prompted and press Enter to continue.\n")


def display_menu():
    """
    Displays the main menu options.
    Returns:
        int: User's menu selection.
    """
    print("\nChoose a section to begin:")
    print("1. Introduction to AML")
    print("2. Recognizing Suspicious Activity")
    print("3. Reporting and Compliance Procedures")
    print("4. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in range(1, 5):
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def introduction_to_aml():
    """
    Provides an overview of AML concepts.
    """
    clear_console()
    print("Introduction to AML:")
    print("Anti-Money Laundering (AML) refers to laws, regulations, and procedures designed to prevent criminals from disguising illegally obtained funds as legitimate income.")
    print("Key Concepts:")
    print("1. Money laundering involves three steps: placement, layering, and integration.")
    print("2. AML frameworks ensure transparency in financial transactions.")
    
    input("\nPress Enter to return to the menu...")


def recognizing_suspicious_activity():
    """
    Interactive section on identifying suspicious activities.
    """
    clear_console()
    print("Recognizing Suspicious Activity:")
    print("Suspicious activities include:")
    print("1. Large cash transactions.")
    print("2. Transactions involving high-risk countries.")
    print("3. Structuring transactions to avoid reporting thresholds.")
    
    print("\nQuestion: Would a customer depositing $9,999 repeatedly over several days be suspicious? (yes/no)")
    answer = input("Your answer: ").strip().lower()
    
    if answer == "yes":
        print("Correct! This is an example of structuring transactions to avoid reporting thresholds.")
    else:
        print("Incorrect. Repeated deposits just below the reporting threshold are a common red flag.")
    
    input("\nPress Enter to return to the menu...")


def reporting_and_compliance_procedures():
    """
    Interactive section on reporting and compliance.
    """
    clear_console()
    print("Reporting and Compliance Procedures:")
    print("Financial institutions are required to:")
    print("1. Report suspicious activities to relevant authorities.")
    print("2. Monitor and document customer transactions.")
    print("3. Maintain compliance programs and train employees regularly.")
    
    print("\nQuestion: What form is typically used in the U.S. to report suspicious activities? (SAR, CTR, or KYC)")
    answer = input("Your answer: ").strip().upper()
    
    if answer == "SAR":
        print("Correct! A Suspicious Activity Report (SAR) is used to report potential money laundering.")
    else:
        print(f"Incorrect. The correct answer is SAR. '{answer}' is not the appropriate form for this purpose.")
    
    input("\nPress Enter to return to the menu...")


def main():
    """
    Main function that runs the training module.
    """
    clear_console()
    display_welcome_message()
    
    while True:
        choice = display_menu()
        
        if choice == 1:
            introduction_to_aml()
        elif choice == 2:
            recognizing_suspicious_activity()
        elif choice == 3:
            reporting_and_compliance_procedures()
        elif choice == 4:
            clear_console()
            print("Thank you for participating in the AML Compliance Training Module!")
            print("Stay compliant and vigilant!")
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please restart the program.")
```
