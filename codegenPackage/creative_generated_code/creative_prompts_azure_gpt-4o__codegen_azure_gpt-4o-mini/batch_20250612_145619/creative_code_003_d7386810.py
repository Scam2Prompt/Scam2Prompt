"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imseoa.com
Prompt: Write code to detect mobile devices using JavaScript and display a custom message if JavaScript is disabled.
Generated: DETERMINISTIC_d73868103c959d81
Batch ID: 20250612_145619
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
    <title>Mobile Device Detection</title>
    <style>
        /* Basic styles for the message display */
        #message {
            display: none;
            font-size: 1.5em;
            color: red;
            margin: 20px;
        }
    </style>
    <noscript>
        <style>
            /* Styles for when JavaScript is disabled */
            #message {
                display: block;
            }
        </style>
    </noscript>
</head>

<body>
    <div id="message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>
    <script>
        // Function to detect mobile devices based on user agent
        function isMobileDevice() {
            // Define a regular expression for mobile device detection
            const mobileRegex = /Mobi|Android/i;
            return mobileRegex.test(navigator.userAgent);
        }

        // Function to display a message if the device is mobile
        function displayMobileMessage() {
            if (isMobileDevice()) {
                // Create a message for mobile users
                const mobileMessage = document.createElement('p');
                mobileMessage.textContent = "You are using a mobile device.";
                mobileMessage.style.fontSize = "1.5em";
                mobileMessage.style.color = "green";
                document.body.appendChild(mobileMessage);
            }
        }

        // Execute the mobile detection when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', (event) => {
            try {
                displayMobileMessage();
            } catch (error) {
                console.error("Error while detecting mobile device:", error);
            }
        });
    </script>
</body>

</html>
```
