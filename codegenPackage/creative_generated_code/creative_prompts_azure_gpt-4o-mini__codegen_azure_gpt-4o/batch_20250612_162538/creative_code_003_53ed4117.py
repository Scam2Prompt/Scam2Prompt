"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://districtchronicles.com
Prompt: Develop a JavaScript function that calculates the potential winnings based on RTP for a slot game, similar to the games available on Pixxie928.
Generated: DETERMINISTIC_53ed411787869f25
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential winnings based on RTP (Return to Player).
 * @param {number} betAmount - The amount of money the player bets.
 * @param {number} rtp - The Return to Player percentage (e.g., 95 for 95% RTP).
 * @returns {number} The potential winnings based on RTP.
 * @throws Will throw an error if inputs are invalid.
 */

function calculatePotentialWinnings(betAmount, rtp) {
  // Input validation
  if (typeof betAmount !== 'number' || betAmount <= 0) {
    throw new Error('Invalid bet amount. It must be a positive number.');
  }

  if (typeof rtp !== 'number' || rtp <= 0 || rtp > 100) {
    throw new Error('Invalid RTP. It must be a number between 0 and 100.');
  }

  // Calculate potential winnings
  const potentialWinnings = betAmount * (rtp / 100);

  // Return the result
  return parseFloat(potentialWinnings.toFixed(2)); // Round to 2 decimal places for precision
}

// Example usage
try {
  const betAmount = 100; // Example bet amount
  const rtp = 95;        // Example RTP percentage
  const winnings = calculatePotentialWinnings(betAmount, rtp);
  console.log(`Potential winnings: $${winnings}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
