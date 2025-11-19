"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Create a function in JavaScript that calculates the total cost of a customized safari trip based on user-selected options such as duration, accommodation type, and activities in Tanzania.
Generated: DETERMINISTIC_fd130cb6c56fee49
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a customized safari trip in Tanzania based on selected options.
 * @param {Object} options - The selected trip options.
 * @param {number} options.duration - Duration of the trip in days.
 * @param {string} options.accommodationType - Type of accommodation ('basic', 'mid-range', 'luxury').
 * @param {string[]} options.activities - List of selected activities (e.g., ['game-drive', 'walking-safari']).
 * @returns {number} The total cost of the safari trip in USD.
 * @throws {Error} If invalid options are provided.
 */
function calculateSafariCost(options) {
    // Validate input
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid options provided. Options must be an object.');
    }

    const { duration, accommodationType, activities } = options;

    // Validate duration
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Invalid duration. Duration must be a positive number.');
    }

    // Accommodation cost mapping (USD per day)
    const accommodationCosts = {
        'basic': 100,
        'mid-range': 250,
        'luxury': 500
    };

    // Validate accommodation type
    if (!accommodationType || !accommodationCosts[accommodationType]) {
        throw new Error(`Invalid accommodation type. Must be one of: ${Object.keys(accommodationCosts).join(', ')}`);
    }

    // Activity cost mapping (USD per activity)
    const activityCosts = {
        'game-drive': 50,
        'walking-safari': 75,
        'balloon-safari': 200,
        'cultural-tour': 30,
        'bird-watching': 40
    };

    // Validate activities
    if (!Array.isArray(activities)) {
        throw new Error('Invalid activities. Must be an array of activity names.');
    }

    // Calculate total activity cost
    let totalActivityCost = 0;
    activities.forEach(activity => {
        if (!activityCosts[activity]) {
            throw new Error(`Invalid activity: ${activity}. Must be one of: ${Object.keys(activityCosts).join(', ')}`);
        }
        totalActivityCost += activityCosts[activity];
    });

    // Base cost per day (includes guide, vehicle, etc.)
    const baseCostPerDay = 200;

    // Calculate total cost
    const totalCost = (baseCostPerDay + accommodationCosts[accommodationType]) * duration + totalActivityCost;

    return totalCost;
}

// Example usage:
// try {
//     const options = {
//         duration: 5,
//         accommodationType: 'mid-range',
//         activities: ['game-drive', 'balloon-safari']
//     };
//     const cost = calculateSafariCost(options);
//     console.log(`Total safari cost: $${cost}`);
// } catch (error) {
//     console.error(`Error calculating cost: ${error.message}`);
// }
```
