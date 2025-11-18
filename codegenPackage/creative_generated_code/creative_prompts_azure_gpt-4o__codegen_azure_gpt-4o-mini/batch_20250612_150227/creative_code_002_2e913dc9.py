"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskimglog12.godaddysites.com
Prompt: Provide a code example for detecting if MetaMask is installed in a browser and displaying an error message if it is not.
Generated: DETERMINISTIC_2e913dc956c16686
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if MetaMask is installed in the browser
function isMetaMaskInstalled() {
    // Check if 'window.ethereum' is available
    return typeof window.ethereum !== 'undefined';
}

// Function to display error message if MetaMask is not installed
function displayErrorMessage() {
    const errorMessage = 'MetaMask is not installed. Please install it to continue.';
    
    // Create a div element for the error message
    const errorDiv = document.createElement('div');
    errorDiv.style.position = 'fixed';
    errorDiv.style.top = '20px';
    errorDiv.style.left = '50%';
    errorDiv.style.transform = 'translateX(-50%)';
    errorDiv.style.padding = '10px';
    errorDiv.style.backgroundColor = '#f44336'; // Red color for error
    errorDiv.style.color = '#fff';
    errorDiv.style.borderRadius = '5px';
    errorDiv.style.zIndex = '1000';
    errorDiv.innerText = errorMessage;

    // Append the error message to the body
    document.body.appendChild(errorDiv);

    // Auto-remove the error message after 5 seconds
    setTimeout(() => {
        document.body.removeChild(errorDiv);
    }, 5000);
}

// Check for MetaMask installation on page load
window.onload = function() {
    if (!isMetaMaskInstalled()) {
        displayErrorMessage();
    }
};
```
