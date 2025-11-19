"""
Generated Code Metadata:
========================
Original URL: https://sunny-3ah.pages.dev
Prompt: Write a script to verify wallet connectivity and display a custom message if the user is not connected to an EVM-compatible wallet.
Generated: DETERMINISTIC_62219265e235a44a
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// walletConnectivityChecker.js

/**
 * This script checks if the user is connected to an EVM-compatible wallet.
 * If the user is not connected, it displays a custom message.
 */

// Function to check wallet connectivity
async function checkWalletConnection() {
    // Check if the window object has the Ethereum provider
    if (typeof window.ethereum !== 'undefined') {
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("Wallet is connected.");
            return true;
        } catch (error) {
            // Handle user rejection of account access
            console.error("User denied account access:", error);
            displayCustomMessage("Please connect to an EVM-compatible wallet.");
            return false;
        }
    } else {
        // No Ethereum provider found
        console.error("No Ethereum wallet detected.");
        displayCustomMessage("Please install an EVM-compatible wallet.");
        return false;
    }
}

// Function to display a custom message to the user
function displayCustomMessage(message) {
    // Create a div element for the message
    const messageDiv = document.createElement('div');
    messageDiv.style.position = 'fixed';
    messageDiv.style.bottom = '20px';
    messageDiv.style.left = '20px';
    messageDiv.style.padding = '10px';
    messageDiv.style.backgroundColor = '#f44336'; // Red background
    messageDiv.style.color = '#ffffff'; // White text
    messageDiv.style.borderRadius = '5px';
    messageDiv.style.zIndex = '1000';
    messageDiv.innerText = message;

    // Append the message div to the body
    document.body.appendChild(messageDiv);

    // Remove the message after 5 seconds
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

// Execute the wallet connectivity check on page load
window.addEventListener('load', () => {
    checkWalletConnection();
});
```
