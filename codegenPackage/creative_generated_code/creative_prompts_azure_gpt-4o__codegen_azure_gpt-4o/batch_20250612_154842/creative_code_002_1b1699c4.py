"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Create a Python script to collect and analyze email sign-up data from the Swell Creative Management website, ensuring compliance with privacy policies.
Generated: DETERMINISTIC_1b1699c477b90b50
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
import re
from datetime import datetime

# Constants
DATA_FILE = 'email_signups.csv'  # CSV file to store the collected data
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # Regex for validating email addresses

# Ensure compliance with privacy policies
PRIVACY_POLICY_NOTICE = """
By using this script, you agree to follow all applicable privacy laws
and regulations, including GDPR and CCPA. Do not use this script to
collect or analyze email data without explicit consent from users.
"""

print(PRIVACY_POLICY_NOTICE)

# Function to validate email address
def is_valid_email(email):
    """Validate email using regex."""
    return re.match(EMAIL_REGEX, email) is not None

# Function to save email data
def save_email_data(email, timestamp):
    """
    Save email sign-up data to a CSV file.

    Args:
        email (str): The email address to save.
        timestamp (str): The timestamp of the sign-up.
    """
    try:
        file_exists = os.path.isfile(DATA_FILE)
        
        # Open the file in append mode
        with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header if the file does not exist
            if not file_exists:
                writer.writerow(['Email', 'Timestamp'])
            
            # Write the email and timestamp
            writer.writerow([email, timestamp])
    except Exception as e:
        print(f"Error saving email data: {e}")

# Function to analyze collected email data
def analyze_email_data():
    """
    Analyze the email sign-up data.
    Prints the total number of sign-ups and unique domains.
    """
    try:
        if not os.path.isfile(DATA_FILE):
            print("No data file found. Please collect email sign-ups first.")
            return
        
        domain_counts = {}
        total_signups = 0
        
        # Read the file
        with open(DATA_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                total_signups += 1
                email = row['Email']
                domain = email.split('@')[-1]
                
                if domain in domain_counts:
                    domain_counts[domain] += 1
                else:
                    domain_counts[domain] = 1
        
        print(f"Total sign-ups: {total_signups}")
        print("Unique domains:")
        for domain, count in domain_counts.items():
            print(f" - {domain}: {count}")
    except Exception as e:
        print(f"Error analyzing email data: {e}")

# Function to collect email data
def collect_email_data():
    """
    Collect email data interactively from the user.
    """
    try:
        print("Enter email addresses to sign up (type 'exit' to stop):")
        while True:
            email = input("Email: ").strip()
            
            if email.lower() == 'exit':
                print("Exiting...")
                break
            
            if is_valid_email(email):
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                save_email_data(email, timestamp)
                print(f"Email '{email}' saved successfully.")
            else:
                print(f"Invalid email address: '{email}'. Please try again.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"Error collecting email data: {e}")

# Main script logic
if __name__ == '__main__':
    print("Welcome to the Swell Creative Management Email Sign-Up Data Tool")
    print("1. Collect email sign-ups")
    print("2. Analyze email data")
    print("3. Exit")
    
    try:
        while True:
            choice = input("Choose an option (1/2/3): ").strip()
            
            if choice == '1':
                collect_email_data()
            elif choice == '2':
                analyze_email_data()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
