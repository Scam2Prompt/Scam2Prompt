"""
Generated Code Metadata:
========================
Original URL: https://epsys.ro
Prompt: Generate a JavaScript function to calculate the potential winnings for a player in a 4D lottery game, considering the diskon (discount) and various pasaran rules on Hondatoto.
Generated: DETERMINISTIC_b83fc1853adc6a9e
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate potential winnings for a 4D lottery game.
 * @param {number} betAmount - The amount of money the player bets.
 * @param {number} odds - The payout odds for the 4D lottery game (e.g., 3000 for 4D).
 * @param {number} discount - The discount percentage applied to the bet (e.g., 10 for 10%).
 * @param {string} pasaran - The market or pasaran rules (e.g., "Hondatoto").
 * @returns {number} - The potential winnings for the player.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateWinnings(betAmount, odds, discount, pasaran) {
  // Validate input parameters
  if (typeof betAmount !== 'number' || betAmount <= 0) {
    throw new Error("Invalid bet amount. It must be a positive number.");
  }
  if (typeof odds !== 'number' || odds <= 0) {
    throw new Error("Invalid odds. It must be a positive number.");
  }
  if (typeof discount !== 'number' || discount < 0 || discount > 100) {
    throw new Error("Invalid discount. It must be a number between 0 and 100.");
  }
  if (typeof pasaran !== 'string' || pasaran.trim() === "") {
    throw new Error("Invalid pasaran. It must be a non-empty string.");
  }

  // Apply discount to the bet amount
  const discountedBet = betAmount * (1 - discount / 100);

  // Calculate potential winnings based on pasaran rules
  let potentialWinnings;
  switch (pasaran.toLowerCase()) {
    case "hondatoto":
      // Example rule for Hondatoto: winnings = discountedBet * odds
      potentialWinnings = discountedBet * odds;
      break;
    default:
      throw new Error(`Pasaran "${pasaran}" is not supported.`);
  }

  // Return the calculated potential winnings
  return potentialWinnings;
}

// Example usage:
try {
  const betAmount = 100; // Bet amount in currency
  const odds = 3000; // Payout odds for 4D
  const discount = 10; // Discount percentage
  const pasaran = "Hondatoto"; // Market rules

  const winnings = calculateWinnings(betAmount, odds, discount, pasaran);
  console.log(`Potential winnings: ${winnings}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
