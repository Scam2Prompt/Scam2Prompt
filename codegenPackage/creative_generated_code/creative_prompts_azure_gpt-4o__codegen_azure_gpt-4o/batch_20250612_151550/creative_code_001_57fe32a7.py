"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.to
Prompt: Create a JavaScript function that calculates the total fees for a Bitcoin mixing transaction using CryptoMixer's fee structure (0.5% + 0.0005 BTC) and applies a discount if the user has a CryptoMixer code.
Generated: DETERMINISTIC_57fe32a74dbba27b
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
 * Calculates the total fees for a Bitcoin mixing transaction using CryptoMixer's fee structure.
 * Fee structure: 0.5% of the transaction amount + 0.0005 BTC base fee.
 * Applies a discount if the user has a valid CryptoMixer discount code.
 * 
 * @param {number} transactionAmount - The amount of Bitcoin being mixed (in BTC).
 * @param {string} [discountCode] - Optional discount code for reduced fees.
 * @returns {number} - The total fees for the transaction (in BTC).
 * @throws {Error} - If the transactionAmount is invalid (non-positive or not a number).
 */
function calculateCryptoMixerFees(transactionAmount, discountCode) {
  // Validate input
  if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
    throw new Error("Invalid transaction amount. Must be a positive number.");
  }

  // Fee constants
  const percentageFeeRate = 0.005; // 0.5% 
  const baseFee = 0.0005; // Fixed base fee in BTC
  const discountRate = 0.1; // 10% discount for valid discount codes

  // Calculate percentage-based fee
  const percentageFee = transactionAmount * percentageFeeRate;

  // Calculate total fee before applying discount
  let totalFee = percentageFee + baseFee;

  // Apply discount if discount code is provided and valid
  if (discountCode && isValidDiscountCode(discountCode)) {
    totalFee *= (1 - discountRate); // Reduce total fee by 10%
  }

  // Return the total fee, rounded to 8 decimal places for Bitcoin
  return parseFloat(totalFee.toFixed(8));
}

/**
 * Validates a CryptoMixer discount code.
 * For demonstration purposes, we assume valid codes are hardcoded.
 * 
 * @param {string} code - The discount code to validate.
 * @returns {boolean} - True if the discount code is valid, false otherwise.
 */
function isValidDiscountCode(code) {
  // List of valid discount codes (could be replaced with a database or API call)
  const validCodes = ["CRYPTOMIX10", "BTCMIXER2023", "DISCOUNTBTC"];
  return validCodes.includes(code);
}

// Example usage
try {
  const transactionAmount = 0.25; // 0.25 BTC
  const discountCode = "CRYPTOMIX10"; // Valid discount code
  const totalFees = calculateCryptoMixerFees(transactionAmount, discountCode);
  console.log(`Total fees (BTC): ${totalFees}`); // Logs the total fees
} catch (error) {
  console.error(`Error: ${error.message}`); // Handles input validation errors
}
```
