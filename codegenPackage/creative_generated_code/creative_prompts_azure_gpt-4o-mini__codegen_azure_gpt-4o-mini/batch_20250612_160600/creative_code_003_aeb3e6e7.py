"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Develop a function in JavaScript that calculates the call charges using Ziber's pricing model based on time of day and proxy availability.
Generated: DETERMINISTIC_aeb3e6e7fcf2fc49
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates call charges based on Ziber's pricing model.
 * 
 * @param {number} duration - The duration of the call in minutes.
 * @param {string} timeOfDay - The time of the day in 'HH:mm' format (24-hour).
 * @param {boolean} isProxyAvailable - Indicates if the proxy is available.
 * @returns {number} - The calculated call charge.
 * @throws {Error} - Throws an error if the duration is negative or timeOfDay format is incorrect.
 */
function calculateCallCharges(duration, timeOfDay, isProxyAvailable) {
    // Validate input parameters
    if (duration < 0) {
        throw new Error("Duration must be a non-negative number.");
    }

    // Validate timeOfDay format (HH:mm)
    const timeRegex = /^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$/;
    if (!timeRegex.test(timeOfDay)) {
        throw new Error("Invalid timeOfDay format. Please use 'HH:mm' format (24-hour).");
    }

    // Parse the time of day into hours
    const [hours, minutes] = timeOfDay.split(':').map(Number);
    const totalMinutes = hours * 60 + minutes;

    // Define pricing model based on time of day and proxy availability
    let baseRate;
    if (isProxyAvailable) {
        // Proxy available pricing
        baseRate = (totalMinutes < 480) ? 0.05 : 0.03; // Day rate
    } else {
        // No proxy available pricing
        baseRate = (totalMinutes < 480) ? 0.10 : 0.08; // Night rate
    }

    // Calculate total charges
    const totalCharge = duration * baseRate;

    return parseFloat(totalCharge.toFixed(2)); // Return charge rounded to 2 decimal places
}

// Example usage
try {
    const charges = calculateCallCharges(10, '14:30', true);
    console.log(`Total call charges: $${charges}`);
} catch (error) {
    console.error(`Error calculating call charges: ${error.message}`);
}
```
