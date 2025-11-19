"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Write a Node.js function to calculate the estimated delivery time for a package shipped from India to Australia using Alexa Shipping's services, taking into account factors like shipping mode, distance, and customs clearance procedures.
Generated: DETERMINISTIC_7cb2e2bd8235cbe7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated delivery time for a package shipped from India to Australia using Alexa Shipping's services.
 * 
 * @param {string} shippingMode - The shipping mode (e.g., 'air', 'sea', 'express').
 * @param {number} distance - The distance between the sender and receiver locations in kilometers.
 * @param {string} customsClearance - The customs clearance procedure (e.g., 'normal', 'express').
 * @returns {number} The estimated delivery time in days.
 */

const alexaShipping = {
  // Base delivery times for each shipping mode in days
  baseDeliveryTimes: {
    air: 3,
    sea: 15,
    express: 2
  },

  // Additional time for customs clearance procedures in days
  customsClearanceTimes: {
    normal: 2,
    express: 0.5
  },

  // Distance-based delivery time adjustments in days
  distanceAdjustments: {
    air: 0.01,
    sea: 0.005,
    express: 0.02
  },

  calculateDeliveryTime: function(shippingMode, distance, customsClearance) {
    try {
      // Check if shipping mode is valid
      if (!(shippingMode in this.baseDeliveryTimes)) {
        throw new Error(`Invalid shipping mode: ${shippingMode}`);
      }

      // Check if customs clearance procedure is valid
      if (!(customsClearance in this.customsClearanceTimes)) {
        throw new Error(`Invalid customs clearance procedure: ${customsClearance}`);
      }

      // Calculate base delivery time
      let baseDeliveryTime = this.baseDeliveryTimes[shippingMode];

      // Calculate distance-based delivery time adjustment
      let distanceAdjustment = distance * this.distanceAdjustments[shippingMode];

      // Calculate customs clearance time
      let customsClearanceTime = this.customsClearanceTimes[customsClearance];

      // Calculate estimated delivery time
      let estimatedDeliveryTime = baseDeliveryTime + distanceAdjustment + customsClearanceTime;

      // Round estimated delivery time to two decimal places
      estimatedDeliveryTime = Math.round(estimatedDeliveryTime * 100) / 100;

      return estimatedDeliveryTime;
    } catch (error) {
      console.error(`Error calculating delivery time: ${error.message}`);
      throw error;
    }
  }
};

// Example usage:
function main() {
  try {
    let shippingMode = 'air';
    let distance = 1000; // kilometers
    let customsClearance = 'normal';

    let estimatedDeliveryTime = alexaShipping.calculateDeliveryTime(shippingMode, distance, customsClearance);
    console.log(`Estimated delivery time: ${estimatedDeliveryTime} days`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main();
```
