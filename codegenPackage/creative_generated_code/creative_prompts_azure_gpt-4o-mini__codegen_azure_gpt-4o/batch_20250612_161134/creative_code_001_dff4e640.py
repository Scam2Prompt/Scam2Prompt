"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudflare-namada-validator48.pages.dev
Prompt: Write a code snippet to enable JavaScript and cookies for a web application that uses Cloudflare.
Generated: DETERMINISTIC_dff4e640300753e0
Batch ID: 20250612_161134
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
  <title>Enable JavaScript and Cookies</title>
  <script>
    // Check if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Display a message confirming JavaScript is enabled
        const jsEnabledMessage = document.createElement('p');
        jsEnabledMessage.textContent = 'JavaScript is enabled.';
        document.body.appendChild(jsEnabledMessage);

        // Check if cookies are enabled
        document.cookie = "testCookie=1";
        const cookiesEnabled = document.cookie.includes("testCookie=1");

        // Display message confirming cookies status
        const cookiesMessage = document.createElement('p');
        cookiesMessage.textContent = cookiesEnabled 
          ? 'Cookies are enabled.' 
          : 'Cookies are disabled. Please enable cookies.';
        document.body.appendChild(cookiesMessage);

        // Clean up test cookie
        if (cookiesEnabled) {
          document.cookie = "testCookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
        }
      } catch (error) {
        // Handle unexpected errors gracefully
        console.error('An error occurred:', error);
      }
    });
  </script>
  <noscript>
    <!-- Message displayed when JavaScript is disabled -->
    <p style="color: red;">
      JavaScript is disabled. Please enable JavaScript to use this application.
    </p>
  </noscript>
</head>
<body>
  <!-- Content of the web application -->
  <h1>Welcome to Our Web Application</h1>
  <p>Ensure JavaScript and cookies are enabled for full functionality.</p>
</body>
</html>
```
