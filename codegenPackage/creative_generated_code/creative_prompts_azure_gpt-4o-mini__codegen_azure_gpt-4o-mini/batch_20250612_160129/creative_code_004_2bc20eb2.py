"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://photon-soitinyastro.pages.dev
Prompt: How do I implement a feature that prompts users to enable JavaScript and cookies on my website?
Generated: DETERMINISTIC_2bc20eb2d0177e21
Batch ID: 20250612_160129
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
    <title>Enable JavaScript and Cookies</title>
    <style>
        /* Basic styling for the notification */
        .notification {
            display: none; /* Initially hidden */
            position: fixed; /* Fixed position */
            top: 20px; /* Spacing from the top */
            left: 50%; /* Center horizontally */
            transform: translateX(-50%); /* Adjust horizontal center */
            background-color: #ffd700; /* Gold background color */
            border: 1px solid #cccc00; /* Border to define the notification */
            padding: 15px; /* Padding for space inside */
            border-radius: 5px; /* Rounded corners */
            z-index: 1000; /* Ensure it's on top of other content */
        }
    </style>
</head>
<body>
    <div id="notification" class="notification">
        <p>Please enable JavaScript and cookies in your browser settings for the best experience on this website.</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // If this script runs, JavaScript is enabled
            document.getElementById('notification').style.display = 'none'; // Hide notification if JavaScript is available
            
            // Optionally, check cookies if you need to do that specifically
            if (!navigator.cookieEnabled) {
                // Display notification if cookies are not enabled
                displayNotification();
            }
        }

        // Function to display the notification
        function displayNotification() {
            const notification = document.getElementById('notification');
            notification.style.display = 'block'; // Show notification
        }

        // Run the check when the script loads
        checkJavaScriptEnabled();
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <div class="notification" style="display: block;">
            <p>Please enable JavaScript in your browser settings for the best experience on this website.</p>
        </div>
    </noscript>
</body>
</html>
```
