"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Create a function in JavaScript that calculates bonus rolls for crafting items in "Big Time," ensuring it incorporates the mechanics of rolling for exciting bonuses as described.
Generated: DETERMINISTIC_bc8b1fb37006cae0
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates bonus rolls for crafting items in "Big Time."
 * 
 * Mechanics:
 * 1. Base chance for a bonus is determined by `baseBonusChance`.
 * 2. Additional bonuses are layered based on thresholds.
 * 3. Randomization is used to simulate exciting roll bonuses.
 * 4. Error handling ensures proper input validation.
 * 
 * @param {number} craftingLevel - The level of crafting skill (must be a positive integer).
 * @param {number} itemRarity - The rarity of the item (scale from 1 to 5, with 5 being the rarest).
 * @returns {number} - The total number of bonus rolls awarded.
 * 
 * @throws {Error} Throws an error if inputs are invalid.
 */
function calculateBonusRolls(craftingLevel, itemRarity) {
  // Validate inputs
  if (!Number.isInteger(craftingLevel) || craftingLevel <= 0) {
    throw new Error('Invalid crafting level. Must be a positive integer.');
  }
  if (!Number.isInteger(itemRarity) || itemRarity < 1 || itemRarity > 5) {
    throw new Error('Invalid item rarity. Must be an integer between 1 and 5.');
  }

  // Base bonus chance (percent) increases with crafting level and item rarity
  const baseBonusChance = Math.min(50, craftingLevel + itemRarity * 10);
  let bonusRolls = 0;

  // Simulate rolling for bonuses
  const rollForBonus = () => Math.random() * 100 < baseBonusChance;

  // Perform initial roll
  if (rollForBonus()) {
    bonusRolls++;
  }

  // Exciting bonus mechanic: chance for additional rolls diminishes iteratively
  let additionalChance = baseBonusChance / 2; // Start with half the base chance
  while (additionalChance > 5) { // Stop when chance is too low
    if (Math.random() * 100 < additionalChance) {
      bonusRolls++;
    }
    additionalChance /= 2; // Reduce chance for subsequent rolls
  }

  return bonusRolls;
}

// Example Usage:
try {
  const craftingLevel = 10;
  const itemRarity = 3;
  const bonuses = calculateBonusRolls(craftingLevel, itemRarity);
  console.log(`Total Bonus Rolls: ${bonuses}`);
} catch (error) {
  console.error(error.message);
}
```
