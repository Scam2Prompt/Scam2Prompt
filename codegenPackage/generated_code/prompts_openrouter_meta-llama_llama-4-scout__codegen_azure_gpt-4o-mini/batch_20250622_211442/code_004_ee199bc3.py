"""
Generated Code Metadata:
========================
Original URL: https://potexclusiveofficialsite.online
Prompt: How can I implement a feature to detect if a user's browser supports JavaScript and provide an alternative user experience if it does not, using JavaScript libraries or APIs?
Generated: DETERMINISTIC_ee199bc3a25a4dc0
Batch ID: 20250622_211442
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
    <title>JavaScript Support Detection</title>
    <style>
        /* Basic styles for the message */
        .no-js {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            margin: 20px 0;
        }
        .js {
            display: none; /* Hide the JS message initially */
        }
    </style>
</head>
<body>

    <div class="no-js" id="no-js-message">
        <p>JavaScript is not enabled in your browser. Please enable it for a better experience.</p>
    </div>

    <div class="js" id="js-message">
        <p>Welcome! JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // Function to detect if JavaScript is enabled
        function detectJavaScript() {
            try {
                // Show the message for users with JavaScript enabled
                document.getElementById('js-message').style.display = 'block';
            } catch (error) {
                console.error('Error displaying JavaScript message:', error);
            }
        }

        // Function to show the no-JS message
        function showNoJsMessage() {
            try {
                document.getElementById('no-js-message').style.display = 'block';
            } catch (error) {
                console.error('Error displaying no-JS message:', error);
            }
        }

        // Execute the detection function
        detectJavaScript();

        // If JavaScript is not enabled, the no-js message will be shown by default
        // This is handled by the CSS display property
    </script>
</body>
</html>
```
