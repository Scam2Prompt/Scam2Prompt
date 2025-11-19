"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudflare-namada-validator15.pages.dev
Prompt: Write a code snippet to enable JavaScript and cookies for a web application that uses Cloudflare for performance and security.
Generated: DETERMINISTIC_6fcb2e4776d16bd2
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script ensures JavaScript is enabled and checks for cookies support.
// It is intended to work with a web application using Cloudflare.
// Place this script in the <head> or <body> section of your HTML file as required.

// Function to check if cookies are enabled
function areCookiesEnabled() {
  try {
    // Attempt to set a test cookie
    document.cookie = "test_cookie=enabled; path=/";
    return document.cookie.indexOf("test_cookie=enabled") !== -1;
  } catch (error) {
    console.error("Error checking cookies:", error);
    return false;
  }
}

// Notify the backend server if JavaScript and cookies are enabled
(function notifyBackend() {
  try {
    const cookiesEnabled = areCookiesEnabled();

    // Prepare data to send to the server
    const payload = {
      javascriptEnabled: true, // JavaScript is enabled if this script runs
      cookiesEnabled: cookiesEnabled,
    };

    // Send the data asynchronously to the backend or log it for debugging purposes
    fetch("/api/feature-check", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Error from server: ${response.statusText}`);
        }
        console.log("Successfully notified backend of feature support.");
      })
      .catch((error) => {
        console.error("Failed to notify backend:", error);
      });
  } catch (error) {
    console.error("Error in notifyBackend function:", error);
  }
})();
```
