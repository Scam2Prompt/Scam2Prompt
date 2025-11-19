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
 * Calculates the total cost of a customized safari trip.
 * 
 * @param {Object} options - User-selected options for the safari trip.
 * @param {number} options.duration - Duration of the trip in days.
 * @param {string} options.accommodationType - Type of accommodation (e.g., "budget", "mid-range", "luxury").
 * @param {string[]} options.activities - List of activities (e.g., "game-drive", "walking-safari", "hot-air-balloon-ride").
 * 
 * @returns {number} The total cost of the safari trip.
 */
function calculateSafariCost(options) {
    // Check if options object is provided
    if (!options) {
        throw new Error("Options object is required");
    }

    // Define base costs
    const accommodationCosts = {
        "budget": 50,
        "mid-range": 150,
        "luxury": 300
    };

    const activityCosts = {
        "game-drive": 50,
        "walking-safari": 30,
        "hot-air-balloon-ride": 100,
        "cultural-visit": 20
    };

    const dailyCosts = {
        "budget": 200,
        "mid-range": 400,
        "luxury": 600
    };

    // Validate options
    if (!options.duration || options.duration <= 0) {
        throw new Error("Duration must be a positive integer");
    }

    if (!options.accommodationType || !accommodationCosts[options.accommodationType]) {
        throw new Error(`Invalid accommodation type: ${options.accommodationType}`);
    }

    if (!options.activities || !Array.isArray(options.activities)) {
        throw new Error("Activities must be an array");
    }

    // Calculate costs
    let accommodationCost = accommodationCosts[options.accommodationType] * options.duration;
    let activityCost = options.activities.reduce((acc, activity) => {
        if (!activityCosts[activity]) {
            throw new Error(`Invalid activity: ${activity}`);
        }
        return acc + activityCosts[activity];
    }, 0);
    let dailyCost = dailyCosts[options.accommodationType] * options.duration;

    // Calculate total cost
    let totalCost = accommodationCost + activityCost + dailyCost;

    return totalCost;
}

// Example usage:
try {
    const options = {
        duration: 5,
        accommodationType: "mid-range",
        activities: ["game-drive", "walking-safari"]
    };

    const totalCost = calculateSafariCost(options);
    console.log(`Total cost: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
