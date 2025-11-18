"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portalbridge.dev
Prompt: Provide an example of integrating Portal Token Bridge services into a decentralized application for cross-chain USDC transfers.
Generated: DETERMINISTIC_ab7e5cfb836aeca3
Batch ID: 20250612_155032
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://wormhole-v2-api.testnet.certus.one": {
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
// Import required libraries
const { ethers } = require("ethers");
const { PortalTokenBridge } = require("@certusone/wormhole-sdk");

// Configuration
const WORMHOLE_RPC_URL = "https://wormhole-v2-api.testnet.certus.one"; // Replace with mainnet URL for production
const USDC_ADDRESS = "0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"; // USDC token address on source chain
const PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // User's wallet private key
const SOURCE_CHAIN_ID = 2; // Example: Ethereum Mainnet (ID: 1), Binance Smart Chain (ID: 56)
const TARGET_CHAIN_ID = 3; // Example: Polygon (ID: 137)

// Initialize provider and wallet
const provider = new ethers.providers.JsonRpcProvider(WORMHOLE_RPC_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Function to transfer USDC using Portal Token Bridge
async function transferUSDC(amount, targetAddress) {
    try {
        // Validate target address
        if (!ethers.utils.isAddress(targetAddress)) {
            throw new Error("Invalid target address");
        }

        // Create an instance of the Portal Token Bridge
        const bridge = new PortalTokenBridge(provider, wallet);

        // Check balance of the sender's wallet
        const balance = await bridge.getTokenBalance(USDC_ADDRESS);
        if (balance.lt(ethers.utils.parseUnits(amount.toString(), 6))) {
            throw new Error("Insufficient balance");
        }

        // Prepare the transaction
        const tx = await bridge.transfer(
            USDC_ADDRESS,
            ethers.utils.parseUnits(amount.toString(), 6),
            TARGET_CHAIN_ID,
            targetAddress
        );

        // Wait for the transaction to be mined
        const receipt = await tx.wait();
        console.log("Transaction successful:", receipt.transactionHash);
    } catch (error) {
        console.error("Error during USDC transfer:", error.message);
    }
}

// Example usage of the transferUSDC function
(async () => {
    const amountToTransfer = 10; // Amount of USDC to transfer
    const recipientAddress = "0xRecipientAddressHere"; // Replace with the recipient's address

    await transferUSDC(amountToTransfer, recipientAddress);
})();
```

Make sure to replace `YOUR_PRIVATE_KEY` and `0xRecipientAddressHere` with actual values before running the code.
