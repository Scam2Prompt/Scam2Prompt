"""
Generated Code Metadata:
========================
Original URL: https://moon5.org
Prompt: Create a JavaScript function that simulates the process of rolling for Doge rewards on Moon5 and displays the results.
Generated: DETERMINISTIC_c141a7bd19f7529d
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates rolling for Doge rewards on Moon5 and displays the results.
 * The function generates a random reward based on predefined probabilities.
 * 
 * @returns {void}
 */
function rollForDogeRewards() {
  // Define reward tiers and their probabilities
  const rewards = [
    { name: '1 Doge', probability: 0.5 },  // 50% chance
    { name: '5 Doge', probability: 0.3 },  // 30% chance
    { name: '10 Doge', probability: 0.15 }, // 15% chance
    { name: '50 Doge', probability: 0.05 }  // 5% chance
  ];

  /**
   * Generates a random reward based on the probabilities defined in the rewards array.
   * 
   * @returns {string} The name of the reward.
   */
  function getRandomReward() {
    const randomValue = Math.random(); // Generate a random number between 0 and 1
    let cumulativeProbability = 0;

    for (const reward of rewards) {
      cumulativeProbability += reward.probability;
      if (randomValue <= cumulativeProbability) {
        return reward.name;
      }
    }

    // Fallback in case probabilities don't sum to 1 (shouldn't happen in this setup)
    return 'No Reward';
  }

  try {
    // Simulate the roll and display the result
    const reward = getRandomReward();
    console.log(`Congratulations! You rolled and received: ${reward}`);
  } catch (error) {
    // Handle any unexpected errors
    console.error('An error occurred while rolling for Doge rewards:', error);
  }
}

// Example usage
rollForDogeRewards();
```
