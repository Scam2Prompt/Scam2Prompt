"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethepools.pages.dev
Prompt: Can you provide code snippets for handling account suspension notifications in a web application?
Generated: DETERMINISTIC_73b014b1ee2f8a88
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app/notifications.py

import smtplib
from email.mime.text import MIMEText

# Function to send account suspension notification via email
def send_suspension_email(user_email, suspension_reason):
    """
    Sends an account suspension notification email to the user.

    Parameters:
        user_email (str): The email address of the user.
        suspension_reason (str): The reason for suspension.

    Returns:
        bool: True if email was sent successfully, False otherwise.
    """
    try:
        # Email configuration
        smtp_server = "smtp.example.com"  # Replace with your SMTP server
        smtp_port = 587  # Replace with your SMTP port
        smtp_username = "your_email@example.com"  # Replace with your email
        smtp_password = "your_password"  # Replace with your password

        # Email content
        subject = "Account Suspension Notification"
        body = f"""
        Dear User,

        Your account has been suspended due to the following reason:
        {suspension_reason}

        If you believe this was a mistake, please contact support.

        Regards,
        The Web App Team
        """

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = smtp_username
        msg['To'] = user_email

        # Sending the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, user_email, msg.as_string())

        return True
    except Exception as e:
        # Log the error (replace with your logging mechanism)
        print(f"Error sending email: {e}")
        return False


# Function to send in-app suspension notification
def send_in_app_notification(user_id, suspension_reason, db_connection):
    """
    Sends an in-app suspension notification to the user.

    Parameters:
        user_id (int): The ID of the user.
        suspension_reason (str): The reason for suspension.
        db_connection (Connection): A database connection object.

    Returns:
        bool: True if notification was sent successfully, False otherwise.
    """
    try:
        # Prepare the notification message
        notification_message = f"Your account has been suspended due to: {suspension_reason}. Contact support for more information."

        # Insert notification into the database
        query = """
        INSERT INTO notifications (user_id, message, created_at)
        VALUES (%s, %s, NOW());
        """
        with db_connection.cursor() as cursor:
            cursor.execute(query, (user_id, notification_message))
            db_connection.commit()

        return True
    except Exception as e:
        # Log the error (replace with your logging mechanism)
        print(f"Error sending in-app notification: {e}")
        return False
```

```javascript
// frontend/notifications.js

/**
 * Displays an in-app notification to the user about account suspension.
 *
 * @param {string} suspensionReason - The reason for the account suspension.
 */
function showSuspensionNotification(suspensionReason) {
    // Create notification container
    const notificationContainer = document.createElement('div');
    notificationContainer.className = 'notification-container';

    // Create notification content
    const notificationContent = document.createElement('p');
    notificationContent.textContent = `Your account has been suspended due to: ${suspensionReason}. Please contact support for more information.`;

    // Append content to container
    notificationContainer.appendChild(notificationContent);

    // Add a close button to the notification
    const closeButton = document.createElement('button');
    closeButton.textContent = 'Close';
    closeButton.className = 'notification-close-btn';
    closeButton.addEventListener('click', () => {
        notificationContainer.remove();
    });

    // Append close button to container
    notificationContainer.appendChild(closeButton);

    // Append container to the body
    document.body.appendChild(notificationContainer);

    // Style the notification (Add CSS classes in your stylesheet)
    notificationContainer.style.position = 'fixed';
    notificationContainer.style.bottom = '20px';
    notificationContainer.style.right = '20px';
    notificationContainer.style.padding = '15px';
    notificationContainer.style.backgroundColor = '#f8d7da';
    notificationContainer.style.color = '#842029';
    notificationContainer.style.border = '1px solid #f5c2c7';
    notificationContainer.style.borderRadius = '5px';
    notificationContainer.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
}
```

```sql
-- database/schema.sql

-- Table to store in-app notifications
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL, -- Foreign key referencing the user table
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
