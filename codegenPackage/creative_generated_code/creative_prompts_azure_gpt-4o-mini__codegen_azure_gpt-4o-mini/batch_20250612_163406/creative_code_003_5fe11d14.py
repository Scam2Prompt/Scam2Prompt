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
 * Function to calculate estimated travel time for a bus route
 * from Salamanca to La Alberca using punctuality data.
 *
 * @param {number} distance - The distance from Salamanca to La Alberca in kilometers.
 * @param {number} averageSpeed - The average speed of the bus in kilometers per hour.
 * @param {number} delay - The average delay in minutes due to punctuality issues.
 * @returns {string} Estimated travel time in the format "HH:MM".
 * @throws {Error} If distance or averageSpeed is not positive or if delay is negative.
 */
function calculateTravelTime(distance, averageSpeed, delay) {
    // Validate input parameters
    if (distance <= 0) {
        throw new Error("Distance must be a positive number.");
    }
    if (averageSpeed <= 0) {
        throw new Error("Average speed must be a positive number.");
    }
    if (delay < 0) {
        throw new Error("Delay cannot be negative.");
    }
    
    // Calculate travel time in hours
    const travelTimeHours = distance / averageSpeed;

    // Convert travel time to minutes and add delay
    const travelTimeMinutes = (travelTimeHours * 60) + delay;

    // Calculate total hours and minutes
    const totalHours = Math.floor(travelTimeMinutes / 60);
    const totalMinutes = Math.round(travelTimeMinutes % 60);

    // Format the result as "HH:MM" with leading zeros
    const formattedTime = `${String(totalHours).padStart(2, '0')}:${String(totalMinutes).padStart(2, '0')}`;
    
    return formattedTime;
}

// Example usage
try {
    const distance = 80; // Distance in kilometers
    const averageSpeed = 50; // Average speed in kilometers per hour
    const delay = 15; // Average delay in minutes

    const estimatedTime = calculateTravelTime(distance, averageSpeed, delay);
    console.log(`Estimated travel time from Salamanca to La Alberca: ${estimatedTime}`);
} catch (error) {
    console.error(`Error calculating travel time: ${error.message}`);
}
```
