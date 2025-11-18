"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suspicious-euler-473151.netlify.app
Prompt: Provide a step-by-step guide for implementing push notifications for new emails in a Mac email client connected to Microsoft Exchange.
Generated: DETERMINISTIC_747a5385cb0a3a45
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from push_notification_service import PushNotificationService  # Assuming this is a custom service for sending push notifications

class EmailNotificationHandler(BaseHTTPRequestHandler):
    """
    Handles incoming HTTP requests from the Microsoft Exchange server.
    This handler processes notifications of new emails.
    """
    
    def do_POST(self):
        """
        Handle POST requests to receive email notifications.
        """
        content_length = int(self.headers['Content-Length'])  # Get the size of the data
        post_data = self.rfile.read(content_length)  # Read the data
        email_data = json.loads(post_data)  # Parse the JSON data

        # Check for new email and send a push notification
        if self.is_new_email_notification(email_data):
            self.send_push_notification(email_data)

        self.send_response(200)  # Send a 200 OK response
        self.end_headers()

    def is_new_email_notification(self, email_data):
        """
        Check if the incoming data contains a new email notification.
        
        Args:
        email_data (dict): The email notification data.
        
        Returns:
        bool: True if it is a new email notification, False otherwise.
        """
        return email_data.get("event") == "new_email"

    def send_push_notification(self, email_data):
        """
        Send a push notification for the new email.
        
        Args:
        email_data (dict): The email notification data.
        """
        notification_service = PushNotificationService()
        try:
            notification_service.send(
                title="New Email Received",
                body=f"You have a new email from {email_data['sender']}",
                data=email_data
            )
        except Exception as e:
            print(f"Error sending push notification: {e}")

def run_server(server_class=HTTPServer, handler_class=EmailNotificationHandler, port=8080):
    """
    Run the HTTP server to listen for Exchange notifications.

    Args:
    server_class (HTTPServer): The server class to use.
    handler_class (BaseHTTPRequestHandler): The request handler class to use.
    port (int): The port to listen on.
    """
    server_address = ('', port)  # Listen on all interfaces
    httpd = server_class(server_address, handler_class)

    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()  # Start the server
    except KeyboardInterrupt:
        print("Server stopped by user.")
    finally:
        httpd.server_close()  # Clean up and close the server

if __name__ == "__main__":
    # Start the HTTP server in a separate thread
    server_thread = Thread(target=run_server)
    server_thread.start()
```

**Note:** This code assumes the existence of a `PushNotificationService` class that handles the mechanics of sending push notifications. This code also assumes that the Microsoft Exchange server is configured to post new email notifications to this HTTP server endpoint. You would need to update the `port` and any other configurations as necessary based on your environment.
