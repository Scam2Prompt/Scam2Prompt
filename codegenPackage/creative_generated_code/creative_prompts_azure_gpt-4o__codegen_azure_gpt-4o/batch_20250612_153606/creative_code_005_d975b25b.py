"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Create a JavaScript function to calculate gas fees for minting NFTs on the Ethereum blockchain, referencing the minting process described on the Robots NFT Minting website.
Generated: DETERMINISTIC_d975b25b198c84ab
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate gas fees for minting NFTs on Ethereum.
 * 
 * This function estimates the gas fees required for minting NFTs based on the 
 * gas price (Gwei) and gas limit specified. Both values are typically obtained 
 * from blockchain data or the minting platform.
 * 
 * @param {number} gasPrice - Gas price in Gwei (1 Gwei = 10^9 Wei).
 * @param {number} gasLimit - Gas limit for the minting transaction.
 * @returns {string} Estimated gas fee in ETH.
 */
function calculateGasFees(gasPrice, gasLimit) {
  try {
    // Validate inputs to ensure they are positive numbers
    if (typeof gasPrice !== "number" || gasPrice <= 0) {
      throw new Error("Invalid gas price. Must be a positive number.");
    }
    if (typeof gasLimit !== "number" || gasLimit <= 0) {
      throw new Error("Invalid gas limit. Must be a positive number.");
    }

    // Convert gas price from Gwei to Wei (1 Gwei = 10^9 Wei)
    const gasPriceInWei = gasPrice * 1e9;

    // Calculate total gas fee in Wei
    const gasFeeInWei = gasPriceInWei * gasLimit;

    // Convert gas fee from Wei to ETH (1 ETH = 10^18 Wei)
    const gasFeeInEth = gasFeeInWei / 1e18;

    // Format result to 6 decimal places for better readability
    return gasFeeInEth.toFixed(6) + " ETH";
  } catch (error) {
    // Handle any unexpected errors
    console.error("Error calculating gas fees:", error.message);
    return "Error calculating gas fees. Please check your inputs.";
  }
}

// Example usage:
// Assuming a gas price of 50 Gwei and a gas limit of 21000 (standard for simple transactions)
const gasPrice = 50;  // Gwei
const gasLimit = 21000;  // Gas units
const estimatedGasFee = calculateGasFees(gasPrice, gasLimit);
console.log("Estimated Gas Fee:", estimatedGasFee);
```
