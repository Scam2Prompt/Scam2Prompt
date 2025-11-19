"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo9969.infinityfreeapp.com
Prompt: How can I enable Javascript in my browser to access web applications?
Generated: DETERMINISTIC_c20d01b6442d78ff
Batch ID: 20250612_155432
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
    <title>Enable JavaScript</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }
        .disabled-message {
            display: none;
            color: red;
        }
    </style>
    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            var disabledMessage = document.getElementById("disabled-message");
            disabledMessage.style.display = "none"; // Hide the message if JS is enabled
        });

        // Function to show a message if JavaScript is disabled
        function showDisabledMessage() {
            var disabledMessage = document.getElementById("disabled-message");
            disabledMessage.style.display = "block"; // Display the message
        }

        // Attempt to call the function when the page loads
        window.onload = showDisabledMessage;
    </script>
</head>
<body>
    <h1>Welcome to Our Web Application</h1>
    <p>If you are seeing this message, it means JavaScript is disabled in your browser.</p>
    <p>Please enable JavaScript to use all features of this web application.</p>
    <p class="disabled-message" id="disabled-message">JavaScript is disabled! Please enable it in your browser settings.</p>
</body>
</html>
```
