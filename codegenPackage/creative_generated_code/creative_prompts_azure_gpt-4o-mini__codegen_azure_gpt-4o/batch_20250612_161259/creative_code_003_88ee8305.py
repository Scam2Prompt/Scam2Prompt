"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ostpp.ru
Prompt: Generate a sample transaction flow using Hop Protocol to move assets from Ethereum to Polygon, highlighting the use of relayers.
Generated: DETERMINISTIC_88ee83058d73f25e
Batch ID: 20250612_161259
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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

```javascript
// Import required libraries and dependencies
// Ensure you have installed ethers.js and Hop SDK: `npm install ethers @hop-protocol/sdk`
const { Hop } = require('@hop-protocol/sdk');
const { ethers } = require('ethers');

// Async function to execute the transaction flow
async function transferAssetsToPolygon() {
  try {
    // Initialize ethers provider (Ethereum mainnet)
    const provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'); // Replace with your Infura project ID

    // Signer for managing transactions (Make sure the private key is securely stored)
    const privateKey = 'YOUR_PRIVATE_KEY'; // Replace with your private key
    const signer = new ethers.Wallet(privateKey, provider);

    // Initialize Hop Protocol SDK
    const hop = new Hop('mainnet'); // Use 'mainnet' for production, 'goerli' for testnet

    // Define transaction details
    const chainFrom = 'ethereum'; // Source chain
    const chainTo = 'polygon'; // Destination chain
    const token = 'USDC'; // Asset to be transferred
    const amount = ethers.utils.parseUnits('100', 6); // 100 USDC, ensure correct decimal places for the token

    // Get the bridge instance for USDC
    const usdcBridge = hop.bridge(token);

    // Estimate the amount received after fees
    const amountReceived = await usdcBridge.getAmountReceived(chainFrom, chainTo, amount);

    console.log(`Estimated amount received on ${chainTo}:`, ethers.utils.formatUnits(amountReceived, 6));

    // Build transaction parameters
    const txOptions = {
      amount, // Amount to transfer
      chainFrom, // Source chain
      chainTo, // Destination chain
      token, // Token to transfer
      signer, // Signer for transaction
      relayerFee: ethers.utils.parseUnits('1', 6), // Optional: Specify relayer fee (if required by relayers)
    };

    // Execute the transfer using Hop Protocol
    const tx = await usdcBridge.send(txOptions);

    console.log('Transaction submitted:', tx.hash);

    // Wait for the transaction confirmation
    const receipt = await tx.wait();

    console.log('Transaction confirmed:', receipt.transactionHash);
  } catch (error) {
    // Catch and log any errors during the process
    console.error('Error during asset transfer:', error.message || error);
  }
}

// Execute the transfer flow
transferAssetsToPolygon();
```

**Notes for Deployment:**
- Replace `YOUR_INFURA_PROJECT_ID` with your real Infura project ID.
- Replace `YOUR_PRIVATE_KEY` with your wallet's private key (use environment variables or secure vaults to store sensitive data).
- Ensure the Hop SDK version matches the API used above (`npm install @hop-protocol/sdk`).
- Add more robust error handling and logging based on production requirements.
