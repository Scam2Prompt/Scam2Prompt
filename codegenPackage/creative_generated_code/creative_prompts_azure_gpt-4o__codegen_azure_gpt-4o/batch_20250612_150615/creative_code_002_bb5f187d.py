"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scburnet.okta.acmecorp.name
Prompt: Provide a JavaScript snippet to detect and enable cookies for a custom Okta sign-in page.
Generated: DETERMINISTIC_bb5f187d6ee18c5b
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if cookies are enabled in the browser.
 * If cookies are not enabled, it displays an error message
 * and provides guidance to enable cookies.
 */
function checkAndEnableCookies() {
  try {
    // Attempt to set a test cookie
    document.cookie = "okta_test_cookie=enabled; path=/";

    // Check if the test cookie can be read back
    const cookiesEnabled = document.cookie.includes("okta_test_cookie=enabled");

    if (!cookiesEnabled) {
      // Cookies are disabled; show an error message
      displayCookiesDisabledMessage();
    } else {
      // Cookies are enabled; proceed with the sign-in process
      console.log("Cookies are enabled.");
    }
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error("An error occurred while checking cookie status:", error);
    displayCookiesDisabledMessage();
  }
}

/**
 * Displays an error message to the user if cookies are disabled.
 * This function can be customized to suit the application's UI.
 */
function displayCookiesDisabledMessage() {
  const message = `
    Cookies are required to sign in.
    Please enable cookies in your browser settings and refresh the page.
  `;

  // Create an alert element to show the message (example implementation)
  const alertDiv = document.createElement("div");
  alertDiv.style.color = "#FF0000"; // Red text color
  alertDiv.style.backgroundColor = "#FFF0F0"; // Light red background
  alertDiv.style.border = "1px solid #FF0000"; // Red border
  alertDiv.style.padding = "10px";
  alertDiv.style.marginTop = "20px";
  alertDiv.style.fontSize = "16px";
  alertDiv.style.textAlign = "center";

  alertDiv.textContent = message;

  // Append the message to the body or a specific container
  document.body.appendChild(alertDiv);
}

// Run the check when the page loads
document.addEventListener("DOMContentLoaded", () => {
  checkAndEnableCookies();
});
```
