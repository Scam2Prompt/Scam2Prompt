"""
Generated Code Metadata:
========================
Original URL: https://cow-swap-dao.org
Prompt: Generate a code example that demonstrates how to enable JavaScript and cookies in a web application to improve user experience, inspired by Cow Swap DAO.
Generated: DETERMINISTIC_8a51f6f95d7861da
Batch ID: 20250612_162734
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
  <title>Enable JavaScript and Cookies</title>
  <style>
    /* Basic styling for the warning messages */
    .warning {
      color: red;
      font-weight: bold;
      display: none; /* Hidden by default */
    }
  </style>
</head>
<body>
  <!-- Warning message for disabled JavaScript -->
  <noscript>
    <div class="warning">
      JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
    </div>
  </noscript>

  <!-- Warning message for disabled cookies -->
  <div id="cookie-warning" class="warning">
    Cookies are disabled in your browser. Please enable cookies for the best experience.
  </div>

  <script>
    // Check if cookies are enabled
    function areCookiesEnabled() {
      try {
        // Attempt to set a test cookie
        document.cookie = "testcookie=1";
        const cookiesEnabled = document.cookie.indexOf("testcookie=1") !== -1;

        // Clean up the test cookie
        document.cookie = "testcookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";

        return cookiesEnabled;
      } catch (error) {
        console.error("Error checking cookies:", error);
        return false;
      }
    }

    // Display a warning if cookies are disabled
    if (!areCookiesEnabled()) {
      const cookieWarning = document.getElementById("cookie-warning");
      if (cookieWarning) {
        cookieWarning.style.display = "block";
      }
    }

    // Example of using cookies to improve user experience
    function setUserPreference(key, value) {
      try {
        // Set a cookie with the user's preference
        document.cookie = `${key}=${value}; path=/; max-age=31536000`; // 1 year expiration
      } catch (error) {
        console.error("Error setting user preference cookie:", error);
      }
    }

    function getUserPreference(key) {
      try {
        // Retrieve the user's preference from cookies
        const cookies = document.cookie.split("; ");
        for (const cookie of cookies) {
          const [cookieKey, cookieValue] = cookie.split("=");
          if (cookieKey === key) {
            return cookieValue;
          }
        }
        return null;
      } catch (error) {
        console.error("Error retrieving user preference cookie:", error);
        return null;
      }
    }

    // Example usage: Save and retrieve a theme preference
    const themePreference = getUserPreference("theme");
    if (themePreference) {
      console.log(`User's theme preference: ${themePreference}`);
      // Apply the theme preference (e.g., dark mode or light mode)
    } else {
      console.log("No theme preference found. Setting default to 'light'.");
      setUserPreference("theme", "light");
    }
  </script>
</body>
</html>
```
