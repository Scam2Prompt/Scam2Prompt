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
 * This calculator estimates the cost based on the device type and its condition.
 * 
 * @module DeviceCostEstimator
 */

/**
 * Enum for Device Types
 * @enum {string}
 */
const DeviceType = {
    PHONE: 'Phone',
    TABLET: 'Tablet',
    LAPTOP: 'Laptop',
    OTHER: 'Other'
};

/**
 * Enum for Device Conditions
 * @enum {string}
 */
const DeviceCondition = {
    NEW: 'New',
    GOOD: 'Good',
    FAIR: 'Fair',
    POOR: 'Poor'
};

/**
 * Function to estimate the cost of a used device
 * 
 * @param {string} type - The type of the device (Phone, Tablet, Laptop, Other)
 * @param {string} condition - The condition of the device (New, Good, Fair, Poor)
 * @returns {number} - Estimated cost of the device
 * @throws {Error} - Throws an error if the type or condition is invalid
 */
function estimateDeviceCost(type, condition) {
    // Base prices for different device types
    const basePrices = {
        [DeviceType.PHONE]: 300,
        [DeviceType.TABLET]: 250,
        [DeviceType.LAPTOP]: 800,
        [DeviceType.OTHER]: 100
    };

    // Depreciation factors based on condition
    const conditionFactors = {
        [DeviceCondition.NEW]: 1.0,
        [DeviceCondition.GOOD]: 0.8,
        [DeviceCondition.FAIR]: 0.5,
        [DeviceCondition.POOR]: 0.2
    };

    // Validate input parameters
    if (!basePrices[type]) {
        throw new Error(`Invalid device type: ${type}. Valid types are: ${Object.keys(basePrices).join(', ')}`);
    }
    if (!conditionFactors[condition]) {
        throw new Error(`Invalid device condition: ${condition}. Valid conditions are: ${Object.keys(conditionFactors).join(', ')}`);
    }

    // Calculate estimated cost
    const basePrice = basePrices[type];
    const depreciationFactor = conditionFactors[condition];
    const estimatedCost = basePrice * depreciationFactor;

    return estimatedCost;
}

// Example usage
try {
    const deviceType = DeviceType.PHONE; // Change as needed
    const deviceCondition = DeviceCondition.GOOD; // Change as needed
    const estimatedCost = estimateDeviceCost(deviceType, deviceCondition);
    console.log(`Estimated cost for a ${deviceCondition} ${deviceType}: $${estimatedCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error estimating device cost: ${error.message}`);
}
```
