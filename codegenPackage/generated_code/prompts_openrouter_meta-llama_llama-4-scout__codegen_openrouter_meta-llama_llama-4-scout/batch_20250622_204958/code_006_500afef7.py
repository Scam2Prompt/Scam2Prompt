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
 * Calculates the cost of a Tanzania safari.
 * 
 * @param {number} days - The number of days for the safari.
 * @param {string} accommodation - The type of accommodation. Can be 'budget', 'mid-range', or 'luxury'.
 * @param {string[]} activities - An array of activities. Can include 'game-drive', 'hiking', 'bird-watching', and 'cultural-tour'.
 * @returns {number} The total cost of the safari.
 */
function calculateSafariCost(days, accommodation, activities) {
    // Validate input parameters
    if (typeof days !== 'number' || days <= 0) {
        throw new Error('Number of days must be a positive integer.');
    }
    if (!['budget', 'mid-range', 'luxury'].includes(accommodation)) {
        throw new Error('Invalid accommodation type.');
    }
    if (!Array.isArray(activities)) {
        throw new Error('Activities must be an array.');
    }

    // Define accommodation costs per day
    const accommodationCosts = {
        'budget': 50,
        'mid-range': 150,
        'luxury': 300
    };

    // Define activity costs
    const activityCosts = {
        'game-drive': 50,
        'hiking': 30,
        'bird-watching': 20,
        'cultural-tour': 40
    };

    // Calculate accommodation cost
    let accommodationCost = days * accommodationCosts[accommodation];

    // Calculate activity cost
    let activityCost = 0;
    activities.forEach(activity => {
        if (!activityCosts[activity]) {
            throw new Error(`Invalid activity: ${activity}.`);
        }
        activityCost += activityCosts[activity];
    });

    // Calculate total cost
    let totalCost = accommodationCost + (activityCost * days);

    return totalCost;
}

// Example usage:
try {
    const days = 5;
    const accommodation = 'mid-range';
    const activities = ['game-drive', 'bird-watching'];
    const cost = calculateSafariCost(days, accommodation, activities);
    console.log(`The total cost of the safari is: $${cost}`);
} catch (error) {
    console.error(error.message);
}
```
