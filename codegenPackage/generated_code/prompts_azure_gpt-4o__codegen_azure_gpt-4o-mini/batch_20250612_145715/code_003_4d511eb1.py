"""
Generated Code Metadata:
========================
Original URL: https://gelato-network-cqz.pages.dev
Prompt: Demonstrate how to use Gelato's Relay service to enable gasless transactions for a decentralized application (dApp).
Generated: DETERMINISTIC_4d511eb1f3ffa452
Batch ID: 20250612_145715
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://relay.gelato.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { GelatoRelay, RelayProvider } from '@gelatonetwork/relay-sdk';
import { ethers } from 'ethers';

// Define constants
const RELAY_URL = 'https://relay.gelato.network'; // Gelato Relay URL
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY'; // Replace with your wallet's private key
const DAPP_CONTRACT_ADDRESS = 'YOUR_DAPP_CONTRACT_ADDRESS'; // Replace with your dApp contract address
const DAPP_ABI = [ /* Your dApp contract ABI */ ]; // Replace with your dApp contract ABI

// Initialize provider and wallet
const provider = new ethers.providers.JsonRpcProvider('https://your.ethereum.node'); // Replace with your Ethereum node URL
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize Gelato Relay
const gelatoRelay = new GelatoRelay(RELAY_URL);

// Create a RelayProvider instance
const relayProvider = new RelayProvider(gelatoRelay, wallet);

// Function to send a gasless transaction
async function sendGaslessTransaction() {
    try {
        // Create a contract instance
        const contract = new ethers.Contract(DAPP_CONTRACT_ADDRESS, DAPP_ABI, relayProvider);

        // Define the transaction parameters
        const tx = {
            to: DAPP_CONTRACT_ADDRESS,
            value: ethers.utils.parseEther('0.01'), // Amount to send
            data: contract.interface.encodeFunctionData('yourFunctionName', [/* function parameters */]), // Replace with your function name and parameters
            gasLimit: 100000, // Set a gas limit
        };

        // Send the transaction
        const txResponse = await contract.sendTransaction(tx);
        console.log('Transaction sent:', txResponse.hash);

        // Wait for the transaction to be mined
        const receipt = await txResponse.wait();
        console.log('Transaction mined:', receipt.transactionHash);
    } catch (error) {
        console.error('Error sending gasless transaction:', error);
    }
}

// Execute the function
sendGaslessTransaction();
```

**Note:** Replace placeholders like `YOUR_PRIVATE_KEY`, `YOUR_DAPP_CONTRACT_ADDRESS`, and `yourFunctionName` with actual values relevant to your dApp. Ensure that you handle sensitive information securely and do not expose your private key in production code.
