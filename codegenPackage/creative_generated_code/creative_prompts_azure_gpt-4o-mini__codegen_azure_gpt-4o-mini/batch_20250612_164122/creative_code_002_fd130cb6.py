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
 * Calculates the total cost of a customized safari trip in Tanzania.
 * 
 * @param {Object} options - An object containing the user's trip options.
 * @param {number} options.duration - The duration of the trip in days.
 * @param {string} options.accommodation - The type of accommodation chosen (e.g., 'tent', 'lodge', 'hotel').
 * @param {Array<string>} options.activities - A list of activities selected by the user (e.g., 'safari', 'hiking', 'cultural tour').
 * @returns {number} - The total cost of the trip.
 * @throws {Error} - Throws an error if the input options are invalid.
 */
function calculateSafariCost(options) {
    // Define base costs for accommodation and activities
    const accommodationCosts = {
        tent: 50,       // cost per day for tent accommodation
        lodge: 150,     // cost per day for lodge accommodation
        hotel: 300      // cost per day for hotel accommodation
    };

    const activityCosts = {
        safari: 100,    // cost per activity
        hiking: 75,     // cost per activity
        culturalTour: 50 // cost per activity
    };

    // Validate input options
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid options provided. Must be an object.');
    }
    if (!options.duration || typeof options.duration !== 'number' || options.duration <= 0) {
        throw new Error('Invalid duration. Must be a positive number.');
    }
    if (!options.accommodation || !accommodationCosts[options.accommodation]) {
        throw new Error('Invalid accommodation type. Must be one of: tent, lodge, hotel.');
    }
    if (!Array.isArray(options.activities)) {
        throw new Error('Activities must be an array of strings.');
    }

    // Calculate total accommodation cost
    const accommodationCost = accommodationCosts[options.accommodation] * options.duration;

    // Calculate total activities cost
    const activitiesCost = options.activities.reduce((total, activity) => {
        if (!activityCosts[activity]) {
            throw new Error(`Invalid activity: ${activity}. Must be one of: ${Object.keys(activityCosts).join(', ')}.`);
        }
        return total + activityCosts[activity];
    }, 0);

    // Calculate total cost
    const totalCost = accommodationCost + activitiesCost;

    return totalCost;
}

// Example usage
try {
    const tripOptions = {
        duration: 5,
        accommodation: 'lodge',
        activities: ['safari', 'hiking']
    };

    const totalCost = calculateSafariCost(tripOptions);
    console.log(`Total cost of the safari trip: $${totalCost}`);
} catch (error) {
    console.error(`Error calculating trip cost: ${error.message}`);
}
```
