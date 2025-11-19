"""
Generated Code Metadata:
========================
Original URL: https://consensysmedia.net
Prompt: Write a code snippet that utilizes Infura’s decentralized infrastructure for a Web3 application.
Generated: DETERMINISTIC_85a0de2879d922bd
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the required libraries
const { ethers } = require("ethers");

// Define the Infura project ID and the Ethereum network to connect to
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura Project ID
const NETWORK = "mainnet"; // Change to desired network (e.g., 'rinkeby', 'ropsten', etc.)

// Create a provider using Infura's endpoint
const provider = new ethers.providers.InfuraProvider(NETWORK, INFURA_PROJECT_ID);

// Function to get the balance of an Ethereum address
async function getBalance(address) {
    try {
        // Validate the Ethereum address
        if (!ethers.utils.isAddress(address)) {
            throw new Error("Invalid Ethereum address");
        }

        // Fetch the balance from the provider
        const balance = await provider.getBalance(address);
        
        // Convert the balance from Wei to Ether
        const balanceInEther = ethers.utils.formatEther(balance);
        
        // Log the balance
        console.log(`Balance of ${address}: ${balanceInEther} ETH`);
    } catch (error) {
        // Handle errors gracefully
        console.error("Error fetching balance:", error.message);
    }
}

// Example usage: Replace with a valid Ethereum address
const exampleAddress = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"; // Replace with a valid address
getBalance(exampleAddress);
```
