"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Create a JavaScript function that calculates the amount of BCKR tokens a user receives based on their ETH contribution during the presale.
Generated: DETERMINISTIC_5c90b1fcbc5ffa36
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the amount of BCKR tokens a user receives based on their ETH contribution.
 * @param {number} ethContribution - The amount of ETH contributed by the user.
 * @param {number} tokenRate - The conversion rate of ETH to BCKR tokens (tokens per 1 ETH).
 * @returns {number} - The amount of BCKR tokens the user receives.
 * @throws Will throw an error if the input is invalid (e.g., negative numbers or non-numeric values).
 */
function calculateBCKRTokens(ethContribution, tokenRate) {
  try {
    // Input validation
    if (typeof ethContribution !== 'number' || typeof tokenRate !== 'number') {
      throw new Error('Both ethContribution and tokenRate must be numeric values.');
    }
    if (ethContribution < 0 || tokenRate <= 0) {
      throw new Error('ethContribution must be non-negative and tokenRate must be positive.');
    }

    // Calculate the amount of BCKR tokens
    const tokens = ethContribution * tokenRate;

    return tokens;
  } catch (error) {
    console.error('Error calculating BCKR tokens:', error.message);
    throw error;
  }
}

// Example usage
try {
  const ethContribution = 1.5; // User contributed 1.5 ETH
  const tokenRate = 1000; // Conversion rate: 1000 BCKR tokens per ETH
  const tokens = calculateBCKRTokens(ethContribution, tokenRate);
  console.log(`User receives ${tokens} BCKR tokens.`);
} catch (error) {
  console.error('Failed to calculate tokens:', error.message);
}
```
