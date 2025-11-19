"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Write a script to automate the process of sending travel advisories and updates to clients, using email or WhatsApp APIs.
Generated: DETERMINISTIC_48d5cf6a4e60e1ab
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional

class TravelAdvisorySender:
    """
    A class to automate sending travel advisories and updates to clients via email or WhatsApp.
    """

    def __init__(self, config_file: str = "config.json"):
        """
        Initialize the TravelAdvisorySender with configuration from a JSON file.

        Args:
            config_file (str): Path to the configuration file. Defaults to "config.json".
        """
        self.config = self._load_config(config_file)
        self.email_config = self.config.get("email", {})
        self.whatsapp_config = self.config.get("whatsapp", {})

    def _load_config(self, config_file: str) -> Dict:
        """
        Load configuration from a JSON file.

        Args:
            config_file (str): Path to the configuration file.

        Returns:
            Dict: Configuration data.

        Raises:
            FileNotFoundError: If the config file does not exist.
            json.JSONDecodeError: If the config file is not valid JSON.
        """
        try:
            with open(config_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file '{config_file}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in config file.", doc=config_file, pos=0)

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """
        Send an email to the recipient.

        Args:
            recipient (str): Email address of the recipient.
            subject (str): Subject of the email.
            body (str): Body content of the email.

        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        try:
            msg = MIMEMultipart()
            msg["From"] = self.email_config.get("sender_email")
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(
                self.email_config.get("smtp_server"),
                self.email_config.get("smtp_port")
            ) as server:
                server.starttls()
                server.login(
                    self.email_config.get("sender_email"),
                    self.email_config.get("sender_password")
                )
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def send_whatsapp(self, recipient: str, message: str) -> bool:
        """
        Send a WhatsApp message to the recipient using an API.

        Args:
            recipient (str): Phone number of the recipient (with country code).
            message (str): Message content.

        Returns:
            bool: True if message was sent successfully, False otherwise.
        """
        try:
            url = self.whatsapp_config.get("api_url")
            headers = {
                "Authorization": f"Bearer {self.whatsapp_config.get('api_key')}",
                "Content-Type": "application/json"
            }
            payload = {
                "to": recipient,
                "message": message
            }
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Failed to send WhatsApp message: {e}")
            return False

    def send_advisory(
        self,
        recipients: List[Dict[str, str]],
        subject: str,
        message: str,
        method: str = "email"
    ) -> None:
        """
        Send travel advisories to a list of recipients via specified method.

        Args:
            recipients (List[Dict[str, str]]): List of recipients with their contact details.
            subject (str): Subject of the advisory.
            message (str): Advisory message content.
            method (str): Method to send advisories ("email" or "whatsapp"). Defaults to "email".

        Raises:
            ValueError: If an unsupported method is provided.
        """
        if method not in ["email", "whatsapp"]:
            raise ValueError("Unsupported method. Use 'email' or 'whatsapp'.")

        for recipient in recipients:
            contact = recipient.get(method)
            if not contact:
                print(f"Skipping recipient {recipient.get('name')}: No {method} contact.")
                continue

            if method == "email":
                success = self.send_email(contact, subject, message)
            else:
                success = self.send_whatsapp(contact, message)

            if success:
                print(f"Advisory sent to {recipient.get('name')} via {method}.")
            else:
                print(f"Failed to send advisory to {recipient.get('name')} via {method}.")

# Example usage
if __name__ == "__main__":
    try:
        sender = TravelAdvisorySender()

        # Example recipients data (replace with actual data)
        recipients = [
            {"name": "John Doe", "email": "john@example.com", "whatsapp": "+1234567890"},
            {"name": "Jane Smith", "email": "jane@example.com", "whatsapp": "+9876543210"}
        ]

        subject = "Important Travel Advisory Update"
        message = """
        Dear Traveler,

        This is an important update regarding your upcoming travel.
        Please check the latest advisories at our website.

        Safe travels,
        Travel Team
        """

        # Send via email
        sender.send_advisory(recipients, subject, message, method="email")

        # Send via WhatsApp
        sender.send_advisory(recipients, subject, message, method="whatsapp")

    except Exception as e:
        print(f"An error occurred: {e}")
```
