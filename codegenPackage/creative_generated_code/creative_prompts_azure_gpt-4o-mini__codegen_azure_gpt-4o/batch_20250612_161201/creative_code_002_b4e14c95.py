"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Create a JavaScript function that calculates the potential earnings for coffee farmers using the CNK token based on the pricing model outlined on the Crypto N' Kafe site.
Generated: DETERMINISTIC_b4e14c9503051a9b
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate potential earnings for coffee farmers using CNK tokens.
 * 
 * @param {number} totalYield - Total coffee yield in kilograms (kg).
 * @param {number} pricePerKgInCNK - Price per kilogram of coffee in CNK tokens.
 * @param {number} tokenConversionRate - Conversion rate of CNK tokens to USD.
 * @returns {object} An object containing potential earnings in CNK tokens and USD.
 * 
 * @throws {Error} If any input parameter is invalid.
 */
function calculateEarningsCNK(totalYield, pricePerKgInCNK, tokenConversionRate) {
  // Input validation
  if (typeof totalYield !== 'number' || totalYield <= 0) {
    throw new Error("Invalid totalYield: Must be a positive number.");
  }
  if (typeof pricePerKgInCNK !== 'number' || pricePerKgInCNK <= 0) {
    throw new Error("Invalid pricePerKgInCNK: Must be a positive number.");
  }
  if (typeof tokenConversionRate !== 'number' || tokenConversionRate <= 0) {
    throw new Error("Invalid tokenConversionRate: Must be a positive number.");
  }

  // Calculate earnings in CNK tokens
  const earningsInCNK = totalYield * pricePerKgInCNK;

  // Calculate earnings in USD
  const earningsInUSD = earningsInCNK * tokenConversionRate;

  // Return results as an object
  return {
    earningsInCNK: earningsInCNK,
    earningsInUSD: earningsInUSD
  };
}

// Example usage:
try {
  const totalYield = 500; // Total coffee yield in kilograms
  const pricePerKgInCNK = 10; // Price per kilogram in CNK tokens
  const tokenConversionRate = 0.25; // CNK to USD conversion rate

  const earnings = calculateEarningsCNK(totalYield, pricePerKgInCNK, tokenConversionRate);
  console.log("Potential Earnings:", earnings);
} catch (error) {
  console.error("Error calculating earnings:", error.message);
}
```
