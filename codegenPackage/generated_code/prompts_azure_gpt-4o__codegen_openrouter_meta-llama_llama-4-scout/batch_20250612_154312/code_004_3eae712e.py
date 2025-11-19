"""
Generated Code Metadata:
========================
Original URL: https://dogeai.eu
Prompt: Write code for a JavaScript snippet that displays a custom error message when JavaScript is disabled, similar to the behavior described on the DogeAI website.
Generated: DETERMINISTIC_3eae712e5a38d7ae
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled by attempting to set a test cookie
function isJavaScriptEnabled() {
    try {
        // Create a test cookie
        document.cookie = "javascriptEnabled=true; expires=Fri, 31 Dec 1970 00:00:00 GMT";
        
        // If the cookie is set, JavaScript is enabled
        if (document.cookie.indexOf("javascriptEnabled=true") !== -1) {
            return true;
        } else {
            return false;
        }
    } catch (error) {
        // If an error occurs, assume JavaScript is disabled
        console.error("Error checking JavaScript enabled status:", error);
        return false;
    }
}

// Display a custom error message if JavaScript is disabled
function displayErrorMessage() {
    // Create a container for the error message
    const errorContainer = document.createElement("div");
    errorContainer.id = "javascript-disabled-error";

    // Define the error message
    const errorMessage = document.createTextNode("Please enable JavaScript to use this website.");

    // Add the error message to the container
    errorContainer.appendChild(errorMessage);

    // Add styles to the error message
    errorContainer.style.position = "fixed";
    errorContainer.style.top = "0";
    errorContainer.style.left = "0";
    errorContainer.style.width = "100%";
    errorContainer.style.backgroundColor = "#FF0000";
    errorContainer.style.color = "#FFFFFF";
    errorContainer.style.textAlign = "center";
    errorContainer.style.padding = "1em";
    errorContainer.style.zIndex = "1000";

    // Add the error container to the page
    document.body.appendChild(errorContainer);
}

// Main function to check JavaScript status and display error message
function main() {
    if (!isJavaScriptEnabled()) {
        displayErrorMessage();
    }
}

// Run the main function on page load
document.addEventListener("DOMContentLoaded", main);
```
