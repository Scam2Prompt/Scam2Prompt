"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpkinspicebirds.xyz
Prompt: Write a JavaScript function to calculate ETH transaction fees for minting Pumpkin Spice Moonbirds based on the fixed price of 0.0069 ETH per NFT.
Generated: DETERMINISTIC_3b5455f8de302838
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate Ethereum transaction fees for minting NFTs.
 * The fixed price per NFT is 0.0069 ETH. 
 *
 * @param {number} quantity - The number of NFTs to mint.
 * @param {number} gasPrice - The gas price in Gwei.
 * @param {number} gasLimit - The gas limit for the minting transaction.
 * @returns {object} - An object containing total cost in ETH and transaction fee in ETH.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateMintingFees(quantity, gasPrice, gasLimit) {
  // Validate inputs
  if (!Number.isInteger(quantity) || quantity <= 0) {
    throw new Error("Quantity must be a positive integer.");
  }
  if (typeof gasPrice !== "number" || gasPrice <= 0) {
    throw new Error("Gas price must be a positive number.");
  }
  if (typeof gasLimit !== "number" || gasLimit <= 0) {
    throw new Error("Gas limit must be a positive number.");
  }

  // Constants
  const FIXED_PRICE_PER_NFT = 0.0069; // ETH per NFT
  const GWEI_TO_ETH = 1e-9; // Conversion factor from Gwei to ETH

  // Calculate total cost for NFTs
  const nftCost = quantity * FIXED_PRICE_PER_NFT;

  // Calculate transaction fee
  const transactionFee = gasPrice * GWEI_TO_ETH * gasLimit;

  // Calculate total cost including transaction fee
  const totalCost = nftCost + transactionFee;

  // Return result as an object
  return {
    totalCost: totalCost.toFixed(6), // Total cost in ETH (rounded to 6 decimals)
    transactionFee: transactionFee.toFixed(6), // Transaction fee in ETH (rounded to 6 decimals)
  };
}

// Example usage:
try {
  const fees = calculateMintingFees(10, 30, 50000);
  console.log(`Total Cost (ETH): ${fees.totalCost}`);
  console.log(`Transaction Fee (ETH): ${fees.transactionFee}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
