"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.shibaswaap.us.com
Prompt: Write a function in JavaScript to calculate payout ratios for various betting types, including kèo chấp, kèo tài xỉu, and special bets, as mentioned in 789Club’s sports betting section.
Generated: DETERMINISTIC_43f7b52489bc72f3
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate payout ratios for various betting types.
 * Supported betting types: kèo chấp, kèo tài xỉu, special bets.
 * 
 * @param {string} betType - The type of bet. Valid values: "keo_chap", "keo_tai_xiu", "special_bet".
 * @param {number} stake - The amount of money bet.
 * @param {number} odds - The odds associated with the bet (positive for winnings, negative for losses).
 * @returns {object} - An object containing success status and payout information.
 */
function calculatePayoutRatio(betType, stake, odds) {
  // Input validation
  if (typeof betType !== "string" || typeof stake !== "number" || typeof odds !== "number") {
    return {
      success: false,
      message: "Invalid input parameters. Ensure betType is a string, stake and odds are numbers."
    };
  }

  if (stake <= 0) {
    return {
      success: false,
      message: "Stake must be greater than zero."
    };
  }

  // Supported betting types
  const supportedBetTypes = ["keo_chap", "keo_tai_xiu", "special_bet"];
  if (!supportedBetTypes.includes(betType)) {
    return {
      success: false,
      message: `Unsupported bet type. Valid types are: ${supportedBetTypes.join(", ")}`
    };
  }

  // Calculate payout based on odds
  let payout;
  if (odds > 0) {
    // Positive odds: Win scenario
    payout = stake + (stake * odds / 100);
  } else if (odds < 0) {
    // Negative odds: Loss scenario
    payout = stake + (stake * odds / 100);
  } else {
    // Odds equal to zero: No win/loss
    payout = stake;
  }

  // Round payout to two decimal places
  payout = Math.round(payout * 100) / 100;

  // Return the calculated result
  return {
    success: true,
    betType: betType,
    stake: stake,
    odds: odds,
    payout: payout
  };
}

// Example usage:
// const result = calculatePayoutRatio("keo_chap", 100, 50);
// console.log(result);
```
