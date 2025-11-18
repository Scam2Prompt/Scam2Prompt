"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.ire-coinbase.com
Prompt: Generate a script to detect the browser version and display a custom message for users accessing cPanel with unsupported browsers like Internet Explorer 11.
Generated: DETERMINISTIC_69663373c9955e94
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: browser-check.js
// Description: Script to detect the browser version and display a warning message for unsupported browsers accessing cPanel.

// IIFE to avoid polluting the global namespace
(function () {
    "use strict";

    // Custom messages
    const unsupportedMessage = "Your browser is not supported for accessing cPanel. Please use a modern browser like Chrome, Firefox, Edge, or Safari.";
    const supportedMessage = "Welcome to cPanel! Your browser is supported.";

    // Function to detect Internet Explorer version
    function isInternetExplorer() {
        const ua = window.navigator.userAgent;
        const msieIndex = ua.indexOf("MSIE "); // Detect Internet Explorer <= 10
        const tridentIndex = ua.indexOf("Trident/"); // Detect Internet Explorer 11

        if (msieIndex > -1) {
            const version = parseInt(ua.substring(msieIndex + 5, ua.indexOf(".", msieIndex)), 10);
            return version <= 11;
        }

        if (tridentIndex > -1) {
            const rvIndex = ua.indexOf("rv:");
            const version = parseInt(ua.substring(rvIndex + 3, ua.indexOf(".", rvIndex)), 10);
            return version <= 11;
        }

        return false;
    }

    // Function to display a message to the user
    function displayMessage(message) {
        // Create a container for the message
        const messageContainer = document.createElement("div");
        messageContainer.style.position = "fixed";
        messageContainer.style.top = "0";
        messageContainer.style.left = "0";
        messageContainer.style.width = "100%";
        messageContainer.style.padding = "10px";
        messageContainer.style.backgroundColor = "#ffcccb"; // Light red background for warning
        messageContainer.style.color = "#000";
        messageContainer.style.fontSize = "16px";
        messageContainer.style.fontWeight = "bold";
        messageContainer.style.textAlign = "center";
        messageContainer.style.zIndex = "1000";
        messageContainer.innerText = message;

        // Append the message to the body
        document.body.appendChild(messageContainer);
    }

    // Main execution
    try {
        if (isInternetExplorer()) {
            // Display warning for unsupported browsers
            displayMessage(unsupportedMessage);
        } else {
            // Optionally display a message for supported browsers
            console.log(supportedMessage);
        }
    } catch (error) {
        console.error("An error occurred while checking the browser version:", error);
    }
})();
```
