"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duoiudf-dsdds.pages.dev
Prompt: How do I create a JavaScript function to alert users to enable cookies for a better experience?
Generated: DETERMINISTIC_25fedfd12202fd1b
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to alert users to enable cookies for a better experience.
 * This function checks whether cookies are enabled in the browser and alerts the user if they are not.
 */
function checkCookiesEnabled() {
  try {
    // Attempt to set a test cookie
    document.cookie = "test_cookie=enabled; path=/;";

    // Check if the test cookie was successfully set
    if (document.cookie.indexOf("test_cookie=enabled") === -1) {
      // If the cookie is not found, alert the user
      alert("Please enable cookies in your browser settings for the best experience on this website.");
    } else {
      // Clean up the test cookie
      document.cookie = "test_cookie=enabled; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    }
  } catch (error) {
    // Handle any unexpected errors gracefully
    console.error("An error occurred while checking cookies:", error);
    alert("There was an issue checking your cookie settings. Please ensure cookies are enabled.");
  }
}

// Example usage: Call the function when the page is loaded
window.onload = checkCookiesEnabled;
```
