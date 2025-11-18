"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-clone-three.vercel.app
Prompt: Generate code for detecting if the user is running Chrome and displaying a message if the browser is incompatible, as described on the OpenSea clone website.
Generated: DETERMINISTIC_a10882195a689b7c
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to detect the user's browser
function detectBrowser() {
    // Get the userAgent string from the browser
    const userAgent = navigator.userAgent;

    // Regular expression to check if the browser is Chrome
    const isChrome = /Chrome/.test(userAgent) && /Google Inc/.test(navigator.vendor);

    return isChrome;
}

// Function to display a warning message if the browser is incompatible
function displayIncompatibleBrowserMessage() {
    // Create a new div element for the message
    const messageDiv = document.createElement('div');
    
    // Set the message text and styles
    messageDiv.textContent = "Your browser is incompatible with this site. Please use Google Chrome for the best experience.";
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '50%';
    messageDiv.style.left = '50%';
    messageDiv.style.transform = 'translate(-50%, -50%)';
    messageDiv.style.padding = '20px';
    messageDiv.style.backgroundColor = '#f44336';
    messageDiv.style.color = '#ffffff';
    messageDiv.style.zIndex = '1000';
    messageDiv.style.borderRadius = '5px';
    messageDiv.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    
    // Append the message to the body
    document.body.appendChild(messageDiv);
}

// Main function to execute on page load
function init() {
    try {
        // Check if the user is running Chrome
        if (!detectBrowser()) {
            // If not, display the incompatible browser message
            displayIncompatibleBrowserMessage();
        }
    } catch (error) {
        console.error("Error detecting browser:", error);
    }
}

// Execute the init function once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', init);
```
