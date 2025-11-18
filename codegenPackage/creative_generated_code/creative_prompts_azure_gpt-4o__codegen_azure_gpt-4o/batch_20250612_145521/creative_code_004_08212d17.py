"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Write a function in JavaScript to calculate the next stage token price based on the current price and presale progress, as demonstrated in the $GEGG presale model.
Generated: DETERMINISTIC_08212d17fd90cbc1
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the next stage token price based on the current price and presale progress.
 * 
 * This function assumes:
 * - Each stage has a fixed percentage of tokens allocated.
 * - The price increases by a defined increment per stage.
 * 
 * @param {number} currentPrice - The current token price in the presale.
 * @param {number} progress - The current progress of the presale as a percentage (0 to 100).
 * @param {number} incrementPerStage - The price increment per stage.
 * @param {number} stageAllocation - The percentage of tokens allocated to each stage.
 * @returns {number} The next stage token price, or the current price if the final stage is reached.
 * 
 * @throws {Error} Throws an error if input parameters are invalid.
 */
function calculateNextStagePrice(currentPrice, progress, incrementPerStage, stageAllocation) {
  // Validate input parameters
  if (typeof currentPrice !== 'number' || currentPrice <= 0) {
    throw new Error('Invalid currentPrice: Must be a positive number.');
  }
  if (typeof progress !== 'number' || progress < 0 || progress > 100) {
    throw new Error('Invalid progress: Must be a number between 0 and 100.');
  }
  if (typeof incrementPerStage !== 'number' || incrementPerStage <= 0) {
    throw new Error('Invalid incrementPerStage: Must be a positive number.');
  }
  if (typeof stageAllocation !== 'number' || stageAllocation <= 0 || stageAllocation > 100) {
    throw new Error('Invalid stageAllocation: Must be a number greater than 0 and less than or equal to 100.');
  }

  // Calculate the number of completed stages based on progress and stage allocation
  const completedStages = Math.floor(progress / stageAllocation);

  // Determine the next stage price
  const nextStagePrice = currentPrice + (completedStages * incrementPerStage);

  // Ensure the price only changes if there are more stages
  const isFinalStage = progress >= 100 || ((completedStages + 1) * stageAllocation) > 100;
  return isFinalStage ? currentPrice : nextStagePrice;
}

// Example usage
try {
  const currentPrice = 0.01; // Current price of the token in USD
  const progress = 35; // Presale progress as a percentage
  const incrementPerStage = 0.002; // Price increment per stage in USD
  const stageAllocation = 20; // Percentage of tokens allocated per stage

  const nextPrice = calculateNextStagePrice(currentPrice, progress, incrementPerStage, stageAllocation);
  console.log(`The next stage token price is: $${nextPrice.toFixed(4)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
