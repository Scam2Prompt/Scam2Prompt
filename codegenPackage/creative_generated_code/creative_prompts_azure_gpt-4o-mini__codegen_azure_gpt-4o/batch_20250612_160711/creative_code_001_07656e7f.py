"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pin-ai.org
Prompt: What are the best practices for enabling JavaScript and cookies to enhance user experience on a website?
Generated: DETERMINISTIC_07656e7f15eb6529
Batch ID: 20250612_160711
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
  <title>Enable JavaScript and Cookies Example</title>
  <style>
    /* Basic styles for visibility */
    .no-js-message {
      display: none;
      color: red;
      font-weight: bold;
    }
    .js-enabled-message {
      display: none;
      color: green;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Message for users without JavaScript enabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript for a better user experience.
    </div>
  </noscript>

  <!-- Message for users with JavaScript enabled -->
  <div id="js-enabled-message" class="js-enabled-message">
    JavaScript is enabled. Welcome to our website!
  </div>

  <script>
    // Check if JavaScript is enabled and show the appropriate message.
    document.getElementById('js-enabled-message').style.display = 'block';

    /**
     * Function to create or update a browser cookie.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {number} days - Number of days until the cookie expires.
     */
    function setCookie(name, value, days) {
      try {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); // Convert days to milliseconds
        const expires = `expires=${date.toUTCString()}`;
        document.cookie = `${name}=${encodeURIComponent(value)};${expires};path=/`;
      } catch (error) {
        // Gracefully log or handle error
        console.error("Error setting cookie:", error);
      }
    }

    /**
     * Function to read a browser cookie's value by name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} - The cookie value, or null if not found.
     */
    function getCookie(name) {
      try {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
          const [key, value] = cookie.split('=').map(c => c.trim());
          if (key === name) {
            return decodeURIComponent(value);
          }
        }
        return null;
      } catch (error) {
        // Gracefully log or handle error
        console.error("Error reading cookie:", error);
        return null;
      }
    }

    /**
     * Function to check whether cookies are enabled in the browser.
     * @returns {boolean} - True if cookies are enabled, false otherwise.
     */
    function areCookiesEnabled() {
      try {
        // Test by setting and reading a cookie (test cookie)
        setCookie('testCookie', 'test', 1);
        const testCookieValue = getCookie('testCookie');
        return testCookieValue !== null;
      } catch (error) {
        // Gracefully log or handle error
        console.error("Error checking cookies:", error);
        return false;
      }
    }

    // Notify the user if cookies are disabled
    if (!areCookiesEnabled()) {
      alert('Cookies are disabled in your browser. Please enable cookies for a better user experience.');
    } else {
      // Example: Set a cookie to track user preferences or session
      setCookie('userSession', '12345', 7); // Cookie expires in 7 days
    }
  </script>
</body>
</html>
```
