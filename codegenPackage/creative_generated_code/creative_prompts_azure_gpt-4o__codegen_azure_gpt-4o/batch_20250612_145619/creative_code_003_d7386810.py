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
    /* Style for the no-JavaScript message */
    .no-js-message {
      display: none;
      text-align: center;
      font-size: 1.2em;
      color: red;
      margin-top: 20px;
    }

    /* This will be visible only if JavaScript is disabled */
    .no-js-enabled .no-js-message {
      display: block;
    }
  </style>
  <script>
    // Add a class to the <html> element to indicate JavaScript is enabled
    document.documentElement.classList.remove('no-js-enabled');
    document.documentElement.classList.add('js-enabled');
  </script>
  <noscript>
    <!-- Provide a custom message if JavaScript is disabled -->
    <style>
      .no-js-enabled { display: block !important; }
    </style>
  </noscript>
</head>
<body>
  <!-- Message shown when JavaScript is disabled -->
  <div class="no-js-message">
    JavaScript is disabled in your browser. Please enable it for the best experience.
  </div>

  <script>
    // Function to check if a device is a mobile device
    function isMobileDevice() {
      // Use the navigator.userAgent property to detect mobile devices
      return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    }

    // Display a custom message based on device type
    function displayDeviceMessage() {
      const messageElement = document.createElement('div');
      messageElement.style.textAlign = 'center';
      messageElement.style.marginTop = '20px';
      messageElement.style.fontSize = '1.2em';

      if (isMobileDevice()) {
        // Display message for mobile devices
        messageElement.textContent = 'You are using a mobile device.';
      } else {
        // Display message for non-mobile devices
        messageElement.textContent = 'You are not using a mobile device.';
      }

      // Append the message to the body
      document.body.appendChild(messageElement);
    }

    // Execute the function after the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', displayDeviceMessage);
  </script>
</body>
</html>
```
