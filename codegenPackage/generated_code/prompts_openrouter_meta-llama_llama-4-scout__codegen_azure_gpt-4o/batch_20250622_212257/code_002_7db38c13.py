"""
Generated Code Metadata:
========================
Original URL: https://msk-rk.ru
Prompt: Explain how to integrate Hop Protocol with MetaMask for seamless token transfers between different blockchain networks.
Generated: DETERMINISTIC_7db38c133306c77e
Batch ID: 20250622_212257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers'); // Ethereum library for interacting with the blockchain
const hop = require('@hop-protocol/sdk'); // Hop Protocol SDK for cross-chain token transfers

// Configuration constants
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura project ID
const HOP_NETWORK = 'mainnet'; // Hop Protocol network (e.g., 'mainnet', 'goerli')
const TOKEN = 'USDC'; // Token to transfer (e.g., 'USDC', 'DAI', 'ETH')
const SOURCE_CHAIN = 'ethereum'; // Source chain (e.g., 'ethereum', 'polygon', 'optimism')
const DESTINATION_CHAIN = 'polygon'; // Destination chain (e.g., 'ethereum', 'polygon', 'optimism')

// Initialize provider and signer for MetaMask
async function initializeMetaMask() {
  if (!window.ethereum) {
    throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
  }

  // Request account access
  await window.ethereum.request({ method: 'eth_requestAccounts' });

  // Create a provider and signer using MetaMask
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const signer = provider.getSigner();

  return { provider, signer };
}

// Perform token transfer using Hop Protocol
async function transferTokens(amount) {
  try {
    // Initialize MetaMask provider and signer
    const { provider, signer } = await initializeMetaMask();

    // Initialize Hop SDK
    const hopSdk = new hop.Hop({
      network: HOP_NETWORK,
      signer: signer,
    });

    // Get the bridge instance for the specified token
    const bridge = hopSdk.bridge(TOKEN);

    // Convert the amount to the appropriate token decimals
    const tokenDecimals = await bridge.getTokenDecimals(SOURCE_CHAIN);
    const amountInWei = ethers.utils.parseUnits(amount.toString(), tokenDecimals);

    // Perform the transfer
    const tx = await bridge.send({
      amount: amountInWei, // Amount to transfer
      sourceChain: SOURCE_CHAIN, // Source chain
      destinationChain: DESTINATION_CHAIN, // Destination chain
      recipient: await signer.getAddress(), // Recipient address (default: sender's address)
    });

    console.log('Transaction sent:', tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log('Transaction confirmed:', receipt.transactionHash);

    return receipt;
  } catch (error) {
    console.error('Error during token transfer:', error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const amountToTransfer = 10; // Amount of tokens to transfer
    const receipt = await transferTokens(amountToTransfer);
    console.log('Token transfer successful:', receipt);
  } catch (error) {
    console.error('Token transfer failed:', error.message);
  }
})();
```

### Notes:
- Replace `your-infura-project-id` with your actual Infura project ID.
- Ensure you have installed the required dependencies (`ethers` and `@hop-protocol/sdk`) using npm or yarn:
  ```bash
  npm install ethers @hop-protocol/sdk
  ```
- This code assumes the user has MetaMask installed and configured.
- Error handling is included to catch and log issues during the token transfer process.
