"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tntmytariff.com
Prompt: Write a JavaScript function that calculates potential winnings based on the user's bet amount on SLOT777 games.
Generated: DETERMINISTIC_ac617e078aa5018f
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential winnings for SLOT777 games.
 * @param {number} betAmount - The amount the user has bet.
 * @param {number} multiplier - The slot game multiplier for winnings (e.g., 2x, 5x, etc.).
 * @returns {number} - The potential winnings based on betAmount and multiplier.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateWinnings(betAmount, multiplier) {
  // Validate inputs
  if (typeof betAmount !== 'number' || betAmount <= 0) {
    throw new Error('Invalid bet amount. It must be a positive number.');
  }
  if (typeof multiplier !== 'number' || multiplier <= 0) {
    throw new Error('Invalid multiplier. It must be a positive number.');
  }

  // Calculate potential winnings
  const winnings = betAmount * multiplier;

  // Ensure winnings are finite and valid
  if (!isFinite(winnings)) {
    throw new Error('Calculation error: winnings are not a finite number.');
  }

  return winnings;
}

// Example usage:
// try {
//   const betAmount = 100; // User's bet amount
//   const multiplier = 5; // SLOT777 multiplier
//   const potentialWinnings = calculateWinnings(betAmount, multiplier);
//   console.log(`Potential winnings: $${potentialWinnings}`);
// } catch (error) {
//   console.error(`Error: ${error.message}`);
// }
```
