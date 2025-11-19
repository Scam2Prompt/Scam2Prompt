"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Develop a script to automate the process of sending WhatsApp messages to inquire about special offers for Jeep tours in Bali based on the contact information provided on the site.
Generated: DETERMINISTIC_24169a9ba3812576
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script for automating the process of sending WhatsApp messages using the Twilio API (which supports WhatsApp messaging). You’ll need a Twilio account and a verified phone number to use this script.

```python
import os
from twilio.rest import Client
import csv

# Configuration
TWILIO_ACCOUNT_SID = 'your_account_sid_here'  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = 'your_auth_token_here'    # Replace with your Twilio Auth Token
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio WhatsApp Sandbox Number
CSV_FILE_PATH = 'contacts.csv'                # Path to the CSV file containing contact information

# Function to load contacts from a CSV file
def load_contacts(file_path):
    """
    Load contacts from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list of dict: List of contacts, each represented as a dictionary.
    """
    contacts = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading contacts - {e}")
    return contacts

# Function to send a WhatsApp message
def send_whatsapp_message(client, to, message):
    """
    Send a WhatsApp message using the Twilio API.

    Args:
        client (twilio.rest.Client): Twilio API client instance.
        to (str): Recipient's WhatsApp number (e.g., 'whatsapp:+123456789').
        message (str): Message content.

    Returns:
        None
    """
    try:
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=to
        )
        print(f"Message sent successfully to {to}")
    except Exception as e:
        print(f"Error: Failed to send message to {to} - {e}")

# Main function
def main():
    """
    Main function to send WhatsApp messages to inquire about Jeep tours in Bali.
    """
    # Ensure Twilio credentials are set
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
        print("Error: Twilio account SID and auth token must be provided.")
        return

    # Initialize Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # Load contacts from the CSV file
    contacts = load_contacts(CSV_FILE_PATH)
    if not contacts:
        print("No contacts found. Exiting.")
        return

    # Define the message content
    message_content = "Hi, I'm interested in learning more about Jeep tours in Bali. Could you please share details about special offers? Thank you!"

    # Iterate over contacts and send messages
    for contact in contacts:
        # Ensure contact has the required fields
        name = contact.get('Name')
        phone = contact.get('Phone')
        if not phone:
            print(f"Skipping contact {name}: Missing phone number.")
            continue

        # Format the recipient's WhatsApp number
        whatsapp_number = f"whatsapp:{phone.strip()}"
        
        # Send the message
        send_whatsapp_message(client, whatsapp_number, message_content)

if __name__ == "__main__":
    main()
```

### Notes:
1. **CSV File Format**: The script assumes the `contacts.csv` file contains a header row with `Name` and `Phone` columns. Example:
   ```
   Name,Phone
   John Doe,+1234567890
   Jane Smith,+9876543210
   ```
2. **Twilio Account Credentials**: Replace `your_account_sid_here` and `your_auth_token_here` with your Twilio credentials.
3. **Twilio Sandbox**: If you’re using the Twilio WhatsApp Sandbox, ensure all recipient numbers are enrolled in the sandbox.
4. **Dependencies**: Install the Twilio Python SDK using `pip install twilio` before running the script.
