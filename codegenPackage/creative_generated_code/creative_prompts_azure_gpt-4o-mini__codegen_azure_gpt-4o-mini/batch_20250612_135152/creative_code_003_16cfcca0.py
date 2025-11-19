"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpadxz.com
Prompt: Create a JavaScript code that displays a warning message for users with outdated browsers when they attempt to log in.
Generated: DETERMINISTIC_16cfcca05d06fef6
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if the browser is outdated
function isBrowserOutdated() {
    // Retrieve the user agent string
    const userAgent = navigator.userAgent;

    // Define a simple regex to check for outdated browsers (Example: Internet Explorer)
    const outdatedBrowsers = /MSIE|Trident/;

    // Return true if the user agent matches the outdated browser regex
    return outdatedBrowsers.test(userAgent);
}

// Function to display a warning message to users with outdated browsers
function displayWarningMessage() {
    const warningMessage = `
        <div id="browser-warning" style="background-color: yellow; padding: 20px; border: 1px solid red; position: fixed; top: 20px; left: 20px; z-index: 1000;">
            <strong>Warning:</strong> You are using an outdated browser. Please update your browser for a better experience.
        </div>
    `;

    // Append the warning message to the body of the document
    document.body.insertAdjacentHTML('afterbegin', warningMessage);
}

// Function to initialize the browser check and display warning if needed
function initBrowserCheck() {
    try {
        // Check if the browser is outdated
        if (isBrowserOutdated()) {
            // Display the warning message if the browser is outdated
            displayWarningMessage();
        }
    } catch (error) {
        // Log any errors to the console for debugging purposes
        console.error("An error occurred while checking the browser version: ", error);
    }
}

// Run the browser check on page load
window.onload = initBrowserCheck;
```
