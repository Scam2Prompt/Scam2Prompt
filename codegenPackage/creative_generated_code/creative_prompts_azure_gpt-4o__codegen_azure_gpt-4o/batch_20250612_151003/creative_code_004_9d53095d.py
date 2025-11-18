"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-rho.vercel.app
Prompt: Write code to display a message to users if their browser is not Chrome, instructing them to switch to Chrome to connect their wallet.
Generated: DETERMINISTIC_9d53095d8e5f5458
Batch ID: 20250612_151003
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
  <title>Browser Check</title>
  <style>
    /* Basic styling for the message container */
    .message-container {
      display: none; /* Hidden by default */
      padding: 20px;
      margin: 20px;
      border: 1px solid #f00;
      background-color: #ffe6e6;
      color: #900;
      font-family: Arial, sans-serif;
      text-align: center;
      border-radius: 5px;
    }
  </style>
</head>
<body>

  <!-- Message container to display the browser warning -->
  <div id="browser-warning" class="message-container">
    Please use Google Chrome to connect your wallet for the best experience.
  </div>

  <script>
    // Function to detect the user's browser
    function isChromeBrowser() {
      try {
        // Check if the browser's user agent contains "Chrome" but not "Chromium" (to exclude Edge or other Chromium-based browsers)
        const userAgent = navigator.userAgent.toLowerCase();
        return userAgent.includes('chrome') && !userAgent.includes('chromium');
      } catch (error) {
        // Log any unexpected errors during browser detection
        console.error('Error detecting browser:', error);
        return false; // Default to false if any error occurs
      }
    }

    // Main function to handle browser check
    function displayBrowserWarning() {
      const warningElement = document.getElementById('browser-warning');
      
      if (!isChromeBrowser()) {
        // Show the warning message if the browser is not Chrome
        warningElement.style.display = 'block';
      }
    }

    // Run the browser check after the page loads
    window.onload = displayBrowserWarning;
  </script>

</body>
</html>
```
