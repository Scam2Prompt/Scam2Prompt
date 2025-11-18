"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.portal-bridge.com
Prompt: Create a script to integrate the Portal Token Bridge into a decentralized application (dApp) for seamless cross-chain USDC transfers.
Generated: DETERMINISTIC_98b561b3dfaa0e38
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// portal-token-bridge.js

/**
 * Portal Token Bridge Integration for seamless cross-chain USDC transfers.
 * 
 * This script connects a decentralized application (dApp) to the Portal Token Bridge,
 * enabling USDC transfers between supported blockchains.
 *
 * Dependencies: ethers.js for Ethereum-related operations and a Portal Token Bridge SDK.
 */

// Import required libraries
const { ethers } = require('ethers');
const { PortalBridgeSDK } = require('@portal-bridge/sdk'); // Hypothetical SDK for the Portal Token Bridge
require('dotenv').config(); // Load environment variables

// Configuration
const config = {
  sourceChain: 'ethereum',
  destinationChain: 'solana',
  tokenAddress: process.env.USDC_CONTRACT_ADDRESS, // USDC contract address on source chain
  portalBridgeAddress: process.env.PORTAL_BRIDGE_ADDRESS, // Portal Bridge contract address
  privateKey: process.env.PRIVATE_KEY, // Wallet private key
  rpcUrl: process.env.RPC_URL, // RPC endpoint for source chain
  destinationRpcUrl: process.env.DESTINATION_RPC_URL // RPC endpoint for destination chain
};

// Initialize the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider(config.rpcUrl);

// Initialize the signer for transactions
const signer = new ethers.Wallet(config.privateKey, provider);

// Initialize the Portal Bridge SDK
const portalBridge = new PortalBridgeSDK({
  sourceChain: config.sourceChain,
  destinationChain: config.destinationChain,
  rpcUrl: config.rpcUrl,
  destinationRpcUrl: config.destinationRpcUrl
});

/**
 * Function to transfer USDC from source chain to destination chain.
 * @param {string} amount - Amount of USDC to transfer (in smallest units, e.g., wei for Ethereum).
 * @param {string} destinationAddress - Recipient address on the destination chain.
 */
async function transferUSDC(amount, destinationAddress) {
  try {
    console.log('Initiating cross-chain USDC transfer...');

    // Check the balance of the sender to ensure sufficient funds
    const usdcContract = new ethers.Contract(
      config.tokenAddress,
      [
        'function balanceOf(address owner) view returns (uint256)',
        'function approve(address spender, uint256 amount) returns (bool)'
      ],
      signer
    );

    const balance = await usdcContract.balanceOf(signer.address);
    if (balance.lt(amount)) {
      throw new Error('Insufficient USDC balance for transfer.');
    }

    console.log(`USDC balance verified: ${ethers.utils.formatUnits(balance, 6)} USDC`);

    // Approve the Portal Bridge contract to spend USDC
    const approveTx = await usdcContract.approve(config.portalBridgeAddress, amount);
    await approveTx.wait();

    console.log('Portal Bridge contract approved for USDC transfer.');

    // Execute the cross-chain transfer using the Portal Bridge SDK
    const transferTx = await portalBridge.transfer({
      fromAddress: signer.address,
      toAddress: destinationAddress,
      tokenAddress: config.tokenAddress,
      amount
    });

    console.log('Cross-chain transfer initiated:', transferTx);

    // Wait for the transaction to be confirmed
    const receipt = await provider.waitForTransaction(transferTx.hash);
    console.log('Transfer transaction confirmed:', receipt);

    console.log('USDC transfer completed successfully.');
  } catch (error) {
    console.error('Error occurred during cross-chain transfer:', error.message);
    // Log additional details for debugging purposes
    console.error(error);
  }
}

// Example usage (Replace with actual values for production)
(async () => {
  const amountToTransfer = ethers.utils.parseUnits('100', 6); // 100 USDC
  const recipientAddressOnDestinationChain = 'RecipientAddressHere';

  await transferUSDC(amountToTransfer, recipientAddressOnDestinationChain);
})();
```

### Notes:
- Set the environment variables in a `.env` file (`USDC_CONTRACT_ADDRESS`, `PORTAL_BRIDGE_ADDRESS`, `PRIVATE_KEY`, `RPC_URL`, `DESTINATION_RPC_URL`) for production.
- Ensure the Portal Bridge SDK is properly installed and configured (`@portal-bridge/sdk` is a placeholder for the actual SDK package name).
