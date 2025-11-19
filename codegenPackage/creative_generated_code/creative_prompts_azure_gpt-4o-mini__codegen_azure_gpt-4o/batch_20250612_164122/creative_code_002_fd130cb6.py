"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://natureexcursionsafaris.com
Prompt: Create a function in JavaScript that calculates the total cost of a customized safari trip based on user-selected options such as duration, accommodation type, and activities in Tanzania.
Generated: DETERMINISTIC_fd130cb6c56fee49
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of a customized safari trip based on user-selected options.
 * @param {Object} options - An object containing the user's trip selections.
 * @param {number} options.duration - Duration of the safari trip in days.
 * @param {string} options.accommodationType - Type of accommodation ("budget", "mid-range", "luxury").
 * @param {Array<string>} options.activities - List of activities selected (e.g., ["gameDrive", "hotAirBalloon", "walkingSafari"]).
 * @returns {number} - Total cost of the safari trip.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateSafariCost(options) {
    // Validate input
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid input: options must be an object.');
    }
    const { duration, accommodationType, activities } = options;

    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Invalid duration: must be a positive number.');
    }
    if (!['budget', 'mid-range', 'luxury'].includes(accommodationType)) {
        throw new Error('Invalid accommodation type: must be "budget", "mid-range", or "luxury".');
    }
    if (!Array.isArray(activities) || activities.some(activity => typeof activity !== 'string')) {
        throw new Error('Invalid activities: must be an array of strings.');
    }

    // Base costs per day for accommodation types
    const accommodationCosts = {
        budget: 100,
        midRange: 200,
        luxury: 500,
    };

    // Activity costs per type
    const activityCosts = {
        gameDrive: 50,
        hotAirBalloon: 300,
        walkingSafari: 100,
    };

    // Calculate accommodation cost
    const accommodationDailyRate = accommodationCosts[accommodationType.replace('-', '')];
    const accommodationCost = accommodationDailyRate * duration;

    // Calculate activities cost
    const activitiesCost = activities.reduce((total, activity) => {
        if (!activityCosts[activity]) {
            throw new Error(`Invalid activity: ${activity} is not supported.`);
        }
        return total + activityCosts[activity];
    }, 0);

    // Calculate total cost
    const totalCost = accommodationCost + activitiesCost;

    return totalCost;
}

// Example usage:
try {
    const safariOptions = {
        duration: 5,
        accommodationType: 'mid-range',
        activities: ['gameDrive', 'hotAirBalloon', 'walkingSafari'],
    };
    const totalCost = calculateSafariCost(safariOptions);
    console.log(`Total safari cost: $${totalCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
