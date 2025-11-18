"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3portal-843.pages.dev
Prompt: Recommend tools or frameworks for debugging JavaScript issues in a Web3 portal environment.
Generated: DETERMINISTIC_b7d096a15b291377
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages for debugging in a Web3 portal environment
import Web3 from 'web3';

// Initialize web3 instance
const web3 = new Web3(Web3.givenProvider || "ws://localhost:8545");

/**
 * Function to enable debugging tools for better error tracking in a Web3 environment.
 * @returns {void}
 */
async function enableDebuggingTools() {
    try {
        // Check if web3 is injected by the browser or extension
        if (!web3) {
            throw new Error("Web3 is not injected. Please install MetaMask or another Web3 provider.");
        }

        // Enable the provider for debugging
        await window.ethereum.enable();

        // Log web3 version for debugging purposes
        console.log(`Web3 version: ${web3.version}`);

        // Check if the user is connected to the network
        const networkId = await web3.eth.net.getId();
        console.log(`Connected to network ID: ${networkId}`);

        // Log accounts for further debugging
        const accounts = await web3.eth.getAccounts();
        console.log(`Available accounts: ${accounts}`);

        // Initialize an error handler for catching promises rejections
        window.addEventListener('unhandledrejection', event => {
            console.error('Unhandled promise rejection:', event.reason);
        });

    } catch (error) {
        console.error("An error occurred while enabling debugging tools:", error.message);
    }
}

// Call the function to enable debugging tools
enableDebuggingTools();
```
