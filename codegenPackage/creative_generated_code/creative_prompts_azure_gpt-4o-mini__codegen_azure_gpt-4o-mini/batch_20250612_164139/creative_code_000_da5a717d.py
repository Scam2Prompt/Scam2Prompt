"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.juta-soft.hu
Prompt: How can I enable cookies in my browser to access Outlook on the Juta Soft Exchange platform?
Generated: DETERMINISTIC_da5a717d50c1bac3
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check and enable cookies in the browser
function enableCookiesForOutlook() {
    // Check if cookies are enabled
    if (navigator.cookieEnabled) {
        console.log("Cookies are already enabled in this browser.");
        return true;
    } else {
        console.warn("Cookies are not enabled. Attempting to guide the user to enable cookies.");
        // Provide instructions to enable cookies based on the user’s browser
        showCookieEnableInstructions();
        return false;
    }
}

// Function to display instructions for enabling cookies
function showCookieEnableInstructions() {
    let instructions = `
    Instructions to enable cookies based on your browser:
    
    1. **Google Chrome**:
       - Go to Settings > Privacy and security > Cookies and other site data
       - Select 'Allow all cookies'.

    2. **Mozilla Firefox**:
       - Go to Options > Privacy & Security > Cookies and Site Data
       - Ensure 'Accept cookies and site data from websites' is checked.

    3. **Microsoft Edge**:
       - Go to Settings > Site permissions > Cookies and site data
       - Enable 'Allow sites to save and read cookie data'.

    4. **Safari**:
       - Go to Preferences > Privacy
       - Uncheck 'Block all cookies'.

    After enabling cookies, please refresh the page to access Outlook on Juta Soft Exchange platform.
    `;
    alert(instructions);
}

// Execute the function to check and enable cookies
try {
    enableCookiesForOutlook();
} catch (error) {
    console.error("An error occurred while checking cookies:", error);
    alert("An unexpected error occurred. Please try again.");
}
```
