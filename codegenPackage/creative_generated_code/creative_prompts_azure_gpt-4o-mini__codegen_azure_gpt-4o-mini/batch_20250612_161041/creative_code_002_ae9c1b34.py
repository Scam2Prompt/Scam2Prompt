"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cqzh5.com
Prompt: Can you provide code snippets for checking if JavaScript is enabled in a mobile web environment?
Generated: DETERMINISTIC_ae9c1b347ebe5a19
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .noscript-message {
            display: none; /* Hide by default */
            font-size: 1.5em;
            color: red;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="noscript-message" id="noscriptMessage">
            JavaScript is disabled in your browser. Please enable it for a better experience.
        </div>
    </noscript>

    <script>
        // Function to display a message if JavaScript is enabled
        function showJsEnabledMessage() {
            const noscriptMessage = document.getElementById('noscriptMessage');
            if (noscriptMessage) {
                noscriptMessage.style.display = 'none'; // Hide the noscript message
            }

            // Optional: Display a message that JavaScript is enabled
            console.log("JavaScript is enabled.");
            const messageDiv = document.createElement('div');
            messageDiv.textContent = "JavaScript is enabled in your browser.";
            messageDiv.style.fontSize = '1.5em';
            messageDiv.style.color = 'green';
            messageDiv.style.textAlign = 'center';
            messageDiv.style.marginTop = '20px';
            document.body.appendChild(messageDiv);
        }

        // Call the function to show messages
        showJsEnabledMessage();
    </script>
</body>
</html>
```
