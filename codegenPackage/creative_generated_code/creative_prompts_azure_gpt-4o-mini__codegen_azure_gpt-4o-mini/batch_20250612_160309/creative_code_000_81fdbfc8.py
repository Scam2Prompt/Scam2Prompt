"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lynexfenance.org
Prompt: How can I implement a token swap using Lynex's low slippage and AMM technology for efficient trading on the Linea blockchain?
Generated: DETERMINISTIC_81fdbfc84aabe30d
Batch ID: 20250612_160309
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.lynex.example.com/swap?tokenIn=${tokenIn}&tokenOut=${tokenOut}&amountIn=${amountIn}`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://linea.rpc.example.com": {
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
// Import necessary libraries and define constants
const { ethers } = require('ethers');
const axios = require('axios');

// Define the token swap function
async function tokenSwap(providerUrl, walletPrivateKey, tokenIn, tokenOut, amountIn, slippage) {
    // Connect to the Linea blockchain provider
    const provider = new ethers.providers.JsonRpcProvider(providerUrl);
    const wallet = new ethers.Wallet(walletPrivateKey, provider);

    // Validate input parameters
    if (!ethers.utils.isAddress(tokenIn) || !ethers.utils.isAddress(tokenOut)) {
        throw new Error('Invalid token addresses');
    }
    if (amountIn <= 0) {
        throw new Error('Amount in must be greater than zero');
    }
    if (slippage < 0 || slippage > 100) {
        throw new Error('Slippage must be between 0 and 100');
    }

    // Fetch the current price and calculate minimum amount out based on slippage
    const priceInfo = await getPriceInfo(tokenIn, tokenOut, amountIn);
    const amountOutMin = priceInfo.amountOut * (1 - slippage / 100);

    // Create a swap transaction
    const swapTransaction = {
        to: priceInfo.routerAddress,
        value: ethers.utils.parseEther('0'), // No ETH sent for token swaps
        data: priceInfo.swapData,
        gasLimit: ethers.utils.hexlify(100000), // Set a reasonable gas limit (can be adjusted)
        gasPrice: await provider.getGasPrice(),
    };

    try {
        // Send the transaction
        const txResponse = await wallet.sendTransaction(swapTransaction);
        console.log(`Transaction sent: ${txResponse.hash}`);

        // Wait for transaction confirmation
        const receipt = await txResponse.wait();
        console.log(`Transaction confirmed in block: ${receipt.blockNumber}`);
    } catch (error) {
        console.error('Transaction failed:', error);
    }
}

// Helper function to fetch price information from Lynex API
async function getPriceInfo(tokenIn, tokenOut, amountIn) {
    const apiUrl = `https://api.lynex.example.com/swap?tokenIn=${tokenIn}&tokenOut=${tokenOut}&amountIn=${amountIn}`;
    
    try {
        const response = await axios.get(apiUrl);
        if (response.data.success) {
            return {
                amountOut: response.data.amountOut,
                routerAddress: response.data.routerAddress,
                swapData: response.data.swapData,
            };
        } else {
            throw new Error('Failed to fetch price info');
        }
    } catch (error) {
        console.error('Error fetching price information:', error);
        throw error;
    }
}

// Example usage
const providerUrl = 'https://linea.rpc.example.com'; // Replace with actual RPC provider URL
const walletPrivateKey = 'YOUR_PRIVATE_KEY'; // Replace with the user's wallet private key
const tokenIn = '0xTokenInAddress'; // Replace with the input token address
const tokenOut = '0xTokenOutAddress'; // Replace with the output token address
const amountIn = 1; // Amount of tokenIn to swap
const slippage = 1; // Slippage tolerance in percentage

// Execute token swap
tokenSwap(providerUrl, walletPrivateKey, tokenIn, tokenOut, amountIn, slippage)
    .then(() => console.log('Token swap executed successfully'))
    .catch(error => console.error('Error during token swap:', error));
```

**Note**: Replace placeholders for the RPC provider URL, private key, and token addresses with actual values before executing the code. Additionally, ensure that the API URL for Lynex is correct and accessible.
