"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Provide an example of how to use MetaMask with Hop Protocol to facilitate cross-chain token transfers between Ethereum and Polygon networks.
Generated: DETERMINISTIC_9f26c5fd284b1a74
Batch ID: 20250612_153809
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
import { Hop } from '@hop-protocol/sdk';

// Initialize Web3 and Hop instances
const web3 = new Web3(window.ethereum); // MetaMask provider
const hopSdk = new Hop('mainnet'); // Hop SDK for mainnet

// Define necessary variables
const token = 'USDC'; // Token symbol to transfer (e.g., USDC)
const amount = '10'; // Amount to transfer (string format)
const senderAddress = ''; // Replace with your MetaMask wallet address
const recipientAddress = ''; // Replace with recipient address
const sourceChain = 'ethereum'; // Source chain
const destinationChain = 'polygon'; // Destination chain

async function setupMetaMask() {
  try {
    // Request connection to MetaMask
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Get the connected account
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      throw new Error('No accounts found in MetaMask');
    }
    return accounts[0]; // Return the active account
  } catch (error) {
    console.error('MetaMask setup failed:', error.message);
    throw error;
  }
}

async function performCrossChainTransfer() {
  try {
    // Setup MetaMask and get the sender's account
    const activeAccount = await setupMetaMask();

    if (senderAddress === '') {
      senderAddress = activeAccount; // Use the MetaMask-connected wallet if not defined
    }

    // Validate recipient address
    if (!web3.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address');
    }

    // Instantiate Hop token bridge for the specified token
    const bridge = hopSdk.bridge(token);

    // Estimate gas fees required for the transfer
    const txData = await bridge.getSendTransaction({
      amount,
      sourceChain,
      destinationChain,
      from: senderAddress,
      to: recipientAddress,
    });

    console.log('Transaction data:', txData);

    // Send the transaction using Web3
    const txHash = await web3.eth.sendTransaction({
      from: senderAddress,
      to: txData.to,
      data: txData.data,
      value: txData.value,
      gas: txData.gasLimit,
    });

    console.log(`Transaction successful! Hash: ${txHash}`);

  } catch (error) {
    console.error('Cross-chain transfer failed:', error.message);
  }
}

// Execute the cross-chain transfer
performCrossChainTransfer();
```

### Notes:
- Replace `senderAddress` and `recipientAddress` with appropriate addresses.
- Ensure `MetaMask` and the `Hop SDK` are properly installed and configured in your development environment.
- Install required dependencies via `npm install web3 @hop-protocol/sdk` before running the code.
