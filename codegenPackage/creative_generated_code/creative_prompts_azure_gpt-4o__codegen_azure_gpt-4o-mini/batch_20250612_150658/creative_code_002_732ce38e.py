"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-ultra.org
Prompt: Generate code to implement token swaps using MetaMask's built-in "Swaps" feature, ensuring the best rates for Ethereum-based tokens.
Generated: DETERMINISTIC_732ce38e205b622d
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this feature.');
}

// Initialize Web3 and ethers.js
const web3 = new Web3(window.ethereum);
const provider = new ethers.providers.Web3Provider(window.ethereum);

// Function to swap tokens using the MetaMask Swaps feature
async function swapTokens(tokenIn, tokenOut, amountIn, slippage, recipient) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get signer to interact with the blockchain
        const signer = provider.getSigner();

        // Fetch the best swap route using the MetaMask API
        const swapRoute = await fetchSwapRoute(tokenIn, tokenOut, amountIn);

        // Calculate the minimum amount out based on slippage
        const amountOutMin = calculateMinAmountOut(swapRoute, slippage);

        // Create transaction object
        const transaction = {
            from: await signer.getAddress(),
            to: swapRoute.contractAddress,
            value: ethers.utils.parseUnits(amountIn.toString(), 'ether'), // Value if sending ETH
            gasLimit: ethers.utils.hexlify(100000), // Estimate gas limit
            data: swapRoute.data, // Transaction data from the swap route
        };

        // Send the transaction
        const txResponse = await signer.sendTransaction(transaction);
        console.log('Transaction sent:', txResponse);

        // Wait for transaction confirmation
        const txReceipt = await txResponse.wait();
        console.log('Transaction confirmed:', txReceipt);
    } catch (error) {
        console.error('An error occurred during the token swap:', error);
        alert(`Error: ${error.message}`);
    }
}

// Function to fetch the best swap route (to be implemented)
async function fetchSwapRoute(tokenIn, tokenOut, amountIn) {
    // Placeholder for API request to get swap route
    // This should be replaced with actual API call to a service like MetaMask Swaps
    return {
        contractAddress: '0xSwapContractAddress', // Example contract address
        data: '0xTransactionData' // Example transaction data
    };
}

// Function to calculate the minimum amount out based on slippage
function calculateMinAmountOut(swapRoute, slippage) {
    // Placeholder for calculating min amount out
    // Example: If swapRoute.amountOut is the expected amount, apply slippage
    const expectedAmountOut = ethers.utils.parseUnits('1.0', 'ether'); // Example expected amount
    const slippageAmount = expectedAmountOut.mul(slippage).div(100);
    return expectedAmountOut.sub(slippageAmount);
}

// Example usage of the swapTokens function
swapTokens('0xTokenInAddress', '0xTokenOutAddress', 1, 2, '0xYourAddress');
```

Make sure to replace placeholder values and implement the `fetchSwapRoute` function with an actual API call to retrieve the swap route data from MetaMask or another swaps service.
