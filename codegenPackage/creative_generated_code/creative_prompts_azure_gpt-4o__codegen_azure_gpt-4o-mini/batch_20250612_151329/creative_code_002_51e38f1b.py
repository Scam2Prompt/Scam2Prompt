"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdddd.pages.dev
Prompt: Generate code to detect whether a user is accessing a website from a desktop or mobile device and display an optimized message, similar to the desktop usage optimization mentioned on the chimpers-dojo website.
Generated: DETERMINISTIC_51e38f1b01895b6f
Batch ID: 20250612_151329
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
    <title>Device Detection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .desktop-message, .mobile-message {
            display: none; /* Initially hide both messages */
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .desktop-message {
            background-color: #e0f7fa;
        }
        .mobile-message {
            background-color: #ffe0b2;
        }
    </style>
</head>
<body>

    <div id="desktopMessage" class="desktop-message">
        Welcome to our website! For the best experience, please use our desktop version.
    </div>
    
    <div id="mobileMessage" class="mobile-message">
        Welcome! You're on a mobile device. Explore our site on the go!
    </div>

    <script>
        /**
         * Function to detect the user's device type
         * @returns {string} - 'desktop' or 'mobile'
         */
        function detectDevice() {
            const userAgent = navigator.userAgent.toLowerCase();

            // Check for mobile devices using regular expressions
            if (/android|iphone|ipad|ipod|blackberry|iemobile|opera mini/.test(userAgent)) {
                return 'mobile';
            }
            return 'desktop';
        }

        /**
         * Displays the appropriate message based on device type
         */
        function displayMessage() {
            try {
                const deviceType = detectDevice();
                const desktopMessage = document.getElementById('desktopMessage');
                const mobileMessage = document.getElementById('mobileMessage');

                if (deviceType === 'mobile') {
                    mobileMessage.style.display = 'block';
                } else {
                    desktopMessage.style.display = 'block';
                }
            } catch (error) {
                console.error('Error detecting device type:', error);
                alert('An error occurred while determining your device type. Please refresh the page.');
            }
        }

        // Run the displayMessage function on page load
        window.onload = displayMessage;
    </script>

</body>
</html>
```
