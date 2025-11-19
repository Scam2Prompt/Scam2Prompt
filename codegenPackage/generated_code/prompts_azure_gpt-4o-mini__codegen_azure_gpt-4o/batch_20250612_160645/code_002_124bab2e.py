"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Create a function in JavaScript that simulates the effects of early cancer detection, inspired by the health awareness content found on Azuharu.
Generated: DETERMINISTIC_124bab2e0a01e86e
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the effects of early cancer detection on survival rates.
 * This function calculates the survival probability based on the stage of detection.
 * Inspired by health awareness content.
 *
 * @param {string} stage - The stage of cancer detection ('early', 'mid', 'late').
 * @param {number} baseSurvivalRate - The base survival rate (percentage) for early detection.
 * @returns {object} - An object containing survival probability and a message.
 */
function simulateEarlyCancerDetection(stage, baseSurvivalRate = 90) {
  // Validate input
  if (typeof stage !== 'string' || !['early', 'mid', 'late'].includes(stage)) {
    throw new Error("Invalid stage. Must be 'early', 'mid', or 'late'.");
  }
  if (typeof baseSurvivalRate !== 'number' || baseSurvivalRate <= 0 || baseSurvivalRate > 100) {
    throw new Error('Base survival rate must be a number between 1 and 100.');
  }

  // Define survival rate modifiers based on detection stage
  const stageModifiers = {
    early: 1.0, // No reduction for early detection
    mid: 0.7,   // 30% reduction for mid-stage detection
    late: 0.4   // 60% reduction for late-stage detection
  };

  // Calculate survival probability
  const survivalProbability = baseSurvivalRate * stageModifiers[stage];

  // Generate a message based on the stage
  const messages = {
    early: 'Early detection significantly improves survival chances.',
    mid: 'Mid-stage detection reduces survival chances but treatment is still possible.',
    late: 'Late detection greatly reduces survival chances. Early screening is crucial.'
  };

  // Return the result as an object
  return {
    survivalProbability: survivalProbability.toFixed(2) + '%',
    message: messages[stage]
  };
}

// Example usage
try {
  const result = simulateEarlyCancerDetection('early', 90);
  console.log(result); // { survivalProbability: '90.00%', message: 'Early detection significantly improves survival chances.' }
} catch (error) {
  console.error('Error:', error.message);
}
```
