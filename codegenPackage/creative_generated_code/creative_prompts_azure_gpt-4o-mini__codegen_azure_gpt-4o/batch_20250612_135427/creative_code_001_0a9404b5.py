"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-bridge-and-tx-hi-d503e2-offchain-labs.vercel.app
Prompt: Write a code snippet demonstrating how to implement the Retryables feature in an Arbitrum-based project.
Generated: DETERMINISTIC_0a9404b505ce9ea6
Batch ID: 20250612_135427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { providers, Wallet } = require("ethers");
const { L1ToL2MessageGasEstimator, EthBridger, getL2Network } = require("@arbitrum/sdk");

// Environment setup
require("dotenv").config();

// Constants
const L1_RPC_URL = process.env.L1_RPC_URL; // Your Layer 1 provider RPC URL
const L2_RPC_URL = process.env.L2_RPC_URL; // Your Layer 2 provider RPC URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key for signing transactions
const RECEIVER_ADDRESS = process.env.RECEIVER_ADDRESS; // Address on L2 to send funds
const DEPOSIT_AMOUNT = "0.01"; // ETH amount to deposit (in ether)

// Initialize providers and wallets
const l1Provider = new providers.JsonRpcProvider(L1_RPC_URL);
const l2Provider = new providers.JsonRpcProvider(L2_RPC_URL);
const wallet = new Wallet(PRIVATE_KEY, l1Provider);

async function main() {
  try {
    // Get L2 network details
    const l2Network = await getL2Network(l2Provider);

    // Initialize ETHBridger
    const ethBridger = new EthBridger(l2Network);

    // Estimate gas limits for retryable ticket creation
    const estimator = new L1ToL2MessageGasEstimator(l2Provider);
    const gasEstimate = await estimator.estimateGasLimits({
      from: wallet.address,
      to: RECEIVER_ADDRESS,
      l2CallValue: 0, // Amount to directly send to L2 contract
      excessFeeRefundAddress: wallet.address,
      callValueRefundAddress: wallet.address,
      data: "0x", // Empty data for a simple ETH transfer
    });

    // Log gas estimates for clarity
    console.log("Gas estimates:", gasEstimate);

    // Deposit ETH and create Retryable Ticket
    const depositTx = await ethBridger.deposit({
      amount: DEPOSIT_AMOUNT,
      l1Signer: wallet,
      destinationAddress: RECEIVER_ADDRESS,
      l2CallValue: 0, // Optional, for contract invocations on L2
      gasLimit: gasEstimate.gasLimit,
      maxSubmissionCost: gasEstimate.maxSubmissionCost,
      maxGas: gasEstimate.maxGas,
      excessFeeRefundAddress: wallet.address,
      callValueRefundAddress: wallet.address,
    });

    console.log("Deposit transaction sent:", depositTx.hash);

    // Wait for transaction confirmation
    const depositReceipt = await depositTx.wait();
    console.log("Deposit confirmed on L1:", depositReceipt.transactionHash);

    console.log("Retryable ticket created successfully.");
  } catch (error) {
    console.error("Error occurred while creating Retryable Ticket:", error);
  }
}

// Execute the function
main();
```
