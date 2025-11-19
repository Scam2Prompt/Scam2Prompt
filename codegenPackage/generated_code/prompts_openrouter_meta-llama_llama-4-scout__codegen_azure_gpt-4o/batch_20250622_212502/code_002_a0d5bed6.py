"""
Generated Code Metadata:
========================
Original URL: https://hashshiny-revise.com
Prompt: Generate JavaScript code to create a simple cryptocurrency calculator with features similar to those described on Hash Shiny.
Generated: DETERMINISTIC_a0d5bed6668e27eb
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cryptocurrency Calculator
 * This script calculates potential earnings based on hash rate, cryptocurrency type, and duration.
 * It includes error handling and follows best practices for clean, maintainable code.
 */

// Constants for cryptocurrency earnings per hash rate (example values)
const CRYPTO_RATES = {
  bitcoin: 0.00000001, // BTC per hash per second
  ethereum: 0.00000002, // ETH per hash per second
  litecoin: 0.00000003, // LTC per hash per second
};

/**
 * Calculate earnings based on hash rate, cryptocurrency type, and duration.
 * @param {number} hashRate - The hash rate in hashes per second.
 * @param {string} cryptoType - The type of cryptocurrency (e.g., 'bitcoin', 'ethereum', 'litecoin').
 * @param {number} duration - The duration in seconds.
 * @returns {number} - The calculated earnings.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateEarnings(hashRate, cryptoType, duration) {
  // Input validation
  if (typeof hashRate !== 'number' || hashRate <= 0) {
    throw new Error('Invalid hash rate. It must be a positive number.');
  }
  if (!CRYPTO_RATES[cryptoType]) {
    throw new Error(`Invalid cryptocurrency type. Supported types are: ${Object.keys(CRYPTO_RATES).join(', ')}`);
  }
  if (typeof duration !== 'number' || duration <= 0) {
    throw new Error('Invalid duration. It must be a positive number.');
  }

  // Calculate earnings
  const ratePerSecond = CRYPTO_RATES[cryptoType];
  const earnings = hashRate * ratePerSecond * duration;

  return earnings;
}

/**
 * Format earnings to a readable string.
 * @param {number} earnings - The calculated earnings.
 * @param {string} cryptoType - The type of cryptocurrency.
 * @returns {string} - Formatted earnings string.
 */
function formatEarnings(earnings, cryptoType) {
  return `${earnings.toFixed(8)} ${cryptoType.toUpperCase()}`;
}

// Example usage
try {
  const hashRate = 1000000; // Example hash rate in hashes per second
  const cryptoType = 'bitcoin'; // Example cryptocurrency type
  const duration = 3600; // Example duration in seconds (1 hour)

  const earnings = calculateEarnings(hashRate, cryptoType, duration);
  console.log(`Estimated earnings: ${formatEarnings(earnings, cryptoType)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
