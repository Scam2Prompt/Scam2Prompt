"""
Generated Code Metadata:
========================
Original URL: https://gasfee.rf.gd
Prompt: Develop a simple Ethereum gas fee calculator using JavaScript.
Generated: DETERMINISTIC_51715e4e69645857
Batch ID: 20250622_205726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Ethereum Gas Fee Calculator
 * This script calculates the total gas fee for a transaction based on gas price and gas limit.
 * 
 * Usage:
 * Call the `calculateGasFee` function with the gas price (in gwei) and gas limit.
 * The function returns the total gas fee in ETH.
 */

// Constants
const WEI_IN_ETH = 1e18; // 1 ETH = 10^18 Wei
const GWEI_IN_WEI = 1e9; // 1 Gwei = 10^9 Wei

/**
 * Converts gwei to wei.
 * @param {number} gwei - The gas price in gwei.
 * @returns {number} - The gas price in wei.
 */
function gweiToWei(gwei) {
  return gwei * GWEI_IN_WEI;
}

/**
 * Converts wei to ETH.
 * @param {number} wei - The value in wei.
 * @returns {number} - The value in ETH.
 */
function weiToEth(wei) {
  return wei / WEI_IN_ETH;
}

/**
 * Calculates the total gas fee for a transaction.
 * @param {number} gasPriceGwei - The gas price in gwei.
 * @param {number} gasLimit - The gas limit for the transaction.
 * @returns {number} - The total gas fee in ETH.
 */
function calculateGasFee(gasPriceGwei, gasLimit) {
  try {
    // Validate inputs
    if (typeof gasPriceGwei !== 'number' || gasPriceGwei <= 0) {
      throw new Error('Invalid gas price. It must be a positive number.');
    }
    if (typeof gasLimit !== 'number' || gasLimit <= 0) {
      throw new Error('Invalid gas limit. It must be a positive number.');
    }

    // Convert gas price to wei
    const gasPriceWei = gweiToWei(gasPriceGwei);

    // Calculate total gas fee in wei
    const totalGasFeeWei = gasPriceWei * gasLimit;

    // Convert total gas fee to ETH
    const totalGasFeeEth = weiToEth(totalGasFeeWei);

    return totalGasFeeEth;
  } catch (error) {
    console.error('Error calculating gas fee:', error.message);
    return null; // Return null in case of an error
  }
}

// Example usage
const gasPriceGwei = 20; // Gas price in gwei
const gasLimit = 21000; // Gas limit for a standard transaction
const totalGasFee = calculateGasFee(gasPriceGwei, gasLimit);

if (totalGasFee !== null) {
  console.log(`Total Gas Fee: ${totalGasFee} ETH`);
} else {
  console.log('Failed to calculate gas fee.');
}
```
