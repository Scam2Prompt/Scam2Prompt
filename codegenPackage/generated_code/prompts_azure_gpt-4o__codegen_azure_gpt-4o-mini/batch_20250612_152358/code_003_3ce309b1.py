"""
Generated Code Metadata:
========================
Original URL: https://poppredict.vercel.app
Prompt: Create a function in JavaScript that calculates the probability of a pop culture event occurring based on user-submitted predictions and weights.
Generated: DETERMINISTIC_3ce309b10cf7637f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the probability of a pop culture event occurring based on user-submitted predictions and weights.
 * 
 * @param {Array<{ prediction: string, weight: number }>} predictions - An array of user predictions with associated weights.
 * @returns {number} - The calculated probability as a percentage (0 to 100).
 * @throws {Error} - Throws an error if the input is invalid or if weights do not sum to a positive value.
 */
function calculateEventProbability(predictions) {
    // Validate input
    if (!Array.isArray(predictions) || predictions.length === 0) {
        throw new Error("Invalid input: predictions must be a non-empty array.");
    }

    let totalWeight = 0;
    let weightedSum = 0;

    // Iterate through predictions to calculate total weight and weighted sum
    predictions.forEach(({ prediction, weight }) => {
        if (typeof prediction !== 'string' || typeof weight !== 'number' || weight < 0) {
            throw new Error("Invalid prediction: each prediction must be a string and weight must be a non-negative number.");
        }
        totalWeight += weight;
        weightedSum += weight; // Assuming each prediction contributes equally to the event's occurrence
    });

    // Check if total weight is positive to avoid division by zero
    if (totalWeight <= 0) {
        throw new Error("Invalid weights: total weight must be greater than zero.");
    }

    // Calculate probability as a percentage
    const probability = (weightedSum / totalWeight) * 100;

    // Return the calculated probability, rounded to two decimal places
    return parseFloat(probability.toFixed(2));
}

// Example usage
try {
    const predictions = [
        { prediction: "Movie A will be a blockbuster", weight: 30 },
        { prediction: "Movie B will flop", weight: 10 },
        { prediction: "Movie C will be critically acclaimed", weight: 20 }
    ];
    
    const probability = calculateEventProbability(predictions);
    console.log(`The probability of the event occurring is: ${probability}%`);
} catch (error) {
    console.error(error.message);
}
```
