"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Explain how to use Hop Protocol's native token, HOP, for paying transaction fees in a cross-chain transfer, and provide a code snippet demonstrating this functionality.
Generated: DETERMINISTIC_201523f07a7f24af
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example code demonstrating how to use Hop Protocol's native token (HOP)
 * for paying transaction fees in a cross-chain transfer.
 *
 * Prerequisites:
 * - Install the Hop SDK: `npm install @hop-protocol/sdk`
 * - Ensure you have a wallet and some HOP tokens in the source chain
 * - Set up environment variables for your private keys securely
 */

const { Hop } = require('@hop-protocol/sdk');
const ethers = require('ethers');

/**
 * Configuration variables
 * Replace with your own values for production use.
 */
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Your wallet's private key (set securely)
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID; // Infura project ID for Ethereum provider
const SOURCE_CHAIN = 'ethereum'; // Source chain (e.g., Ethereum)
const DESTINATION_CHAIN = 'polygon'; // Destination chain (e.g., Polygon)
const TOKEN = 'USDC'; // Token to be transferred (e.g., USDC)

/**
 * Initialize wallet and Hop SDK
 */
async function init() {
  try {
    // Set up Ethereum provider
    const provider = new ethers.providers.InfuraProvider(SOURCE_CHAIN, INFURA_PROJECT_ID);

    // Create wallet instance
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

    // Initialize Hop SDK
    const hop = new Hop('mainnet');

    return { hop, wallet };
  } catch (error) {
    console.error('Initialization failed:', error);
    throw error;
  }
}

/**
 * Execute cross-chain transfer using HOP token for transaction fees
 * @param hop - Hop SDK instance
 * @param wallet - Wallet instance
 */
async function executeTransfer(hop, wallet) {
  try {
    // Get bridge instance for the specified token
    const bridge = hop.bridge(TOKEN);

    // Define transfer parameters
    const amount = ethers.utils.parseUnits('100', 6); // Amount to transfer (100 USDC, adjust decimals as needed)
    const recipient = '0xRecipientAddressHere'; // Recipient address on destination chain

    // Perform the transfer
    console.log('Executing transfer...');
    const tx = await bridge.send({
      amount,
      recipient,
      sourceChain: SOURCE_CHAIN,
      destinationChain: DESTINATION_CHAIN,
      account: wallet.address,
      bonderFee: ethers.utils.parseUnits('1', 18), // Fee paid in HOP (adjust value as required)
      token: TOKEN,
    });

    console.log('Transaction submitted:', tx.hash);

    // Wait for transaction confirmation
    const receipt = await tx.wait();
    console.log('Transaction confirmed:', receipt.transactionHash);
  } catch (error) {
    console.error('Transfer failed:', error);
    throw error;
  }
}

/**
 * Main function to execute the transfer.
 */
(async () => {
  try {
    console.log('Initializing Hop Protocol SDK and wallet...');
    const { hop, wallet } = await init();

    console.log('Starting transfer...');
    await executeTransfer(hop, wallet);

    console.log('Transfer completed successfully.');
  } catch (error) {
    console.error('An error occurred:', error);
  }
})();
```
