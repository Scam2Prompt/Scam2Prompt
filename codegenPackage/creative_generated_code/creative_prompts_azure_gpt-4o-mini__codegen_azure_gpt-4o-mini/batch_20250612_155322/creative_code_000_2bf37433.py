"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-wallet.de
Prompt: How can I enable JavaScript for better functionality in the MetaMask wallet application?
Generated: DETERMINISTIC_2bf37433627d2228
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    return typeof window !== 'undefined';
}

// Function to prompt the user to enable JavaScript
function promptEnableJavaScript() {
    const message = "JavaScript is required for better functionality in the MetaMask wallet application. Please enable it in your browser settings.";
    alert(message);
}

// Main function to initialize MetaMask functionality
function initializeMetaMask() {
    // Check if JavaScript is enabled
    if (!isJavaScriptEnabled()) {
        promptEnableJavaScript();
        return; // Exit if JavaScript is not enabled
    }
    
    // MetaMask initialization logic
    if (typeof window.ethereum !== 'undefined') {
        // MetaMask is installed and available
        const provider = window.ethereum;

        // Request account access if needed
        provider.request({ method: 'eth_requestAccounts' })
            .then(accounts => {
                console.log("Connected accounts: ", accounts);
                // You can add your application logic here
            })
            .catch(error => {
                console.error("Error accessing accounts: ", error);
                // Handle the error appropriately (e.g., show a message to the user)
                alert("Failed to access MetaMask accounts. Please try again.");
            });
    } else {
        // MetaMask is not installed
        alert("Please install MetaMask to access the wallet functionalities.");
    }
}

// Execute the initialization function when the window loads
window.onload = initializeMetaMask;
```
