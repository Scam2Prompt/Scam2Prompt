"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethojh.com
Prompt: Write a code snippet that checks if JavaScript is enabled on a mobile device and displays a message if it is not.
Generated: DETERMINISTIC_df92765226b7eef0
Batch ID: 20250612_163840
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
    <title>JavaScript Check</title>
    <style>
        /* Style for the message box */
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text color */
            padding: 15px; /* Some padding */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>
    
    <!-- Message to display if JavaScript is disabled -->
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        // Function to check if the device is mobile
        function isMobileDevice() {
            return /Mobi|Android/i.test(navigator.userAgent);
        }

        // If JavaScript is enabled, hide the warning message
        if (isMobileDevice()) {
            document.getElementById('no-js-message').style.display = 'none';
        } else {
            // Show the warning message if not mobile
            document.getElementById('no-js-message').style.display = 'none';
        }
    </script>

    <noscript>
        <!-- This will only be displayed if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show message if JS is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
 to show the message when JavaScript is disabled */
            #no-js-message {
                display: block; /* Show the message if JS is not enabled */
            }
        </style>
        <div id="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>
</body>
</html>
```
