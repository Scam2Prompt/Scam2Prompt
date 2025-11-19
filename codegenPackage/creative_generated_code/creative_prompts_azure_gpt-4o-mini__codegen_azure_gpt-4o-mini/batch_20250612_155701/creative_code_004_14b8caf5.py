"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usa-metamask-insignn.godaddysites.com
Prompt: Generate a code example that demonstrates how to check if MetaMask is installed in the user's browser.
Generated: DETERMINISTIC_14b8caf5c611b062
Batch ID: 20250612_155701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if MetaMask is installed in the user's browser.
 * 
 * @returns {boolean} - Returns true if MetaMask is installed, otherwise false.
 */
function isMetaMaskInstalled() {
    // Check if the window.ethereum object is available
    // This is the standard way to detect MetaMask
    return Boolean(window.ethereum && window.ethereum.isMetaMask);
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    // Get a reference to the status element
    const statusElement = document.getElementById('metamask-status');

    try {
        if (isMetaMaskInstalled()) {
            statusElement.textContent = 'MetaMask is installed!';
            statusElement.style.color = 'green';
        } else {
            statusElement.textContent = 'MetaMask is not installed. Please install it to access this feature.';
            statusElement.style.color = 'red';
        }
    } catch (error) {
        console.error('Error checking MetaMask installation:', error);
        statusElement.textContent = 'An error occurred while checking for MetaMask.';
        statusElement.style.color = 'orange';
    }
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Check MetaMask Installation</title>
    <script src="path/to/your/script.js" defer></script> <!-- Include your JavaScript file -->
</head>
<body>
    <h1>MetaMask Installation Check</h1>
    <div id="metamask-status"></div>
</body>
</html>
```
