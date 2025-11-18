"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.app
Prompt: Write a script to implement a cross-chain bridging solution using deBridge for transferring liquidity between Solana and Binance Smart Chain.
Generated: DETERMINISTIC_8ee573fcb15328e0
Batch ID: 20250612_151705
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
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
const deBridge = require("@debridge-finance/debridge-sdk");

// Configuration for Solana and Binance Smart Chain
const SOLANA_NETWORK = "https://api.mainnet-beta.solana.com";
const BSC_NETWORK = "https://bsc-dataseed.binance.org/";

// Setup providers for both networks
const solanaProvider = new deBridge.SolanaProvider(SOLANA_NETWORK);
const bscProvider = new ethers.providers.JsonRpcProvider(BSC_NETWORK);

// User wallet addresses and private keys (securely manage your keys)
const userWalletAddress = "YOUR_WALLET_ADDRESS"; // Replace with your wallet address
const userPrivateKey = "YOUR_PRIVATE_KEY"; // Replace with your private key

// Function to transfer liquidity from Solana to Binance Smart Chain
async function transferLiquidity(amount, fromChain, toChain) {
    try {
        // Validate parameters
        if (amount <= 0) {
            throw new Error("Transfer amount must be greater than zero.");
        }

        console.log(`Initiating transfer of ${amount} from ${fromChain} to ${toChain}.`);

        // Connect to the user's wallet
        const wallet = new ethers.Wallet(userPrivateKey, bscProvider);

        // Prepare transaction details
        const transaction = {
            from: userWalletAddress,
            to: toChain,
            value: ethers.utils.parseEther(amount.toString()), // Convert amount to Ether format
            gasLimit: 21000, // Set a reasonable gas limit
        };

        // Execute transfer
        const tx = await wallet.sendTransaction(transaction);
        console.log(`Transaction successful with hash: ${tx.hash}`);

        // Wait for transaction to be mined
        await tx.wait();
        console.log("Transaction mined successfully!");
    } catch (error) {
        console.error("Error while transferring liquidity:", error.message);
    }
}

// Example usage
(async () => {
    const amountToTransfer = 0.1; // Amount to transfer in Ether
    const fromChain = "Solana";
    const toChain = "Binance Smart Chain";

    // Call the transfer function
    await transferLiquidity(amountToTransfer, fromChain, toChain);
})();
```

**Note**: Replace `YOUR_WALLET_ADDRESS` and `YOUR_PRIVATE_KEY` with actual values. Ensure to manage your private key securely and not expose it in your code.
