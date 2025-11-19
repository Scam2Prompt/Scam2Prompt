"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-feat-bridge-sdk-b50625-offchain-labs.vercel.app
Prompt: Can you provide an example of code that utilizes the Arbitrum token bridge SDK for transferring assets?
Generated: DETERMINISTIC_cbea463f431b6207
Batch ID: 20250612_162325
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://arb1.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is an example of clean, production-ready JavaScript/TypeScript code that uses the Arbitrum Token Bridge SDK to transfer assets:

```typescript
// Import necessary libraries
import { ethers } from "ethers";
import { L1ToL2MessageGasEstimator, Erc20Bridger } from "@arbitrum/sdk";

// Configuration: Ensure you replace these with actual values
const L1_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID";   // Replace with your L1 network RPC URL
const L2_RPC_URL = "https://arb1.arbitrum.io/rpc";                          // Replace with your L2 network RPC URL
const PRIVATE_KEY = "YOUR_PRIVATE_KEY";                                     // Replace with your private key
const L1_ERC20_ADDRESS = "0xYourL1TokenAddress";                           // Replace with the token's L1 contract address
const RECEIVER_ADDRESS = "0xReceiverAddressOnL2";                          // Replace with the L2 receiver address
const TRANSFER_AMOUNT = ethers.utils.parseUnits("10", 18);                 // Amount to transfer, adjust decimal units accordingly

// Main function to execute the token transfer
async function main() {
    try {
        // Initialize providers for L1 and L2
        const l1Provider = new ethers.providers.JsonRpcProvider(L1_RPC_URL);
        const l2Provider = new ethers.providers.JsonRpcProvider(L2_RPC_URL);

        // Initialize the wallet
        const wallet = new ethers.Wallet(PRIVATE_KEY, l1Provider);

        // Initialize the ERC20 bridger
        const erc20Bridger = new Erc20Bridger(l2Provider);

        console.log("Estimating gas costs for L1 → L2 transfer...");

        // Estimate the gas required for the transaction
        const gasEstimator = new L1ToL2MessageGasEstimator(l2Provider);
        const gasEstimate = await gasEstimator.estimateGas({
            from: wallet.address,
            to: RECEIVER_ADDRESS,
            tokenAddress: L1_ERC20_ADDRESS,
            amount: TRANSFER_AMOUNT,
        });

        console.log("Gas estimate:", gasEstimate);

        console.log("Initiating the token transfer...");

        // Execute the token transfer
        const tx = await erc20Bridger.deposit({
            l1Signer: wallet,
            l1TokenAddress: L1_ERC20_ADDRESS,
            amount: TRANSFER_AMOUNT,
            destinationAddress: RECEIVER_ADDRESS,
            gasOverride: gasEstimate,
        });

        console.log("Transaction submitted. Waiting for confirmation...");
        const receipt = await tx.wait();
        console.log("Transaction confirmed:", receipt);

        console.log("Token transfer successful!");
    } catch (error) {
        console.error("An error occurred during the token transfer:", error);
    }
}

// Execute the main function
main();
```

**Notes in Code Comments**:
1. Make sure to replace placeholder values (`YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, etc.) with actual values.
2. Always handle sensitive information securely (e.g., private keys).
3. The `TRANSFER_AMOUNT` assumes the token has 18 decimals; adjust accordingly for tokens with different decimal places.
4. Error handling is included to catch and log any issues during execution.

Make sure you have installed the required dependencies (`@arbitrum/sdk` and `ethers`) in your project:
```bash
npm install @arbitrum/sdk ethers
```
