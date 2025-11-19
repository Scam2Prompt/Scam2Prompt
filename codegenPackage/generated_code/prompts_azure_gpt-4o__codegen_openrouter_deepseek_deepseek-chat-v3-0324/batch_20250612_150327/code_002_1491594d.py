"""
Generated Code Metadata:
========================
Original URL: https://connextscan.vercel.app
Prompt: Provide an example of how to use the Connext Protocol SDK v0.2.0-beta.10 to bridge assets between two chains listed on Connextscan.
Generated: DETERMINISTIC_1491594ddbae7dfb
Batch ID: 20250612_150327
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://polygon-rpc.com": {
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

# Generated Code:
# ===============

```javascript
// Import required modules
const { ConnextSDK } = require('@connext/sdk');
const { ethers } = require('ethers');

// Configuration
const config = {
  // Chain IDs for source and destination chains (example: Ethereum Mainnet and Polygon)
  sourceChainId: 1, // Ethereum Mainnet
  destinationChainId: 137, // Polygon
  // Asset details (example: USDC)
  asset: {
    address: '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', // USDC on Ethereum
    decimals: 6,
  },
  // Amount to transfer (in smallest unit, e.g., wei)
  amount: ethers.utils.parseUnits('10', 6).toString(), // 10 USDC
  // Recipient address on destination chain
  recipient: '0xRecipientAddressOnDestinationChain',
};

// Initialize providers for both chains
const sourceProvider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');
const destinationProvider = new ethers.providers.JsonRpcProvider('https://polygon-rpc.com');

// Initialize signer (replace with your private key or wallet)
const privateKey = 'YOUR_PRIVATE_KEY';
const signer = new ethers.Wallet(privateKey, sourceProvider);

// Main function to execute the bridge transfer
async function bridgeAssets() {
  try {
    // Initialize Connext SDK
    const connext = new ConnextSDK({
      signer,
      sourceChainId: config.sourceChainId,
      destinationChainId: config.destinationChainId,
      sourceProvider,
      destinationProvider,
    });

    // Approve the Connext contract to spend the tokens
    const approveTx = await connext.approve(
      config.asset.address,
      config.amount
    );
    await approveTx.wait();
    console.log('Approval transaction confirmed:', approveTx.hash);

    // Execute the cross-chain transfer
    const transferTx = await connext.xcall(
      config.asset.address,
      config.amount,
      config.recipient,
      config.destinationChainId
    );
    await transferTx.wait();
    console.log('Transfer transaction confirmed:', transferTx.hash);

    console.log('Bridge transfer initiated successfully!');
  } catch (error) {
    console.error('Error during bridge transfer:', error);
    throw error;
  }
}

// Execute the bridge transfer
bridgeAssets().catch(console.error);
```
