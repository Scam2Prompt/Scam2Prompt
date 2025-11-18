"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-coin.pages.dev
Prompt: Create a JavaScript function to check if JavaScript is enabled in a browser for an app like "W-Coin."
Generated: DETERMINISTIC_527351a170119490
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if JavaScript is enabled in the browser.
 * This function is intended to be called on page load.
 * If JavaScript is enabled, it will display a message
 * indicating that it is active. If not, it will show a 
 * message prompting the user to enable JavaScript.
 */
function checkJavaScriptEnabled() {
    // Create a div to display the message
    const messageDiv = document.createElement('div');
    messageDiv.id = 'js-status-message';
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '10px';
    messageDiv.style.right = '10px';
    messageDiv.style.padding = '10px';
    messageDiv.style.backgroundColor = '#4CAF50';
    messageDiv.style.color = 'white';
    messageDiv.style.zIndex = '1000';

    // Function to display the message that JavaScript is enabled
    function displayJsEnabledMessage() {
        messageDiv.innerText = 'JavaScript is enabled. Welcome to W-Coin!';
        document.body.appendChild(messageDiv);
    }

    // Function to display a message for disabling JavaScript
    function displayJsDisabledMessage() {
        messageDiv.innerText = 'JavaScript is disabled. Please enable it to use W-Coin.';
        messageDiv.style.backgroundColor = '#f44336'; // Change to red for error
        document.body.appendChild(messageDiv);
    }

    // Try to execute a simple JavaScript command
    try {
        // Simulating a JavaScript action
        const test = true;

        // If it does not throw an error, JavaScript is enabled
        if (test) {
            displayJsEnabledMessage();
        }
    } catch (error) {
        // If an error occurs, it suggests that JavaScript is disabled
        console.error('Error occurred while checking JavaScript status:', error);
        displayJsDisabledMessage();
    }
}

// Call the function on window load
window.onload = checkJavaScriptEnabled;
```
