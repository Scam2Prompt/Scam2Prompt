"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3.da2a.net
Prompt: Create a code snippet that demonstrates how to handle wallet connection errors when using MetaMask on mobile devices.
Generated: DETERMINISTIC_2ea4efd5ec4f2d2b
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Create an instance of Web3
let web3;

// Function to initialize Web3 and handle wallet connection
async function initWeb3() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            // Create a Web3 instance using the current provider
            web3 = new Web3(window.ethereum);

            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected successfully');
        } else {
            throw new Error('MetaMask is not installed. Please install it to use this application.');
        }
    } catch (error) {
        // Handle connection errors
        handleConnectionError(error);
    }
}

// Function to handle connection errors
function handleConnectionError(error) {
    console.error('Error connecting to wallet:', error.message);
    
    // Display user-friendly error messages
    if (error.message.includes('user rejected')) {
        alert('Connection request was rejected. Please try again.');
    } else if (error.message.includes('MetaMask is not installed')) {
        alert('MetaMask is not installed. Please install it from the browser extension store.');
    } else {
        alert('An unexpected error occurred. Please check the console for details.');
    }
}

// Event listener for window load to initialize Web3
window.onload = () => {
    initWeb3();
};
```
