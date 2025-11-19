"""
Generated Code Metadata:
========================
Original URL: https://imetobken.com
Prompt: Create a script that checks for JavaScript support on mobile devices and redirects users to an alternative page if JavaScript is disabled, specifically for the "ETH Pledge" platform.
Generated: DETERMINISTIC_5c5fc8a2b115d64b
Batch ID: 20250612_145619
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
    <title>ETH Pledge - JavaScript Check</title>
    <script>
        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // If JavaScript is enabled, remove the no-js class
            document.documentElement.classList.remove('no-js');
            
            // Check if the device is mobile
            function isMobileDevice() {
                return (typeof window.orientation !== "undefined") || 
                       (navigator.userAgent.indexOf('IEMobile') !== -1);
            }
            
            // If JavaScript is enabled and not a mobile device, proceed normally
            if (!isMobileDevice()) {
                return;
            }
            
            // If JavaScript is enabled on mobile, check for specific features
            try {
                // Test for modern JavaScript features
                const testFeatures = () => {
                    if (typeof Promise === 'undefined' || 
                        typeof fetch === 'undefined' || 
                        typeof Object.assign === 'undefined') {
                        throw new Error('Missing required JavaScript features');
                    }
                };
                testFeatures();
            } catch (e) {
                // Redirect if essential features are missing
                window.location.href = '/mobile-nojs.html';
            }
        });
    </script>
    <noscript>
        <meta http-equiv="refresh" content="0; url=/mobile-nojs.html">
    </noscript>
    <style>
        .no-js #js-check-message {
            display: block;
        }
        #js-check-message {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 1rem;
            background-color: #ffeb3b;
            color: #000;
            text-align: center;
            z-index: 9999;
        }
    </style>
</head>
<body class="no-js">
    <div id="js-check-message">
        JavaScript is disabled or not fully supported on your device. You will be redirected shortly.
    </div>
    
    <!-- Your normal content here -->
    <script>
        // This script will only execute if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Main application initialization
            console.log('ETH Pledge application initialized');
        });
    </script>
</body>
</html>
```
