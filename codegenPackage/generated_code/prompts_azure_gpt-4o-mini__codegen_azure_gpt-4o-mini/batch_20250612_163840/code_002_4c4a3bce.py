"""
Generated Code Metadata:
========================
Original URL: https://imotokaen.com
Prompt: Can you provide code snippets to detect if JavaScript is enabled on a mobile device and display a message if it is not?
Generated: DETERMINISTIC_4c4a3bce0e0a3c02
Batch ID: 20250612_163840
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
    <title>JavaScript Detection</title>
    <style>
        /* Style for the message container */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 10px;
            border: 1px solid #f5c6cb; /* Border color */
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'block'; // Show the message
        }

        // Check if JavaScript is enabled
        if (typeof window === 'undefined' || typeof document === 'undefined') {
            // If window or document is undefined, JavaScript is not enabled
            showNoJsMessage();
        } else {
            // JavaScript is enabled, you can add more functionality here
            console.log("JavaScript is enabled.");
        }
    </script>

    <noscript>
        <!-- Fallback message for users with JavaScript disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
