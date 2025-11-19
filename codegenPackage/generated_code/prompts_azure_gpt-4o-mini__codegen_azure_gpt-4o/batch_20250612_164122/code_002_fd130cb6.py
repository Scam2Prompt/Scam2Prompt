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
 * Function to calculate the total cost of a customized safari trip in Tanzania.
 * @param {number} duration - Number of days for the safari trip.
 * @param {string} accommodationType - Type of accommodation ("budget", "midrange", "luxury").
 * @param {Array<string>} activities - List of activities selected (e.g., ["game drive", "hot air balloon", "cultural tour"]).
 * @returns {number} - Total cost of the safari trip.
 * @throws {Error} - Throws an error if invalid inputs are provided.
 */
function calculateSafariCost(duration, accommodationType, activities) {
  // Validate inputs
  if (typeof duration !== 'number' || duration <= 0) {
    throw new Error("Invalid duration. Duration must be a positive number.");
  }
  if (!["budget", "midrange", "luxury"].includes(accommodationType)) {
    throw new Error("Invalid accommodation type. Must be 'budget', 'midrange', or 'luxury'.");
  }
  if (!Array.isArray(activities) || activities.some(activity => typeof activity !== 'string')) {
    throw new Error("Invalid activities. Activities must be an array of strings.");
  }

  // Base cost per day for each accommodation type
  const accommodationCosts = {
    budget: 100, // USD per day
    midrange: 200, // USD per day
    luxury: 400, // USD per day
  };

  // Activity costs
  const activityCosts = {
    "game drive": 50, // USD per activity
    "hot air balloon": 300, // USD per activity
    "cultural tour": 100, // USD per activity
    "walking safari": 75, // USD per activity
  };

  // Calculate accommodation cost
  const accommodationCost = accommodationCosts[accommodationType] * duration;

  // Calculate activity cost
  let activityCost = 0;
  for (const activity of activities) {
    if (activityCosts[activity] !== undefined) {
      activityCost += activityCosts[activity];
    } else {
      throw new Error(`Invalid activity: ${activity}. Please select valid activities.`);
    }
  }

  // Calculate total cost
  const totalCost = accommodationCost + activityCost;

  return totalCost;
}

// Example usage:
try {
  const duration = 5; // 5 days
  const accommodationType = "midrange";
  const activities = ["game drive", "hot air balloon", "cultural tour"];
  const totalCost = calculateSafariCost(duration, accommodationType, activities);
  console.log(`Total cost of the safari trip: $${totalCost}`);
} catch (error) {
  console.error(error.message);
}
```
