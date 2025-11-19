"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-savcr.com
Prompt: Explain how to create a custom transaction builder in DeFi Saver that combines multiple DeFi actions in one transaction.
Generated: DETERMINISTIC_9121d1a0a8e9783d
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules for Web3 and DeFi Saver
const Web3 = require('web3');
const DeFiSaverSDK = require('@defisaver/sdk');

// Initialize Web3 and DeFi Saver SDK
const web3 = new Web3('<YOUR_INFURA_OR_ALCHEMY_URL>'); // Replace with your Web3 provider URL
const walletAddress = '<YOUR_WALLET_ADDRESS>'; // Replace with your wallet address
const privateKey = '<YOUR_PRIVATE_KEY>'; // Replace with your private key for signing transactions
const sdk = new DeFiSaverSDK(web3); // Initialize SDK with Web3 instance

// Define the custom transaction builder function
async function createCustomTransaction() {
  try {
    // Step 1: Define the actions to include in the transaction
    const actions = [
      {
        type: 'deposit', // Example action: deposit
        protocol: 'MakerDAO', // Example protocol: MakerDAO
        params: {
          asset: 'ETH', // Asset to deposit
          amount: Web3.utils.toWei('1', 'ether'), // Amount in wei
        },
      },
      {
        type: 'borrow', // Example action: borrow
        protocol: 'MakerDAO', // Example protocol: MakerDAO
        params: {
          asset: 'DAI', // Asset to borrow
          amount: Web3.utils.toWei('200', 'ether'), // Amount in wei
        },
      },
      {
        type: 'swap', // Example action: swap
        protocol: 'Uniswap', // Example protocol: Uniswap
        params: {
          fromAsset: 'DAI', // Asset to swap from
          toAsset: 'USDC', // Asset to swap to
          amount: Web3.utils.toWei('100', 'ether'), // Amount in wei
        },
      },
    ];

    // Step 2: Build the transaction using DeFi Saver SDK
    const transactionData = await sdk.buildTransaction(walletAddress, actions);

    // Step 3: Sign the transaction
    const signedTransaction = await web3.eth.accounts.signTransaction(
      transactionData,
      privateKey
    );

    // Step 4: Send the transaction to the network
    const receipt = await web3.eth.sendSignedTransaction(
      signedTransaction.rawTransaction
    );

    // Log the transaction receipt
    console.log('Transaction successfully sent. Receipt:', receipt);
  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred while creating the custom transaction:', error);
  }
}

// Call the custom transaction builder function
createCustomTransaction();
```

Note:
- Replace `<YOUR_INFURA_OR_ALCHEMY_URL>`, `<YOUR_WALLET_ADDRESS>`, and `<YOUR_PRIVATE_KEY>` with your actual values.
- Ensure proper permissions are in place for accessing private keys and using the DeFi Saver SDK.
- Test thoroughly before deploying in a production environment.
