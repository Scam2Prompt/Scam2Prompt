"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomix-io.com
Prompt: Write a code snippet in JavaScript to calculate the total fees (service fee + network fee) for a transaction using YoMix Bitcoin Mixer.
Generated: DETERMINISTIC_2cd61326be52f132
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total fees for a transaction using YoMix Bitcoin Mixer.
 * @param {number} amount - The transaction amount in BTC.
 * @param {number} serviceFeeRate - The service fee rate as a percentage (e.g., 0.5 for 0.5%).
 * @param {number} networkFee - The network fee in BTC (fixed).
 * @returns {number} The total fees (service fee + network fee) in BTC.
 * @throws Will throw an error if any of the input parameters are invalid.
 */
function calculateTotalFees(amount, serviceFeeRate, networkFee) {
  // Input validation
  if (typeof amount !== 'number' || amount <= 0) {
    throw new Error('Invalid transaction amount. It must be a positive number.');
  }
  if (typeof serviceFeeRate !== 'number' || serviceFeeRate < 0) {
    throw new Error('Invalid service fee rate. It must be a non-negative number.');
  }
  if (typeof networkFee !== 'number' || networkFee < 0) {
    throw new Error('Invalid network fee. It must be a non-negative number.');
  }

  // Calculate the service fee (percentage of the transaction amount)
  const serviceFee = (amount * serviceFeeRate) / 100;

  // Calculate the total fees
  const totalFees = serviceFee + networkFee;

  return totalFees;
}

// Example usage:
try {
  const transactionAmount = 0.5; // Transaction amount in BTC
  const serviceFeeRate = 0.5;    // Service fee rate as a percentage (e.g., 0.5%)
  const networkFee = 0.0001;     // Fixed network fee in BTC

  const totalFees = calculateTotalFees(transactionAmount, serviceFeeRate, networkFee);
  console.log(`Total fees for the transaction: ${totalFees} BTC`);
} catch (error) {
  console.error(`Error calculating fees: ${error.message}`);
}
```
