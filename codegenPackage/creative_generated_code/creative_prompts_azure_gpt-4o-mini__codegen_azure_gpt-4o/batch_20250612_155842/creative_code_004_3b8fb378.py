"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://66789.pages.dev
Prompt: Write a simple JavaScript function that alerts users to enable cookies for a specific site.
Generated: DETERMINISTIC_3b8fb3784a30aac4
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if cookies are enabled in the user's browser
 * and display an alert if cookies are disabled.
 * 
 * This function is designed to be simple, clean, and production-ready.
 */
function alertIfCookiesDisabled() {
  try {
    // Attempt to set a test cookie to detect if cookies are enabled
    document.cookie = "test_cookie=enabled; path=/";

    // Check if the test cookie was successfully set
    const cookiesEnabled = document.cookie.includes("test_cookie=enabled");

    // If cookies are disabled, notify the user
    if (!cookiesEnabled) {
      alert("Cookies are disabled in your browser. Please enable cookies to use this site properly.");
    }

    // Clean up the test cookie
    document.cookie = "test_cookie=enabled; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC";
  } catch (error) {
    // Handle any unexpected errors gracefully
    console.error("An error occurred while checking cookie settings:", error);
    alert("An unexpected error occurred. Please ensure cookies are enabled in your browser.");
  }
}

// Call the function to check cookies on page load
alertIfCookiesDisabled();
```
