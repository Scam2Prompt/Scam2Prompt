"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-presale-dogcoin.pages.dev
Prompt: Create a JavaScript function that calculates the amount of DOG tokens received based on the ETH amount sent in the presale.
Generated: DETERMINISTIC_a489f5ef0a126cf7
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the number of DOG tokens received based on ETH sent in the presale.
 * @param {number} ethAmount - The amount of ETH sent.
 * @param {number} tokenRate - The exchange rate of DOG tokens per 1 ETH.
 * @returns {number} - The amount of DOG tokens received.
 * @throws Will throw an error if the input values are invalid.
 */
function calculateDogTokens(ethAmount, tokenRate) {
  // Input validation
  if (typeof ethAmount !== 'number' || ethAmount <= 0) {
    throw new Error("Invalid ETH amount. It must be a positive number.");
  }
  
  if (typeof tokenRate !== 'number' || tokenRate <= 0) {
    throw new Error("Invalid token rate. It must be a positive number.");
  }

  // Calculate DOG tokens
  const dogTokens = ethAmount * tokenRate;

  // Ensure the result is valid and finite
  if (!isFinite(dogTokens)) {
    throw new Error("Calculation error. Result is not finite.");
  }

  return dogTokens;
}

// Example usage:
try {
  const ethAmount = 2; // Example: 2 ETH sent
  const tokenRate = 1000; // Example: 1000 DOG tokens per 1 ETH
  const tokensReceived = calculateDogTokens(ethAmount, tokenRate);
  console.log(`You will receive ${tokensReceived} DOG tokens.`);
} catch (error) {
  console.error(error.message);
}
```
