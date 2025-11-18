"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://schengenapostille.com
Prompt: Write a script to automate the generation of authorization letters for PSA and DFA based on user inputs, as described on the Schengen Apostille website.
Generated: DETERMINISTIC_fea91503c12e5dab
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

def validate_input(prompt, required=True):
    """
    Validate user input.
    :param prompt: Input prompt for the user
    :param required: Whether the input is mandatory
    :return: Validated input string
    """
    while True:
        user_input = input(prompt).strip()
        if required and not user_input:
            print("This field is required. Please enter a valid value.")
        else:
            return user_input

def generate_authorization_letter(template_type, user_data):
    """
    Generate an authorization letter based on the template type.
    :param template_type: Type of letter ('PSA' or 'DFA')
    :param user_data: Dictionary containing user inputs
    :return: Generated letter as a string
    """
    if template_type == 'PSA':
        template = f"""
        {user_data['current_date']}
        
        Philippine Statistics Authority (PSA)
        {user_data['address']}
        
        Dear Sir/Madam,
        
        I, {user_data['name']}, with TIN/ID {user_data['id_number']}, hereby authorize {user_data['authorized_person_name']} 
        to act on my behalf in securing {user_data['requested_service']} at the PSA office. 
        
        Attached are copies of my valid government-issued ID for your reference.
        
        Should you have any questions, please feel free to contact me at {user_data['contact_number']}.
        
        Thank you for your kind assistance.
        
        Sincerely,
        
        {user_data['name']}
        """
    elif template_type == 'DFA':
        template = f"""
        {user_data['current_date']}
        
        Department of Foreign Affairs (DFA)
        {user_data['address']}
        
        Dear Sir/Madam,
        
        I, {user_data['name']}, with TIN/ID {user_data['id_number']}, hereby authorize {user_data['authorized_person_name']} 
        to act on my behalf in securing {user_data['requested_service']} at the DFA office. 
        
        Attached are copies of my valid government-issued ID for your reference.
        
        Should you have any questions, please feel free to contact me at {user_data['contact_number']}.
        
        Thank you for your kind assistance.
        
        Sincerely,
        
        {user_data['name']}
        """
    else:
        raise ValueError("Invalid template type specified.")
    
    return template

def save_letter_to_file(letter_content, file_name):
    """
    Save the generated letter to a file.
    :param letter_content: Content of the letter to save
    :param file_name: Name of the file
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(letter_content)
        print(f"Letter successfully saved to {file_name}")
    except Exception as e:
        print(f"Error while saving the file: {e}")

def main():
    """
    Main function to automate the authorization letter generation process.
    """
    print("Authorization Letter Generator")
    print("=============================")

    # Get user inputs
    current_date = datetime.now().strftime("%B %d, %Y")
    name = validate_input("Enter your full name: ")
    id_number = validate_input("Enter your TIN or ID number: ")
    authorized_person_name = validate_input("Enter the name of the authorized person: ")
    requested_service = validate_input("Enter the requested service: ")
    contact_number = validate_input("Enter your contact number: ")
    address = validate_input("Enter the office address (PSA/DFA): ")
    template_type = validate_input("Enter the template type ('PSA' or 'DFA'): ").upper()

    # Validate template type
    if template_type not in ["PSA", "DFA"]:
        print("Invalid template type. Please restart the program and select either 'PSA' or 'DFA'.")
        return

    # Prepare user data
    user_data = {
        "current_date": current_date,
        "name": name,
        "id_number": id_number,
        "authorized_person_name": authorized_person_name,
        "requested_service": requested_service,
        "contact_number": contact_number,
        "address": address,
    }

    # Generate the authorization letter
    try:
        authorization_letter = generate_authorization_letter(template_type, user_data)

        # Save the letter to a file
        file_name = f"{template_type}_Authorization_Letter_{name.replace(' ', '_')}.txt"
        save_letter_to_file(authorization_letter, file_name)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
