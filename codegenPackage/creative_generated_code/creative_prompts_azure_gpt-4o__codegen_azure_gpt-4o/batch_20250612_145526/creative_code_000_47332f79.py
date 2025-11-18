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
// Function to check if cookies are enabled in the user's browser
function checkCookiesEnabled() {
    try {
        // Test if cookies can be set
        document.cookie = "test_cookie=1";
        const cookiesEnabled = document.cookie.indexOf("test_cookie=") !== -1;

        // Clean up the test cookie
        if (cookiesEnabled) {
            document.cookie = "test_cookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        }

        return cookiesEnabled;
    } catch (error) {
        // In case of unexpected errors, assume cookies are disabled
        console.error("Error while checking cookies:", error);
        return false;
    }
}

// Function to display a message if cookies are disabled
function promptEnableCookies() {
    if (!checkCookiesEnabled()) {
        // Create a message element
        const messageDiv = document.createElement("div");

        // Style the message for visibility
        messageDiv.style.position = "fixed";
        messageDiv.style.top = "0";
        messageDiv.style.left = "0";
        messageDiv.style.width = "100%";
        messageDiv.style.backgroundColor = "red";
        messageDiv.style.color = "white";
        messageDiv.style.textAlign = "center";
        messageDiv.style.padding = "10px";
        messageDiv.style.zIndex = "1000";
        messageDiv.textContent = "Cookies are disabled in your browser. Please enable cookies for a better experience.";

        // Append the message to the body
        document.body.appendChild(messageDiv);
    }
}

// Run the check when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    promptEnableCookies();
});
```
