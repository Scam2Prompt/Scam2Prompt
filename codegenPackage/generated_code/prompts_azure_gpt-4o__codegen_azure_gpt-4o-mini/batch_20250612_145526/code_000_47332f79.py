"""
Generated Code Metadata:
========================
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Write JavaScript code to check if browser cookies are enabled and display a message prompting the user to enable cookies if they are disabled.
Generated: DETERMINISTIC_47332f79afed33ba
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to check if cookies are enabled in the browser
function areCookiesEnabled() {
    // Try to set a test cookie
    document.cookie = "testcookie=1; SameSite=Lax";
    
    // Check if the cookie was set successfully
    const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;

    // Clean up by deleting the test cookie
    if (cookiesEnabled) {
        document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax";
    }

    return cookiesEnabled;
}

// Function to display a message to the user
function displayCookieMessage() {
    // Create a message element
    const messageElement = document.createElement("div");
    messageElement.style.position = "fixed";
    messageElement.style.bottom = "20px";
    messageElement.style.left = "20px";
    messageElement.style.padding = "10px";
    messageElement.style.backgroundColor = "#f8d7da";
    messageElement.style.color = "#721c24";
    messageElement.style.border = "1px solid #f5c6cb";
    messageElement.style.borderRadius = "5px";
    messageElement.innerText = "Cookies are disabled. Please enable cookies for a better experience.";

    // Append the message to the body
    document.body.appendChild(messageElement);
}

// Main function to check cookies and display message if necessary
function checkCookies() {
    try {
        if (!areCookiesEnabled()) {
            displayCookieMessage();
        }
    } catch (error) {
        console.error("An error occurred while checking cookies:", error);
    }
}

// Run the check on page load
window.onload = checkCookies;
```
