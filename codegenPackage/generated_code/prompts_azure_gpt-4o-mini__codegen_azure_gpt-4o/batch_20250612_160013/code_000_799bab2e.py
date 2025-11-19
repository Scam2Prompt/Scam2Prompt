"""
Generated Code Metadata:
========================
Original URL: https://prohappyfamily.com
Prompt: Generate a Python script that implements a method for improving communication in relationships, inspired by the techniques discussed in the "Счастливая жена - счастливая семья" course.
Generated: DETERMINISTIC_799bab2ec6f55a93
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script implements a method for improving communication in relationships.
Inspired by techniques from the "Счастливая жена - счастливая семья" course, it focuses on active listening,
expressing gratitude, and constructive dialogue. The script provides a simple CLI-based tool for practicing these techniques.
"""

import sys

def active_listening():
    """
    Prompts the user to practice active listening by entering what their partner said
    and reflecting it back to ensure understanding.
    """
    try:
        print("\n--- Active Listening Exercise ---")
        partner_message = input("Enter what your partner said: ").strip()
        if not partner_message:
            raise ValueError("Input cannot be empty. Please enter a valid message.")
        
        print(f"Reflecting back: 'I hear you saying: \"{partner_message}\". Is that correct?'")
        confirmation = input("Did your partner confirm this? (yes/no): ").strip().lower()
        if confirmation == "yes":
            print("Great! You've successfully practiced active listening.")
        else:
            print("Try again to ensure you understand your partner's message.")
    except Exception as e:
        print(f"Error during active listening exercise: {e}")

def express_gratitude():
    """
    Prompts the user to express gratitude by entering something they appreciate about their partner.
    """
    try:
        print("\n--- Expressing Gratitude Exercise ---")
        gratitude_message = input("Enter something you appreciate about your partner: ").strip()
        if not gratitude_message:
            raise ValueError("Input cannot be empty. Please enter a valid message.")
        
        print(f"Expressing gratitude: 'I really appreciate {gratitude_message}. Thank you for being amazing!'")
    except Exception as e:
        print(f"Error during expressing gratitude exercise: {e}")

def constructive_dialogue():
    """
    Prompts the user to practice constructive dialogue by entering a concern and framing it positively.
    """
    try:
        print("\n--- Constructive Dialogue Exercise ---")
        concern = input("Enter a concern you'd like to discuss with your partner: ").strip()
        if not concern:
            raise ValueError("Input cannot be empty. Please enter a valid concern.")
        
        print(f"Framing positively: 'I feel [emotion] about [concern]. Can we work together to find a solution?'")
    except Exception as e:
        print(f"Error during constructive dialogue exercise: {e}")

def main():
    """
    Main function to run the communication improvement exercises.
    Provides a menu for the user to select an exercise.
    """
    try:
        print("Welcome to the Relationship Communication Improvement Tool!")
        while True:
            print("\nPlease select an exercise:")
            print("1. Active Listening")
            print("2. Express Gratitude")
            print("3. Constructive Dialogue")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ").strip()
            if choice == "1":
                active_listening()
            elif choice == "2":
                express_gratitude()
            elif choice == "3":
                constructive_dialogue()
            elif choice == "4":
                print("Thank you for using the tool. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1-4).")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
