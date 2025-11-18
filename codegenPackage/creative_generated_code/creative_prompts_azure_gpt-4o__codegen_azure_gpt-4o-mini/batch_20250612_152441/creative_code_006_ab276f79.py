"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-ten.pages.dev
Prompt: Explain how to use the Ten Gateway to set up encrypted communication between MetaMask and the Ten Testnet, including code examples.
Generated: DETERMINISTIC_ab276f79ec9c1803
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');  // Web3.js library
const { TenGateway } = require('ten-gateway-sdk');  // Ten Gateway SDK

// Function to set up encrypted communication with MetaMask and the Ten Testnet
async function setupEncryptedCommunication() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install it to use this application.');
        }

        // Create a new instance of Web3
        const web3 = new Web3(window.ethereum);

        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's Ethereum address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        console.log(`Connected to MetaMask with address: ${userAddress}`);

        // Initialize Ten Gateway with the required configuration
        const tenGateway = new TenGateway({
            network: 'testnet', // Specify the testnet
            privateKey: process.env.TEN_PRIVATE_KEY, // Private key for encryption (should be stored securely)
        });

        // Set up encrypted message
        const message = 'Hello, Ten Testnet!';
        const encryptedMessage = await tenGateway.encryptMessage(message, userAddress);
        console.log('Encrypted Message:', encryptedMessage);

        // Send the encrypted message to Ten Testnet
        const txHash = await tenGateway.sendMessage(encryptedMessage, userAddress);
        console.log('Transaction Hash:', txHash);

        // Listen for transaction confirmation
        const receipt = await web3.eth.getTransactionReceipt(txHash);
        if (receipt && receipt.status) {
            console.log('Transaction confirmed successfully.');
        } else {
            console.error('Transaction failed or is still pending.');
        }

    } catch (error) {
        console.error('Error setting up encrypted communication:', error.message);
    }
}

// Call the setup function
setupEncryptedCommunication();
```

### Notes:
- Ensure you have the necessary libraries installed via npm:
  ```bash
  npm install web3 ten-gateway-sdk
  ```
- Make sure to set `TEN_PRIVATE_KEY` in your environment variables to keep your private key secure.
- This code should be run in an environment that supports MetaMask (like a web browser) and should be integrated as part of a larger application.
