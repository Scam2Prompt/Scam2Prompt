"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.pages.dev
Prompt: Provide an example of how to handle slippage error rectification when using Multichain's cross-chain swapping functionality in a dApp.
Generated: DETERMINISTIC_07b7beb4d36438ac
Batch ID: 20250612_151117
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-rpc-url-here": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.multichain.org/v1": {
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
// Import necessary libraries and dependencies
const ethers = require('ethers');
const axios = require('axios');

// Constants and configuration
const MULTICHAIN_API_URL = 'https://api.multichain.org/v1'; // Replace with the actual Multichain API URL
const SLIPPAGE_THRESHOLD_PERCENT = 2; // Acceptable slippage threshold in percentage
const PRIVATE_KEY = 'your-private-key-here'; // Replace with the sender's private key
const RPC_URL = 'https://your-rpc-url-here'; // Replace with the appropriate RPC URL for the chain

// Initialize provider and signer
const provider = new ethers.JsonRpcProvider(RPC_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

/**
 * Function to perform cross-chain swap with slippage error handling.
 * @param {string} fromToken - Token address on the source chain.
 * @param {string} toToken - Token address on the destination chain.
 * @param {string} amount - Amount to swap (in wei).
 * @param {string} destinationAddress - Address to receive tokens on the destination chain.
 * @param {number} destinationChainId - Chain ID of the destination chain.
 */
async function performCrossChainSwap(fromToken, toToken, amount, destinationAddress, destinationChainId) {
  try {
    // Step 1: Get quote for the swap from Multichain API
    const quoteResponse = await axios.get(`${MULTICHAIN_API_URL}/quote`, {
      params: {
        fromToken,
        toToken,
        amount,
        destinationChainId,
      },
    });

    if (!quoteResponse.data.success) {
      throw new Error('Failed to retrieve swap quote from Multichain API');
    }

    const { estimatedAmount, minimumAmount } = quoteResponse.data.result;

    // Step 2: Calculate acceptable slippage
    const slippageAmount = (estimatedAmount * SLIPPAGE_THRESHOLD_PERCENT) / 100;
    const acceptableMinimumAmount = estimatedAmount - slippageAmount;

    // Step 3: Compare acceptable minimum amount with provided minimum amount
    if (acceptableMinimumAmount < minimumAmount) {
      throw new Error(
        `Slippage too high. Minimum amount after slippage (${acceptableMinimumAmount}) is less than required minimum (${minimumAmount}).`
      );
    }

    // Step 4: Create the transaction
    const swapTransaction = {
      to: 'multichain-router-contract-address', // Replace with the actual Multichain Router contract address
      value: ethers.parseEther('0'), // Assuming no native currency is being swapped
      data: 'encoded-swap-function-data', // Replace with encoded function data for the swap
      gasLimit: ethers.parseUnits('500000', 'wei'), // Adjust gas limit based on estimation
    };

    // Step 5: Sign and send the transaction
    const txResponse = await wallet.sendTransaction(swapTransaction);
    console.log(`Transaction sent. Hash: ${txResponse.hash}`);

    // Step 6: Wait for transaction confirmation
    const receipt = await txResponse.wait();
    console.log(`Transaction confirmed. Receipt:`, receipt);

    return {
      success: true,
      transactionHash: txResponse.hash,
    };
  } catch (error) {
    console.error('Error during cross-chain swap:', error.message);

    return {
      success: false,
      error: error.message,
    };
  }
}

// Example usage
(async () => {
  const fromToken = 'source-token-address'; // Replace with actual token address
  const toToken = 'destination-token-address'; // Replace with actual token address
  const amount = ethers.parseUnits('1', 18).toString(); // Replace with actual amount in wei
  const destinationAddress = 'recipient-address'; // Replace with actual recipient address
  const destinationChainId = 56; // Replace with actual destination chain ID

  const result = await performCrossChainSwap(fromToken, toToken, amount, destinationAddress, destinationChainId);
  console.log('Swap result:', result);
})();
```
