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
 * @param {Array<{ prediction: string, weight: number }>} predictions - An array of prediction objects,
 * where each object contains a prediction string and a corresponding weight (numeric).
 * @returns {number} The calculated probability as a percentage (0-100).
 * @throws {Error} Throws an error if the input is invalid.
 */
function calculateEventProbability(predictions) {
    // Validate input is an array
    if (!Array.isArray(predictions)) {
        throw new Error("Input must be an array of predictions.");
    }

    let totalWeight = 0;
    let weightedSum = 0;

    // Iterate through each prediction to calculate total weight and weighted sum
    predictions.forEach((item, index) => {
        // Validate each item in the array
        if (typeof item !== 'object' || !item.hasOwnProperty('prediction') || !item.hasOwnProperty('weight')) {
            throw new Error(`Invalid prediction at index ${index}: Must be an object with 'prediction' and 'weight'.`);
        }
        
        // Validate weight is a number and not negative
        if (typeof item.weight !== 'number' || item.weight < 0) {
            throw new Error(`Invalid weight at index ${index}: Must be a non-negative number.`);
        }

        // Accumulate total weight and weighted sum
        totalWeight += item.weight;
        weightedSum += item.weight; // Assuming each prediction contributes equally to the event occurring
    });

    // Handle case where total weight is zero
    if (totalWeight === 0) {
        return 0; // No predictions, probability is 0%
    }

    // Calculate the probability as a percentage
    const probability = (weightedSum / totalWeight) * 100;

    // Ensure the probability is between 0 and 100
    return Math.min(Math.max(probability, 0), 100);
}

// Example usage:
try {
    const predictions = [
        { prediction: "Event A will happen", weight: 30 },
        { prediction: "Event B will happen", weight: 70 },
    ];
    const probability = calculateEventProbability(predictions);
    console.log(`Probability of event occurring: ${probability.toFixed(2)}%`);
} catch (error) {
    console.error(error.message);
}
```
