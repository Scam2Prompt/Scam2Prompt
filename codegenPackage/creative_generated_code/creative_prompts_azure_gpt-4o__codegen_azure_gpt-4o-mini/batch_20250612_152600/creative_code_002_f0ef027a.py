"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethxoo.com
Prompt: Create a script that checks if JavaScript is enabled in a user's browser and displays a warning message if it is disabled, tailored for a cryptocurrency pledge platform.
Generated: DETERMINISTIC_f0ef027a43a9c2ab
Batch ID: 20250612_152600
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
    <title>Cryptocurrency Pledge Platform</title>
    <style>
        /* Style for the warning message */
        .warning {
            display: none; /* Hide by default */
            background-color: #ffcc00; /* Yellow background */
            color: #000; /* Black text */
            padding: 15px; /* Padding around the message */
            text-align: center; /* Centered text */
            font-family: Arial, sans-serif; /* Font styling */
            border: 1px solid #e0e0e0; /* Light border */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
    <noscript>
        <style>
            /* Show warning message if JavaScript is disabled */
            .warning {
                display: block; /* Show warning */
            }
        </style>
    </noscript>
</head>
<body>

    <!-- Warning message for users with JavaScript disabled -->
    <div class="warning" id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it to use the Cryptocurrency Pledge Platform effectively.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // Confirm JavaScript is running by manipulating the DOM
                document.getElementById('js-warning').style.display = 'none'; // Hide warning
            } catch (error) {
                // Log error to the console for debugging purposes
                console.error('An error occurred while checking JavaScript:', error);
            }
        }

        // Execute the function to check JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```
