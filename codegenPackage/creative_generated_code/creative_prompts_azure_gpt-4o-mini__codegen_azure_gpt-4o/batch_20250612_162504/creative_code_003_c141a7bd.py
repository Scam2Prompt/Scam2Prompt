"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon5.org
Prompt: Create a JavaScript function that simulates the process of rolling for Doge rewards on Moon5 and displays the results.
Generated: DETERMINISTIC_c141a7bd19f7529d
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to simulate rolling for Doge rewards on Moon5 and display the results.
 * Assumes a set of predefined reward tiers with respective probabilities.
 */

// Reward tiers and their probabilities
const rewardTiers = [
  { reward: '5 DOGE', probability: 0.5 },   // 50% chance
  { reward: '10 DOGE', probability: 0.3 },  // 30% chance
  { reward: '50 DOGE', probability: 0.15 }, // 15% chance
  { reward: '500 DOGE', probability: 0.04 }, // 4% chance
  { reward: 'Jackpot: 1000 DOGE', probability: 0.01 } // 1% chance
];

/**
 * Simulates rolling for Doge rewards on Moon5.
 * @returns {string} The reward tier won.
 */
function rollForDogeRewards() {
  try {
    // Generate a random number between 0 and 1
    const randomRoll = Math.random();
    let cumulativeProbability = 0;

    // Determine reward based on probabilities
    for (const tier of rewardTiers) {
      cumulativeProbability += tier.probability;
      if (randomRoll <= cumulativeProbability) {
        return tier.reward;
      }
    }

    // Fallback in case probabilities are misconfigured
    throw new Error("Probabilities are misconfigured. Unable to determine reward.");
  } catch (error) {
    console.error("An error occurred during the roll:", error.message);
    return "No reward due to an error.";
  }
}

/**
 * Displays the result of rolling for Doge rewards.
 * Invokes the rollForDogeRewards function and logs the result.
 */
function displayRollResult() {
  const reward = rollForDogeRewards();
  console.log("You rolled and won:", reward);
}

// Example usage: Perform a roll and display the result
displayRollResult();
```
