"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtaoekecn.com
Prompt: How can I implement a JavaScript-enabled feature for mobile devices on my website?
Generated: DETERMINISTIC_54e0520bac06250f
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
    <title>Mobile Feature Example</title>
    <style>
        /* Basic styles for mobile-friendly layout */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        #mobile-feature {
            display: none; /* Hidden by default */
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            text-align: center;
        }
    </style>
</head>
<body>

    <h1>Welcome to Our Website</h1>
    <div id="mobile-feature">This is a mobile-enabled feature!</div>
    
    <script>
        /**
         * Checks if the user is on a mobile device.
         * @returns {boolean} True if the user is on a mobile device, false otherwise.
         */
        function isMobileDevice() {
            return /Mobi|Android/i.test(navigator.userAgent);
        }

        /**
         * Initializes the mobile feature if on a mobile device.
         */
        function initializeMobileFeature() {
            try {
                if (isMobileDevice()) {
                    const mobileFeatureElement = document.getElementById('mobile-feature');
                    mobileFeatureElement.style.display = 'block'; // Show the feature
                } else {
                    console.log("Not a mobile device. Mobile feature not displayed.");
                }
            } catch (error) {
                console.error("Error initializing mobile feature:", error);
            }
        }

        // Run the initialization function when the DOM is fully loaded
        document.addEventListener("DOMContentLoaded", initializeMobileFeature);
    </script>

</body>
</html>
```
