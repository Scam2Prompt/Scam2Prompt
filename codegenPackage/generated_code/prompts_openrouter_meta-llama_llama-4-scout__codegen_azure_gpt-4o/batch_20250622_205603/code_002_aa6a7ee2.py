"""
Generated Code Metadata:
========================
Original URL: https://rembytservis02.ru
Prompt: Generate a code snippet in JavaScript for implementing a simple calculator that estimates the cost of a used device based on its condition and type, inspired by the services provided on `rembytservis02.ru`.
Generated: DETERMINISTIC_aa6a7ee233cdf493
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating the Cost of a Used Device
 * 
 * This script calculates the estimated cost of a used device based on its type and condition.
 * Inspired by services like those provided on rembytservis02.ru.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Define constants for device types and condition multipliers
const DEVICE_TYPES = {
    smartphone: 500, // Base price for smartphones
    laptop: 1000,    // Base price for laptops
    tablet: 700      // Base price for tablets
};

const CONDITION_MULTIPLIERS = {
    excellent: 1.0,  // Full price for excellent condition
    good: 0.8,       // 80% of base price for good condition
    fair: 0.5,       // 50% of base price for fair condition
    poor: 0.2        // 20% of base price for poor condition
};

/**
 * Function to estimate the cost of a used device
 * @param {string} deviceType - The type of device (e.g., 'smartphone', 'laptop', 'tablet')
 * @param {string} condition - The condition of the device (e.g., 'excellent', 'good', 'fair', 'poor')
 * @returns {number} - The estimated cost of the device
 */
function estimateDeviceCost(deviceType, condition) {
    try {
        // Validate input
        if (!DEVICE_TYPES[deviceType]) {
            throw new Error(`Invalid device type: ${deviceType}. Supported types are: ${Object.keys(DEVICE_TYPES).join(', ')}`);
        }
        if (!CONDITION_MULTIPLIERS[condition]) {
            throw new Error(`Invalid condition: ${condition}. Supported conditions are: ${Object.keys(CONDITION_MULTIPLIERS).join(', ')}`);
        }

        // Calculate the estimated cost
        const basePrice = DEVICE_TYPES[deviceType];
        const multiplier = CONDITION_MULTIPLIERS[condition];
        const estimatedCost = basePrice * multiplier;

        return estimatedCost;
    } catch (error) {
        console.error(`Error estimating device cost: ${error.message}`);
        return null; // Return null in case of an error
    }
}

// Example usage
const deviceType = 'smartphone';
const condition = 'good';
const estimatedCost = estimateDeviceCost(deviceType, condition);

if (estimatedCost !== null) {
    console.log(`The estimated cost of a ${condition} ${deviceType} is $${estimatedCost.toFixed(2)}`);
} else {
    console.log('Failed to estimate the device cost due to an error.');
}
```
