"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethlast.com
Prompt: Create a script that checks for JavaScript support on a mobile device and redirects users to an alternative page if JavaScript is disabled, inspired by the ETH Pledge website functionality.
Generated: DETERMINISTIC_4d9e3fc7db80489a
Batch ID: 20250612_152600
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
  <noscript>
    <!-- Redirect users with JavaScript disabled to an alternative page -->
    <meta http-equiv="refresh" content="0;url=/no-javascript.html">
  </noscript>
  <script>
    // Ensure the script runs only on devices supporting JavaScript
    document.addEventListener("DOMContentLoaded", () => {
      try {
        // Optional: Perform additional checks for device type (mobile)
        const isMobile = /Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i.test(navigator.userAgent);
        if (!isMobile) {
          console.log("Non-mobile device detected.");
        }
        // No further action needed since JavaScript is enabled
        console.log("JavaScript is enabled.");
      } catch (error) {
        // Log errors in the console for debugging purposes
        console.error("Error during JavaScript check:", error);
      }
    });
  </script>
</head>
<body>
  <h1>JavaScript is Enabled</h1>
  <p>Thank you for visiting our website. Everything is working as expected.</p>
</body>
</html>
```
