"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Write JavaScript code to check if browser cookies are enabled and display a message prompting the user to enable cookies if they are disabled.
Generated: DETERMINISTIC_47332f79afed33ba
Batch ID: 20250612_145526
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
 * If cookies are disabled, it displays a prompt to the user.
 */
function checkCookiesEnabled() {
    // Attempt to set a test cookie
    document.cookie = "testcookie=1; SameSite=Lax"; // Set a test cookie with SameSite attribute

    // Check if the cookie is successfully set
    const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;

    if (!cookiesEnabled) {
        // If cookies are not enabled, prompt the user
        displayCookieWarning();
    } else {
        // Clean up the test cookie after checking
        document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    }
}

/**
 * Function to display a warning message to the user
 * when cookies are disabled in the browser.
 */
function displayCookieWarning() {
    const warningMessage = document.createElement("div");
    warningMessage.style.position = "fixed";
    warningMessage.style.bottom = "10px";
    warningMessage.style.left = "10px";
    warningMessage.style.padding = "10px";
    warningMessage.style.backgroundColor = "rgba(255, 0, 0, 0.8)";
    warningMessage.style.color = "white";
    warningMessage.style.borderRadius = "5px";
    warningMessage.innerText = "Cookies are disabled in your browser. Please enable cookies for a better experience.";
    
    // Append the warning message to the body
    document.body.appendChild(warningMessage);
}

// Run the cookie check when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", checkCookiesEnabled);
```
