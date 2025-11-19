"""
Generated Code Metadata:
========================
Original URL: https://vnsupvc.com
Prompt: Design a simple webpage content using HTML and CSS that displays a notification about expired services and provides a contact phone number, inspired by vnsupvc.com.
Generated: DETERMINISTIC_50a4d1a6b059cc6c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Expiration Notification</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="notification-container">
        <h1>Important Notification</h1>
        <p>We would like to inform you that your services have expired. Please take action to renew your services to avoid any interruptions.</p>
        <p>If you have any questions or need assistance, feel free to contact us at:</p>
        <p class="contact-number">Phone: <a href="tel:+1234567890">+1 (234) 567-890</a></p>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, h1, p {
    margin: 0;
    padding: 0;
}

/* Set a background color and font for the body */
body {
    background-color: #f4f4f4;
    font-family: Arial, sans-serif;
    color: #333;
}

/* Style the notification container */
.notification-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

/* Style the heading */
.notification-container h1 {
    font-size: 24px;
    color: #d9534f; /* Bootstrap danger color */
    margin-bottom: 20px;
}

/* Style the paragraphs */
.notification-container p {
    font-size: 16px;
    line-height: 1.5;
    margin-bottom: 15px;
}

/* Style the contact number */
.contact-number {
    font-weight: bold;
}

/* Style the link */
.contact-number a {
    color: #007bff; /* Bootstrap primary color */
    text-decoration: none;
}

.contact-number a:hover {
    text-decoration: underline;
}
```
