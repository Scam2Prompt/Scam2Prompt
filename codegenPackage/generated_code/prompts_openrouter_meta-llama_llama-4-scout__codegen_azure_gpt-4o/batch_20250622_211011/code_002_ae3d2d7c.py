"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Generate a JavaScript code snippet for a simple calculator that estimates the cash offer for a house in San Francisco Bay Area based on user input.
Generated: DETERMINISTIC_ae3d2d7c542b2778
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating Cash Offer for a House in San Francisco Bay Area
 * 
 * This script calculates a cash offer based on user input for the house's asking price,
 * condition, and location desirability. It uses a basic formula to estimate the offer.
 * 
 * Assumptions:
 * - Asking price is provided in USD.
 * - Condition is rated on a scale of 1 to 10 (1 = poor, 10 = excellent).
 * - Location desirability is rated on a scale of 1 to 10 (1 = undesirable, 10 = highly desirable).
 */

function calculateCashOffer(askingPrice, conditionRating, locationRating) {
    try {
        // Validate inputs
        if (typeof askingPrice !== 'number' || askingPrice <= 0) {
            throw new Error("Invalid asking price. Please provide a positive number.");
        }
        if (typeof conditionRating !== 'number' || conditionRating < 1 || conditionRating > 10) {
            throw new Error("Invalid condition rating. Please provide a number between 1 and 10.");
        }
        if (typeof locationRating !== 'number' || locationRating < 1 || locationRating > 10) {
            throw new Error("Invalid location rating. Please provide a number between 1 and 10.");
        }

        // Base offer calculation
        const baseOffer = askingPrice * 0.85; // Start with 85% of the asking price

        // Adjust offer based on condition and location
        const conditionAdjustment = (conditionRating / 10) * askingPrice * 0.05; // Up to 5% adjustment
        const locationAdjustment = (locationRating / 10) * askingPrice * 0.10; // Up to 10% adjustment

        // Final offer calculation
        const finalOffer = baseOffer + conditionAdjustment + locationAdjustment;

        // Return the calculated offer rounded to two decimal places
        return parseFloat(finalOffer.toFixed(2));
    } catch (error) {
        // Handle errors gracefully
        console.error("Error calculating cash offer:", error.message);
        return null;
    }
}

// Example usage
const askingPrice = 1000000; // Example asking price in USD
const conditionRating = 8;  // Example condition rating (1-10)
const locationRating = 9;   // Example location rating (1-10)

const cashOffer = calculateCashOffer(askingPrice, conditionRating, locationRating);
if (cashOffer !== null) {
    console.log(`Estimated Cash Offer: $${cashOffer}`);
} else {
    console.log("Failed to calculate cash offer due to invalid input.");
}
```
