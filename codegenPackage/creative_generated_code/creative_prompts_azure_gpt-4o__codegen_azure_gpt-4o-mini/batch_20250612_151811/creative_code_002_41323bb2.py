"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-web3.com
Prompt: Generate a code snippet to enable Web3.js in a JavaScript-based dApp for connecting to a blockchain network.
Generated: DETERMINISTIC_41323bb2ba79d19f
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the required libraries
import Web3 from 'web3';

// Function to initialize Web3 and connect to the Ethereum network
async function initWeb3() {
    let web3;

    // Check if the browser has the Ethereum provider (e.g., MetaMask)
    if (window.ethereum) {
        // Create a new instance of Web3 using the injected provider
        web3 = new Web3(window.ethereum);
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("Ethereum accounts granted access");
        } catch (error) {
            // Handle user rejection of access request
            console.error("User denied account access", error);
            return null; // Return null if access is denied
        }
    } else if (window.web3) {
        // Legacy dApp browsers (e.g., Mist)
        web3 = new Web3(window.web3.currentProvider);
    } else {
        // Fallback option for non-dApp browsers
        console.error("No Ethereum provider found. Please install MetaMask or another wallet.");
        return null; // Return null if no provider is found
    }

    // Return the Web3 instance for further use
    return web3;
}

// Example usage
(async () => {
    const web3Instance = await initWeb3();
    if (web3Instance) {
        // Continue with interacting with the blockchain using the web3Instance
        console.log("Web3 initialized successfully:", web3Instance);
    } else {
        console.log("Web3 initialization failed");
    }
})();
```
