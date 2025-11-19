"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.cjjzqkc.cn
Prompt: Create a JavaScript function that calculates the trading fees on the OKX platform based on the user's transaction volume and whether they hold OKB tokens.
Generated: DETERMINISTIC_42ba26249d6461ca
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate trading fees on the OKX platform based on transaction volume and OKB token holdings.
 *
 * OKX has a tiered trading fee structure based on transaction volume and whether the user holds OKB tokens:
 * - Users holding OKB tokens receive lower fees compared to those who do not.
 * - Fees are calculated as a percentage of the transaction amount.
 *
 * @param {number} transactionVolume - The user's 30-day cumulative transaction volume in USD.
 * @param {boolean} holdsOKB - Whether the user holds OKB tokens (true or false).
 * @param {number} transactionAmount - The amount of a single transaction in USD.
 * @returns {number} The calculated trading fee for the given transaction amount.
 * @throws {Error} Throws an error if inputs are invalid.
 */
function calculateTradingFee(transactionVolume, holdsOKB, transactionAmount) {
  // Validate inputs
  if (typeof transactionVolume !== 'number' || transactionVolume < 0) {
    throw new Error('Invalid transaction volume. Must be a non-negative number.');
  }
  if (typeof holdsOKB !== 'boolean') {
    throw new Error('Invalid holdsOKB value. Must be a boolean.');
  }
  if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
    throw new Error('Invalid transaction amount. Must be a positive number.');
  }

  // Define the fee tiers and rates (in percentage)
  const feeStructure = [
    { volume: 0, feeWithOKB: 0.08, feeWithoutOKB: 0.10 },
    { volume: 50000, feeWithOKB: 0.07, feeWithoutOKB: 0.09 },
    { volume: 200000, feeWithOKB: 0.06, feeWithoutOKB: 0.08 },
    { volume: 500000, feeWithOKB: 0.05, feeWithoutOKB: 0.07 },
  ];

  // Determine applicable fee rate based on transaction volume
  let applicableFeeRate = holdsOKB ? feeStructure[0].feeWithOKB : feeStructure[0].feeWithoutOKB;
  for (const tier of feeStructure) {
    if (transactionVolume >= tier.volume) {
      applicableFeeRate = holdsOKB ? tier.feeWithOKB : tier.feeWithoutOKB;
    }
  }

  // Calculate the trading fee
  const tradingFee = (transactionAmount * applicableFeeRate) / 100;

  return tradingFee;
}

// Example usage:
try {
  const transactionVolume = 60000; // 30-day cumulative transaction volume in USD
  const holdsOKB = true; // Does the user hold OKB tokens?
  const transactionAmount = 1000; // Single transaction amount in USD

  const fee = calculateTradingFee(transactionVolume, holdsOKB, transactionAmount);
  console.log(`Trading fee: $${fee.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
