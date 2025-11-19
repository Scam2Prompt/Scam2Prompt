"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: How can I implement a registration system for a prize giveaway similar to the one described on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_d9ef2051bdc0d704
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

# Define a dictionary to store registrants' data
registrants = {}

# Validate email address format
def is_valid_email(email):
    """Validate if the email address has a proper format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

# Validate name format (e.g., only letters and spaces)
def is_valid_name(name):
    """Ensure the name contains only valid characters."""
    return bool(re.match(r"^[a-zA-Z\s]+$", name))

# Register a new user
def register_user(name, email):
    """
    Register a user for the prize giveaway.

    Args:
        name (str): Full name of the registrant.
        email (str): Email address of the registrant.

    Returns:
        str: Success message or error message.
    """
    if not is_valid_name(name):
        return "Error: Name must contain only letters and spaces."
    
    if not is_valid_email(email):
        return "Error: Invalid email format."
    
    if email in registrants:
        return "Error: This email has already been registered."
    
    # Add the registrant to the dictionary
    registrants[email] = {
        "name": name,
        "email": email,
        "registration_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return f"Success: {name} has been registered for the prize giveaway."

# Display all registrants (for admin use)
def list_registrants():
    """
    List all registrants for the prize giveaway.

    Returns:
        str: A formatted list of all registrants.
    """
    if not registrants:
        return "No registrants found."
    
    formatted_list = "Prize Giveaway Registrants:\n"
    formatted_list += "-" * 30 + "\n"
    for idx, (email, data) in enumerate(registrants.items(), start=1):
        formatted_list += f"{idx}. Name: {data['name']}, Email: {data['email']}, Registered At: {data['registration_time']}\n"
    return formatted_list

# Main function to simulate the registration system
def main():
    """
    Main function to interact with the registration system.
    """
    print("Welcome to the Prize Giveaway Registration System!")
    while True:
        print("\nChoose an option:")
        print("1. Register for the giveaway")
        print("2. List all registrants (Admin view)")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue
        
        if choice == 1:
            name = input("Enter your full name: ")
            email = input("Enter your email address: ")
            print(register_user(name, email))
        elif choice == 2:
            print(list_registrants())
        elif choice == 3:
            print("Thank you for using the registration system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
