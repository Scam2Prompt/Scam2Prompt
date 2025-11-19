"""
Generated Code Metadata:
========================
Original URL: https://bot12.cc
Prompt: Generate a basic HTML structure for a chatbot webpage that displays a "Please enable JavaScript to continue" message when JavaScript is disabled.
Generated: DETERMINISTIC_2bf072082b166510
Batch ID: 20250622_204816
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
    <title>Chatbot Webpage</title>
    <style>
        /* Add some basic styling to make the page look decent */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        
        #noscript-message {
            display: none;
        }
    </style>
</head>
<body>
    <noscript id="noscript-message">
        <h1>Please enable JavaScript to continue</h1>
        <p>This chatbot requires JavaScript to function properly. Please enable JavaScript in your browser settings to continue.</p>
    </noscript>
    <div id="chat-container">
        <!-- Chatbot interface will be rendered here -->
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            const noscriptMessage = document.getElementById('noscript-message');
            if (noscriptMessage) {
                noscriptMessage.style.display = 'none';
            }
            // Render chatbot interface here
            const chatContainer = document.getElementById('chat-container');
            chatContainer.innerHTML = '<h1>Chatbot Interface</h1>';
            // Add event listeners and chatbot functionality here
        });
    </script>
</body>
</html>
```
