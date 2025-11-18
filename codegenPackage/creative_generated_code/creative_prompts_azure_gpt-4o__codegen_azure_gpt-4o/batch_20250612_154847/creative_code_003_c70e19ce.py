"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ostpp.ru
Prompt: Write JavaScript code using web3.js to connect a MetaMask wallet to Hop Protocol and initiate a token transfer between Ethereum and Optimism networks. Include steps for handling transaction fees and relayer interactions.
Generated: DETERMINISTIC_c70e19cea28d20fd
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the web3.js library and necessary dependencies
const Web3 = require('web3');
const { Hop } = require('@hop-protocol/sdk');

// Initialize web3 instance (assumes MetaMask extension is installed and configured)
const web3 = new Web3(Web3.givenProvider);

// Define global variables
let accounts, hopSdk;

// Connect MetaMask wallet
async function connectWallet() {
  try {
    // Request account access
    accounts = await web3.eth.requestAccounts();
    console.log('Connected account:', accounts[0]);
  } catch (error) {
    console.error('Failed to connect MetaMask wallet:', error);
    throw error;
  }
}

// Initialize Hop Protocol SDK
async function initializeHopSdk() {
  try {
    // Instantiate Hop SDK (Ethereum mainnet as default network)
    hopSdk = new Hop('mainnet');
    console.log('Hop Protocol SDK initialized.');
  } catch (error) {
    console.error('Failed to initialize Hop SDK:', error);
    throw error;
  }
}

// Transfer tokens using Hop Protocol
async function transferTokens() {
  try {
    // Define transfer parameters
    const sourceChain = 'ethereum'; // Source chain
    const destinationChain = 'optimism'; // Destination chain
    const token = 'USDC'; // Token to transfer
    const amount = '100'; // Amount to transfer (specify as a string for compatibility)

    // Get signer (MetaMask wallet)
    const signer = web3.eth.accounts.wallet.add(accounts[0]);

    // Get transaction fee estimate (includes relayer fees and gas costs)
    const { fee, estimatedReceived } = await hopSdk.getFeeEstimate({
      sourceChain,
      destinationChain,
      token,
      amount,
    });
    console.log('Estimated transaction fee:', fee);
    console.log('Estimated amount received on destination chain:', estimatedReceived);

    // Perform transfer
    const tx = await hopSdk.send({
      sourceChain,
      destinationChain,
      token,
      amount,
      recipient: accounts[0], // Recipient address (user's MetaMask wallet)
      signer, // Signer to authorize transaction
    });

    console.log('Transaction hash:', tx.hash);
    console.log('Transfer initiated successfully.');
  } catch (error) {
    console.error('Failed to transfer tokens using Hop Protocol:', error);
    throw error;
  }
}

// Main function to execute the workflow
async function main() {
  try {
    // Step 1: Connect MetaMask wallet
    await connectWallet();

    // Step 2: Initialize Hop SDK
    await initializeHopSdk();

    // Step 3: Initiate token transfer
    await transferTokens();
  } catch (error) {
    console.error('Error in main function:', error);
  }
}

// Execute the main function
main();
```

**Note:** Ensure that the required dependencies (`web3` and `@hop-protocol/sdk`) are installed in your project before running this script:

```bash
npm install web3 @hop-protocol/sdk
```

Also, make sure to configure MetaMask and have sufficient funds (including gas fees) for the transaction.
