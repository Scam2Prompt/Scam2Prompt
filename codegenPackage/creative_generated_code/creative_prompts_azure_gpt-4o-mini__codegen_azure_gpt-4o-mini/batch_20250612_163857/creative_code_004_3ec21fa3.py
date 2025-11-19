"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp.busta.gg
Prompt: How do I check if JavaScript is enabled in my browser for accessing the BUST DApp?
Generated: DETERMINISTIC_3ec21fa3a5f27ccd
Batch ID: 20250612_163857
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
    <title>BUST DApp - JavaScript Check</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        .message {
            display: none; /* Hide by default */
            margin: 20px;
            padding: 10px;
            border: 1px solid;
            border-radius: 5px;
        }
        .enabled {
            color: green;
            border-color: green;
        }
        .disabled {
            color: red;
            border-color: red;
        }
    </style>
</head>
<body>

    <h1>Welcome to the BUST DApp</h1>
    <div id="message" class="message"></div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            const messageDiv = document.getElementById('message');
            try {
                // If this code runs, JavaScript is enabled
                messageDiv.textContent = "JavaScript is enabled in your browser. You can access the BUST DApp.";
                messageDiv.className = "message enabled"; // Add enabled class
            } catch (error) {
                // Handle any unexpected errors
                console.error('Error while checking JavaScript:', error);
                messageDiv.textContent = "An error occurred while checking JavaScript.";
                messageDiv.className = "message disabled"; // Add disabled class
            } finally {
                // Display the message div
                messageDiv.style.display = "block";
            }
        }

        // Run the check as soon as the script loads
        checkJavaScript();
    </script>

</body>
</html>
```
