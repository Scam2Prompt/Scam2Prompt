"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mallconomy-claimreward.pages.dev
Prompt: Create a JavaScript widget to showcase Mallconomy's multi-device compatibility, allowing users to access the platform on PCs, mobiles, and Smart TVs.
Generated: DETERMINISTIC_0382e71e4f6d7800
Batch ID: 20250612_152235
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
    <title>Mallconomy Multi-Device Widget</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        #device-widget {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 20px;
            background-color: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .device {
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #007bff;
            border-radius: 5px;
            background-color: #e7f3ff;
        }
    </style>
</head>
<body>
    <div id="device-widget">
        <h2>Mallconomy Multi-Device Compatibility</h2>
        <div id="device-info"></div>
    </div>

    <script>
        /**
         * Function to detect the device type based on user agent.
         * @returns {string} - Returns the type of device.
         */
        function detectDevice() {
            const userAgent = navigator.userAgent.toLowerCase();
            if (/mobile|android|iphone/i.test(userAgent)) {
                return "Mobile Device";
            } else if (/smarttv|apple tv|google tv|hulu|roku/i.test(userAgent)) {
                return "Smart TV";
            } else {
                return "PC";
            }
        }

        /**
         * Function to display device compatibility information.
         */
        function displayDeviceInfo() {
            const deviceType = detectDevice();
            const deviceInfoContainer = document.getElementById('device-info');

            // Create a device info message
            const message = `You are accessing Mallconomy using a ${deviceType}. Enjoy seamless compatibility across all your devices!`;

            // Create a new div for device information
            const deviceDiv = document.createElement('div');
            deviceDiv.className = 'device';
            deviceDiv.textContent = message;

            // Append to the device info container
            deviceInfoContainer.appendChild(deviceDiv);
        }

        // Handle potential errors
        try {
            displayDeviceInfo();
        } catch (error) {
            console.error('Error displaying device information:', error);
            alert('An error occurred while detecting your device. Please try again later.');
        }
    </script>
</body>
</html>
```
