"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftgo.site
Prompt: Create a Python script to automate sending personalized gift suggestions via email, inspired by the GiftGo app's functionality.
Generated: DETERMINISTIC_e379d48c2b38cfcb
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Function to send personalized gift suggestions via email
def send_gift_suggestion(recipient_email, recipient_name, gift_suggestion):
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Personalized Gift Suggestion"

    # Create the email body
    body = f"Hi {recipient_name},\n\nWe thought you'd love this gift suggestion:\n{gift_suggestion}\n\nHappy gifting!"
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(message)  # Send the email
        print(f"Gift suggestion sent to {recipient_name} at {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email to {recipient_name}. Error: {e}")

# Function to read recipients and their gift suggestions from a CSV file
def read_gift_suggestions(file_path):
    suggestions = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                suggestions.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return suggestions

# Main function to automate sending gift suggestions
def main():
    # File path to the CSV containing email, name, and gift suggestion
    csv_file_path = 'gift_suggestions.csv'
    gift_suggestions = read_gift_suggestions(csv_file_path)

    # Iterate through each suggestion and send an email
    for entry in gift_suggestions:
        send_gift_suggestion(entry['email'], entry['name'], entry['gift'])

if __name__ == "__main__":
    main()
```

**Note**: Before running the script, replace `your_email@example.com`, `your_password`, and `smtp.example.com` with actual email credentials and SMTP server details. The CSV file `gift_suggestions.csv` should have columns: `email`, `name`, and `gift`.
