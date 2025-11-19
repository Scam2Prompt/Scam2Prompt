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
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expired Services Notification</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="notification-container">
        <div class="notification-header">
            <h2>Notification: Expired Services</h2>
        </div>
        <div class="notification-content">
            <p>Dear valued customer,</p>
            <p>We regret to inform you that your services have expired. Please be advised to renew your services to avoid any disruptions.</p>
            <p>For assistance, please contact us at:</p>
            <p><strong>Phone:</strong> <a href="tel:+1234567890">+1 234 567 890</a></p>
        </div>
        <div class="notification-footer">
            <p>Thank you for your prompt attention.</p>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f2f2f2;
}

.notification-container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.notification-header {
    background-color: #f0f0f0;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}

.notification-header h2 {
    margin: 0;
    padding: 0;
    font-size: 18px;
}

.notification-content {
    padding: 20px;
}

.notification-content p {
    margin-bottom: 10px;
}

.notification-footer {
    padding: 10px;
    background-color: #f0f0f0;
    border-top: 1px solid #ddd;
    text-align: center;
}

a {
    text-decoration: none;
    color: #337ab7;
}

a:hover {
    color: #23527c;
}
```
