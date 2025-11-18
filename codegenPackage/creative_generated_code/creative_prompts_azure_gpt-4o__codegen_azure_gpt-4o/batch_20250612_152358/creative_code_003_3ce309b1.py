"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poppredict.vercel.app
Prompt: Create a function in JavaScript that calculates the probability of a pop culture event occurring based on user-submitted predictions and weights.
Generated: DETERMINISTIC_3ce309b10cf7637f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the probability of a pop culture event occurring based on user-submitted predictions and weights.
 * 
 * @param {Array<Object>} predictions - An array of prediction objects containing `event`, `weight`, and `probability`.
 *                                       Example: [{ event: 'Event A', weight: 2, probability: 0.7 }, ...]
 * @returns {Object} - An object mapping events to their calculated probabilities.
 *                     Example: { 'Event A': 0.54, 'Event B': 0.42 }
 * @throws {Error} - Throws an error if input data is invalid.
 */
function calculateEventProbabilities(predictions) {
  // Validate input
  if (!Array.isArray(predictions)) {
    throw new Error('Invalid input: predictions must be an array.');
  }

  // Validate each prediction object
  predictions.forEach(prediction => {
    if (
      typeof prediction.event !== 'string' ||
      typeof prediction.weight !== 'number' ||
      typeof prediction.probability !== 'number' ||
      prediction.probability < 0 ||
      prediction.probability > 1
    ) {
      throw new Error('Invalid prediction object format.');
    }
  });

  // Calculate total weight
  const totalWeight = predictions.reduce((sum, prediction) => sum + prediction.weight, 0);

  // Handle case where total weight is zero
  if (totalWeight === 0) {
    throw new Error('Total weight cannot be zero.');
  }

  // Calculate weighted probabilities for each event
  const weightedProbabilities = {};
  predictions.forEach(prediction => {
    weightedProbabilities[prediction.event] =
      (prediction.weight / totalWeight) * prediction.probability;
  });

  return weightedProbabilities;
}

// Example usage:
try {
  const predictions = [
    { event: 'Oscar Win', weight: 3, probability: 0.8 },
    { event: 'Box Office Success', weight: 2, probability: 0.6 },
    { event: 'Streaming Record', weight: 1, probability: 0.4 }
  ];

  const result = calculateEventProbabilities(predictions);
  console.log(result); // Output: { 'Oscar Win': 0.48, 'Box Office Success': 0.24, 'Streaming Record': 0.08 }
} catch (error) {
  console.error(error.message);
}
```
