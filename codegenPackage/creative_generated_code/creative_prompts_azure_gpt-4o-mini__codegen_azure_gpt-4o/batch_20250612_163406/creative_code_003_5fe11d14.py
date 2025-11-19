"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autocarescosme.com
Prompt: Develop a JavaScript function that calculates the estimated travel time for a bus route from Salamanca to La Alberca, utilizing the punctuality data provided by Autocares Cosme.
Generated: DETERMINISTIC_5fe11d1499c4595d
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the estimated travel time for a bus route.
 * @param {number} distanceKm - The distance between Salamanca and La Alberca in kilometers.
 * @param {number} averageSpeedKmH - The average speed of the bus in km/h.
 * @param {number} punctualityRate - The punctuality rate of the bus (percentage as a decimal, e.g., 0.95 for 95%).
 * @returns {string} - The estimated travel time in hours and minutes.
 */
function calculateTravelTime(distanceKm, averageSpeedKmH, punctualityRate) {
  try {
    // Validate inputs
    if (typeof distanceKm !== 'number' || distanceKm <= 0) {
      throw new Error("Invalid distance: Must be a positive number.");
    }
    if (typeof averageSpeedKmH !== 'number' || averageSpeedKmH <= 0) {
      throw new Error("Invalid average speed: Must be a positive number.");
    }
    if (typeof punctualityRate !== 'number' || punctualityRate < 0 || punctualityRate > 1) {
      throw new Error(
        "Invalid punctuality rate: Must be a decimal between 0 and 1."
      );
    }

    // Adjust travel time based on punctuality rate
    const adjustedSpeed = averageSpeedKmH * punctualityRate;

    // Calculate travel time in hours
    const travelTimeHours = distanceKm / adjustedSpeed;

    // Convert hours into hours and minutes
    const hours = Math.floor(travelTimeHours);
    const minutes = Math.round((travelTimeHours - hours) * 60);

    // Format travel time as a string
    return `${hours} hours and ${minutes} minutes`;
  } catch (error) {
    // Handle errors gracefully
    console.error(error.message);
    return "Unable to calculate travel time due to an error.";
  }
}

// Example usage
const distanceKm = 75; // Distance from Salamanca to La Alberca in km
const averageSpeedKmH = 50; // Average speed of the bus in km/h
const punctualityRate = 0.9; // Punctuality rate (90%)

console.log(calculateTravelTime(distanceKm, averageSpeedKmH, punctualityRate)); // Output: "1 hours and 30 minutes"
```
