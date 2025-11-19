"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbreimapp.com
Prompt: Can you provide code snippets for enabling JavaScript in different browsers for accessing CBRE IM?
Generated: DETERMINISTIC_68428f1c23d4242a
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Enabling JavaScript is a browser setting and cannot be achieved programmatically. However, I can provide script snippets that detect whether JavaScript is disabled and prompt users to enable it in their browsers via a fallback message. Here's the code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enable JavaScript Prompt</title>
    <!-- This message will be shown if JavaScript is disabled -->
    <noscript>
        <style>
            .noscript-message {
                background-color: #f8d7da;
                color: #721c24;
                padding: 20px;
                border: 1px solid #f5c6cb;
                border-radius: 5px;
                margin: 20px;
                font-family: Arial, sans-serif;
                text-align: center;
            }
        </style>
        <div class="noscript-message">
            JavaScript is required to access CBRE IM. Please enable JavaScript in your browser settings.
            <br>Here’s how to enable JavaScript:
            <ul style="text-align: left; display: inline-block; margin: auto">
                <li><b>Chrome:</b> Go to Settings -> Privacy and security -> Site Settings -> JavaScript -> Enable.</li>
                <li><b>Firefox:</b> Go to Settings -> Privacy & Security -> Permissions -> Enable JavaScript.</li>
                <li><b>Safari:</b> Go to Preferences -> Security -> Enable JavaScript.</li>
                <li><b>Edge:</b> Go to Settings -> Site permissions -> JavaScript -> Enable.</li>
            </ul>
        </div>
    </noscript>
</head>
<body>
    <h1>Welcome to CBRE IM</h1>
    <p>If you're seeing this, JavaScript is enabled and working properly.</p>
    
    <script>
        // Example code for testing JavaScript functionality
        console.log("JavaScript is enabled.");
        document.body.style.backgroundColor = "#e8f4f8"; // Example JavaScript action: Changing background color
    </script>
</body>
</html>
```

This code snippet provides a user-friendly message explaining how to enable JavaScript in popular browsers if it is disabled. It also includes a simple JavaScript test to verify functionality.
