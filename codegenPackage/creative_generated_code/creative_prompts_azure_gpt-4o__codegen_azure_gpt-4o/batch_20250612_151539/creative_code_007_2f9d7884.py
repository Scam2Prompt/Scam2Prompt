"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksa4-gen-ai.appcino-tech.com
Prompt: Create a script to authenticate users and allow them to view and print certificates as described in the services section of the Royal Commission for AlUla.
Generated: DETERMINISTIC_2f9d78843d3285c9
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for user authentication and certificate management system.
This script allows users to log in, view certificates, and print them.
"""

import sys
import hashlib
import json
import os

# Mock user database
USER_DB = {
    "user1": {
        "password_hash": hashlib.sha256("password123".encode()).hexdigest(),  # Password stored as hash
        "certificates": [
            {"id": 1, "name": "Certificate of Excellence", "details": "Issued on 2023-10-01"},
            {"id": 2, "name": "Environmental Stewardship Award", "details": "Issued on 2023-09-20"}
        ]
    },
    "user2": {
        "password_hash": hashlib.sha256("securepass".encode()).hexdigest(),  # Password stored as hash
        "certificates": [
            {"id": 1, "name": "Community Service Recognition", "details": "Issued on 2023-08-15"}
        ]
    }
}

def authenticate_user(username, password):
    """
    Authenticate user based on username and password.
    
    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    
    Returns:
        dict: User data if authentication is successful.
        None: If authentication fails.
    """
    user = USER_DB.get(username)
    if user and user.get("password_hash") == hashlib.sha256(password.encode()).hexdigest():
        return user
    return None

def view_certificates(user):
    """
    Display the list of certificates for the authenticated user.

    Args:
        user (dict): Authenticated user's data.
    """
    print("\nYour Certificates:")
    for cert in user["certificates"]:
        print(f"ID: {cert['id']}, Name: {cert['name']}, Details: {cert['details']}")

def print_certificate(user, certificate_id):
    """
    Print the content of a specific certificate.

    Args:
        user (dict): Authenticated user's data.
        certificate_id (int): The ID of the certificate to print.
    """
    certificate = next((cert for cert in user["certificates"] if cert["id"] == certificate_id), None)
    if certificate:
        print("\nPrinting Certificate:")
        print(f"Name: {certificate['name']}")
        print(f"Details: {certificate['details']}")
    else:
        print("\nError: Certificate not found.")

def main():
    """
    Main function to handle user interaction and execute authentication and certificate management.
    """
    try:
        # User authentication
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        user = authenticate_user(username, password)
        if not user:
            print("\nAuthentication failed. Please check your credentials.")
            return
        
        print("\nAuthentication successful!")

        # User menu for certificate management
        while True:
            print("\nMenu:")
            print("1. View Certificates")
            print("2. Print Certificate")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                view_certificates(user)
            elif choice == "2":
                cert_id = input("Enter the certificate ID to print: ").strip()
                if cert_id.isdigit():
                    print_certificate(user, int(cert_id))
                else:
                    print("\nError: Invalid certificate ID.")
            elif choice == "3":
                print("\nExiting. Have a great day!")
                break
            else:
                print("\nError: Invalid choice.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
