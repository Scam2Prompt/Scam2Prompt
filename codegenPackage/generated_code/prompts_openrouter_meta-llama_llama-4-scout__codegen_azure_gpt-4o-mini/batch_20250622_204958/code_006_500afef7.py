"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Write a JavaScript function to calculate the cost of a Tanzania safari based on the number of days, type of accommodation, and activities.
Generated: DETERMINISTIC_500afef7a65346bd
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a Tanzania safari based on the number of days,
 * type of accommodation, and activities selected.
 *
 * @param {number} days - The number of days for the safari (must be a positive integer).
 * @param {string} accommodation - The type of accommodation ('budget', 'midrange', 'luxury').
 * @param {Array<string>} activities - An array of selected activities (e.g., ['safari', 'hiking']).
 * @returns {number} - The total cost of the safari.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateSafariCost(days, accommodation, activities) {
    // Validate input parameters
    if (typeof days !== 'number' || days <= 0 || !Number.isInteger(days)) {
        throw new Error('Invalid number of days. It must be a positive integer.');
    }

    const accommodationCosts = {
        budget: 100,    // Cost per day for budget accommodation
        midrange: 200,  // Cost per day for midrange accommodation
        luxury: 400     // Cost per day for luxury accommodation
    };

    // Check if the accommodation type is valid
    if (!accommodationCosts[accommodation]) {
        throw new Error('Invalid accommodation type. Choose from: budget, midrange, luxury.');
    }

    // Base cost calculation
    let totalCost = days * accommodationCosts[accommodation];

    // Define activity costs
    const activityCosts = {
        safari: 50,     // Cost per activity
        hiking: 30,
        cultural: 40,
        birdWatching: 20
    };

    // Calculate total cost for selected activities
    if (Array.isArray(activities)) {
        activities.forEach(activity => {
            if (activityCosts[activity]) {
                totalCost += activityCosts[activity];
            } else {
                console.warn(`Activity "${activity}" is not recognized and will be ignored.`);
            }
        });
    } else {
        throw new Error('Activities must be provided as an array of strings.');
    }

    return totalCost;
}

// Example usage
try {
    const totalCost = calculateSafariCost(5, 'midrange', ['safari', 'hiking']);
    console.log(`Total cost for the safari: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
