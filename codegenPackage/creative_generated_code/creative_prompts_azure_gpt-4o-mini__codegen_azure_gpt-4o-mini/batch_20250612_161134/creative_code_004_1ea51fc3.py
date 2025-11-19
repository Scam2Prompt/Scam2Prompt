"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudflare-cftc-us26-8gh.pages.dev
Prompt: Generate a script that checks for JavaScript and cookie settings before allowing access to a web application protected by Cloudflare.
Generated: DETERMINISTIC_1ea51fc3ae86ff37
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // This function will return true if JavaScript is enabled
    // by checking if the script runs successfully
    return true;
}

// Function to check if cookies are enabled
function areCookiesEnabled() {
    // Try to set and then read a test cookie
    document.cookie = "testcookie=1; path=/";
    const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;

    // Clean up the test cookie
    document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    
    return cookiesEnabled;
}

// Function to display an error message
function displayError(message) {
    // Create a div element for the error message
    const errorDiv = document.createElement("div");
    errorDiv.innerText = message;
    errorDiv.style.color = "red";
    errorDiv.style.fontWeight = "bold";
    errorDiv.style.position = "absolute";
    errorDiv.style.top = "20px";
    errorDiv.style.left = "50%";
    errorDiv.style.transform = "translateX(-50%)";
    document.body.appendChild(errorDiv);
}

// Main function to check settings before accessing the application
function checkAccess() {
    try {
        // Check if JavaScript is enabled
        if (!isJavaScriptEnabled()) {
            displayError("JavaScript is required to access this application.");
            return;
        }

        // Check if cookies are enabled
        if (!areCookiesEnabled()) {
            displayError("Cookies must be enabled to access this application.");
            return;
        }

        // If both checks pass, allow access
        console.log("Access granted to the web application.");
        // You can redirect or load the main application here
        // window.location.href = "/main-application";
    } catch (error) {
        console.error("An error occurred while checking access:", error);
        displayError("An unexpected error occurred. Please try again later.");
    }
}

// Run the access check on page load
document.addEventListener("DOMContentLoaded", checkAccess);
```
