"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-nft.vercel.app
Prompt: Generate code to display a warning message if a user tries to access a wallet connection feature on a browser other than Chrome.
Generated: DETERMINISTIC_08705daa84d197c0
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check the user's browser and display a warning if it's not Chrome
function checkBrowserForWalletConnection() {
    try {
        // Get the user agent string from the browser
        const userAgent = navigator.userAgent;

        // Check if the browser is Chrome. Chrome's user agent string includes "Chrome".
        const isChrome = userAgent.includes("Chrome") && !userAgent.includes("Edge") && !userAgent.includes("OPR");

        // If the browser is not Chrome, display a warning message
        if (!isChrome) {
            alert("Warning: The wallet connection feature is optimized for Chrome. Please use Chrome for the best experience.");
        } else {
            console.log("Browser check passed: User is on Chrome.");
        }
    } catch (error) {
        // Log any unexpected errors to the console
        console.error("An error occurred while checking the browser:", error);
    }
}

// Call the function to perform the browser check
checkBrowserForWalletConnection();
```
