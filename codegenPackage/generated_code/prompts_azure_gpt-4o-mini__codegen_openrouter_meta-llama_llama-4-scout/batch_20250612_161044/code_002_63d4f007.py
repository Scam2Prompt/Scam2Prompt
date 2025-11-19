"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: Create a script that automates the process of sending an online enquiry for a Chardham Yatra tour package, including user input for travel dates and preferences.
Generated: DETERMINISTIC_63d4f007c5d1eeb4
Batch ID: 20250612_161044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import getpass

# Define constants
CHARDHAM_YATRA_PACKAGE_DETAILS = {
    "package_name": "Chardham Yatra Tour Package",
    "duration": "10 days",
    "destinations": ["Yamunotri", "Gangotri", "Kedarnath", "Badrinath"]
}

# Function to get user input for travel dates and preferences
def get_user_input():
    try:
        # Get travel dates from user
        travel_dates = input("Enter travel dates (DD-MM-YYYY to DD-MM-YYYY): ")
        start_date, end_date = travel_dates.split(" to ")
        start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y").date()
        end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y").date()

        # Get user preferences
        num_travelers = int(input("Enter number of travelers: "))
        accommodation_type = input("Enter accommodation type (Hotel/Guest House): ")

        return {
            "travel_dates": f"{start_date} to {end_date}",
            "num_travelers": num_travelers,
            "accommodation_type": accommodation_type
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Function to send online enquiry email
def send_enquiry_email(user_input):
    try:
        # Define email configuration
        sender_email = input("Enter sender email: ")
        sender_password = getpass.getpass("Enter sender password: ")
        recipient_email = "chardhamyatra@example.com"  # Replace with actual recipient email

        # Create email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = "Online Enquiry for Chardham Yatra Tour Package"

        # Create email body
        email_body = f"""
        Dear Chardham Yatra Team,

        I am writing to inquire about the {CHARDHAM_YATRA_PACKAGE_DETAILS['package_name']}.

        Travel Dates: {user_input['travel_dates']}
        Number of Travelers: {user_input['num_travelers']}
        Accommodation Type: {user_input['accommodation_type']}

        Please find below my details:
        - Package Name: {CHARDHAM_YATRA_PACKAGE_DETAILS['package_name']}
        - Duration: {CHARDHAM_YATRA_PACKAGE_DETAILS['duration']}
        - Destinations: {', '.join(CHARDHAM_YATRA_PACKAGE_DETAILS['destinations'])}

        Thank you for your time and assistance.

        Best regards,
        {sender_email}
        """
        msg.attach(MIMEText(email_body, "plain"))

        # Send email using SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print("Enquiry email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Main function
def main():
    user_input = get_user_input()
    if user_input:
        send_enquiry_email(user_input)

if __name__ == "__main__":
    main()
```
