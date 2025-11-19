"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hgdsjhgdjhsgff.pages.dev
Prompt: How can I create a notification for users to enable JavaScript on my website?
Generated: DETERMINISTIC_88f20f9158f201ac
Batch ID: 20250612_163732
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
    <title>JavaScript Notification</title>
    <style>
        /* Styles for the notification banner */
        #js-notification {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around the text */
            text-align: center; /* Centered text */
            position: fixed; /* Fixed position */
            top: 0; /* At the top of the page */
            width: 100%; /* Full width */
            z-index: 1000; /* On top of other elements */
        }
    </style>
</head>
<body>
    <!-- Notification banner for JavaScript -->
    <div id="js-notification">
        JavaScript is disabled in your browser. Please enable JavaScript for a better experience.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Select the notification element
            const notification = document.getElementById('js-notification');

            // Display the notification if JavaScript is disabled
            if (!navigator.javaEnabled()) {
                notification.style.display = 'block';
            }
        }

        // Call the function to check for JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```
