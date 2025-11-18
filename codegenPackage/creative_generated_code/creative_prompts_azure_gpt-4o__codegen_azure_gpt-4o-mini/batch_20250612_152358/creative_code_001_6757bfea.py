"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smart-multichain.pages.dev
Prompt: Generate code for connecting a wallet to blockchain Dapps using the Chain Cloud and Sequence infrastructure as described on the webpage.
Generated: DETERMINISTIC_6757bfea336d7792
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ChainCloud } from 'chain-cloud-sdk'; // Assuming a library for Chain Cloud interactions
import { Sequence } from 'sequence-sdk'; // Assuming a library for Sequence wallet interactions

// Configuration for the blockchain connection
const CHAIN_CLOUD_API_KEY = 'YOUR_CHAIN_CLOUD_API_KEY';
const SEQUENCE_WALLET_NETWORK = 'mainnet'; // Change to 'testnet' as needed

// Initialize Chain Cloud and Sequence instances
const chainCloud = new ChainCloud({ apiKey: CHAIN_CLOUD_API_KEY });
const sequenceWallet = new Sequence({ network: SEQUENCE_WALLET_NETWORK });

// Function to connect wallet to DApp
async function connectWallet() {
    try {
        // Request user to connect their wallet
        const wallet = await sequenceWallet.connect();

        // Check if wallet connection was successful
        if (wallet) {
            console.log('Wallet connected:', wallet.address);
            // Optionally, you can fetch wallet balance or other details here
            const balance = await chainCloud.getBalance(wallet.address);
            console.log(`Wallet balance: ${balance} ETH`);
        } else {
            console.error('Wallet connection failed.');
        }
    } catch (error) {
        // Handle errors appropriately
        console.error('Error connecting wallet:', error.message);
    }
}

// Function to disconnect wallet
async function disconnectWallet() {
    try {
        await sequenceWallet.disconnect();
        console.log('Wallet disconnected successfully.');
    } catch (error) {
        console.error('Error disconnecting wallet:', error.message);
    }
}

// Call the connectWallet function when needed (e.g., on button click)
// For demonstration, we'll call it immediately here
connectWallet();

// Optionally, you can provide a way to disconnect the wallet
// disconnectWallet(); // Uncomment to disconnect the wallet
```

**Note:**
- Replace `'YOUR_CHAIN_CLOUD_API_KEY'` with your actual Chain Cloud API key.
- Ensure the library imports are correct based on the actual SDK or libraries you use.
