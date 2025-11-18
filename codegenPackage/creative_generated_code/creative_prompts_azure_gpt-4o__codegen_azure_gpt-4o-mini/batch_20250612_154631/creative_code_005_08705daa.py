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
// walletConnectionWarning.js

/**
 * Checks if the user's browser is Chrome.
 * @returns {boolean} - True if the browser is Chrome, otherwise false.
 */
function isChromeBrowser() {
    const userAgent = navigator.userAgent;
    return userAgent.includes("Chrome") && !userAgent.includes("Edg"); // Exclude Edge, which contains "Chrome" in user agent
}

/**
 * Displays a warning message if the user is not using Chrome.
 */
function displayBrowserWarning() {
    // Check if the browser is not Chrome
    if (!isChromeBrowser()) {
        // Create a warning message element
        const warningMessage = document.createElement('div');
        warningMessage.setAttribute('id', 'browser-warning');
        warningMessage.style.position = 'fixed';
        warningMessage.style.top = '10px';
        warningMessage.style.left = '50%';
        warningMessage.style.transform = 'translateX(-50%)';
        warningMessage.style.padding = '10px';
        warningMessage.style.backgroundColor = 'rgba(255, 0, 0, 0.8)'; // Red background
        warningMessage.style.color = 'white';
        warningMessage.style.borderRadius = '5px';
        warningMessage.style.zIndex = '1000';
        warningMessage.innerText = 'Warning: This feature is only available on Chrome.';

        // Append the warning message to the body
        document.body.appendChild(warningMessage);

        // Auto-remove the warning message after 5 seconds
        setTimeout(() => {
            if (document.getElementById('browser-warning')) {
                document.body.removeChild(warningMessage);
            }
        }, 5000);
    }
}

// Initialize the warning message display when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    try {
        displayBrowserWarning();
    } catch (error) {
        console.error('Error displaying the browser warning:', error);
    }
});
```
