"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Provide code to build a feature that allows users to save a list of desired properties and email it to themselves, similar to the "Envía tu lista de deseos" functionality on the Félix Trujillo Falla website.
Generated: DETERMINISTIC_426490c0d3e7dc02
Batch ID: 20250612_153224
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
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PropertyWishlist:
    """
    A class to represent a user's property wishlist.
    """

    def __init__(self, user_email):
        """
        Initialize the wishlist with the user's email.

        :param user_email: Email of the user to whom the wishlist will be sent.
        """
        self.user_email = user_email
        self.properties = []

    def add_property(self, property_name):
        """
        Add a property to the wishlist.

        :param property_name: Name of the property to be added.
        """
        if property_name:
            self.properties.append(property_name)
            logging.info(f"Property '{property_name}' added to the wishlist.")
        else:
            logging.warning("Attempted to add an empty property name to the wishlist.")

    def remove_property(self, property_name):
        """
        Remove a property from the wishlist.

        :param property_name: Name of the property to be removed.
        """
        try:
            self.properties.remove(property_name)
            logging.info(f"Property '{property_name}' removed from the wishlist.")
        except ValueError:
            logging.error(f"Property '{property_name}' not found in the wishlist.")

    def send_wishlist(self):
        """
        Send the wishlist to the user's email.
        """
        if not self.properties:
            logging.warning("Cannot send wishlist. The property list is empty.")
            return "Wishlist is empty. Please add properties before sending."

        try:
            # Email server configuration
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "your_email@gmail.com"  # Replace with your email
            sender_password = "your_password"      # Replace with your email password

            # Construct the email content
            subject = "Your Property Wishlist"
            body = "Here is your list of desired properties:\n\n" + "\n".join(self.properties)
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = self.user_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure encrypted SSL/TLS
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, self.user_email, message.as_string())

            logging.info(f"Wishlist successfully sent to {self.user_email}.")
            return "Wishlist sent successfully."

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email: {e}")
            return f"Failed to send wishlist: {e}"


# Example usage
if __name__ == "__main__":
    # Replace with the user's email address
    user_email = "user_email@example.com"

    # Create a wishlist instance
    wishlist = PropertyWishlist(user_email)

    # Add properties to the wishlist
    wishlist.add_property("Beachfront Villa")
    wishlist.add_property("Modern Apartment")
    wishlist.add_property("Cozy Cottage")

    # Remove a property from the wishlist
    wishlist.remove_property("Modern Apartment")

    # Send the wishlist to the user's email
    result = wishlist.send_wishlist()
    print(result)
```

### Notes:
- Replace `your_email@gmail.com` and `your_password` with the sender's actual email credentials.
- Ensure that the email account used for sending allows less secure app access or use an application-specific password for better security.
- Use environment variables or secure vaults for managing sensitive credentials in production environments.
- Setup logging to capture and monitor activity in production systems.
