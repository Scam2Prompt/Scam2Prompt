"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethvnq.com
Prompt: Write a JavaScript snippet to detect mobile devices and display a custom error message if JavaScript is disabled, specifically for BTC pledge services.
Generated: DETERMINISTIC_1907b3b6d0d54ef0
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BTC Pledge Service</title>
  <noscript>
    <!-- This message will display if JavaScript is disabled -->
    <style>
      body {
        display: none;
      }
    </style>
    <div style="color: red; text-align: center; font-size: 20px; margin-top: 20%;">
      JavaScript is required for the BTC pledge service. Please enable JavaScript in your browser settings.
    </div>
  </noscript>
  <script>
    // Immediately invoked function to detect mobile devices
    (function() {
      /**
       * Checks if the current device is a mobile device
       * @returns {boolean} true if the device is mobile, false otherwise
       */
      function isMobileDevice() {
        const userAgent = navigator.userAgent || navigator.vendor || window.opera;
        return /android|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(userAgent.toLowerCase());
      }

      /**
       * Displays an error message for mobile users if detected.
       */
      function handleMobileDeviceDetection() {
        if (isMobileDevice()) {
          alert("The BTC pledge service is currently optimized for desktop. Some features may not work properly on mobile devices.");
        }
      }

      try {
        // Run the mobile device detection
        handleMobileDeviceDetection();
      } catch (error) {
        // Log any unexpected errors
        console.error("An error occurred while detecting the device:", error);
      }
    })();
  </script>
</head>
<body>
  <h1>Welcome to BTC Pledge Service</h1>
  <p>Use this platform to securely pledge BTC for various services.</p>
</body>
</html>
```
