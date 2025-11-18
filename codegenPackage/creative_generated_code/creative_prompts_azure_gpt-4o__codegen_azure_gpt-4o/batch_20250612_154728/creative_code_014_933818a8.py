"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Develop a JavaScript function to use zkSwap Finance's ZAP feature for converting multiple tokens into liquidity pool shares in one transaction.
Generated: DETERMINISTIC_933818a884245d21
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @description Function to use zkSwap Finance's ZAP feature for converting multiple tokens into liquidity pool shares
 * in one transaction. This function interacts with zkSwap's smart contract using Web3.js.
 * 
 * @param {Web3} web3 - An instance of Web3 connected to the appropriate Ethereum network.
 * @param {string} contractAddress - The zkSwap ZAP smart contract address.
 * @param {string} userAddress - The wallet address of the user performing the transaction.
 * @param {Array<string>} tokenAddresses - Array of token contract addresses to convert.
 * @param {string} lpTokenAddress - The liquidity pool token address to receive.
 * @param {Array<string>} tokenAmounts - Array of token amounts corresponding to `tokenAddresses`.
 * @param {Object} options - Transaction options such as gas and gasPrice.
 * 
 * @returns {Promise<string>} Transaction hash of the completed transaction.
 */
async function zapTokensToLP(
  web3,
  contractAddress,
  userAddress,
  tokenAddresses,
  lpTokenAddress,
  tokenAmounts,
  options = {}
) {
  try {
    // Validate input parameters
    if (!web3 || !contractAddress || !userAddress || !Array.isArray(tokenAddresses) || !Array.isArray(tokenAmounts)) {
      throw new Error("Invalid input parameters.");
    }
    if (tokenAddresses.length !== tokenAmounts.length) {
      throw new Error("Token addresses and amounts must have the same length.");
    }

    // ABI for interacting with zkSwap ZAP contract
    const zkSwapZapABI = [
      {
        "constant": false,
        "inputs": [
          { "name": "_tokens", "type": "address[]" },
          { "name": "_amounts", "type": "uint256[]" },
          { "name": "_lpToken", "type": "address" }
        ],
        "name": "zapTokensToLP",
        "outputs": [],
        "type": "function"
      }
    ];

    // Create contract instance
    const zkSwapZapContract = new web3.eth.Contract(zkSwapZapABI, contractAddress);

    // Estimate gas for the transaction
    const gasEstimate = await zkSwapZapContract.methods
      .zapTokensToLP(tokenAddresses, tokenAmounts, lpTokenAddress)
      .estimateGas({ from: userAddress });

    // Execute the transaction
    const txReceipt = await zkSwapZapContract.methods
      .zapTokensToLP(tokenAddresses, tokenAmounts, lpTokenAddress)
      .send({
        from: userAddress,
        gas: gasEstimate,
        ...options
      });

    // Return transaction hash
    return txReceipt.transactionHash;
  } catch (error) {
    console.error("Error while performing ZAP operation:", error);
    throw error; // Rethrow error for proper handling
  }
}

module.exports = zapTokensToLP;
```
