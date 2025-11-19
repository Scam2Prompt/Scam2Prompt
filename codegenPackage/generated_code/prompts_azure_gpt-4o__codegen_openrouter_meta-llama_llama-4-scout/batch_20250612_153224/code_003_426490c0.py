"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: Provide code to build a feature that allows users to save a list of desired properties and email it to themselves, similar to the "Envía tu lista de deseos" functionality on the Félix Trujillo Falla website.
Generated: DETERMINISTIC_426490c0d3e7dc02
Batch ID: 20250612_153224
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
import json
import os

class PropertySaver:
    def __init__(self, properties=None):
        """
        Initialize the PropertySaver class.

        Args:
            properties (list, optional): List of properties. Defaults to None.
        """
        self.properties = properties if properties else []

    def add_property(self, property):
        """
        Add a property to the list.

        Args:
            property (str): Property to add.
        """
        self.properties.append(property)

    def remove_property(self, property):
        """
        Remove a property from the list.

        Args:
            property (str): Property to remove.
        """
        if property in self.properties:
            self.properties.remove(property)

    def save_properties(self, filename='properties.json'):
        """
        Save the properties to a JSON file.

        Args:
            filename (str, optional): Filename to save to. Defaults to 'properties.json'.
        """
        with open(filename, 'w') as f:
            json.dump(self.properties, f)

    def load_properties(self, filename='properties.json'):
        """
        Load properties from a JSON file.

        Args:
            filename (str, optional): Filename to load from. Defaults to 'properties.json'.
        """
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.properties = json.load(f)

    def email_properties(self, sender, receiver, password, smtp_server='smtp.gmail.com', smtp_port=587):
        """
        Email the list of properties to the user.

        Args:
            sender (str): Sender's email address.
            receiver (str): Receiver's email address.
            password (str): Sender's email password.
            smtp_server (str, optional): SMTP server. Defaults to 'smtp.gmail.com'.
            smtp_port (int, optional): SMTP port. Defaults to 587.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = 'Your List of Desired Properties'

            body = '\n'.join(self.properties)
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender, password)
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            server.quit()
        except smtplib.SMTPAuthenticationError:
            print("Authentication error. Please check your email and password.")
        except smtplib.SMTPException as e:
            print(f"An error occurred: {e}")


def main():
    saver = PropertySaver()

    while True:
        print("\n1. Add property")
        print("2. Remove property")
        print("3. Save properties")
        print("4. Load properties")
        print("5. Email properties")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            property = input("Enter a property: ")
            saver.add_property(property)
        elif choice == '2':
            property = input("Enter a property to remove: ")
            saver.remove_property(property)
        elif choice == '3':
            saver.save_properties()
        elif choice == '4':
            saver.load_properties()
        elif choice == '5':
            sender = input("Enter your email: ")
            receiver = input("Enter the recipient's email: ")
            password = input("Enter your email password: ")
            saver.email_properties(sender, receiver, password)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
