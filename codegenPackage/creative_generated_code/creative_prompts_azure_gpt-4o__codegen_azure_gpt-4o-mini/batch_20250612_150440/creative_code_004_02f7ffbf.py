"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-bridge-and-tx-hi-d503e2-offchain-labs.vercel.app
Prompt: Create a tutorial-style script for developers to integrate the Arbitrum SDK into a DeFi project, highlighting L2 gas savings and retryable transactions.
Generated: DETERMINISTIC_02f7ffbf8cf8170f
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arb1.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");
const { ArbitrumSDK } = require("arbitrum-sdk");

// Define constants
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura project ID
const ARBITRUM_RPC_URL = "https://arb1.arbitrum.io/rpc"; // Arbitrum RPC URL
const PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key

// Initialize provider and wallet
const provider = new ethers.providers.JsonRpcProvider(ARBITRUM_RPC_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize the Arbitrum SDK
const sdk = new ArbitrumSDK({
    provider: provider,
    signer: wallet,
});

// Function to demonstrate gas savings on L2
async function demonstrateGasSavings() {
    try {
        // Fetch gas price on L1 and L2
        const l1GasPrice = await provider.getGasPrice(); // L1 gas price
        const l2GasPrice = await sdk.getGasPrice(); // L2 gas price

        console.log(`L1 Gas Price: ${ethers.utils.formatUnits(l1GasPrice, 'gwei')} Gwei`);
        console.log(`L2 Gas Price: ${ethers.utils.formatUnits(l2GasPrice, 'gwei')} Gwei`);
        
        const savings = l1GasPrice.sub(l2GasPrice);
        console.log(`Potential Gas Savings: ${ethers.utils.formatUnits(savings, 'gwei')} Gwei`);
    } catch (error) {
        console.error("Error fetching gas prices:", error);
    }
}

// Function to send a transaction with retryable feature
async function sendRetryableTransaction() {
    try {
        // Define transaction parameters
        const txParams = {
            to: "0xRecipientAddress", // Replace with the recipient address
            value: ethers.utils.parseEther("0.01"), // Amount to send
            gasLimit: 100000, // Estimated gas limit
        };

        // Send transaction and wait for confirmation
        const txResponse = await wallet.sendTransaction(txParams);
        console.log("Transaction sent! Hash:", txResponse.hash);

        // Wait for the transaction to be confirmed
        const receipt = await txResponse.wait();
        console.log("Transaction confirmed in block:", receipt.blockNumber);
    } catch (error) {
        console.error("Error sending transaction:", error);
    }
}

// Execute functions
(async () => {
    await demonstrateGasSavings();
    await sendRetryableTransaction();
})();
```

**Note:** Before running the script, ensure you replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, and `0xRecipientAddress` with actual values. Additionally, install the required dependencies using:
```bash
npm install ethers arbitrum-sdk
```
