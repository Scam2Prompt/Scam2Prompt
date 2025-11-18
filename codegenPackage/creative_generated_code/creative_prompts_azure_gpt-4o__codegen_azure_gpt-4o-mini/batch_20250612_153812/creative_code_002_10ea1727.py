"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://palform-metamaskio-cdn.bravesites.com
Prompt: Generate JavaScript code to detect if the MetaMask extension is installed in a browser and prompt the user to log in.
Generated: DETERMINISTIC_10ea1727211f0c90
Batch ID: 20250612_153812
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
    // Check if the window.ethereum object exists
    return typeof window.ethereum !== 'undefined';
}

// Function to prompt user to log in to MetaMask
async function promptMetaMaskLogin() {
    // Check if MetaMask is installed
    if (!isMetaMaskInstalled()) {
        alert("MetaMask is not installed. Please install it to use this application.");
        return;
    }

    try {
        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        if (accounts.length > 0) {
            // Successfully logged in, account is available
            console.log("Connected account:", accounts[0]);
            alert("Successfully logged in to MetaMask!");
        } else {
            // No accounts found
            alert("No accounts found. Please ensure you have an account in MetaMask.");
        }
    } catch (error) {
        // Handle errors in a user-friendly manner
        if (error.code === 4001) {
            // User denied the request
            alert("User denied account access to MetaMask.");
        } else {
            // Other errors
            console.error("Error accessing MetaMask:", error);
            alert("An error occurred while trying to access MetaMask. Please try again.");
        }
    }
}

// Call the function to prompt user for MetaMask login
promptMetaMaskLogin();
```
