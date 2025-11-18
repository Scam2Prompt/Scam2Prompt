"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soneium.app
Prompt: Create a basic HTML and JavaScript template for a web app that displays a warning message if JavaScript is disabled.
Generated: DETERMINISTIC_77163bbbc491e4ad
Batch ID: 20250612_150347
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
    <title>JavaScript Warning Template</title>
    <style>
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px; /* Padding for better appearance */
            border: 1px solid #f5c6cb; /* Border color */
            margin: 20px; /* Margin around the warning */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>
    <!-- Warning message that will be displayed if JavaScript is disabled -->
    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to display the warning message if JavaScript is enabled
        function showWarning() {
            const warningMessage = document.getElementById('js-warning');
            warningMessage.style.display = 'block'; // Show the warning message
        }

        // Set a timeout to show warning after a short delay
        setTimeout(showWarning, 100); // Adjust delay as needed
    </script>
</body>
</html>
```
