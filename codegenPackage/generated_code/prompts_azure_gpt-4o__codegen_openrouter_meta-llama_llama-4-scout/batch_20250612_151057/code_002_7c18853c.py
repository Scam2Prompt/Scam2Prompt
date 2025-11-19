"""
Generated Code Metadata:
========================
Original URL: https://sealana-presale.pages.dev
Prompt: Create a JavaScript function to calculate the maximum $SEAL tokens a user can receive based on their ETH payment, using the rate of 1 $SEAL = $0.022 as described on the Sealana Presale site.
Generated: DETERMINISTIC_7c18853c5e36e18d
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the maximum $SEAL tokens a user can receive based on their ETH payment.
 * 
 * @param {number} ethPayment - The user's ETH payment.
 * @param {number} [sealRate=0.022] - The rate of 1 $SEAL in USD (default: 0.022).
 * @param {number} [ethToUsdRate=1] - The current ETH to USD exchange rate (default: 1).
 * @returns {number} The maximum $SEAL tokens the user can receive.
 */
function calculateSealTokens(ethPayment, sealRate = 0.022, ethToUsdRate = 1) {
    // Check if ethPayment is a valid number
    if (typeof ethPayment !== 'number' || isNaN(ethPayment) || ethPayment < 0) {
        throw new Error('Invalid ETH payment. Please provide a valid number.');
    }

    // Check if sealRate is a valid number
    if (typeof sealRate !== 'number' || isNaN(sealRate) || sealRate <= 0) {
        throw new Error('Invalid $SEAL rate. Please provide a valid positive number.');
    }

    // Check if ethToUsdRate is a valid number
    if (typeof ethToUsdRate !== 'number' || isNaN(ethToUsdRate) || ethToUsdRate <= 0) {
        throw new Error('Invalid ETH to USD exchange rate. Please provide a valid positive number.');
    }

    // Convert ETH payment to USD
    const ethPaymentInUsd = ethPayment * ethToUsdRate;

    // Calculate the maximum $SEAL tokens
    const sealTokens = ethPaymentInUsd / sealRate;

    return sealTokens;
}

// Example usage:
try {
    const ethPayment = 1; // 1 ETH
    const sealTokens = calculateSealTokens(ethPayment);
    console.log(`The user can receive ${sealTokens} $SEAL tokens.`);
} catch (error) {
    console.error(error.message);
}
```
