"""
Generated Code Metadata:
========================
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Write code to display a message prompting users to enable JavaScript if it is disabled, as seen in the Moonbirds Q1 '24 Holder Survey webpage.
Generated: DETERMINISTIC_2170e7cba6dce9fe
Batch ID: 20250612_153225
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
    <title>JavaScript Required</title>
    <style>
        /* Basic styling for the message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 15px; /* Padding around the message */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
            font-family: Arial, sans-serif; /* Font style */
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>JavaScript is disabled in your browser.</strong> Please enable JavaScript to view this page properly.
    </div>

    <script>
        // Function to display the warning message if JavaScript is disabled
        function showWarning() {
            const warningDiv = document.getElementById('js-warning');
            warningDiv.style.display = 'block'; // Show the warning message
        }

        // Check if JavaScript is enabled
        if (typeof showWarning === 'function') {
            // If JavaScript is enabled, do nothing
        } else {
            // If JavaScript is disabled, show the warning
            showWarning();
        }
    </script>

    <noscript>
        <!-- Fallback content for users with JavaScript disabled -->
        <style>
            #js-warning {
                display: block; /* Show the warning message */
            }
        </style>
    </noscript>

</body>
</html>
```
