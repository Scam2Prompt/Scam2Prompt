"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portalbridge.dev
Prompt: Provide an example of integrating Portal Token Bridge services into a decentralized application for cross-chain USDC transfers.
Generated: DETERMINISTIC_ab7e5cfb836aeca3
Batch ID: 20250612_155032
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.portalbridge.com/v1": {
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
const ethers = require('ethers');
const axios = require('axios');

// Configuration
const PORTAL_TOKEN_BRIDGE_API = 'https://api.portalbridge.com/v1'; // Replace with actual API endpoint
const SOURCE_CHAIN_ID = 1; // Example: Ethereum Mainnet (Chain ID 1)
const TARGET_CHAIN_ID = 56; // Example: Binance Smart Chain (Chain ID 56)
const USDC_ADDRESS = '0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'; // USDC contract address on Ethereum
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY'; // Replace with your wallet's private key
const PROVIDER_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Ethereum provider URL

// Initialize Ethereum provider and signer
const provider = new ethers.providers.JsonRpcProvider(PROVIDER_URL);
const signer = new ethers.Wallet(PRIVATE_KEY, provider);

// Portal Token Bridge Transfer function
async function transferUSDC(amount, recipientAddress) {
  try {
    // Step 1: Validate the recipient address
    if (!ethers.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address');
    }

    // Step 2: Get the Portal Token Bridge quote
    const quoteResponse = await axios.post(`${PORTAL_TOKEN_BRIDGE_API}/quote`, {
      sourceChainId: SOURCE_CHAIN_ID,
      targetChainId: TARGET_CHAIN_ID,
      tokenAddress: USDC_ADDRESS,
      amount,
      recipientAddress,
    });

    if (quoteResponse.status !== 200 || !quoteResponse.data) {
      throw new Error('Failed to fetch quote from Portal Token Bridge API');
    }

    const { quoteId, fee, targetTokenAddress } = quoteResponse.data;

    console.log('Quote obtained successfully:', quoteResponse.data);

    // Step 3: Approve USDC for transfer
    const usdcContract = new ethers.Contract(
      USDC_ADDRESS,
      [
        'function approve(address spender, uint256 amount) public returns (bool)',
      ],
      signer
    );

    const approveTx = await usdcContract.approve(targetTokenAddress, amount);
    await approveTx.wait();
    console.log('USDC approved successfully');

    // Step 4: Initiate the bridge transfer
    const bridgeContract = new ethers.Contract(
      targetTokenAddress,
      [
        'function transferWithQuote(uint256 amount, uint256 fee, bytes32 quoteId) public',
      ],
      signer
    );

    const transferTx = await bridgeContract.transferWithQuote(
      amount,
      fee,
      quoteId
    );
    await transferTx.wait();
    console.log('USDC transferred successfully');

    return `Transfer successful. Transaction hash: ${transferTx.hash}`;
  } catch (error) {
    console.error('Error during USDC transfer:', error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const result = await transferUSDC(
      ethers.utils.parseUnits('100', 6), // Amount to transfer (100 USDC in 6 decimals)
      '0xRecipientAddressHere' // Replace with the recipient's address on the target chain
    );
    console.log(result);
  } catch (error) {
    console.error('Transfer failed:', error.message);
  }
})();
```

This code demonstrates how to integrate USDC cross-chain transfers using the Portal Token Bridge API. Be sure to replace placeholder values like `YOUR_PRIVATE_KEY`, `YOUR_INFURA_PROJECT_ID`, and `0xRecipientAddressHere` with actual values.
