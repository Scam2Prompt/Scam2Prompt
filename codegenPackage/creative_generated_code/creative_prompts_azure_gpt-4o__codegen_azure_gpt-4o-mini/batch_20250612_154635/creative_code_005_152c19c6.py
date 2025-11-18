"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-five.vercel.app
Prompt: Write JavaScript code to display an error message if a user tries to access a wallet connection feature on a browser other than Chrome.
Generated: DETERMINISTIC_152c19c69f70347a
Batch ID: 20250612_154635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if the current browser is Chrome
function isChromeBrowser() {
    const userAgent = navigator.userAgent;
    // Regular expression to detect Chrome
    const chromePattern = /Chrome\/[0-9]+/;

    // Check if the user agent contains 'Chrome' and not 'Edge' (because Edge also contains 'Chrome' in its user agent)
    return chromePattern.test(userAgent) && !/Edge\/[0-9]+/.test(userAgent);
}

// Function to display an error message if the browser is not Chrome
function checkBrowserAndDisplayError() {
    // If the browser is not Chrome, display an error message
    if (!isChromeBrowser()) {
        // Create an error message element
        const errorMessage = document.createElement('div');
        errorMessage.textContent = "Error: This feature is only available in Google Chrome.";
        errorMessage.style.color = "red"; // Set text color to red
        errorMessage.style.fontWeight = "bold"; // Make the text bold
        errorMessage.style.position = "fixed"; // Fix the position on the screen
        errorMessage.style.top = "20px"; // Position it at the top
        errorMessage.style.left = "50%"; // Center it horizontally
        errorMessage.style.transform = "translateX(-50%)"; // Adjust for centering
        errorMessage.style.backgroundColor = "white"; // Background color for better visibility
        errorMessage.style.border = "2px solid red"; // Red border for emphasis
        errorMessage.style.padding = "10px"; // Padding for better spacing
        errorMessage.style.zIndex = "1000"; // Ensure it appears above other content

        // Append the error message to the body
        document.body.appendChild(errorMessage);
        
        // Optional: Automatically remove the error message after 5 seconds
        setTimeout(() => {
            document.body.removeChild(errorMessage);
        }, 5000);
    }
}

// Call the function to check the browser when the document is fully loaded
document.addEventListener('DOMContentLoaded', checkBrowserAndDisplayError);
```
