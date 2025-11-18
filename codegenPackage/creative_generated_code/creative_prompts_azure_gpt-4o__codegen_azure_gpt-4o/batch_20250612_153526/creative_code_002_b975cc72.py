"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realis.pages.dev
Prompt: Create a function in JavaScript that calculates the probability of obtaining a specific Meowgon rarity (e.g., Epic or Supreme) based on the rarity drop rates provided on the Realis site.
Generated: DETERMINISTIC_b975cc72726c27f0
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the probability of obtaining a specific Meowgon rarity based on drop rates.
 *
 * @param {string} rarity - The desired rarity (e.g., "Epic", "Supreme").
 * @param {Object} dropRates - An object mapping rarities to their respective drop probabilities.
 * Example: { Common: 0.5, Rare: 0.3, Epic: 0.15, Supreme: 0.05 }
 * @returns {number} - The probability of obtaining the specified rarity (as a percentage).
 *                     Returns -1 if the rarity is not found in the dropRates object.
 */
function calculateRarityProbability(rarity, dropRates) {
  try {
    // Ensure the input dropRates is a valid object
    if (typeof dropRates !== "object" || dropRates === null) {
      throw new Error("Invalid dropRates object provided.");
    }

    // Check if the desired rarity exists in the dropRates object
    if (!dropRates.hasOwnProperty(rarity)) {
      console.warn(`Rarity "${rarity}" not found. Please provide a valid rarity.`);
      return -1; // Indicate an invalid rarity
    }

    // Retrieve the probability for the specified rarity
    const probability = dropRates[rarity];

    // Ensure the probability is a valid number
    if (typeof probability !== "number" || probability < 0 || probability > 1) {
      throw new Error(`Invalid probability value for rarity "${rarity}": ${probability}`);
    }

    // Convert the probability to a percentage and return
    return probability * 100;
  } catch (error) {
    // Log the error and rethrow it for further handling if needed
    console.error(`Error calculating rarity probability: ${error.message}`);
    throw error;
  }
}

// Example usage
const meowgonDropRates = {
  Common: 0.5,
  Rare: 0.3,
  Epic: 0.15,
  Supreme: 0.05,
};

try {
  const rarity = "Epic";
  const probability = calculateRarityProbability(rarity, meowgonDropRates);
  console.log(`The probability of obtaining an "${rarity}" Meowgon is ${probability}%`);
} catch (error) {
  console.error("An error occurred:", error.message);
}
```
