"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betfur.pages.dev
Prompt: Write a function in TypeScript to calculate the expected payout for BetFury's Megaways slots based on reel bonuses and bonus symbols like Wild and Scatter.
Generated: DETERMINISTIC_6a7c6ea0c186a7f6
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
/**
 * Calculates the expected payout for BetFury's Megaways slots.
 * The calculation is based on reel bonuses, bonus symbols like Wild and Scatter,
 * and the number of ways to win.
 *
 * @param basePayout - The base payout amount for the slot.
 * @param reelBonuses - An array of reel bonus multipliers (e.g., [1.5, 2]).
 * @param wildMultiplier - Multiplier for Wild symbols (e.g., 2 if Wild doubles payouts).
 * @param scatterCount - Number of Scatter symbols present on the reels.
 * @param scatterBonus - Bonus payout for each Scatter symbol.
 * @returns The expected payout calculated based on the input parameters.
 */
function calculateMegawaysPayout(
  basePayout: number, 
  reelBonuses: number[], 
  wildMultiplier: number, 
  scatterCount: number, 
  scatterBonus: number
): number {
  // Validate input parameters
  if (basePayout <= 0) {
    throw new Error('Base payout must be greater than zero.');
  }
  if (wildMultiplier < 1) {
    throw new Error('Wild multiplier must be at least 1.');
  }
  if (scatterCount < 0) {
    throw new Error('Scatter count cannot be negative.');
  }
  if (scatterBonus < 0) {
    throw new Error('Scatter bonus must be non-negative.');
  }

  // Apply reel bonuses
  let totalMultiplier = reelBonuses.reduce((acc, bonus) => acc * bonus, 1);

  // Apply Wild multiplier
  totalMultiplier *= wildMultiplier;

  // Calculate Scatter payouts
  const scatterPayout = scatterCount * scatterBonus;

  // Calculate total expected payout
  const totalPayout = basePayout * totalMultiplier + scatterPayout;

  return totalPayout;
}

// Example usage:
try {
  const basePayout = 100; // Base payout amount
  const reelBonuses = [1.5, 2]; // Reel bonus multipliers
  const wildMultiplier = 2; // Multiplier for Wild symbols
  const scatterCount = 3; // Number of Scatter symbols
  const scatterBonus = 50; // Bonus payout per Scatter symbol
  
  const expectedPayout = calculateMegawaysPayout(basePayout, reelBonuses, wildMultiplier, scatterCount, scatterBonus);
  console.log(`Expected Payout: $${expectedPayout}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
