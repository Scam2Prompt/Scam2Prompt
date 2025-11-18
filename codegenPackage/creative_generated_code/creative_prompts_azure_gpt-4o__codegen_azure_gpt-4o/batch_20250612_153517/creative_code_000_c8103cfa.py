"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-feat-bridge-sdk-b50625-offchain-labs.vercel.app
Prompt: Write code using the Arbitrum Bridge SDK to transfer tokens from Ethereum to Arbitrum Sepolia, referencing the Stylus functionality.
Generated: DETERMINISTIC_c8103cfaae6b8580
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Arbitrum Bridge SDK
const { Bridge, L1ToL2MessageGasEstimator } = require("@arbitrum/sdk");
const { ethers } = require("ethers");

// Environment variables for sensitive data (recommended for production)
require('dotenv').config();

const main = async () => {
  // Set up provider and signer for Ethereum (L1) and Arbitrum Sepolia (L2)
  const l1Provider = new ethers.providers.JsonRpcProvider(process.env.ETHEREUM_RPC_URL); // Ethereum RPC URL
  const l2Provider = new ethers.providers.JsonRpcProvider(process.env.ARBITRUM_SEPOLIA_RPC_URL); // Arbitrum Sepolia RPC URL
  
  const l1Wallet = new ethers.Wallet(process.env.PRIVATE_KEY, l1Provider); // L1 signer
  const l2Wallet = new ethers.Wallet(process.env.PRIVATE_KEY, l2Provider); // L2 signer
  
  // Instantiate the Bridge object for interacting with the Arbitrum bridge
  const bridge = await Bridge.init(l1Wallet, l2Wallet);
  
  // Token and transfer details
  const tokenAddress = process.env.TOKEN_ADDRESS; // ERC20 token address on Ethereum
  const amount = ethers.utils.parseUnits("1.0", 18); // Amount to transfer (1 token, 18 decimals)

  try {
    // Approve the token for transfer through the bridge
    console.log("Approving token for transfer...");
    const approveTx = await bridge.approveToken(tokenAddress, amount);
    await approveTx.wait(); // Wait for approval to be mined
    console.log("Token approved successfully.");

    // Estimate L2 gas costs for the transfer
    console.log("Estimating L2 gas costs...");
    const gasEstimator = new L1ToL2MessageGasEstimator(l2Provider);
    const estimatedGas = await gasEstimator.estimateGas(tokenAddress, amount);
    console.log(`Estimated L2 gas cost: ${estimatedGas.toString()}`);

    // Initiate the token transfer
    console.log("Initiating token transfer...");
    const transferTx = await bridge.depositERC20({
      tokenAddress,
      amount,
      destinationWalletAddress: l2Wallet.address, // Receiver address on Arbitrum Sepolia
      l2CallValue: 0, // Amount of ETH to send to L2 (none for ERC20 transfer)
      maxGas: estimatedGas.maxGas,
      gasPriceBid: estimatedGas.gasPriceBid,
      maxSubmissionCost: estimatedGas.maxSubmissionCost,
    });
    await transferTx.wait(); // Wait for the transaction to be mined
    console.log("Token transfer initiated successfully.");

    // Wait for the L2 message to be executed (optional)
    console.log("Waiting for message execution on L2...");
    const l2Message = await transferTx.getL2Message();
    const status = await l2Message.waitUntilExecuted();
    console.log(`Message executed on L2 with status: ${status}`);
  } catch (error) {
    console.error("An error occurred during the token transfer:", error);
  }
};

// Execute the main function
main().catch((error) => {
  console.error("Fatal error during execution:", error);
  process.exit(1); // Exit the process with an error code
});
```
