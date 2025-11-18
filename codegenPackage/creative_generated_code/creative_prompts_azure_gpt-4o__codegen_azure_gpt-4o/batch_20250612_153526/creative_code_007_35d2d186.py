"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asd-45l.pages.dev
Prompt: Create a guide for developers participating in a hackathon using Safe CORE tools, including examples of integrating the Protocol Kit and Relay Kit.
Generated: DETERMINISTIC_35d2d1865a467342
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Hackathon Developer Guide: Safe CORE Tools Integration
 *
 * This guide demonstrates how to integrate Safe's Protocol Kit and Relay Kit.
 * The code includes setup, transaction creation, and relay execution.
 * Ensure you have installed the required dependencies: `@safe-global/protocol-kit` and `@safe-global/relay-kit`.
 *
 * Install the dependencies:
 * npm install @safe-global/protocol-kit @safe-global/relay-kit ethers dotenv
 */

require('dotenv').config(); // Load environment variables from .env
const { SafeFactory, SafeAccountConfig } = require('@safe-global/protocol-kit');
const { EthersAdapter } = require('@safe-global/protocol-kit');
const { GelatoRelay, SponsoredRelayResponse } = require('@safe-global/relay-kit');
const { ethers } = require('ethers');

/**
 * Environment Variables (Ensure these are set in your .env file)
 * - PRIVATE_KEY: Your wallet's private key
 * - RPC_URL: RPC endpoint for the blockchain network
 * - RELAY_API_KEY: Gelato Relay API key
 */

// Constants
const RELAY_API_KEY = process.env.RELAY_API_KEY;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const RPC_URL = process.env.RPC_URL;

// Ensure all environment variables are provided
if (!PRIVATE_KEY || !RPC_URL || !RELAY_API_KEY) {
  throw new Error('Missing environment variables. Please check your .env file.');
}

/**
 * Initialize Ethers.js Provider and Signer
 */
const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
const signer = new ethers.Wallet(PRIVATE_KEY, provider);

/**
 * Initialize Safe Protocol Kit
 */
async function initializeSafe() {
  const ethAdapter = new EthersAdapter({
    ethers,
    signer,
  });

  const safeFactory = await SafeFactory.create({ ethAdapter });

  // Configure the Safe account
  const safeAccountConfig = {
    owners: [signer.address], // Add your wallet address as the owner
    threshold: 1, // Number of confirmations required
  };

  console.log('Deploying Safe...');
  const safe = await safeFactory.deploySafe({ safeAccountConfig });
  console.log('Safe deployed:', safe.getAddress());

  return safe;
}

/**
 * Create and Execute a Transaction using Gelato Relay
 */
async function relayTransaction(safeAddress) {
  const gelatoRelay = new GelatoRelay();

  // Example transaction: Sending funds from Safe to another address
  const targetAddress = '0x1234567890abcdef1234567890abcdef12345678'; // Replace with recipient address
  const transferAmount = ethers.utils.parseEther('0.01'); // 0.01 ETH

  const safeTransactionData = {
    to: targetAddress,
    value: transferAmount.toString(),
    data: '0x',
  };

  console.log('Relaying transaction...');
  try {
    const relayResponse = await gelatoRelay.sponsoredCallERC2771(
      {
        target: safeAddress,
        data: safeTransactionData,
        chainId: await provider.getNetwork().then((network) => network.chainId),
      },
      RELAY_API_KEY
    );

    console.log('Transaction relayed successfully:', relayResponse.taskId);
  } catch (error) {
    console.error('Failed to relay transaction:', error.message);
  }
}

/**
 * Main Function to Run the Guide
 */
async function main() {
  console.log('Initializing Safe...');
  const safe = await initializeSafe();

  console.log('Relaying transaction via Gelato...');
  await relayTransaction(safe.getAddress());
}

// Execute the script
main().catch((error) => {
  console.error('Error in hackathon guide script:', error.message);
  process.exit(1);
});
```

### Notes:
1. To run the code, create a `.env` file with your `PRIVATE_KEY`, `RPC_URL`, and `RELAY_API_KEY`.
2. Install necessary dependencies using `npm install @safe-global/protocol-kit @safe-global/relay-kit ethers dotenv`. 
3. Adjust transaction parameters (`to`, value, etc.) as per your requirements.
