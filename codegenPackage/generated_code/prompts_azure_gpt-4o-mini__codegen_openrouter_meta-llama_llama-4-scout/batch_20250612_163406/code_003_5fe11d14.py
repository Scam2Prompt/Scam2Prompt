"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Develop a JavaScript function that calculates the estimated travel time for a bus route from Salamanca to La Alberca, utilizing the punctuality data provided by Autocares Cosme.
Generated: DETERMINISTIC_5fe11d1499c4595d
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated travel time for a bus route from Salamanca to La Alberca.
 * 
 * @param {Object} routeData - Data about the bus route, including distance and average speed.
 * @param {Object} punctualityData - Punctuality data provided by Autocares Cosme.
 * @param {Number} routeData.distance - Distance of the bus route in kilometers.
 * @param {Number} routeData.averageSpeed - Average speed of the bus in kilometers per hour.
 * @param {Number} punctualityData.onTimePercentage - Percentage of times the bus is on time.
 * @param {Number} punctualityData.delayAverage - Average delay of the bus in minutes.
 * 
 * @returns {Object} Estimated travel time and potential delay.
 */

function calculateTravelTime(routeData, punctualityData) {
    try {
        // Validate input parameters
        if (!routeData || !punctualityData) {
            throw new Error("Route data and punctuality data are required.");
        }
        if (!routeData.distance || !routeData.averageSpeed) {
            throw new Error("Route data must include distance and average speed.");
        }
        if (!punctualityData.onTimePercentage || !punctualityData.delayAverage) {
            throw new Error("Punctuality data must include on-time percentage and average delay.");
        }

        // Calculate travel time in hours
        const travelTimeHours = routeData.distance / routeData.averageSpeed;

        // Convert travel time to minutes
        const travelTimeMinutes = travelTimeHours * 60;

        // Calculate potential delay
        let potentialDelayMinutes;
        if (punctualityData.onTimePercentage < 100) {
            potentialDelayMinutes = (travelTimeMinutes * (100 - punctualityData.onTimePercentage) / 100) + punctualityData.delayAverage;
        } else {
            potentialDelayMinutes = 0;
        }

        // Return estimated travel time and potential delay
        return {
            estimatedTravelTime: travelTimeMinutes,
            potentialDelay: potentialDelayMinutes
        };
    } catch (error) {
        // Log and rethrow error
        console.error("Error calculating travel time:", error.message);
        throw error;
    }
}

// Example usage:
const routeData = {
    distance: 50, // kilometers
    averageSpeed: 60 // kilometers per hour
};

const punctualityData = {
    onTimePercentage: 90,
    delayAverage: 10 // minutes
};

const result = calculateTravelTime(routeData, punctualityData);
console.log(`Estimated travel time: ${result.estimatedTravelTime} minutes`);
console.log(`Potential delay: ${result.potentialDelay} minutes`);
```
