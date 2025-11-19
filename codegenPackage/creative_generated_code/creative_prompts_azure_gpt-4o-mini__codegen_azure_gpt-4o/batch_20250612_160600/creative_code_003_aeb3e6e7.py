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
 * Calculate call charges based on Ziber's pricing model.
 * Pricing Model:
 * - Regular hours (8 AM - 8 PM):
 *   - $0.05 per minute if a proxy is available
 *   - $0.10 per minute if no proxy is available
 * - Off hours (8 PM - 8 AM):
 *   - $0.02 per minute if a proxy is available
 *   - $0.05 per minute if no proxy is available
 * 
 * @param {number} callDuration - Duration of the call in minutes.
 * @param {Date} callStartTime - Start time of the call as a Date object.
 * @param {boolean} isProxyAvailable - Whether a proxy is available for the call.
 * @returns {number} - The calculated call charges.
 * @throws {Error} - Throws an error if input parameters are invalid.
 */
function calculateCallCharges(callDuration, callStartTime, isProxyAvailable) {
  // Input validation
  if (typeof callDuration !== 'number' || callDuration < 0) {
    throw new Error("Invalid call duration. It must be a non-negative number.");
  }
  if (!(callStartTime instanceof Date) || isNaN(callStartTime.getTime())) {
    throw new Error("Invalid call start time. It must be a valid Date object.");
  }
  if (typeof isProxyAvailable !== 'boolean') {
    throw new Error("Invalid proxy availability. It must be a boolean.");
  }

  // Extract hour from the call start time
  const callHour = callStartTime.getHours();

  // Determine hourly rate based on time of day and proxy availability
  let ratePerMinute;
  if (callHour >= 8 && callHour < 20) {
    // Regular hours (8 AM - 8 PM)
    ratePerMinute = isProxyAvailable ? 0.05 : 0.10;
  } else {
    // Off hours (8 PM - 8 AM)
    ratePerMinute = isProxyAvailable ? 0.02 : 0.05;
  }

  // Calculate total call charges
  const totalCharges = callDuration * ratePerMinute;

  // Return the calculated charges
  return totalCharges;
}

// Example usage:
try {
  const callDuration = 30; // 30 minutes
  const callStartTime = new Date('2023-10-11T19:45:00'); // 7:45 PM
  const isProxyAvailable = true; // Proxy is available

  const charges = calculateCallCharges(callDuration, callStartTime, isProxyAvailable);
  console.log(`Call charges: $${charges.toFixed(2)}`);
} catch (error) {
  console.error("Error calculating call charges:", error.message);
}
```
