"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudflare-cftc-us8-73s.pages.dev
Prompt: Write a code snippet to enable JavaScript and cookies for a web application to improve user verification with Cloudflare.
Generated: DETERMINISTIC_88d13d4b678c5dd7
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
    /**
     * Set a cookie to verify that JavaScript is enabled.
     * This cookie can be used by Cloudflare or other verification services.
     */
    function setJavascriptCookie() {
      try {
        // Define the cookie name and value
        const cookieName = "js_enabled";
        const cookieValue = "true";

        // Set the cookie with a secure flag and expiration
        const secureFlag = "; Secure"; // Only send to HTTPS
        const expiryDays = 1; // Cookie validity (1 day)
        const expiryDate = new Date();
        expiryDate.setDate(expiryDate.getDate() + expiryDays);

        // Set the cookie
        document.cookie = `${cookieName}=${cookieValue}; expires=${expiryDate.toUTCString()}; path=/; SameSite=Strict${secureFlag}`;
      } catch (error) {
        console.error("Error setting JavaScript cookie:", error);
      }
    }

    /**
     * Run the function to set the JavaScript cookie once the DOM has loaded.
     */
    window.onload = () => {
      setJavascriptCookie();
    };
  </script>
</head>
<body>
  <!-- This message will appear if JavaScript is disabled -->
  <noscript>
    <p style="color: red;">JavaScript is required to access this site. Please enable JavaScript in your browser.</p>
  </noscript>

  <p>Cookies will be used for verification purposes. Please ensure cookies are enabled in your browser.</p>
</body>
</html>
```
