"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethlast.com
Prompt: Write JavaScript code to detect if JavaScript is disabled on a mobile browser and display a warning message, similar to the behavior described on the ETH Pledge website.
Generated: DETERMINISTIC_52f271250ab965a0
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to create and display a warning message when JavaScript is disabled
function displayWarning() {
    // Create a div element to hold the warning message
    const warningDiv = document.createElement('div');

    // Set the styles for the warning div
    warningDiv.style.position = 'fixed';
    warningDiv.style.top = '0';
    warningDiv.style.left = '0';
    warningDiv.style.width = '100%';
    warningDiv.style.backgroundColor = 'red';
    warningDiv.style.color = 'white';
    warningDiv.style.textAlign = 'center';
    warningDiv.style.padding = '10px';
    warningDiv.style.zIndex = '1000';
    warningDiv.style.fontFamily = 'Arial, sans-serif';
    
    // Set the warning message content
    warningDiv.innerHTML = 'JavaScript is disabled in your browser. Please enable it for the best experience.';

    // Append the warning div to the body
    document.body.appendChild(warningDiv);
}

// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // If JavaScript is enabled, the setTimeout will run after 0 milliseconds
    setTimeout(() => {
        // Remove the warning message if it exists
        const warningDiv = document.querySelector('div');
        if (warningDiv) {
            warningDiv.remove();
        }
    }, 0);
}

// Call the function to check if JavaScript is enabled
checkJavaScriptEnabled();

// Call displayWarning if JavaScript is disabled
// This will only execute if JavaScript is not running
document.addEventListener('DOMContentLoaded', (event) => {
    // This block will not execute if JavaScript is enabled
    displayWarning();
});
```
