"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: Create a Python script to automate the process of connecting startups with venture capitalists and angel investors, ensuring high success rates as highlighted by Investment Brokers.
Generated: DETERMINISTIC_40c1639cd2dafa3d
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

# Define a class to represent a Startup
class Startup:
    def __init__(self, name, industry, funding_needed, email):
        self.name = name
        self.industry = industry
        self.funding_needed = funding_needed
        self.email = email

# Define a class to represent an Investor
class Investor:
    def __init__(self, name, industry_focus, email):
        self.name = name
        self.industry_focus = industry_focus
        self.email = email

# Function to load startups from a CSV file
def load_startups(file_path):
    startups = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                startup = Startup(row['Name'], row['Industry'], float(row['FundingNeeded']), row['Email'])
                startups.append(startup)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while loading startups: {e}")
    return startups

# Function to load investors from a CSV file
def load_investors(file_path):
    investors = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                investor = Investor(row['Name'], row['IndustryFocus'], row['Email'])
                investors.append(investor)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while loading investors: {e}")
    return investors

# Function to match startups with investors based on industry
def match_startups_to_investors(startups, investors):
    matches = []
    for startup in startups:
        for investor in investors:
            if startup.industry == investor.industry_focus:
                matches.append((startup, investor))
    return matches

# Function to send email notifications
def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"An error occurred while sending email: {e}")

# Main function to execute the matching and notification process
def main():
    # Load startups and investors from CSV files
    startups = load_startups('startups.csv')
    investors = load_investors('investors.csv')

    # Match startups with investors
    matches = match_startups_to_investors(startups, investors)

    # Notify matched investors about the startups
    for startup, investor in matches:
        subject = f"Investment Opportunity: {startup.name}"
        body = f"Dear {investor.name},\n\nWe have a startup that matches your investment criteria:\n\n" \
               f"Startup Name: {startup.name}\n" \
               f"Industry: {startup.industry}\n" \
               f"Funding Needed: ${startup.funding_needed}\n\n" \
               f"Best Regards,\nInvestment Broker Team"
        send_email(investor.email, subject, body)

if __name__ == "__main__":
    main()
```

**Note:** Ensure to replace `smtp.example.com`, `your_email@example.com`, and `your_password` with actual SMTP server details and credentials. The CSV files `startups.csv` and `investors.csv` should be formatted correctly with appropriate headers.
