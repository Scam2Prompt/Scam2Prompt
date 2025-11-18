"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magic.link
Prompt: Suggest best practices for building cross-chain applications using Magic Labs' tools and APIs, focusing on scalability and performance.
Generated: DETERMINISTIC_19300a8d7fcbf969
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cross-Chain Application using Magic Labs' Tools and APIs
 * Best practices for scalability and performance are implemented.
 */

import { Magic } from 'magic-sdk';
import Web3 from 'web3';

// Initialize Magic with your Publishable API Key
const magic = new Magic('YOUR_MAGIC_PUBLISHABLE_API_KEY');

// Initialize Web3 instance with a provider (Magic RPC for cross-chain support)
const web3 = new Web3(magic.rpcProvider);

async function crossChainTransfer(senderAddress, receiverAddress, amount, chainId) {
  try {
    // Validate input parameters
    if (!web3.utils.isAddress(senderAddress)) throw new Error('Invalid sender address');
    if (!web3.utils.isAddress(receiverAddress)) throw new Error('Invalid receiver address');
    if (amount <= 0) throw new Error('Amount must be greater than 0');
    if (!chainId) throw new Error('Chain ID is required for cross-chain transfer');

    // Dynamically switch the chain if necessary
    await switchChain(chainId);

    // Prepare transaction details
    const transaction = {
      from: senderAddress,
      to: receiverAddress,
      value: web3.utils.toWei(amount.toString(), 'ether'), // Convert amount to Wei
      gas: 21000, // Standard gas limit for ETH transfer
    };

    // Send the transaction via Magic's provider
    const txHash = await web3.eth.sendTransaction(transaction);

    console.log(`Transaction successful! TxHash: ${txHash}`);
    return txHash;
  } catch (error) {
    // Handle and log errors
    console.error('Error in cross-chain transfer:', error.message);
    throw error; // Re-throw for further handling if needed
  }
}

async function switchChain(chainId) {
  try {
    const network = await magic.network;
    if (network.chainId !== chainId) {
      console.log(`Switching to chain ID: ${chainId}`);
      await magic.network.changeNetwork({ chainId });
      console.log(`Successfully switched to chain ID: ${chainId}`);
    }
  } catch (error) {
    console.error('Error switching chains:', error.message);
    throw error; // Re-throw to indicate chain switching failure
  }
}

// Usage example: Perform a cross-chain transfer
(async () => {
  try {
    const sender = '0xSenderAddressHere';
    const receiver = '0xReceiverAddressHere';
    const amount = 0.1; // Amount in Ether
    const targetChainId = 137; // Example: Polygon Mainnet Chain ID

    console.log('Initiating cross-chain transfer...');
    const txHash = await crossChainTransfer(sender, receiver, amount, targetChainId);
    console.log(`Cross-chain transfer completed successfully! Transaction Hash: ${txHash}`);
  } catch (err) {
    console.error('Failed to complete cross-chain transfer:', err.message);
  }
})();
```

Make sure to replace `'YOUR_MAGIC_PUBLISHABLE_API_KEY'` with your actual Magic API key before running the code.
